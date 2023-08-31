from scapy.all import IP, ICMP, send

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

target_ip = ""
original_payload = "Hello, world!"
encrypted_payload = caesar_cipher(original_payload, 13)
packet = IP(dst=target_ip) / ICMP() / f"Encrypted Payload: {encrypted_payload}"

send(packet)
