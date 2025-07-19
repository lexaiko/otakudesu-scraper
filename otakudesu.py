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

def list_ongoing_anime_all_pages():
    page = 1
    all_results = []

    while True:
        url = f'https://otakudesu.cloud/ongoing-anime/page/{page}/'
        print(f"Fetching page {page}...")
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        venz_div = soup.find('div', class_='venz')
        if not venz_div:
            print("No 'venz' div found, stop.")
            break

        ul = venz_div.find('ul')
        if not ul:
            print("No <ul> found, stop.")
            break

        lis = ul.find_all('li', recursive=False)
        if not lis:
            print("No more items found, stop.")
            break

        page_results = []

        for li in lis:
            detpost = li.find('div', class_='detpost')
            if not detpost:
                continue

            thumb_div = detpost.find('div', class_='thumb')
            a_tag = thumb_div.find('a') if thumb_div else None
            if not a_tag:
                continue

            link = a_tag['href']
            judul_tag = a_tag.find('h2', class_='jdlflm')
            judul = judul_tag.text.strip() if judul_tag else 'No Title'

            rating_div = detpost.find('div', class_='epztipe')
            rating = rating_div.text.strip() if rating_div else 'N/A'

            episode_div = detpost.find('div', class_='epz')
            episode = episode_div.text.strip() if episode_div else 'N/A'

            page_results.append({
                'judul': judul,
                'link': link,
                'rating': rating,
                'episode': episode
            })

        if not page_results:
            print("Page empty, stop.")
            break

        all_results.extend(page_results)
        page += 1

    return all_results



def get_anime_list():
    url = 'https://otakudesu.cloud/anime-list/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    container = soup.find('div', id='abtext')
    if not container:
        print("Gagal menemukan div#abtext")
        return []

    hasil = []
    for a_tag in container.select('ul li a'):
        judul = a_tag.get_text(strip=True)
        link = a_tag.get('href')
        if judul and link:
            hasil.append({'judul': judul, 'link': link})

    return hasil



if __name__ == '__main__':
    print("Pilih opsi:")
    print("1. Search Anime")
    print("2. Lihat Anime On Going")
    print("3. Lihat Semua List Anime")
    opsi = input("Masukkan pilihan (1/2/3): ").strip()

    if opsi == '1':
        title = input("Masukkan judul anime: ")
        print(f"[SEARCHING] {title}...\n")
        hasil = search_anime(title)
    elif opsi == '2':
        print("[LOAD] Anime On Going...\n")
        hasil = list_ongoing_anime_all_pages()
    elif opsi == '3':
        print("[LOAD] Semua List Anime...\n")
        hasil = get_anime_list()
    else:
        print("Pilihan tidak valid.")
        exit()

    if not hasil:
        print("Tidak ditemukan.")
        exit()

    print("Ditemukan hasil:\n")
    for i, anime in enumerate(hasil):
        print(f"{i+1}. {anime['judul']} — {anime['link']}")
    print()

    pilih = int(input("Pilih nomor anime untuk lihat episode: ")) - 1
    selected = hasil[pilih]

    print(f"\n[DETAIL] {selected['judul']}\n")
    eps = get_episode_links(selected['link'])

    if not eps:
        print("Episode tidak ditemukan.")
        exit()

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
