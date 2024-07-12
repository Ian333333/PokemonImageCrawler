import requests
from bs4 import BeautifulSoup
import threading

def download(num):
    # 加入 try 保護避免遇到無法下載的狀況而發生錯誤
    try:
        web = requests.get(f'https://tw.portal-pokemon.com/play/pokedex/{num}')   # 使用變數替換網址
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
# 使用迴圈，一次可以下載 1～99 張圖片
for i in range(1,100):
    n = f'{i:04d}'
    threading.Thread(target=download, args=(n,)).start()