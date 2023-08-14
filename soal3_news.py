import requests
import os

from dotenv import load_dotenv

load_dotenv()
api = os.environ.get('api')

# mengambil berita dari NEWS API
def get_news(category):
    url = f"https://newsapi.org/v2/top-headlines?country=id&category={category}&apiKey={api}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    return articles

# mengakategorikan berita
categories = {
    1: "technology",
    2: "business",
    3: "sports",
    4: "health",
    5: "science"
}

# menginput berita dari pengguna
print("Selamat datang, mau tahu berita apa hari ini?")
for num, category in categories.items():
    print(f"[{num}] Berita seputar {category.capitalize()}")

choice = int(input("Ketik pilihan Anda : "))

if choice in categories:
    selected_category = categories[choice]
    news = get_news(selected_category)
    
    print(f"Berikut adalah top 5 berita Indonesia bidang {selected_category.capitalize()}:")
    for idx, article in enumerate(news[:5], start=1):
        print(f"{idx} - {article['title']} - {article['source']['name']}")
else:
    print("Pilihan tidak valid.")