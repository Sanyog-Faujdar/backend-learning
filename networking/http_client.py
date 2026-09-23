#TCP CLIENT SOCKET

import socket

con = socket.socket()
con.connect(("127.0.0.1",8000))

body = '{"name":"Saiam","age":21}'
send_msg = (
    "POST /unknown HTTP/1.1\r\n"
    "Host: 127.0.0.1:8000\r\n"
    "Content-Type: application/json\r\n"
    "Content-Length: 29\r\n"
    "\r\n"
    f"{body}"
    )

con.send(send_msg.encode('UTF-8'))

retrieve_msg = con.recv(1024).decode()
print(retrieve_msg)

con.close()