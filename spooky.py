"""
Lucid 0 Day
Christian DeCoske
07/12/25
The goal of this program is to spoof your ip address;
while delivering a payload.
"""
import subprocess

#data needed to run
target_ip = input(f"What is the target ip address?")
spoof_ip = input(f"What ip address would you like to use?")

#`hping -S --target <ip> --spoof <ip> 
command = ["hping", "-S", "--target", target_ip, "--spoof", spoof_ip]
run = subprocess.run(command, capture_output=True, text=True)
