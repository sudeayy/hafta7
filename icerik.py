import requests
from bs4 import BeautifulSoup


def icerik_cek(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    tarih_tag = soup.find("span", {"class": "date"})
    tarih = tarih_tag.getText().strip() if tarih_tag else "Tarih bulunamadı"
    print(tarih)

    baslik = soup.find_all("h1", {"class": "news-title"})
    title = ''
    for i in baslik:
        title = i.getText().strip()
    print(title)


    plist = soup.find_all("p")
    icerik = ''
    for i in plist:
        icerik += i.getText().strip()
    print(icerik)

    data = '{};{};{}\n'.format(tarih.strip(), title.strip(), icerik.strip())

    with open('milligazete_yazi.txt', "a", encoding="utf-8") as file:
        file.write(data)
