from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 80

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/good":
            self.wfile.write("HTTP/1.0 404 Not Found\r\n\r\nThis is the good page.".encode("utf-8"))
            return
        elif self.path == "/bad":
            self.wfile.write("HTTP/1.0 b'404 Not Found'\r\n\r\nThis is the bad page.".encode("utf-8"))
            return
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(
            "Test app to produce good and bad responses\n"
            "For successful 404 response, use /good URL\n"
            "For incorrectly formatted response, use /bad URL\n".encode("utf-8"))
        return

server = HTTPServer(('', PORT_NUMBER), myHandler)
print('Started httpserver on port ', PORT_NUMBER)

server.serve_forever()
