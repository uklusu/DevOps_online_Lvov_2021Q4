1) linux process can have such status as : Running (R ,Stopped (T),Interruptable sleep (D, Uninterruptable sleep(S), Zombie(Z). to see all proceses u need to type * Ps -aux *
2)pstree comand display a tree of proccess 

![test1](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.3/image/1.png?raw=true)

3) Proc file system (procfs) is virtual file system created on fly when system boots and is dissolved at time of system shut down.
It contains useful information about the processes that are currently running, it is regarded as control and information center for kernel.
The proc file system also provides communication medium between kernel space and user space.
4)lscpu to get info about cpu    

![test2](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.3/image/2.png?raw=true)

5)ps -au to get all info about proceses for curent user

![test3](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.3/image/3.png?raw=true)

6) kernel process = system process,usualy have id=2 we can see it with comand sudo pstree2,This is all processes frome kthreadd. all others procceses gona be userproc ,we can print it with ps -N --ppid=2 --pid=2 comand.


7) ps -aux to print all processes , 

![test5](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.3/image/5.png?raw=true)

8) to list processes only for specific user u can use ps =au *username*
9) to analyse existing running tasks we can use pgrep, pstree, top, proc
10)The  top  program  provides  a dynamic real-time view of a running system.  It can display system summary information as well as a list of processes or threads currently being managed by the Linux kernel.  The types of system summary information shown and the types, order and size of information displayed for processes are all user configurable and that configuration can be made persistent across restarts. 

![test6](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.3/image/6.png?raw=true)

11) to display "top" command for a specific user just add -u key with username ex. top -u uklusu
12) there is such interactive comands as
d | s  :Change-Delay-Time-interval
              You will be prompted to enter the delay time, in seconds,
              between display updates.
k  :Kill-a-task
              You will be prompted for a PID and then the signal to
              send.
 l  :Load-Average/Uptime toggle
              This is also the line containing the program name
              (possibly an alias) when operating in full-screen mode or
              the `current' window name when operating in
              alternate-display mode.
u - sort process by username
To sort all Linux running processes by Memory usage, press M and P keys.
Press ‘c‘ option in running top command will display the absolute path of the running process.
L -search by word
V - display processes as tree
and many many others...
13) for sorting press shift+f and just chose what sorting u need with S button after that press enter . 

![test7](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.3/image/7.png?raw=true)


![test8](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.3/image/8.png?raw=true)

14) process prio -  is how many CPU time will be given for process compared to others, it have value frome 19 to -20. example of command  nice -n 17 processname. Or renice via PID,  sudo renice -n5 -p 455332
15) we can change process prio with top via r key, then type PID and value.
16)we can kill process with "kill" comand using kill PID. kill -L to list all signals that can be send via kill comand. u can send it by adding number or name of signal to kill comand like " kill -9 1211" to send kill signal to PID 1211. or "kill -KILL 1211" or "kill -SIGKILL 1211"
17) jobs command can show u what comands exist in current session. fg bring stopped comand frome background to foreground. bg do oposite thing.  nohup - run a command immune to hangups, with output to a non-tty. 

![test9](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.3/image/9.png?raw=true)

Part 2
1) in ms Windows u can following comand in ssh ssh user@host - to conect to remote host via ssh .  ssh-keygen to generate keygen

ssh-keygen - for generating ssh key

![test10](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.3/image/10.png?raw=true)

2) to increase security we can use strong passwords, use Private keys for Authentification, disable Root Logins, also change port to nonstandart.
3) there is such options for key encript : rsa ,dsa,ecdsa,ecdsa-sk,ed25519. we can use them by adding -t encryptname. like ssh-keygen -t dsa  or ssh-keygen -t ed25519
4) for creating port forwarding to virt machine we must just add at network settings,nat - advanced - port forwarding


