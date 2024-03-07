from utils.allMediaApi import download_and_save
from threading import Thread
import os
from tqdm import tqdm
import datetime

url = input("url?")
wo = 'noneed'
error_url = []
        
if __name__ == "__main__":
	os.makedirs('one', exist_ok=True)
	r = download_and_save(url, author_id=wo, save_folder='one')
 
	# for chunk in chunk_urls:
	# 	print(len(chunk), chunk, end = ' ')
	# 	print('\n')
	
	print("=" * 80)
	print("COMPLETE")
	print(error_url)