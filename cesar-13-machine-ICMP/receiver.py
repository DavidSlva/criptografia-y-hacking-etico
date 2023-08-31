from scapy.all import sniff, ICMP
import re

def caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def packet_handler(packet):
    if ICMP in packet:
        payload = packet[ICMP].load.decode()
        match = re.match(r'^Encrypted Payload: (.+)$', payload)
        if match:
            encrypted_payload = match.group(1)
            decrypted_payload = caesar_cipher(encrypted_payload, 13)
            print(f"Received: {decrypted_payload}")

sniff(filter="icmp", prn=packet_handler)
