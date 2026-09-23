# python TCP Server
# ser → listening socket that accepts incoming connections.
# con → connection socket representing the connection between your server and one particular client.

import socket
import json

ser = socket.socket()


def parse_headers(lines: list[str]) -> dict[str, str]:
    header_details = {}

    for detail in lines[1:]:
        if not detail:
            break

        key, value = detail.split(":", 1)
        header_details[key.strip()] = value.strip()

    return header_details


def parse_query_params(words: list[str]) -> dict[str, str]:
    query_params = {}

    if "?" in words[1]:
        query_string = words[1].split("?", 1)[1]

        for parameter in query_string.split("&"):
            key, value = parameter.split("=", 1)
            query_params[key.strip()] = value.strip()

    return query_params


def parse_request(msg: str):
    parts = msg.split("\r\n\r\n", 1)

    header_part = parts[0]
    body = parts[1] if len(parts) == 2 else ""

    lines = header_part.split("\r\n")

    request_words = lines[0].split()

    method = request_words[0]
    target = request_words[1]
    version = request_words[2]

    path = target.split("?", 1)[0]
    query_params = parse_query_params(request_words)

    headers = parse_headers(lines)

    return method, path, version, query_params, headers, body


def generate_response(method, path, headers, body):
    # POST /users
    if method == "POST" and path == "/users":

        if headers.get("Content-Type") == "application/json":

            try:
                data = json.loads(body)

            except json.JSONDecodeError:
                response_body = "Invalid JSON"

                return (
                    "HTTP/1.1 400 Bad Request\r\n"
                    "Content-Type: text/plain\r\n"
                    f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
                    "\r\n"
                    f"{response_body}"
                )

            response_body = json.dumps(data)

            return (
                "HTTP/1.1 201 Created\r\n"
                "Content-Type: application/json\r\n"
                f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
                "\r\n"
                f"{response_body}"
            )

    # GET /users
    if method == "GET" and path == "/users":

        response_body = "Hello users"

        return (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
            "\r\n"
            f"{response_body}"
        )

    # Everything else
    response_body = "Not Found"

    return (
        "HTTP/1.1 404 Not Found\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
        "\r\n"
        f"{response_body}"
    )


ser.bind(("127.0.0.1", 8000))
ser.listen(4)

while True:

    con, con_addr = ser.accept()

    rec_msg = con.recv(1024).decode()

    method, path, version, query_params, headers, body = parse_request(rec_msg)

    print(f"Method: {method}")
    print(f"Path: {path}")
    print(f"Version: {version}")
    print(f"Query params: {query_params}")
    print(f"Headers: {headers}")
    print(f"Body: {body}")

    send_msg = generate_response(
        method,
        path,
        headers,
        body
    )

    con.send(send_msg.encode("utf-8"))

    con.close()