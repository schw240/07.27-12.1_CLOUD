from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime
class HelloHandler(BaseHTTPRequestHandler):
   def do_GET(self):
        print(self.path)
        if self.path == '/my':
           self.send_response(200)
           self.end_headers()
           self.wfile.write("MyPage!".encode('utf-8'))
        elif self.path == '/portfolio':
           self.send_response(200)
           self.end_headers()
           self.wfile.write("Portfolio!".encode('utf-8'))
        elif self.path == '/':
           html = f"""
           <html>
           <head>
                <title>나의홈페이지</title>
           </head>
           <body>
                <h1>안녕하세요~ 저의 웹사이트에 오신걸 환영합니다.</h1>
                <h2>{datetime.datetime.now()}</h2>
           </body>
           </html>
           """
           self.send_response(200)
           self.send_header("content-type", "text/html; charset=UTF-8")
           self.end_headers()
           self.wfile.write(html.encode('utf-8'))
        else:
           self.send_response(404)
           self.end_headers()
           self.wfile.write("404".encode('utf-8'))
if __name__== '__main__':
    server = HTTPServer(('', 8888), HelloHandler)
    print("Start Server")
    server.serve_forever()