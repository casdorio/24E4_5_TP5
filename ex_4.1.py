from scapy.all import ARP, Ether, srp

def scan_rede(rede):
    arp_request = ARP(pdst=rede)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = ether_frame / arp_request

    resposta, _ = srp(pacote, timeout=2, verbose=False)

    if resposta:
        print("\nHosts ativos na rede:")
        for _, recebido in resposta:
            print(f"IP: {recebido.psrc}, MAC: {recebido.hwsrc}")
    else:
        print("\nNenhum host ativo encontrado na rede.")

rede_alvo = "172.17.0.0/16"

scan_rede(rede_alvo)
