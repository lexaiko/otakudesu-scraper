import requests
from bs4 import BeautifulSoup

# Fungsi untuk mencari anime berdasarkan judul
def search_anime(title):
    q = title.replace(' ', '+')
    url = f'https://otakudesu.cloud/?s={q}&post_type=anime'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    results = []
    ul = soup.find('ul', class_='chivsrc')
    if not ul:
        return results

    for li in ul.find_all('li', recursive=False):
        a = li.find('h2').find('a')
        judul = a.text.strip()
        link = a['href']

        # Ekstrak genre, status, rating (opsional)
        sets = li.find_all('div', class_='set')
        genre = []
        status, rating = None, None
        for s in sets:
            text = s.get_text(strip=True)
            if text.startswith('Genres'):
                genre = [x.strip() for x in s.text.replace('Genres','').split(',')]
            elif text.startswith('Status'):
                status = text.replace('Status :','').strip()
            elif text.startswith('Rating'):
                rating = text.replace('Rating :','').strip()

        results.append({
            'judul': judul,
            'link': link,
            'genre': genre,
            'status': status,
            'rating': rating,
        })
    return results

# Fungsi untuk ambil link episode terakhir dari halaman anime
def get_last_episode_url(anime_url):
    res = requests.get(anime_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    eps_list = soup.find('div', class_='episodelist')
    if not eps_list:
        return None

    last_ep = eps_list.find_all('a')[-1]  # ambil episode terakhir
    return last_ep['href']

# Fungsi untuk ambil embed video dari halaman episode
def get_embed_video(ep_url):
    res = requests.get(ep_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    embed = soup.find('div', class_='responsive-embed')
    if not embed:
        return None

    iframe = embed.find('iframe')
    return iframe['src'] if iframe else None

# MAIN PROGRAM
if __name__ == '__main__':
    title = input("Masukkan judul anime: ")
    print(f"[SEARCHING] {title}...\n")
    data = search_anime(title)

    if data:
        print("Ditemukan hasil:\n")
        for idx, anime in enumerate(data):
            print(f"{idx+1}. {anime['judul']} — {anime['link']} — genre: {', '.join(anime['genre'])}")
        
        try:
            pilih = int(input("\nPilih nomor anime yang ingin dilihat embed episodenya: "))
            selected = data[pilih - 1]
            print(f"\n[INFO] Mengambil episode terakhir dari: {selected['judul']}")
            last_ep_url = get_last_episode_url(selected['link'])
            if last_ep_url:
                print(f"[INFO] Link Episode Terakhir: {last_ep_url}")
                embed_url = get_embed_video(last_ep_url)
                if embed_url:
                    print(f"[EMBED VIDEO] {embed_url}")
                else:
                    print("[ERROR] Embed video tidak ditemukan.")
            else:
                print("[ERROR] Tidak ada episode ditemukan.")
        except Exception as e:
            print(f"[ERROR] Terjadi kesalahan: {e}")
    else:
        print("Anime tidak ditemukan di hasil pencarian.")
