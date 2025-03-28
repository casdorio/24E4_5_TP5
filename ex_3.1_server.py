import socket
import ssl


def run_tls_server(host='127.0.0.1', port=8443, certfile='certificado.pem', keyfile='chave.pem'):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    print(f"Servidor TLS: aguardando conexões em {host}:{port}...")

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)

    while True:
        try:

            client_sock, client_addr = sock.accept()

            ssl_client = context.wrap_socket(client_sock, server_side=True)
            print(f"Conexão estabelecida com {client_addr}")

            data = ssl_client.recv(1024)
            print("Recebido:", data.decode())

            ssl_client.sendall(data)
            ssl_client.close()
        except Exception as e:
            print("Erro no servidor:", e)
            break


if __name__ == '__main__':
    run_tls_server()