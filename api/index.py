import http.server
import socketserver
import json
import google.generativeai as genai
import os

# আপনার এপিআই কি এখানে সেট করুন
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # CORS হেডার সেট করা (যাতে ফ্রন্টএন্ড থেকে রিকোয়েস্ট কাজ করে)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        user_message = data.get('message', '')

        try:
            # জেমিনি এপিআই কল করা
            response = model.generate_content(user_message)
            reply = response.text
        except Exception as e:
            reply = "দুঃখিত, এই মুহূর্তে আমি কোনো উত্তর দিতে পারছি না।"

        # রেসপন্স পাঠানো
        response_data = {"reply": reply}
        self.wfile.write(json.dumps(response_data).encode())

# সার্ভার রান করার কনফিগারেশন
PORT = 8000
with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"AI Tutor সার্ভার চলছে http://localhost:{PORT}")
    httpd.serve_forever()
