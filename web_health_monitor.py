import urllib.request
import time
from datetime import datetime

# The website you want to protect
target_url = "https://www.google.com" 

print(f"📡 STARTING MONITOR FOR: {target_url}")

def check_site():
    now = datetime.now().strftime("%H:%M:%S")
    try:
        # Try to open the website
        response = urllib.request.urlopen(target_url)
        status = response.getcode()
        
        if status == 200:
            print(f"[{now}] ✅ SITE IS HEALTHY (Status: {status})")
        else:
            print(f"[{now}] ⚠️ WARNING: Site returned status {status}")
            
    except Exception as e:
        print(f"[{now}] 🚨 ALERT: SITE IS DOWN! Error: {e}")
        # In a real job, this is where you'd send an email/text alert.

# Monitor every 10 seconds (for testing)
for i in range(5):
    check_site()
    time.sleep(10)
