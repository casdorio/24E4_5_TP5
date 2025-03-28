from scapy.all import ARP, sniff

ip_mac_map = {}

def detectar_arp_spoofing(pkt):
    if pkt.haslayer(ARP):
        ip = pkt.psrc
        mac = pkt.hwsrc

        if ip in ip_mac_map:
            if ip_mac_map[ip] != mac:
                print(f"Alerta: Possível ARP Spoofing detectado para IP {ip}!")
                print(f"MAC anterior: {ip_mac_map[ip]}, MAC atual: {mac}")
        else:
            ip_mac_map[ip] = mac

def monitorar_arp():
    print("Monitorando pacotes ARP. Pressione Ctrl+C para parar.")
    sniff(prn=detectar_arp_spoofing, filter="arp", store=0)

monitorar_arp()
