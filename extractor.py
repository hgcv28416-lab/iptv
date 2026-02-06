import requests

# البيانات من صورتك الأصلية
BASE_URL = "http://smarter8k.ru"
USER = "iptvload61af"
PASS = "686c93b64f"

def get_live_streams():
    # استخدام رابط الـ API المباشر لـ Xtream Codes
    url = f"{BASE_URL}/player_api.php?username={USER}&password={PASS}&action=get_live_streams"
    
    try:
        print("--- بدأت عملية الاستخراج المباشر ---")
        response = requests.get(url, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                print(f"✅ تم العثور على {len(data)} قناة!")
                print("-" * 30)
                for item in data[:50]: # سنطبع أول 50 قناة للتجربة
                    name = item.get('name')
                    stream_id = item.get('stream_id')
                    container = item.get('container_extension', 'ts')
                    link = f"{BASE_URL}/{USER}/{PASS}/{stream_id}.{container}"
                    print(f"القناة: {name} | الرابط: {link}")
                print("-" * 30)
                print("ملاحظة: طبعت لك أول 50 قناة فقط في الـ Logs لتسهيل النسخ.")
            else:
                print("❌ السيرفر استجاب ولكن البيانات ليست قائمة قنوات. قد يكون الحساب منتهي.")
        else:
            print(f"❌ فشل الاتصال. كود الحالة: {response.status_code}")
            
    except Exception as e:
        print(f"❌ حدث خطأ تقني: {e}")

if __name__ == "__main__":
    get_live_streams()
