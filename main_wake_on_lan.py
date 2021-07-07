import socket
import binascii
import struct
import re

'''
格式化mac地址，生成魔法唤醒包，然后发送。
mac格式： mac = A1B2C3D4E5F6
唤醒包格式： send_data = binascii.unhexlify('FF'*6 + str(mac)*16)
'''

MAC = "8C-EC-4B-9A-B1-BD"


# MAC = "98-90-96-C1-FE-CB"


# 格式化MAC地址989096C1FECB为这种形式
def format_mac0(mac):
    if len(mac) == 12:
        pass
    elif len(mac) == 17:
        if mac.count(':') == 5 or mac.count('-') == 5:
            sep = mac[2]
            mac = mac.replace(sep, '')
        else:
            raise ValueError('Incorrect MAC format')
    else:
        raise ValueError('Incorrect MAC format')
    return mac


def format_mac(mac):
    mac_re = re.compile(r'''
                      (^([0-9A-F]{1,2}[-]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[:]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[.]){5}([0-9A-F]{1,2})$
                      )''', re.VERBOSE | re.IGNORECASE)
    # print(re.match(mac_re, mac))
    if re.match(mac_re, mac):
        if mac.count(':') == 5 or mac.count('-') == 5 or mac.count('.'):
            sep = mac[2]
            mac_fm = mac.replace(sep, '')
            return mac_fm
    else:
        raise ValueError('Incorrect MAC format')


# 方法一：将989096C1FECB格式的mac地址创建唤醒包
def create_magic_packet0(mac):
    data = b'FF' * 6 + (mac * 16).encode()
    print(data)

    print(type(data))
    send_data = b''
    for i in range(0, len(data), 2):
        # int(data[i: i+2], 16) 把16进制转换成整数
        send_data = send_data + struct.pack(b'B', int(data[i: i + 2], 16))
    print(type(send_data))
    return send_data


# 方法二：将989096C1FECB格式的mac地址创建唤醒包，使用binascii.unhexlify()方法
def create_magic_packet(mac):
    data = 'FF' * 6 + str(mac) * 16
    # print(data)
    # print(type(data))
    send_data = binascii.unhexlify(data)
    # print(type(send_data))
    return send_data


def send_magic_packet(send_data):
    # broadcast_address = '192.168.255.255'
    broadcast_address = '10.45.19.255'
    port = 9
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(send_data, (broadcast_address, port))


# print('mac地址：', format_mac(MAC))
mac = format_mac(MAC)
send_data = create_magic_packet(mac)
# print(send_data)
send_magic_packet(send_data)
