from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

with HTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
