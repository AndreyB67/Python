import hashlib

def substr_count(string_):
    sum_substr = set()

    for i in range(len(string_)):
        for j in range(len(string_), i,-1):
            hash_str = hashlib.sha1(string_[i:j].encode('utf-8')).hexdigest()
            sum_substr.add(hash_str)
    return len(sum_substr)-1

s = input("Введите строку: ")
print(substr_count(s))




