import re
text = "10.0.0.0/24"

pattern = r"(\d{1,3}(?:\.\d{1,3}){3})/(\d{1,2})"

match = re.match(pattern,text)
if match:
    ip  = match.group(1)
    mask = match.group(2)
    print(f'Ip: {ip}',f'CDR: {mask}')