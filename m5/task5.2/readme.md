1)The /etc/passwd file stores essential information, which required during login. In other words, it stores user account information.

2)Os know users by UID(user identifier)  superuser always has 0 ,it saves in passwd file,so to define it just cat  /etc/passwd or use comand "id -u " to find the UID for a particular user . Most Linux distributions reserve the first 100 UIDs for system use New users are assigned UIDs starting from 500 or 1000. For example, new users in Ubuntu start from 1000.  

![test1](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.2/image/1.png?raw=true)

3) GID -group ID , Type the command "id -g " to find the primary GID for a particular user.  Type the command "id -G " to list all the GIDs for a particular user. Replace "" with the user's Unix or Linux username. 1 

![test2](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.2/image/1.png?raw=true)

4)comand *groups* to determine belonging of user to group 1

5)sudo adduser userNameHere ,u need to use comand via sudo 
6) sudo usermod -l newUsername oldUsername to change name ,also  sudo usermod -d /home/newHomeDir -m newUsername to change home dirr
7) skel_dir contains basic structure of home directory
8) userdel userName for deletting user, and  userdel -r userName for deleting home dir mailbox included
9)usermod -L testuser to lock user, usermod -U testuser  to unlock
10)sudo passwd -d  $username to delete password.But if u want to do same with sudo user
open the sudoers configuration file with *sudo visudo*, and add the following line to the file, 

*superuser_name* ALL=(ALL) NOPASSWD:ALL

11)to Display the extended format of information about the directory just type ls -F, and u can see rights for users (rwx) owner,date of last change,amount of hardlinks,weight  

![test2](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.2/image/2.png?raw=true)

12) there is access rights like Read Write and eXecute, they not same for owner,group of owner and others.
13) just type stat *filename* to know owner,group of owner and access rights.
14) for changing owner of file simply use chown,and for changing access mode use chmod comand with options, 
![test3]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.2/image/3.png?raw=true)

15)  octal representation of access rights mean that access right will be shown as numbers where X=1 W=2 R=4 . to see access right as octal representation just type, stat *filename* 
0777 mean full access for everyone (-rwxrwxrwx)  0744 mean that owner can do anything and others only read. Umask show standart access rights for new file, if umask 0002 than file will have 0775 (-rwxrwxrw-)
16)u can add or delete sticky bit with chmod +t ,sticky bit block deleting of file frome everyone exept SU or owner.to delete sticky bit use chmod -t ,example -rwxr-xr-t. As octal stickybit =1 example -rwxr-xr-t
17)  u need to have R attribute in comand script to run it via bash. Or X to run as sudo. Or RX if just run 

![test4](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.2/image/4.png?raw=true)
