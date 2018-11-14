import socket

def print_machine_info():
    hsot_name = socket.gethostname()
    ip_address = socket.gethostbyname(hsot_name)
    print("Host name: %s" % hsot_name)
    print("IP address: %s" % ip_address)

if __name__ == '__main__':
    print_machine_info()