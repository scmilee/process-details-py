import os
import sys
import threading
import stat
from subprocess import Popen, PIPE
 
def getListOfProcceses(none):
        process = Popen(['ps', '-eo' ,'pid,args'], stdout=PIPE, stderr=PIPE)
        stdout, notused = process.communicate()
        for line in stdout.splitlines():
                print line

def getListOfThreads(ppidFilter):
        process = Popen(['ps', '-eo' ,'pid,ppid,args'], stdout=PIPE, stderr=PIPE)
        stdout, notused = process.communicate()
        for line in stdout.splitlines():
                pid,ppid,command = line.split(' ', 2)
                if ppidFilter == ppid:
                        print pid,command

def getDllsForProcess(pidFilter):
        stringFilter = '%s' % pidFilter
        process = Popen(['lsof', '-p', stringFilter ], stdout=PIPE, stderr=PIPE)
        stdout, notused = process.communicate()
        for line in stdout.splitlines():
                print line

def getExecutabblesForProccess(pidFilter):
        stringFilter = '%s' % pidFilter
        process = Popen(['lsof', '-p', stringFilter ], stdout=PIPE, stderr=PIPE)
        stdout, notused = process.communicate()
        executable = stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
        for line in stdout.splitlines():
                line = line.rsplit(' ')
                filename = line[-1]
                if os.path.isfile(filename):
                        st = os.stat(filename)
                        mode = st.st_mode
                        if mode & executable:
                                print(pidFilter, filename)

def getMemoryForProccess(pidFilter):
        stringFilter = '%s' % pidFilter
        process = Popen(['vmmap', stringFilter ], stdout=PIPE, stderr=PIPE)
        stdout, notused = process.communicate()
        for line in stdout.splitlines():
                print line
        

options = {
        'ls' : getListOfProcceses,
        'lsthread': getListOfThreads,
        'lsimport' : getDllsForProcess,
        'lspages' : getExecutabblesForProccess,
        'lsmem' : getMemoryForProccess
}

def main():
        secondArg = None
        if len(sys.argv) > 2:
                secondArg = sys.argv[2]
        options[sys.argv[1]](secondArg)
    
if __name__ == '__main__':
   main()