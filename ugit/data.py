# Manages the data in .ugit directory. Here will be the code that actually touches files on disk.


import os
import hashlib

GIT_DIR = '.ugit'


# Initialises the Repo
def init():
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}\\objects')


# Reads and stores a file to .ugit\objects\ with its sha1 hash as the name
def hash_object(data, type_='blob'):
    obj = type_.encode() + b'\x00' + data
    oid = hashlib.sha1(obj).hexdigest()
    with open(f'{GIT_DIR}\\objects\\{oid}', 'wb') as out:
        out.write(obj)
    return oid


def get_object(oid, expected='blob'):
    with open(f'{GIT_DIR}\\objects\\{oid}', 'rb') as f:
        obj = f.read()

    # Partitionam tipul si contentul folosindune de null byte
    type_, _, content = obj.partition(b"\x00")
    type_ = type_.decode()

    if expected is not None and type_ !=expected:
        raise ValueError(f'Exepected {expected}, got {type_}')

