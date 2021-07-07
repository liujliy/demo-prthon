import main_wake_on_lan
import sys


def boot_computer():
    try:
        parameter = "8C-EC-4B-9A-B1-BD"
        if parameter == '-h':
            print(
                '参数使用方法：python3 main_boot_computer.py mac地址\npython3 main_boot_computer.py 98:90:96:C1:FE:CB')
        else:
            print('正在向 ', parameter, ' 发送魔法唤醒包！')
            # mac = '98:90:96:C1:FE:CB'

            mac = main_wake_on_lan.format_mac(parameter)
            send_data = main_wake_on_lan.create_magic_packet(mac)

            main_wake_on_lan.send_magic_packet(send_data)
            return '成功向' + parameter + '发送唤醒包！'
    except ValueError:
        print('未收到传入的参数\n获取帮助：python3 main_boot_computer.py -h')


boot_computer()
