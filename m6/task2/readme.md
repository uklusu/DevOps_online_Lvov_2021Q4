1)add 3rd machine same way as 2nd machine was aded (create,add port redirect etc)
2)next work on vm1 with dhcp and dns server
1.stop conflict service
 sudo systemctl stop systemd-resolved
2.install dnsmasq via * sudo apt install dnsmasq *  
3.config it as dhcp and dns  sever 

![test2](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m6/task2/images/1.png?raw=true)

2) check dns and dhcp  2
![test3](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m6/task2/images/2.png?raw=true)

3)everything fine and work.
