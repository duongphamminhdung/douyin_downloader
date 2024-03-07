import httpx
from tqdm import tqdm
import os

# lst = ['https://p3-sign.douyinpic.com/tos-cn-i-0813/677e382344fc4464b2aa5473a19abd3e~tplv-dy-kuchen-v1:1440:1920:q80.webp?x-expires=1711562400&x-signature=Sx%2B8VmjEoUjWhi%2BAxqFSPGKjqoU%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=image&biz_tag=aweme_images&l=2024022702200757EE5A0C539C9B2A8F5A', ]
    #    'https://p26-sign.douyinpic.com/tos-cn-i-0813/8da95de1bf3d4aec85b50a92682d1a09~tplv-dy-kuchen-v1:1440:1990:q80.webp?x-expires=1711562400&x-signature=05SK7sS7R%2FDvGxgp1gwwwuRjllo%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=image&biz_tag=aweme_images&l=2024022702200757EE5A0C539C9B2A8F5A']
def download_from_url(url, out):
    try:
        
        with open(out, 'wb') as download_file:
            with httpx.stream("GET", url, headers={'User-agent': 'Mozilla/5.0'}) as response:
                for chunk in response.iter_bytes():
                    download_file.write(chunk)
                # total = int(response.headers["Content-Length"])
                # with tqdm(total=total, unit_scale=True, unit_divisor=1024, unit="B") as progress:
                #     num_bytes_downloaded = response.num_bytes_downloaded
                #     for chunk in response.iter_bytes():
                #         download_file.write(chunk)
                #         progress.update(response.num_bytes_downloaded - num_bytes_downloaded)
                #         num_bytes_downloaded = response.
        # print('hehe')
        return True
    except Exception as e:
        try:
            print('trying 2nd time')
            with open(out, 'wb') as download_file:
                with httpx.stream("GET", url, headers={'User-agent': 'Mozilla/5.0'}) as response:
                    for chunk in response.iter_bytes():
                        download_file.write(chunk)
            return True
        except Exception as e:
            print("httpx", e)
            os.remove(out)
            return e                        
# download_from_url(lst[0], 'test.jpg')
