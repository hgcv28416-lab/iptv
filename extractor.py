import requests

# البيانات المستخرجة من صورتك
BASE_URL = "http://smarter8k.ru"
USERNAME = "iptvload61af"
PASSWORD = "686c93b64f"

def fetch_channels():
    # رابط استدعاء القنوات بصيغة M3U من سيرفر Xtream
    url = f"{BASE_URL}/get.php?username={USERNAME}&password={PASSWORD}&type=m3u_plus&output=ts"
    
    try:
        print("جاري استخراج القنوات... انتظر قليلاً")
        response = requests.get(url)
        if response.status_code == 200:
            with open("channels_list.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("تم استخراج جميع القنوات بنجاح في ملف channels_list.m3u")
        else:
            print(f"فشل الاتصال. كود الخطأ: {response.status_code}")
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    fetch_channels()
