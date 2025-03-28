import subprocess
import sys

def varredura_nmap(ip):
    try:
        comando = ["nmap", "-sV", ip]        
        resultado = subprocess.check_output(comando, stderr=subprocess.STDOUT, universal_newlines=True)        
        print(resultado)
    
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o Nmap: {e.output}")
    except FileNotFoundError:
        print("Nmap não encontrado. Certifique-se de que o Nmap está instalado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if len(sys.argv) != 2:
    sys.exit(1)

ip_alvo = sys.argv[1]

varredura_nmap(ip_alvo)
