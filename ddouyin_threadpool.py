from utils.allMediaApi import download_and_save
from multiprocessing.pool import ThreadPool
import os
from tqdm import tqdm
import time

file = "wo.txt"
num_thread = 7

with open(file, "r") as f:
    urls = f.readlines()
    # print(len(urls))
    save_folder = urls[0][:-1]
    author_id = urls[1].strip()
    urls = [url[:-1] for url in urls[2:]]
    # print(urls)

    # print(url)
error_url = []
def run(url):
    # print(url)
    # time.sleep(2)
    r = download_and_save(url, author_id, save_folder)
    # if r is not None and r is not True: 
    #     error_url.append(r)
    return r

if __name__ == "__main__":
    os.makedirs(save_folder, mode = 0o777, exist_ok = True)

    with ThreadPool(processes=num_thread) as pool:
        # execute tasks in order
        for r in tqdm(pool.imap_unordered(run, urls), total=len(urls)):
            if r is not None and r is not True: 
                error_url.append(r)

    print("=" * 80)
    print("COMPLETE")
    print(error_url)
    with open("error_url.txt", "w") as f:
        for i in error_url:
            f.write(i[0] + ' ' + str(i[1]) + "\n")