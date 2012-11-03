import socket


def valid(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

print valid("127.0.0.1")
print valid("fabc:de12:3456:7890:ABCD:EF98:7654:3210")