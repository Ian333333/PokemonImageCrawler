import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def download(num):
    try:
        web = requests.get(f'https://tw.portal-pokemon.com/play/pokedex/{num}')
        soup = BeautifulSoup(web.text, "html.parser")
        img = soup.select('meta[property="og:image"]')
        imgUrl = img[0]['content']
        imgFile = requests.get(imgUrl)
        f = open(f'images/{num}.png', 'wb')
        f.write(imgFile.content)
        f.close()
        print(num)
    except Exception as e:
        print(e)
        pass

numArr = [f'{j:04d}' for j in range(1,1026)]  # 建立圖片檔名清單

executor = ThreadPoolExecutor()          # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(download, numArr)       # 同時下載圖片