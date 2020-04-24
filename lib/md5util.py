
import hashlib


def get_file_md5(file):

    md5_l = hashlib.md5()
    with open(file, mode="rb") as f:
        by = f.read()

    md5_l.update(by)
    ret = md5_l.hexdigest()
    return ret
