import re
def text_match(text):
    pattern = r'\w+\S*$'
    ans = re.search(pattern,text)
    return True if ans else False

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))