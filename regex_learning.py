import re

ip_config = """
Windows IP Configuration

   Host Name . . . . . . . . . . . . : Eitan
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : home

Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Intel(R) I211 Gigabit Network Connection
   Physical Address. . . . . . . . . : 00-D8-61-19-FF-8B
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Ethernet adapter Ethernet 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Intel(R) Ethernet Connection (7) I219-V
   Physical Address. . . . . . . . . : 00-D8-61-19-FF-8A
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 8:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter
   Physical Address. . . . . . . . . : 52-3E-AA-AB-FC-A8
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 9:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #2
   Physical Address. . . . . . . . . : 52-3E-AA-AB-F4-A8
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Ethernet adapter VMware Network Adapter VMnet1:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : VMware Virtual Ethernet Adapter for VMnet1
   Physical Address. . . . . . . . . : 00-50-56-C0-00-01
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::98ad:598a:e470:e31f%11(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.139.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Monday, April 27, 2026 18:31:29
   Lease Expires . . . . . . . . . . : Monday, April 27, 2026 20:46:27
   Default Gateway . . . . . . . . . :
   DHCP Server . . . . . . . . . . . : 192.168.139.254
   DHCPv6 IAID . . . . . . . . . . . : 855658582
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2D-30-82-97-00-D8-61-19-FF-8A
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter VMware Network Adapter VMnet8:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : VMware Virtual Ethernet Adapter for VMnet8
   Physical Address. . . . . . . . . : 00-50-56-C0-00-08
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::88ec:ce7b:ff07:f68a%4(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.142.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Monday, April 27, 2026 18:31:29
   Lease Expires . . . . . . . . . . : Monday, April 27, 2026 20:46:28
   Default Gateway . . . . . . . . . :
   DHCP Server . . . . . . . . . . . : 192.168.142.254
   DHCPv6 IAID . . . . . . . . . . . : 872435798
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2D-30-82-97-00-D8-61-19-FF-8A
   Primary WINS Server . . . . . . . : 192.168.142.2
   NetBIOS over Tcpip. . . . . . . . : Enabled

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : home
   Description . . . . . . . . . . . : Broadcom 802.11ac Network Adapter
   Physical Address. . . . . . . . . : 50-3E-AA-AB-FC-A8
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   IPv6 Address. . . . . . . . . . . : 2a0d:6fc0:d29:db00:29c3:d7b5:62dd:5cb0(Preferred)
   Temporary IPv6 Address. . . . . . : 2a0d:6fc0:d29:db00:d8f1:4adc:319f:4445(Preferred)
   Link-local IPv6 Address . . . . . : fe80::9911:54be:3ee8:9aa0%15(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.1.247(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Monday, April 27, 2026 18:32:05
   Lease Expires . . . . . . . . . . : Monday, April 27, 2026 21:02:03
   Default Gateway . . . . . . . . . : fe80::1%15
                                       192.168.1.1
   DHCP Server . . . . . . . . . . . : 192.168.1.1
   DHCPv6 IAID . . . . . . . . . . . : 55590570
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2D-30-82-97-00-D8-61-19-FF-8A
   DNS Servers . . . . . . . . . . . : 192.168.1.1
                                       2001:40a8:809:0:80:179:52:100
                                       2001:40a8:819:0:80:179:55:100
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter vEthernet (WSL (Hyper-V firewall)):

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter
   Physical Address. . . . . . . . . : 00-15-5D-DB-FD-20
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::50dc:673d:af3f:a455%49(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.19.176.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 822089053
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2D-30-82-97-00-D8-61-19-FF-8A
   NetBIOS over Tcpip. . . . . . . . : Enabled"""

# pattern = r"IPv4 Address\.\s\.*.*:\s(?P<ip>\d+\.\d+\.\d+\.\d+)"
# ipv4_addresses = re.findall(pattern,ip_config)
#
# print(ipv4_addresses)


ip_a_output = """
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet 10.255.255.254/32 brd 10.255.255.254 scope global lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host proto kernel_lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1488 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:4f:cb:ec brd ff:ff:ff:ff:ff:ff
    inet 172.19.187.64/20 brd 172.19.191.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fe4f:cbec/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether ca:b7:72:31:85:c7 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::c8b7:72ff:fe31:85c7/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
4: br-eae6ad2cb1c7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether fe:40:5e:31:12:c1 brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-eae6ad2cb1c7
       valid_lft forever preferred_lft forever
    inet6 fc00:f853:ccd:e793::1/64 scope global nodad
       valid_lft forever preferred_lft forever
    inet6 fe80::fc40:5eff:fe31:12c1/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
5: vethe2a64b5@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default
    link/ether 0a:a4:1d:f4:f2:69 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::8a4:1dff:fef4:f269/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
6: veth59a51eb@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-eae6ad2cb1c7 state UP group default
    link/ether 6e:ee:fa:ab:85:da brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::6cee:faff:feab:85da/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
"""



regex_pattern = r"inet\s(?P<ip>\d+\.\d+\.\d+\.\d+)"

for ipv4 in re.finditer(regex_pattern, ip_a_output):
    print(ipv4)
