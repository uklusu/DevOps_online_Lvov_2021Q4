Networking with Linux

1) 1. create conection, add nat + internal to vm1, add internal to vm2,and conect vm 2 to internet via vm1.
2. add ip addres to both machines for subnet,
via ifconfig enp0s3 *ip* netmask 255.255.255.0,
3 .  open forwarding on VM1 via         
sudo echo 1 > /proc/sys/net/ipv4/ip_forward
4. config VM2 , add route via *sudo ip route add default 192.168.1.1 via enp0s3* .Also add DNS with comand   *sudo echo namerserver 8.8.8.8 >> /etc/resolv.conf *
5. Add iptables rules for forward trafic to host VM2 and Masquerade trafic from VM2  
sudo iptables -t nat - A POSTROUTING -o enp0s3 -j MASQUERADE
sudo iptables -t nat -A PREROUTING -i enp0s3 -p tcp --dport 2223 -j DNAT --to-destination 192.168.1.10:22   

![test2](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m6/task1/images/1.png?raw=true)


3)check route from vm2 to host, and ping 8.8.8.8 to check internet conection

![test2](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m6/task1/images/2.png?raw=true)


4)for finding owner of 8.8.8.8 i used comand whois 8.8.8.8  

![test2](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m6/task1/images/3.png?raw=true)


5) for finding ip of epam com i used comand dig epam.com 

![test1](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m6/task1/images/4.png?raw=true)


6) to show routes and gate on host i used comand 
ip route list              

 ![test2](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m6/task1/images/5.png?raw=true)

7) and for trace i used traceroute 8.8.8.8
