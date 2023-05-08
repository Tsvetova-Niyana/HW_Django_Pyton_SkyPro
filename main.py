from my_server import MyServer
from http.server import HTTPServer

hostName = "localhost"
hostPort = 8080


if __name__ == '__main__':
    webServer = HTTPServer((hostName, hostPort), MyServer)
    print("Server started http://%s:%s" % (hostName, hostPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped")

