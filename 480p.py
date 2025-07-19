import requests
from bs4 import BeautifulSoup

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

        sets = li.find_all('div', class_='set')
        genre = []
        status, rating = None, None
        for s in sets:
            text = s.get_text(strip=True)
            if text.startswith('Genres'):
                genre = [x.strip() for x in s.text.replace('Genres', '').split(',')]
            elif text.startswith('Status'):
                status = text.replace('Status :', '').strip()
            elif text.startswith('Rating'):
                rating = text.replace('Rating :', '').strip()

        results.append({
            'judul': judul,
            'link': link,
            'genre': genre,
            'status': status,
            'rating': rating,
        })
    return results

def get_episode_links(anime_url):
    res = requests.get(anime_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    episodes = []
    episodelists = soup.find_all('div', class_='episodelist')
    for ep_section in episodelists:
        if "Episode List" in ep_section.text:
            for a in reversed(list(ep_section.find_all('a'))):
                eps_title = a.text.strip()
                eps_link = a['href']
                episodes.append({
                    'judul': eps_title,
                    'link': eps_link
                })

    return episodes

def get_embed_links(episode_url):
    res = requests.get(episode_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    embed_div = soup.find('div', class_='player-embed')
    if not embed_div:
        return []

    iframes = embed_div.find_all('iframe')
    links = []

    for iframe in iframes:
        if 'src' in iframe.attrs:
            links.append(iframe['src'])

    return links

if __name__ == '__main__':
    title = input("Masukkan judul anime: ")
    print(f"[SEARCHING] {title}...\n")
    hasil = search_anime(title)

    if not hasil:
        print("Tidak ditemukan.")
        exit()

    print("Ditemukan hasil:\n")
    for i, anime in enumerate(hasil):
        print(f"{i+1}. {anime['judul']} — {anime['link']} — Genre: {', '.join(anime['genre'])}")
    print()

    pilih = int(input("Pilih nomor anime untuk lihat episode: ")) - 1
    selected = hasil[pilih]

    print(f"\n[DETAIL] {selected['judul']}\n")
    eps = get_episode_links(selected['link'])

    for i, e in enumerate(eps):
        print(f"{i+1}. {e['judul']} — {e['link']}")
    print()

    ep_pilih = int(input("Pilih nomor episode untuk ambil semua embed link: ")) - 1
    embed_links = get_embed_links(eps[ep_pilih]['link'])

    if embed_links:
        print(f"\n🎬 Embed link yang ditemukan:")
        for i, link in enumerate(embed_links, 1):
            print(f"{i}. {link}")
    else:
        print("Gagal menemukan embed.")
