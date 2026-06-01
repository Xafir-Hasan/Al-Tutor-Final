from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    
    # GET রিকোয়েস্ট হ্যান্ডেল করার জন্য
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"AI Tutor is running! Please use POST to send a query.")

    # POST রিকোয়েস্ট হ্যান্ডেল করার জন্য (যেখানে আপনার জেমিনি লজিক আছে)
    def do_POST(self):
        # ... আপনার বর্তমান জেমিনি কোড এখানে থাকবে ...
