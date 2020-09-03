from http.server import BaseHTTPRequestHandler, HTTPServer
import pymysql
import datetime
class HelloHandler(BaseHTTPRequestHandler):
   def do_GET(self):
        print(self.path)
        if self.path == '/my':
            html = f"""
            <html>
            <head>
                <title나에 대하여</title>
            </head>
            <body>
                <a href="/">홈</a>
                <a href="/my">나에 대해서</a>
                <a href="/portfolio">포트폴리오</a> 
                <h1>김한주를 소개합니다.</h1>
                <p>나이: 27,  직업: 프로그래머</p>
            </body>
            </html>
            """
            self.send_response(200)
            self.send_header("content-type", "text/html; charset=UTF-8")
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        elif self.path == '/portfolio':
            conn = pymysql.connect(host="220.90.200.176", port=3306, user="w3schools", passwd="w3schools!)@(", db="w3schools", charset='utf8')
            sql = """
            SELECT *
            FROM portfolio
            WHERE 이름 = "김한주"
            """
            cursor = conn.cursor()
            cursor.execute(sql)
            rs = cursor.fetchall()
            name_list = list()
            for i, item in enumerate(rs):
                name_list.append(item)
            

            html = """
            <html>
            <head>
                <title나에 대하여</title>
                <style>
                     table, th, td {{
                         border: 1px solid #bcbcbc;
                     }}
                </style>
            </head>
            <body>
                <a href="/">홈</a>
                <a href="/my">나에 대해서</a>
                <a href="/portfolio">포트폴리오</a> 
                <table>
                    <tr>
                        <td>순번</td>
                        <td>이름</td>
                        <td>깃허브</td>
                    </tr>
                    <tr>
                        <td>{0}</td>
                        <td>{1}</td>
                        <td>{2}</td>
                    </tr>
                </table>
            </body>
            </html>
            """

            self.send_response(200)
            self.send_header("content-type", "text/html; charset=UTF-8")
            self.end_headers()
            self.wfile.write(html.format(item[0], item[1], item[2]).encode('utf-8'))
        elif self.path == '/':
            html = f"""
            <html>
            <head>
                    <title>나의홈페이지</title>
            </head>
            <body>
                    <a href="/">홈</a>
                    <a href="/my">나에 대해서</a>
                    <a href="/portfolio">포트폴리오</a> 
                    <h1>안녕하세요~ 저의 웹사이트에 오신걸 환영합니다.</h1>
                    <p>지금 시간은 {datetime.datetime.now()}</p>
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