# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input()
res = ""
for ch in string:
    if ch.isalnum() or ch == ' ':
        res += ch

print(res)