from scapy.all import IP, ICMP, sr1

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

def send_custom_ping(ip, payload):
    encrypted_payload = caesar_cipher(payload, 13)
    packet = IP(dst=ip) / ICMP() / encrypted_payload
    response = sr1(packet, timeout=2, verbose=False)
    print(encrypted_payload)
    if response:
        print(f"Respuesta recibida desde {response.src}")
    else:
        print("No se recibió respuesta")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Uso: python script.py <IP_destino> <payload>")
        sys.exit(1)
    
    ip = sys.argv[1]
    payload = sys.argv[2]  # No es necesario convertirlo en bytes aquí
    target_ip = ip
    send_custom_ping(target_ip, payload)
