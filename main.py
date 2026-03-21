import socket
import ssl
from urllib.parse import urlparse


class Client:
    def __init__(self, url) -> None:
        self.url = urlparse(url)
        self.connection = None

    def open(self):
        hostname = self.url.hostname
        port = self.url.port
        clear_socket = socket.create_connection((hostname, port), timeout=1)
        if self.url.scheme == "https":
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = True
            encrypted_socket = ssl_context.wrap_socket(
                clear_socket,
                server_hostname=hostname,
            )
            self.connection = encrypted_socket
        else:
            self.connection = clear_socket

    def send(self, message):
        print(message)
        self.connection.sendall(message.encode("utf-8"))
        print("-----")
        max_response_size = 1024
        response = self.connection.recv(max_response_size)
        response = response.decode("utf-8", errors="replace")
        print("-----")
        print(response)

    def close(self):
        self.connection.close()


def main():
    url = "https://dmerej.info:443"

    client = Client(url)
    client.open()

    message = "GET / HTTP/1.1\r\n"

    client.send(message)

    client.close()


if __name__ == "__main__":
    main()
