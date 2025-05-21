import hashlib
from tqdm import tqdm
passwords = open('rockyou.txt', 'rb')
hash = input('enter hash: ').strip()
for line in tqdm(passwords.readlines()):
    line = line.strip()
    if hash == hashlib.md5(line).hexdigest():
        print(f'found the passord -> {line.decode(errors="ignore")}')
        break
