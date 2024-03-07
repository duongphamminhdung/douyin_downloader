#500/month
#https://rapidapi.com/nguyenmanhict-MuTUtGWD7K/api/all-media-api/

import requests
import os
from utils.download_httpx import download_from_url
from utils.usage import get_api_key
import time

def download_douyin(url, author_id):    
    api_url = "https://all-media-api.p.rapidapi.com/v1/social/douyin/media/download"
    
    payload = { "url": url }
    key = get_api_key()
    print(key)

    headers = {
        "content-type": "application/json",
        "Content-Type": "application/json",
        'X-RapidAPI-Key': key,

        "X-RapidAPI-Host": "all-media-api.p.rapidapi.com"
    }
    # print(url)
    # time.sleep(1)
    response = requests.post(api_url, json=payload, headers=headers)
    print(response)
    # print(url)
    # print(url, response.json())
    # import
    if response.status_code != 200:
        print("status code not 200")
        return (False, "status code not 200")
    elif response.json()['error'] != False:
        print("error", response.json()['error'])
        return (False, ("error", response.json()['error']))
    elif response.json()['aweme_detail']['author']['sec_uid'] != author_id and author_id != "noneed":
        print("author_id not match")
        return (False, "author_id not match")
    
    if 'video' in url:
        try:
            return (True, [(response.json()['aweme_detail']['video']['play_addr']['url_list'][0])])
        except Exception as e:
            return (False, e)
    elif 'note' in url:
        try:
            url_list = []
            for i in (response.json()['aweme_detail']['images']):
                url_list.append(i['url_list'][0])
            return (True, url_list)
        except Exception as e:
            return (False, e)
def download_and_save(url, author_id, save_folder):
    # print(url)
    if 'video' in url:
        out = save_folder+'/'+save_folder+'-'+os.path.split(url)[-1]+'.mp4'
    elif 'note' in url:
        out = save_folder+'/'+save_folder+'-'+os.path.split(url)[-1]+'.jpg'
    # print(out)
    if os.path.isfile(out):
        # print("exist", out)
        pass
    else:    
        uri = download_douyin(url, author_id)
        # print(uri)
        if uri[0] is True:
            # import ipdb; ipdb.set_trace()
            for i in range(len(uri[1])):
                try:
                    r = download_from_url(uri[1][i], out=out)
                    if r is not True:
                        return (url, r)
                except Exception as e:
                    return (url, e)
            return True
                        # time.sleep(2)
        else:
            return (url, uri[1])
# print(download_douyin_video('https://www.douyin.com/note/7290019654746115343'))