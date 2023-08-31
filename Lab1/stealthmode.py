import socket
import struct
# python3 .\stealthmode.py 192.168.1.1 12

def ping(host, byte):
    """
    Envia un ping a un host con el bit menos significativo modificado.

    Args:
        host: El host al que enviar el ping.
        byte: El byte a agregar al bit menos significativo.
    """

    # Crear un socket ICMP.
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    # Construir el paquete ICMP.
    icmp_header = struct.pack(">BBHHH", 8, 0, 0, 0, 0)
    icmp_payload = struct.pack(">B", byte)
    packet = icmp_header + icmp_payload

    # Enviar el paquete ICMP.
    print(sock.sendto(packet, (host, 80)))

def main():
    """
    Programa principal.
    """
    import sys
    
    if len(sys.argv) != 3:
        print("Uso: python script.py <IP_destino> <payload>")
        sys.exit(1)
    
    ip = sys.argv[1]

    # Obtener la cadena de entrada.
    string = sys.argv[2]

    # Separar la cadena por letras.
    letters = list(string)

    # Enviar un ping a cada letra.
    for letter in letters:
        ping(ip, ord(letter))

if __name__ == "__main__":
    main()