import pyshark
import colorama
from colorama import Fore, Style

global_payload = ""

def process_packet(packet):
    global global_payload
    
    if "ICMP" in packet and "IP" in packet:
        icmp_type = packet.icmp.type
        icmp_payload = packet.icmp.data
        
        if icmp_type == "8" and len(icmp_payload) >= 2:
            last_char_hex = icmp_payload[-2:]
            last_char = chr(int(last_char_hex, 16))
            global_payload += last_char
            
            print(f"Received ICMP Request: Last Hex Character - {last_char_hex}, Last Char - {last_char}, Global Payload - {global_payload}")
            
            # Brute force Caesar cipher decryption
            probable_shift = 0
            most_probable_text = ""
            max_score = 0
            
            for shift in range(26):
                decrypted_text = ""
                for char in global_payload:
                    if char.isalpha():
                        shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                        decrypted_text += shifted_char
                    else:
                        decrypted_text += char
                
                score = calculate_score(decrypted_text)
                if score > max_score:
                    max_score = score
                    most_probable_text = decrypted_text
                    probable_shift = shift
                
                print(f"Shift {shift}: Deciphered text: '{decrypted_text}'")
            
            print(f"\nMost Probable Text: {Fore.GREEN}{most_probable_text}{Style.RESET_ALL} (Shift: {probable_shift})")

def calculate_score(text):
    letter_frequencies = {
        'a': 0.1152, 'b': 0.0220, 'c': 0.0402, 'd': 0.0502, 'e': 0.1218, 'f': 0.0069,
        'g': 0.0170, 'h': 0.0070, 'i': 0.0608, 'j': 0.0031, 'k': 0.0047, 'l': 0.0499,
        'm': 0.0315, 'n': 0.0671, 'o': 0.0868, 'p': 0.0248, 'q': 0.0084, 'r': 0.0687,
        's': 0.0798, 't': 0.0463, 'u': 0.0393, 'v': 0.0090, 'w': 0.0002, 'x': 0.0022,
        'y': 0.0090, 'z': 0.0042
    }
    
    score = sum(letter_frequencies.get(char, 0) for char in text)
    return score

def main():
    colorama.init(autoreset=True)
    capture = pyshark.LiveCapture(interface="Wi-Fi", bpf_filter="icmp")
    
    print("Listening for ICMP packets on Wi-Fi interface...")
    for packet in capture.sniff_continuously():
        process_packet(packet)

if __name__ == "__main__":
    main()
