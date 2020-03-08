import threading
import time
import datetime
import logging
import requests
import os

def download_gambar(url=None, i=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"Gambar{i}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__=='__main__':
    url_download = ['https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg',
                    'https://images.unsplash.com/photo-1468872961186-1d26f74f3355?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80']

    threads = []
    i=1
    for url in url_download:
        t = threading.Thread(target=download_gambar, args=(url,i,))
        threads.append(t)
        i+=1
        
    for thr in threads:
        thr.start()