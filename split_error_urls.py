import os

file = 'error_url.txt'
with open(file, "r") as f:
    urls = f.readlines()
    urls = [url.split()[0] for url in urls if not url.split()[1].startswith('author')]
file = 'wo.txt'
with open(file, "r") as f:
    urls = f.readlines()
    urls = [url.split()[0] for url in urls]
    name_id = urls[:2]
new_file = 'error_url_new.txt'
with open(new_file, "w") as f:
    for i in name_id:
        f.write(i + '\n')
    for url in urls:
        f.write(url + '\n')