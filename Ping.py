# coding=utf-8
import ipaddress, datetime, socket, time
from subprocess import Popen, PIPE

#return Time 
def getTimeNow():
    zeit = str(datetime.datetime.now())
    return zeit[:19]

startTime = time.time()
#Create new document or continue
document = open("NetworkPing.txt", "a")
document.write(getTimeNow() + "\n")

#Ping each host in network and write down IP and Time
network = ipaddress.ip_network(u"192.168.1.0/24")
for i in network.hosts():
    i = str(i)
    toping = Popen(["ping", "-c", "1", "-W", "1", i], stdout=PIPE)
    output = toping.communicate()[0]
    hostalive = toping.returncode
    if hostalive == 0:
        try:
                sock = socket.gethostbyaddr(i)
                document.write("{} {} {} {}".format(getTimeNow(), i, sock[0], "\n"))
        except:
                document.write("{} {} {} {}".format(getTimeNow(), i, "Except", "\n" ))

document.write("Duration of the entire scan: " + str(int(0.5+(time.time() - startTime))) + " seconds\n")
document.close()








