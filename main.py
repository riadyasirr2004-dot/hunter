import asyncio
import aiohttp
import random
import string
import requests

T = "8526040045:AAEzHONIjI1IezTLNsYRMmadARh5BD-hYr0"
C = "-1004337788630"
URL = f"https://telegram.org{T}/sendMessage"

UA = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
]

async def check(session, u):
    try:
        async with session.get(f"https://tiktok.com@{u}", headers={"User-Agent": random.choice(UA)}, timeout=4) as r:
            if r.status == 404:
                print(f"[+] Available: {u}")
                requests.post(URL, json={"chat_id": C, "text": f"🎯 يوزر ثلاثي متاح الآن: @{u}"})
            elif r.status == 429:
                await asyncio.sleep(5)
    except: pass

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = []
            for _ in range(5):
                u = ''.join(random.choices(string.ascii_lowercase, k=3))
                tasks.append(check(session, u))
            await asyncio.gather(*tasks)
            await asyncio.sleep(random.uniform(2.0, 4.0))

if __name__ == "__main__":
    try: requests.post(URL, json={"chat_id": C, "text": "🚀 الأداة تعمل الآن سحابياً وبدأت فحص اليوزرات الثلاثية!"})
    except: pass
    asyncio.run(main())
