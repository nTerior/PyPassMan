#!/bin/python

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

from utils import password_file


def chunkify(string, chunk_size):
    return [string[i:i + chunk_size] for i in range(0, len(string), chunk_size)]


def sha256(pwd):
    return SHA256.new(pwd.encode("utf-8")).digest()


def generate_iv(size):
    return Random.new().read(size)


def encrypt_file(key, data, chunk_size=32 * 1024):
    key = sha256(key)
    iv = generate_iv(16)
    aes = AES.new(key, AES.MODE_CFB, iv)

    chunks = chunkify(data, chunk_size)
    chunk_ptr = 0
    with open(password_file, "wb") as f_out:
        f_out.write(iv)

        while True:
            try:
                chunk = chunks[chunk_ptr]
                chunk_ptr += 1
            except IndexError:
                break
            if len(chunk) % 16:
                chunk += b' ' * (16 - (len(chunk) % 16))
            f_out.write(aes.encrypt(chunk))


def decrypt_file(key, chunk_size=32 * 1024):
    key = sha256(key)
    data = bytes()
    with open(password_file, "rb") as f_in:
        iv = f_in.read(16)
        aes = AES.new(key, AES.MODE_CFB, iv)
        while True:
            chunk = f_in.read(chunk_size)
            if len(chunk) == 0:
                break
            data += aes.decrypt(chunk)

    return data
