# Task 7.1 scripts

## Part A (Ascript) can scan host open ports,hostname and ip of other devices
![test1](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m7/task1/images/1.png?raw=true)

#!/bin/bash
#this function list open tcp ports on host
function portscan
{
         echo " next ports are open: "
         ss -ant
}
# This function show ip and names at network
function netscan
{
# check if NMAP installed
test -e /usr/bin/nmap
if [[ "$?" == "0" ]]
then
      echo "NMAP installed,scaning network"
else
      echo "trying to install NMAP"
            sudo apt install nmap -y
fi
# perform scaning network with nmap
           addr=$1
           echo "next hosts being found in this network"
           nmap -sP $addr | awk 'NR % 2 == 0 {print "Hostname:" $5 "   " "ip adress:" $6}' | sed 's/(//g; s/)//g'
           }
           # this part for showing keys when starting without parametrs
if [[ "$#" == "0" ]]
then 
              echo " u can use such keys: "
              echo "for displaying ip and names for all hosts in curent subnet use  --all" 
              echo "for displaying list of open tcp ports use   --target net ip"
              exit 0 
fi 
# part where script check input parametrs
if [ "$1" == "--all" ]
then
       portscan 
 elif [ "$1" == "--target" ]
 then
      netscan $2
fi


## Part B (Bscript) Can parse apach log and give various info ,like most popular pages,ip request ,etc

![test3](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m7/task1/images/2.png?raw=true)



#!/bin/bash

#show most popular ip
function mip
{
             if [[ -z "$1" ]]
             then
                   echo  "please specify log file"
                   exit 0

             fi 
             logname=$1       
             awk '{ print $1}' $logname | sort | uniq -c | sort -nr | head -n 1 |   awk '{print " Most request was frome this ip: "  $2}'

             
}

#show most popular page
function pages
{
             if [[ -z "$1" ]]
             then
                   echo  "please specify log file"
                   exit 0
             elif [[ -z "$2" ]]
             then
                   echo "please specify amount of pages"
                   
                 exit 0
             fi 
             logname=$1       
             echo "most $2 popular pages"
             awk '{ print $7}' $logname | sort | uniq -c | sort -nr | head -n $2 | sed 's/\///g'
}

# show amount of requests frome each ip

function popular
{
             if [[ -z "$1" ]]
             then
                   echo  "please specify log file"
                   exit 0
             elif [[ -z "$2" ]]
             then
                   echo "please specify ip amount"
                   
                 exit 0
             fi 
             logname=$1       
             echo "was so much requests frome such ip "
            awk '{ print $1}' $logname | sort | uniq -c | sort -nr | head -n $2 |   awk '{print " was "  $1 " requests frome ip: " $2}'

}

#show non existing pages that were refered to
function er404
{ 
 if [[ -z "$1" ]]
             then
                   echo  "please specify log file"
                   exit 0
                   
                 fi      
                logname=$1    
               echo  "list of non existing pages that were refered to"
            awk '$9 == "404" { print $7 }' $1 | sort | uniq
  }
  
  #this show What time did site get the most requests
  function time
{
             if [[ -z "$1" ]]
             then
                   echo  "please specify log file"
                   exit 0
          

             fi 
             logname=$1       
             echo "site"
            awk '{ print $4 }' $1 | cut -d":" -f2,3 | uniq -c | sort -nr | head -1 | awk '{ print $2 }'
}

 function bot
{
             if [[ -z "$1" ]]
             then
                   echo  "please specify log file"
                   exit 0
          

             fi 
             logname=$1       
             echo "such search bot have accesed the site"
            cat $logname | awk '/bot/ {print $1, $12, $14, $15, $16}' | sort | uniq | awk '{print $1, $2, $3, $5}' | sort | uniq | sed 's/\"//g' | head -n $2

}

#this show list of keys for script
if [[ "$#" == "0" ]]

   then
         echo "u must use agrument name of script and amount of lines if needed [--argument] [filename] [number_of_lines]"
         echo "to use this script u can use next arguments "
         echo "to display frome which ip was most arguments use [--mip] [filename] "
         echo "to display most popular page use --pages filename amount of pages"
         echo "to show amount of request frome each ip use --popular filename amount of pages"
         echo "to show show non existing pages that were refered to use --er404 filename "
         echo "to  show what time did site get the most requests use --time filename"
         echo "to show what search bot have accesed the site use --bot filename "
         exit 0
         fi
         
        # part of script where is cheking input parametrs
        if [ "$1" == "--mip" ]
        then 
             mip 
             
         elif [ "$1" == "--pages" ]
         then 
         pages 
         
         elif [ "$1" == "--popular" ]
         then 
         popular 
         
         elif [ "$1" == "--er404" ]   
         then 
                 er404 
          elif [ "$1" == "--time" ]
          then
               time 
          elif [ "$1" == "--bot" ]
          then
          bot 
         fi    




## Part C (Cscript) Make backup of any folder and files inside,and write changes into log file

![test9](http://github.com/uklusu/DevOps_online_Lvov_2021Q4/blob/master/m7/task1/images/3.png?raw=true)

#!/bin/bash
#this part check input
if [[ "$#" == "0" ]]
then
          echo "example of using script ./Cscript [path to source folder] [path to destination folder]"
          exit 0
elif ! [[ -d $1 ]]
then 
          echo "source directory not exist "
          exit 0
          
elif [[ -z $2 ]] 

then
          echo  "u must specify destination folder"
          exit 0
 elif ! [[ -d $2 ]]
 then
            echo "Destination directory is absent,trying to create $2 "
            mkdir $2 
            echo "directory $2 created "
        fi
        
#Set parametrs 
srcdir=$1
dstdir=$2
log=$dstdir/backup.log
tmpdir=$dstdir/tmp
if ! [[ -d $tmpdir ]] ; then
 mkdir $tmpdir 
 fi
 touch $dstdir/backup.log
 touch $tmpdir/ls.tmp;
 touch $tmpdir/snapshot.tmp;
 ls $srcdir > $tmpdir/ls.tmp
 
 #logging part
 
 dt=$(date '+%d.%m.%Y_%H:%M::%S');
 for var1 in $(diff -y --suppress-common-lines $tmpdir/ls.tmp $tmpdir/snapshot.tmp | awk '{print $1 }' | sed 's/>//g; /^[[:space:]]*$/d')
 do
              echo "$dt CREATED $var1" >> $log
              tar -rvf $dstdir/Backup.tar $srcdir/$var1 > /dev/null 
              echo " $dt BACKUPED $var1 " >> $log
              done
              echo " Backuped "
              
              
              for var2 in $(diff -y --suppress-common-lines $tmpdir/ls.tmp $tmpdir/snapshot.tmp | awk '{print $2 $3}' | sed 's/<//g; /^[[:space::]]*$/d; s/|//g')
              do
              
              echo " $dt DELETED $var2" >> $log
              done
              
              rm -rf $tmpdir/ls.tmp;
              ls $srcdir > $tmpdir/snapshot.tmp
              
