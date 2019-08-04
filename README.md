This cli was built using python 2.7.10 and needs no external libraries, YAY!

- Enumerate all the running processes.
`python main.py ls`
- List all the running threads within process boundary*.
*By process boundary I interpreted that as parent process ID. So when executing a ppid is required.
`python main.py lsthread $ppid`
- Enumerate all the loaded modules within the processes.
`python main.py lsimport $pid`
- Is able to show all the executable pages within the processes.
`python main.py lspages $pid`
- Gives us a capability to read the memory.
`python main.py lsmem $pid`