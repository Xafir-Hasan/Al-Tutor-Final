import os
import json
import random
from http.server import BaseHTTPRequestHandler
from google import genai

# এখানে ৭টি কি কমা দিয়ে আলাদা করে এনভায়রনমেন্ট ভেরিয়েবলে দিবেন
# Vercel-এ Key হবে: GEMINI_API_KEYS (পুরো স্ট্রিংটি এখানে দিবেন)
API_KEYS_STR = os.environ.get("GEMINI_API_KEYS", "")
API_KEYS = API_KEYS_STR.split(",")

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # ... (আপনার আগের কোড)
        # এখানে কি রোটেশন লজিক ব্যবহার করুন:
        current_key = random.choice(API_KEYS)
        client = genai.Client(api_key=current_key)
        # ...