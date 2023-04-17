import requests

# Kullanıcı adını değiştirin
username = "kaantsn"

# GitHub API isteği için kullanılan URL
url = f"https://api.github.com/users/{username}/repos"

# API isteğini yap
response = requests.get(url)

# İstek başarılıysa
if response.status_code == 200:
    # Depo listesi
    repos = response.json()

    # Depolardan en son güncellenenleri bul
    last_updated = sorted(repos, key=lambda r: r["updated_at"], reverse=True)[:5]

    # En son güncellenenleri ekrana yazdır
    print(f"{username} kullanıcısının en son güncellenen depoları:")
    for repo in last_updated:
        print(f"- {repo['name']} (son güncelleme: {repo['updated_at']})")

else:
    # İstek başarısızsa hata kodunu yazdır
    print(f"Hata: {response.status_code}")
