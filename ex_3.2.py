import socket
import ssl

def run_tls_client_with_logging(server_host='127.0.0.1', server_port=8443,
                                message="Mensagem segura com logging de pacotes"):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    ssl_sock = context.wrap_socket(sock, server_hostname=server_host)
    ssl_sock.connect((server_host, server_port))
    print("Cliente: conexão estabelecida")

    original_send = ssl_sock.send
    original_recv = ssl_sock.recv


    def patched_send(data, *args, **kwargs):
        print("Interceptado (envio):", data)
        return original_send(data, *args, **kwargs)


    def patched_recv(bufsize, *args, **kwargs):
        data = original_recv(bufsize, *args, **kwargs)
        print("Interceptado (recebido):", data)
        return data

    ssl_sock.send = patched_send
    ssl_sock.recv = patched_recv

    ssl_sock.send(message.encode())

    data = ssl_sock.recv(1024)
    print("Cliente: recebido:", data.decode())

    ssl_sock.close()


if __name__ == '__main__':
    run_tls_client_with_logging()