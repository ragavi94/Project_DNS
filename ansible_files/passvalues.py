import os
import subprocess
import configparser
import json
import random


create_container_ansible = '~/jaga/try_ansible/ansible_files/check.yaml'
dns_list = ["dns1", "dns2"]
veth_list = ["dns1l2br0", "dns2l2br10"]
bridge_list = ["l2br", "l2br1"]
net1_servers = [{'hostname': 'www.csc', 'ip': '192.168.10.5'},{'hostname': 'www.ece', 'ip': '192.168.10.4'}]

net_server_list= [[{'ip': '192.168.10.5', 'hostname': 'www.csc'}, {'ip': '192.168.10.4', 'hostname': 'www.ece'}], [{'ip': '192.168.20.4', 'hostname': 'www.csc'}, {'ip': '192.168.20.6', 'hostname': 'www.csc'}, {'ip': '192.168.20.5', 'hostname': 'www.ece'}]]

print("net1_server: " + str(net1_servers)+ "\r\n")

print("net_server_list: " + str(net_server_list))
#args_pass = "\'{'container_names': "+ str(dns_list) + ", 'veth_names': " + str(veth_list) + ", 'net1_servers': " + str(net1_servers) + " }\'"

args_pass = "\'{'net_server': " +str(net_server_list) + " }\'"
os.system("sudo ansible-playbook "+create_container_ansible+" -e " + args_pass)



