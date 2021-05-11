import hashlib

def substr_count(str):
    sum_substring = set()

    for i in range(len(str)):
        for j in range(len(str), i,-1):
            hash_str = hashlib.sha1(str[i:j].encode('utf-8')).hexdigest()
            sum_substring.add(hash_str)
    return len(sum_substring)-1

s = input("Введите строку: ")
print(substr_count(s))




