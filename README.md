# Step By Step guide for Hadoop installation on Ubuntu 16.04.3 with MapReduce example using Streaming

1. Download Virtual Box from: https://www.virtualbox.org/wiki/Downloads
![](https://github.com/maniraniyal/BigData/blob/master/A1.png?raw=true)


2. Download Ubuntu 16.04.3 (desktop version **amd64**) from: https://www.ubuntu.com/download/desktop
   OR 
   Direct Download from: http://mirror.pnl.gov/releases/xenial/ubuntu-16.04.3-desktop-amd64.iso
![](https://github.com/maniraniyal/BigData/blob/master/A4.png?raw=true)


3. create a VM with Ubuntu 16.04.3 image
![](https://github.com/maniraniyal/BigData/blob/master/A3.png?raw=true)


4. After installing Ubuntu login to th VM and follow instructions given in https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html . **Here I am giving step by step details for the installation steps.**


5. First we will update the system's local repository and then install JAVA (default JDK). Run below commands on the terminal.

   **sudo apt-get update**
   
   **sudo apt-get install default-jdk -y**
![](https://github.com/maniraniyal/BigData/blob/master/7.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/8.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/9.png?raw=true)


6. Now we will install ssh and rsync packages by running following commands.

   **sudo apt-get install ssh -y**
   
   **sudo apt-get install rsync -y**
![](https://github.com/maniraniyal/BigData/blob/master/10.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/11.png?raw=true)


7. Now download Hadoop **2.7.4** from http://www.apache.org/dyn/closer.cgi/hadoop/common/
![](https://github.com/maniraniyal/BigData/blob/master/download_hadoop.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/12.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/13.png?raw=true)


8. Change directory to Downloads or where ever you have downloaded the hadoop tar file. In my case it is in Downloads and all further instruction are considering that hadoop tart file is in ~/Downloads.
![](https://github.com/maniraniyal/BigData/blob/master/14.png?raw=true)


9. Change directory to extracted folder 
![](https://github.com/maniraniyal/BigData/blob/master/15.png?raw=true)


10. Update JAVA_HOME variable in etc/hadoop/hadoop-env.sh file using gedit command as shown below.

   **export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")**
![](https://github.com/maniraniyal/BigData/blob/master/22.png?raw=true)


11. Now you should be able to run hadoop; check it by running below command

   **bin/hadoop**
![](https://github.com/maniraniyal/BigData/blob/master/16.png?raw=true)


12. Now we will update some configuration files for pseudo-distributed operation. First we will edit **etc/hadoop/core-site.xml** file as below.

   `<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
   </configuration>`
![](https://github.com/maniraniyal/BigData/blob/master/18_1.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/18.png?raw=true)


13. Similarly, we will update **etc/hadoop/hdfs-site.xml** file as below.

`<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>`
![](https://github.com/maniraniyal/BigData/blob/master/19.png?raw=true)


14. Now we will setup passwordless ssh for Hadoop. First check if you already have passwordless ssh authentication setup; if it is new Ubuntu installation most likely it wouldn't set up. If passwordless ssh authentication is not setup, please follow next step othervise skip it.

   **ssh localhost**
   
![](https://github.com/maniraniyal/BigData/blob/master/20.png?raw=true)


15. run below commands:

  **ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa**
  
  **cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys**
  
  **chmod 0600 ~/.ssh/authorized_keys**
  
![](https://github.com/maniraniyal/BigData/blob/master/21.png?raw=true)


16. Now we will start NameNode and DataNode but before that we will format the HDFS file system.
![](https://github.com/maniraniyal/BigData/blob/master/23.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/24.png?raw=true)


17. Now we can access Web-interface for NameNode at http://localhost:50070/
![](https://github.com/maniraniyal/BigData/blob/master/25.png?raw=true)


18. Now let's create some directories in HDFS filesystem.
![](https://github.com/maniraniyal/BigData/blob/master/26.png?raw=true)


19. Let's download one html page http://hadoop.apache.org and upload into HDFS file system.

   **wget http://hadoop.apache.org -O hadoop_home_page.html**
![](https://github.com/maniraniyal/BigData/blob/master/27.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/28.png?raw=true)

**Please note that HDFS file system is not same as root file system.**
![](https://github.com/maniraniyal/BigData/blob/master/30.png?raw=true)

# Grep example:
20. For this example we are using **hadoop-mapreduce-examples-2.7.4.jar** file which comes along with Hadoop. In this example we are trying to count the total number of 'https' word occurences in the given files. First we run the Hadoop job then copy the results from HDFS to the local file system.
![](https://github.com/maniraniyal/BigData/blob/master/35.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/36.png?raw=true)
We can see that there are 2 occurences of https in the given file and same we can validate using wget command.


# Wordcount example:
21. For wordcount example also we are using **hadoop-mapreduce-examples-2.7.4.jar** file. The wordcount example returns the count of each word in the given documents.
![](https://github.com/maniraniyal/BigData/blob/master/33.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/34.png?raw=true)


# Wordcount using Hadoop streaming (python)
21. Here is mapper and reducer program for wordcount.
![](https://github.com/maniraniyal/BigData/blob/master/39.png?raw=true)


22. We run the program as below and the copy the result to local file system. 
![](https://github.com/maniraniyal/BigData/blob/master/37.png?raw=true)
![](https://github.com/maniraniyal/BigData/blob/master/38.png?raw=true)
