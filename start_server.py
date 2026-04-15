import http.server
import socketserver
import os
import socket

PORT = 8888

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return '127.0.0.1'

with socketserver.TCPServer(('0.0.0.0', PORT), MyHandler) as httpd:
    ip = get_ip()
    print(f"========================================")
    print(f"  风电功率预测平台 - 服务器已启动")
    print(f"========================================")
    print(f"  本地访问: http://127.0.0.1:{PORT}")
    print(f"  局域网访问: http://{ip}:{PORT}")
    print(f"========================================")
    print(f"  按 Ctrl+C 停止服务器")
    print(f"========================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.shutdown()