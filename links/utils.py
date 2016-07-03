import random
import string


def gen_url(length=6):
    pool = string.ascii_letters + ''.join([str(x) for x in range(10)])
    url = ''.join([random.choice(pool) for _ in range(length)])
    return url
