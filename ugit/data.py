# Manages the data in .ugit directory. Here will be the code that actually touches files on disk.


import os
import hashlib

GIT_DIR = '.ugit'


# Initialises the Repo
def init():
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}\\objects')


# Reads and stores a file to .ugit\objects\ with its sha1 hash as the name
def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}\\objects\\{oid}', 'wb') as out:
        out.write(data)
    return oid


def get_object(oid):
    with open(f'{GIT_DIR}\\objects\\{oid}', 'rb') as f:
        return f.read()
