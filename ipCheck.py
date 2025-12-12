import re 
def Solve(text):
    pattern = r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$'
    return True if re.fullmatch(pattern,text) else 0 

text = "10.0.0.1"
print(Solve(text))