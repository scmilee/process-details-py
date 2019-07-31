This cli was built using python 2.7.10 and needs no external libraries, YAY!

- Enumerate all the running processes.
`python hw2.py ls`
- List all the running threads within process boundary.
`python hw2.py lsthread $ppid`
- Enumerate all the loaded modules within the processes.
`python hw2.py lsimport $pid`
- Is able to show all the executable pages within the processes.
`python hw2.py lspages $pid`
- Gives us a capability to read the memory.
`python hw2.py lsmem $pid`