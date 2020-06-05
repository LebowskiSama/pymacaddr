# pyprobe
A simple pet python project to find all hostnames and mac addresses connected to a given local network using socket and getmac currently supported exclusively on linux based distros.</br>

# Usage
pip install -r requirements.txt</br>
python pyprobe.py</br>
python pyprobe -m , if you want to monitor the local network space continuously with a default delay of 1s.

# Limitations
The script only detects local ips in the range 192.168.0.xxx and 192.168.1.xxx where xxx ranges from 0-255, which, should suffice for local home networks that typically use common subnetting  255.255.255.0</br></br>

It thus, only works on local ip's in the range 192.168.0.(0-255) and 192.168.1.(0-255) which are the most commonly assigned local <b>HOME</b> addresses.
  
# DISCLAIMER
This script might not work in non-home networks / an office setup. It's a casual prober written with home users in mind.</br>
Anybody having any corrections or valuable additions are welcome to contribute.
