
import requests
# lst = ['https://p3-sign.douyinpic.com/tos-cn-i-0813/677e382344fc4464b2aa5473a19abd3e~tplv-dy-kuchen-v1:1440:1920:q80.webp?x-expires=1711562400&x-signature=Sx%2B8VmjEoUjWhi%2BAxqFSPGKjqoU%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=image&biz_tag=aweme_images&l=2024022702200757EE5A0C539C9B2A8F5A', 
    #    'https://p26-sign.douyinpic.com/tos-cn-i-0813/8da95de1bf3d4aec85b50a92682d1a09~tplv-dy-kuchen-v1:1440:1990:q80.webp?x-expires=1711562400&x-signature=05SK7sS7R%2FDvGxgp1gwwwuRjllo%3D&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=image&biz_tag=aweme_images&l=2024022702200757EE5A0C539C9B2A8F5A']
import shutil
def download_from_url(url, out):
    r = requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
    if r.status_code == 200:
        with open(out, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    print('done', url)