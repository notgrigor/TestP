#!/usr/bin/python

# 1.Get from the operating system information about its network interface
# (for example ifconfig <interface name>). Parse it to get the MAC address and IPv4 address of that interface.
# You can use https://docs.python.org/3/library/subprocess.html#subprocess.check_output to get stdout
# Example output for ifconfig:
import re
import subprocess

out_example = """enp0s31f6 Link encap:Ethernet  HWaddr 54:ee:75:bc:46:ad
          inet addr:10.3.1.51  Bcast:10.3.255.255  Mask:255.255.0.0
          inet6 addr: fe80::3c57:6367:7504:55e1/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:9923366 errors:0 dropped:33059 overruns:0 frame:0
          TX packets:2162683 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:4225315751 (4.2 GB)  TX bytes:476649014 (476.6 MB)
          Interrupt:16 Memory:e1200000-e1220000"""

MAC = re.search('(?<=HWaddr)(.*)', out_example)
IP = re.search('(?<=inet addr:)(.*)', out_example)
print(MAC.groups()[0].strip())
print(IP.groups()[0][:10])

print(out_example.split('Hwaddr ')[0].split()[4])
print(out_example.split('Bcast:')[0].split()[-1][5:])

proc = subprocess.check_output("ipconfig").decode('utf-8')
####################################################################################################################
# list = []
# for e in proc.split(":"):
#    list.append(e)
# for i in range(len(list)):
#    if list[i] == "da20%18\r\n   IPv4 Address. . . . . . . . . . . ":
#        IPaddress = list[i+1]
#        IPaddress = IPaddress[:10]
#    elif list[i] == " 255.255.255.0\r\n   Default Gateway . . . . . . . . . ":
#        mac = list[i+1] + ":" + list[i+2] + ":" + list[i+3] + ":" + list[i+4] + ":" + list[i+5] + ":" + list[i+6][:4]
####################################################################################################################
# 2.
x = [
    {u'nodeId': u'P1K707183200',
     u'vapsState': [{
         u'realizedOnRadios': [u'5G', u'2.4G'],
         u'wifiNetwork': {u'ssid': u'BELL776', u'encryption': u'WPA-PSK',
                          u'encryptionKey': u'77E9DEECEC5E', u'enabled': True},
         u'vapType': u'home'}]},
    {u'nodeId': u'DM1719903003132',
     u'vapsState': [{
         u'realizedOnRadios': [u'2.4G', u'5GU', u'5GL'],
         u'wifiNetwork': {u'ssid': u'BELL776', u'encryption': u'WPA-PSK',
                          u'encryptionKey': u'77E9DEECEC5E', u'enabled': True},
         u'vapType': u'home'}]},
    {u'nodeId': u'P1K707181700',
     u'vapsState': [{
         u'realizedOnRadios': [u'2.4G', u'5G'],
         u'wifiNetwork': {u'ssid': u'BELL776', u'encryption': u'WPA-PSK',
                          u'encryptionKey': u'77E9DEECEC5E', u'enabled': True},
         u'vapType': u'home'}]},
    {u'nodeId': u'P1K634158400',
     u'vapsState': []}
]


# 2. Write a method, which checks that all nodes (table x elements) return correctly vapsState.
# If there is an element, which does not print its ID. For the rest check that all nodes
# have the same network settings (ssid, encryption and encryption).
# If not raise an exception with custom message: “It does not work again”
def check_nodes(nodes):
    ssid = set()
    encryption = set()
    encryptionK = set()
    for el in nodes:
        state = el["vapsState"]
        if not state:
            print(f'vapState is missing, the nodeId is: {nodes[0]["nodeId"]}')
        else:
            for elements in state:
                network = elements["wifiNetwork"]
                ssid.add(network['ssid'])
                encryption.add(network['encryption'])
                encryptionK.add(network['encryptionKey'])
                if len(ssid) == 1 or len(encryption) == 1 or len(encryptionK) == 1:
                    return True
            else:
                return "It does not work again"


print(check_nodes(x))


# 2a. Write class Animal with 5 attributes (1 string, 1 int, 1 float, 2 methods).
# String and int initialize in the Init method.
class Animal:
    def __init__(self, flt, string="string", integer=0):
        self.string = string
        self.integer = integer
        self.flt = flt

    def print_integer(self):
        return self.integer

    def print_string(self):
        return self.string


# 2b. Write a class Dog, which inherits class Animal with two additional attributes
# (1 string - initialized in Init + 1 additional method)
class Dog(Animal):
    def __init__(self, flt, integer=0, string="string", new_string="new_string"):
        super().__init__(flt, string, integer)
        self.new_string = new_string

    def print_newstring(self):
        return self.new_string


# 2c. Create an instance of class Dog and initialize all required elements.
# Call methods from class Dog and Animal.
an = Animal(1, string="bla", integer=1)
print(an.print_string())
print(an.print_integer())

dg = Dog(1, integer=14, string="string", new_string="new_string")
print(dg.print_integer())
print(dg.new_string)

# List comprehension
a = {'value': [0, 0, 0], 'color': 'black'}
b = {'value': [255, 255, 255], 'color': 'white'}
list_temp = [a, b]

# Filter elements in list_temp that have color 'black' using list comprehension
filtered_list = [x for x in list_temp if x['color'] == 'black']

# Print logs for every element in filtered_list: 'Color: "black" has value: [0, 0, 0]'
for a in filtered_list:
    print(f'The Color: {a["color"]} has a value of: {a["value"]}')
