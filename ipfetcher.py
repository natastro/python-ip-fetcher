# Project from https://theinsightfulcoder.com/5-more-python-projects-that-can-be-built-in-under-5-minutes

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print("Computer Name:" + hostname)
print("IP address:" +IP)