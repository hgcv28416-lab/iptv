import requests
import os

BASE_URL = "http://smarter8k.ru"
USERNAME = "iptvload61af"
PASSWORD = "686c93b64f"

def fetch_channels():
    # الرابط المباشر للملف
    url = f"{BASE_URL}/get.php?username={USERNAME}&password={PASSWORD}&type=m3u_plus&output=ts"
    
    try:
        print(f"Connecting to: {BASE_URL}...")
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200 and len(response.text) > 100:
            with open("channels_list.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("✅ Success: File created successfully!")
        else:
            print(f"❌ Error: Received empty content or status {response.status_code}")
            # إنشاء ملف فارغ مؤقتاً لتجنب فشل الـ Action
            with open("channels_list.m3u", "w") as f: f.write("# Empty list - Check Credentials")
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        with open("channels_list.m3u", "w") as f: f.write(f"# Error: {e}")

if __name__ == "__main__":
    fetch_channels()
