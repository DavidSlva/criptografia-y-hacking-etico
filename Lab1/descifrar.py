import pyshark
import sys

# Abecedario en minúsculas
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def is_valid_letter(char):
    # Verifica si el carácter es una letra del abecedario
    return char in alphabet

def caesar_cipher_decrypt(char, shift):
    if char in alphabet:
        # Decodificar utilizando el cifrado César
        index = alphabet.index(char)
        decrypted_index = (index - shift) % 26
        return alphabet[decrypted_index]
    else:
        # Si no es una letra del abecedario, devolver tal cual
        return char

def process_icmp_packet(packet, shift):
    try:
        icmp_data = packet.icmp.data
        if icmp_data and len(icmp_data) >= 2:
            # Obtener el byte menos significativo y convertirlo a carácter
            byte_value = int(icmp_data[-2:], 16)
            char = chr(byte_value)
            
            if is_valid_letter(char):
                decrypted_char = caesar_cipher_decrypt(char, shift)
                print(decrypted_char)
    except Exception as e:
        pass

def main():
    if len(sys.argv) != 2:
        print("Uso: python sniffer.py <corrimiento_cesar>")
        sys.exit(1)
    
    try:
        shift = int(sys.argv[1])
    except ValueError:
        print("El corrimiento César debe ser un número entero.")
        sys.exit(1)
    
    # Capturar paquetes ICMP en la interfaz de red
    cap = pyshark.LiveCapture(interface='Wi-Fi', bpf_filter='icmp[icmptype] == icmp-echo')

    print("Iniciando el sniffer. Presiona Ctrl+C para detenerlo.")
    
    try:
        for packet in cap.sniff_continuously():
            process_icmp_packet(packet, shift)
    except KeyboardInterrupt:
        print("Sniffer detenido.")

if __name__ == "__main__":
    main()
