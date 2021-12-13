# Task1.
## Part1
1) to login as root u can type sudo -s or sudo -i
2) for changing password u can just use comand sudo passwd *username* 
3) for determining all users in the system u can read passwd file with comand  cat /etc/passwd or u can look just username with cut -d: -f1 /etc/passwd   ,history for determine what comand they execute  1
![test1](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/1.png?raw=true)



4-5) for changing personal info u can use  chfn comand, with -f (change full name) -h (home phone) also u can use man to see some extra keys  
![test2](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/2.png?raw=true)
6) for viewing contens of .bash files page by page or line by line   u just need to type more or less .bash_history   .bash_logout   .bashrc 3 . also u can write ls .bash* to show all bash files. 
8.   for listing content of home directory u can just use ls,if u need something more u can use various keys or alias like ll /home to show hidden files ,long listing format and classify

## Part2 
1)  u cant type "sudo tree root -l 2" for listing root directories and subdirectories up to 2nd level
for listing files with some symbols in name u can use -P or -I key  


![test3]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/5.png?raw=true)


![test4]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/4.png?raw=true)

2) to determine type of file simply use file comand  

![test5]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/6.png?raw=true)


3) cd  for returning to home dir,  also cd for moving to another dir like absolute "cd /home/uklusu " or relative "cd uklusu" . 
4) ls comand will show content of directory -a key show hidden files and -l for long listing format ( show u permissions, owner, date of creating, etc) 


![test7]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/7.png?raw=true)


5) create dirr with "mkdir " put info into file about sudo dirr with sudo "ls /root -l -i -a >file"  view content with cat, copy with cp /home/uklusu  and delete with rm -r  

![test8]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/8.png?raw=true)

6) A symbolic or soft link is an actual link to the original file, whereas a hard link is a mirror copy of the original file. If you delete the original file, the soft link has no value, because it points to a non-existent file.       to create hard link u can use command  ln filename linkname for soft same with key -s . to verify use ls -l  if u change data by soft link,u will change orig file too.  if u delete orig file soft link will stop work.but hard link will stay the same 

![test9]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/9.png?raw=true)

7) for using locate u must install,use sudo updatedb comand and then "locate file" 


![test10]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/10.png?raw=true)


8)  fdisk -l,to  Determine which partitions are mounted in the system, as well as the types of these partitions. Or df    

![tes11]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/11.png?raw=true)

9)grep -c "pattern" my_text_file.txt for counting number of lines  that containt give sequence
10)Just use sudo find /etc -name host


 11)To List all objects in /etc that contain the ss character  sequence at name  "sudo find /etc -name '*ss*' " 12 , or  grep ss /etc/*  to list objects that have ss inside

![test12]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/12.png?raw=true)

13) lshw or lspci to show all devices their types etc
14) to determine the type of file in the system u can just use "file" comand.
15) find . -type f -amin -30  to List the first 5 directory files that were recently accessed in the /etcdirectory.  or ls -t | head -n5 for last 5 files that was modified 

![test5]http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m5/task5.1/image/13.png?raw=true)
