import requests
from bs4 import BeautifulSoup

BASE_URL = "https://otakudesu.cloud"

def search_anime(keyword):
    print(f"[SEARCHING] {keyword}...")
    r = requests.get(f"{BASE_URL}/?s={keyword}&post_type=anime")
    soup = BeautifulSoup(r.text, 'html.parser')
    result = soup.find("div", class_="venser")

    if not result:
        print("Anime tidak ditemukan.")
        return None

    anime_list = result.find_all("div", class_="search-page")
    if not anime_list:
        print("Anime tidak ditemukan di hasil pencarian.")
        return None

    # Ambil link pertama aja (paling relevan)
    anime_link = anime_list[0].a["href"]
    print(f"[FOUND] {anime_link}")
    return anime_link

def get_episode_links(anime_url):
    print(f"[GETTING EPISODES] from {anime_url}")
    r = requests.get(anime_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    eps_list = soup.find("div", class_="episodelist").find_all("li")

    episodes = []
    for li in eps_list:
        link = li.a["href"]
        title = li.a.text.strip()
        episodes.append((title, link))

    print(f"[FOUND] {len(episodes)} episodes.")
    return episodes[::-1]  # Reverse so Episode 1 muncul duluan

def get_embed_link(episode_url):
    r = requests.get(episode_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # cari iframe embed dari desustream, mp4upload, atau lainnya
    iframe = soup.find("iframe")
    if iframe and "src" in iframe.attrs:
        return iframe["src"]
    return None

def scrape_anime(keyword):
    anime_page = search_anime(keyword)
    if not anime_page:
        return

    episodes = get_episode_links(anime_page)
    print("\n🎬 LIST EPISODES + EMBED LINK:\n")

    for title, ep_url in episodes:
        embed = get_embed_link(ep_url)
        if embed:
            print(f"{title} -> {embed}")
        else:
            print(f"{title} -> [embed not found]")

if __name__ == "__main__":
    keyword = input("Masukkan judul anime: ")
    scrape_anime(keyword.strip())
