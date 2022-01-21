import glob
import os, random, struct
from Cryptodome.Cipher import AES

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

key = b'qwer asdf zxcv 1234 !@#$'
windows_user_name = os.path.expanduser('~')
startPath = windows_user_name+'/Desktop/**'

for filename in glob.iglob(startPath, recursive=True):
    if(os.path.isfile(filename)):
        fname, ext = os.path.splitext(filename)
        if (ext == '.enc'):
            decrypt_file(key, filename)
            os.remove(filename)
