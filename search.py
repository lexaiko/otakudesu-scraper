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
        return results  # berarti tidak ada hasil

    for li in ul.find_all('li', recursive=False):
        a = li.find('h2').find('a')
        judul = a.text.strip()
        link = a['href']

        # ekstrak genre/status/rating
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

if __name__ == '__main__':
    title = input("Masukkan judul anime: ")
    print(f"[SEARCHING] {title}...")
    data = search_anime(title)
    if data:
        print("Ditemukan hasil:")
        for idx, anime in enumerate(data):
            print(f"{idx+1}. {anime['judul']} — {anime['link']} — genre: {', '.join(anime['genre'])}")
    else:
        print("Anime tidak ditemukan di hasil pencarian.")
