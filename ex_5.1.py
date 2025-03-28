import dns.resolver

def coletar_registros_dns(domínio):
    try:
        print("Registros A:")
        respostas_a = dns.resolver.resolve(domínio, 'A')
        for rdata in respostas_a:
            print(f"  {rdata.to_text()}")

        print("\nRegistros MX:")
        respostas_mx = dns.resolver.resolve(domínio, 'MX')
        for rdata in respostas_mx:
            print(f"  {rdata.preference} {rdata.exchange.to_text()}")

        print("\nRegistros NS:")
        respostas_ns = dns.resolver.resolve(domínio, 'NS')
        for rdata in respostas_ns:
            print(f"  {rdata.to_text()}")

    except dns.resolver.NoAnswer:
        print(f"Nenhuma resposta encontrada para o domínio: {domínio}")
    except dns.resolver.NXDOMAIN:
        print(f"O domínio {domínio} não existe.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

domínio = "ways.us"
coletar_registros_dns(domínio)
