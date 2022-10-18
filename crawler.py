import json
import os
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

article_html_folder_dir = "article_html"

largest_idx = 1030

def mednet_status(url, request_code):
    current_time = str(datetime.now())
    buf = {
        "url": url, 
        "request_code": request_code,
        "crawl_time": current_time
    }
    print(buf)
    if os.path.exists("mednet_article_status.json"):
        with open("mednet_article_status.json", "r", encoding="utf-8")as f:
            mednet_article_status = json.load(f)
    else:
        mednet_article_status = []
    current_data_in_json = list(filter(lambda x:x["url"]==url, mednet_article_status))
    if current_data_in_json == []:
        mednet_article_status.append(buf)
    else:
        for i, artical in enumerate(mednet_article_status):
            if artical == current_data_in_json[0]:
                mednet_article_status[i] = buf
                break
    with open("mednet_article_status.json", "w", encoding="utf-8")as f:
        json.dump(mednet_article_status, f, ensure_ascii=False, indent=2)


def crawler(idx):
    url = "https://med-net.com/CMSContent/Content/{}".format(idx)
    response = requests.get(url, allow_redirects=False)
    request_code = response.status_code
    article_name = "CMSContent_Content_{}.html".format(idx)

    if not os.path.exists(article_html_folder_dir):
        os.mkdir(article_html_folder_dir)
    else:
        pass

    if request_code == 200:
        # 醫聯網有此文章
        soup = BeautifulSoup(response.text, "html.parser")
        mednet_status(url, request_code)
        with open("{}/{}".format(article_html_folder_dir, article_name), "w")as f:
            f.write(soup.prettify())
    elif request_code == 302:
        mednet_status(url, request_code)


def main():
    idx = 0
    while idx<largest_idx:
        crawler(idx)
        idx += 1

    

if __name__ == "__main__":
    main()
