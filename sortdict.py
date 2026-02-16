dictionary = {
    "b": 2 ,
    "c": 3 ,
    "a": 1,
    "d": 4
}

res = dict(sorted(dictionary.items(), key = lambda item: item[1] ))
print(res)