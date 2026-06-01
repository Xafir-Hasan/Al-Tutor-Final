from http.server import BaseHTTPRequestHandler
import json
import os
import random
from google import genai

# API Key setup
API_KEYS_STR = os.environ.get("GEMINI_API_KEYS", "")
API_KEYS = API_KEYS_STR.split(",")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"AI Tutor is running. Please send a POST request.")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # আপনার বাকি জেমিনি লজিক এখানে থাকবে...
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Response from AI")
