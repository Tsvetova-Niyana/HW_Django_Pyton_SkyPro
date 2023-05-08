from http.server import BaseHTTPRequestHandler

hostName = "localhost"
hostPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Создайте простое веб-приложение, которое будет на любой GET запрос возвращать текст “Hello, World wide web!”
        """
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("Hello, World wide web!", "utf-8"))

    def do_POST(self):
        """
        Реализуйте в вашем веб-приложения прием POST запроса и печать в консоль всех данных, которые были приняты
        от пользователя. Протестируйте решение через Postman.
        """

        c_len = int(self.headers.get("Content-Length"))
        client_data = self.rfile.read(c_len)
        print(client_data.decode())

        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes('data Post request input concole', 'utf-8'))
