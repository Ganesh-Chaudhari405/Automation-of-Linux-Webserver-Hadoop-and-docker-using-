import os

def main():
    p=20*'*'
    print("\n\n\t\t{}Automation{}\n\n".format(p,p))
    print("Welcome to my program...")  
    while True:
         inp= input("\nWhat do you want\n")
         if inp in "configure hadoop":
            bigdata(inp)
         
         elif inp in "date"or inp in "create directory" or inp in "cal" or inp in "hard disk" or inp in "display IP":
            linuxcmd(inp)
         elif inp in "help" or inp in "help me":
             print("date - for date\ncal - for calender\nconfigure hadoop - for hadoop configuration\ninstall docker - for docker configuration\n")
             print("configure httpd/apache server - configuration of apache server")
             print("exit - close the program")
             print("display IP - used to display IPv4\ncreate directory - used for create directory")
         elif inp in "exit":
             break
         elif inp in "configure httpd server" or inp in "configure apache server":
             web(inp)
         else: 
             print("Enter proper requirement")
             

#linux command automation
def linuxcmd(inp):
  #  inp= input("\nWhat do you want\n")
    if inp in "date" or inp in "tell date" or inp in "show date":
      os.system("date")
    elif inp in "cal" or inp in "calender" or inp in "show calender":
      os.system("cal")
    elif inp in "hard disk" or inp in "disk size":
        os.system("df -h")
    elif inp in "display IP" or inp in "IP" or inp in "ip" or inp in "IPv4":
      os.system("ifconfig")
    elif inp in "create directory":
        di=input("Enter name of directory\n")
        os.system("mkdir {}".format(di))
    elif inp in "create empty file":
        di=input("enter name of file")
        os.system("mkdir {}".format(di))

                
    else:
    	print("Enter correct requirement")
    
#webserver automation
def web(inp):
    if inp in "configure httpd server" or inp in "configure the apache server" or inp in "apache":
        os.system("yum install httpd")
        print("enter page information")
        os.system("vim /var/www/html/index.html")
        os.system("systemctl start httpd")
        os.system("firewall-cmd --add-port=80/tcp")

    else:
        print("enter exact info")


#configure hadoop namenode
def bigdata(inp):


    if inp in "configure hadoop" or inp in "hadoop":      
         

        print("which part of hadoop do you want to configure")
        print("enter 1 for master node and 2 for slave node")
        ik=int(input())
        if ik==1:

            ing=input("enter machine IP")      
            por=input("enter port number")
            os.system("scp jdk-8u171-linux-x64.rpm {}:/".format(ing))
            os.system("ssh {} rpm -i /jdk-8u171-linux-x64.rpm".format(ing))
            os.system("scp hadoop-1.2.1-1.x86_64.rpm {}:/".format(ing))
            os.system("ssh {} rpm -i /hadoop-1.2.1-1.x86_64.rpm --force".format(ing))
            os.system("ssh {} jps".format(ing))
            os.system("mkdir {} /nam".format(ing))
            os.system("rm -rf /hdfs-site.xml")
            os.system("echo  '<?xml version=\"1.0\"?>'>>/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >>/hdfs-site.xml")
            os.system("echo '<configuration>'>>/hdfs-site.xml")
            os.system("echo '<property>'>>/hdfs-site.xml")
            os.system("echo '<name>dfs.name.dir</name>' >>/hdfs-site.xml")
            os.system("echo '<value>/nam</value>' >>/hdfs-site.xml") 
            os.system("echo '</property>' >>/hdfs-site.xml")
            os.system("echo '</configuration>'>>/hdfs-site.xml")
            os.system("scp /hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ing))
            os.system("rm -rf /hdfs-site.xml")
            os.system("echo '<?xml version=\"1.0\"?>' >>/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>'>>/core-site.xml")
            os.system("echo '<configuration>'>>/core-site.xml")   
            os.system("echo '<property>'>>/core-site.xml")
            os.system("echo '<name>fs.default.name</name>' >>/core-site.xml")
            os.system("echo '<value>hdfs://{}:{}</value>' >>/core-site.xml".format(ing,por))
            os.system("echo '</property>' >>/core-site.xml")
            os.system("echo '</configuration>'>>/core-site.xml")
            os.system("scp /core-site.xml {}:/etc/hadoop/core-site.xml".format(ing))
            os.system("rm -rf /core-site.xml")
            os.system("ssh {} hadoop namenode -format".format(ing))
            os.system("ssh {} hadoop-daemon.sh start namenode".format(ing))
            os.system("ssh {} jps".format(ing))
       
        elif ik==2:
            print("Enter IP node which you want to make datanode")
            ig=input("Enter machine IP")
            ing=input("Enter ip of Master node")
            por=input("enter port number")
            os.system("scp jdk-8u171-linux-x64.rpm {}:/".format(ig))
            os.system("ssh {} rpm -i /jdk-8u171-linux-x64.rpm".format(ig))
            os.system("scp hadoop-1.2.1-1.x86_64.rpm {}:/".format(ig))
            os.system("ssh {} rpm -i /hadoop-1.2.1-1.x86_64.rpm --force".format(ig))
            os.system("ssh {} jps".format(ig))
            os.system("mkdir {} /dat1".format(ig))
            os.system("rm -rf /hdfs-site.xml")
            os.system("echo  '<?xml version=\"1.0\"?>'>>/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >>/hdfs-site.xml")
            os.system("echo '<configuration>'>>/hdfs-site.xml")
            os.system("echo '<property>'>>/hdfs-site.xml")
            os.system("echo '<name>dfs.data.dir</name>' >>/hdfs-site.xml")
            os.system("echo '<value>/dat1</value>' >>/hdfs-site.xml") 
            os.system("echo '</property>' >>/hdfs-site.xml")
            os.system("echo '</configuration>'>>/hdfs-site.xml")
            os.system("scp /hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ig))
            os.system("rm -rf /hdfs-site.xml")
            os.system("rm -rf /core-site.xml")
            os.system("echo '<?xml version=\"1.0\"?>' >>/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>'>>/core-site.xml")
            os.system("echo '<configuration>'>>/core-site.xml")   
            os.system("echo '<property>'>>/core-site.xml")
            os.system("echo '<name>fs.default.name</name>' >>/core-site.xml")
            os.system("echo '<value>hdfs://{}:{}</value>' >>/core-site.xml".format(ing,por))
            os.system("echo '</property>' >>/core-site.xml")
            os.system("echo '</configuration>'>>/core-site.xml")
            os.system("scp /core-site.xml {}:/etc/hadoop/core-site.xml".format(ig))
            os.system("rm -rf /core-site.xml")
            os.system("ssh {} hadoop-daemon.sh start datanode".format(ig))
            os.system("ssh {} jps".format(ig))
            os.system("ssh {} hadoop dfsadmin -report".format(ig))









if __name__=="__main__":
    main()
