import socket
import threading

"""
    A convenience class to handle strings the way RESP (REdis Serialization Protocol) expects it
"""
class RESPString:
    def __init__(self, s: str) -> None:
        self.s = s
    def str_as_simple_string(self) -> str:
        return f"+{self.s}\r\n"
    def bulk_str_to_list(self):
        return self.s.split("\r\n")

PING_RESP_STR = RESPString("PONG").str_as_simple_string()

def get_cmd_response(cmd, args):
    if cmd == "echo":
        return "".join(args)
    elif cmd == "ping":
        return PING_RESP_STR

def process_connection(client_connection: socket):
    while True:
        try:
            req_RESP_str = RESPString(client_connection.recv(1024).decode()) # The server receives data from the client connection.
            req_list = req_RESP_str.bulk_str_to_list()
            cmd, args = req_list[2].lower(), req_list[4::2]
            
            formatted_response = get_cmd_response(cmd, args)
            
            client_connection.send(formatted_response.encode())
        except ConnectionError:
            break

def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client_connection, _ = server_socket.accept() # main waits for a new client connection.
        threading.Thread(target=process_connection, args=(client_connection,)).start() # new thread is created to process the new connection, and we start it.

if __name__ == "__main__":
    main()