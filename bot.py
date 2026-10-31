import requests
import time

BOT_TOKEN = "9104837985:AAHMGE8n5L7-WmaVf7L9Wg24VSg7o1Vrpv4"
CHAT_ID = "5144440884"

# هون حط سعرك اللي بدك تبيع فيه
MY_SELL_PRICE = 42000  
PLAYER_ID = "25537"  

def send(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def get_lowest_ps_price():
    url = f"https://www.futbin.com/26/playerPrices?player={PLAYER_ID}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": f"https://www.futbin.com/26/player/{PLAYER_ID}"
    }
    try:
        r = requests.get(url, headers=headers, timeout=15).json()
        price_str = r[str(PLAYER_ID)]["prices"]["ps"]["LCPrice"]
        price = int(str(price_str).replace(",", "").replace(".", ""))
        return price
    except Exception as e:
        print(f"خطأ بالسحب: {e}")
        return None

send(f"✅ بوت التجارة اشتغل!\nعم راقبلك اذا سعرك {MY_SELL_PRICE} صار ارخص سعر بالسوق")

notified = False
while True:
    lowest = get_lowest_ps_price()
    
    if lowest:
        print(f"سعرك: {MY_SELL_PRICE} | ارخص سعر بالسوق PS5: {lowest}")
        
        if lowest >= MY_SELL_PRICE:
            # ما في حدا ارخص منك
            if not notified:
                send(f"🚀 يا حسين انت هلق ارخص واحد!\nسعرك: {MY_SELL_PRICE}\nارخص سعر بالسوق: {lowest}\nفيك تحط اللاعب للبيع هلق!")
                notified = True
        else:
            # في حدا ارخص منك
            print(f"بعد في حدا ارخص منك بـ {MY_SELL_PRICE - lowest}")
            notified = False # برجع بصفر لحتى يرجع يبعت اذا صرت ارخص مرة تانية
    
    time.sleep(120) # بيشيك كل دقيقتين
