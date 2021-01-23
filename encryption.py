import hashlib


def get_md5(msg: str):
    secret_key = '@#$%^&*()'
    md5 = hashlib.md5(msg.encode('utf-8'))
    md5.update(secret_key.encode('utf-8'))
    return md5.hexdigest()


# a = [1, 2, 3, 4, 5, 6]
# print(sum(list(map(lambda x: a[x] + 3, list(filter(lambda x: a.index(x) % 2 == 0, a))))))
#
# print(sum([a[i] + 3 for i in list(filter(lambda x: a.index(x) % 2 == 0, a))]))