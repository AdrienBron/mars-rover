from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000
#toto2234
with HTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
