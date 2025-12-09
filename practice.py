# import re
# text = '192.168.1.1 - - [01/Dec/2025:10:30:45 +0000] "GET /api/users HTTP/1.1" 200'
# pattern = re.compile(r'\b(?P<ip>(?:\d{1,3}\.){3}\d{1,3})(?::(?P<port>\d{1,3}))?\b.*?(?P<timestamp>\d{1,2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2}\s[+\-]\d{4})')
# m = pattern.search(text)
# if m:
#     print(m.group('ip'))
#     print(m.group('port'))
#     print(m.group('timestamp'))
# else:
#     print('No match')

import re
text = """(555) 123-4567
555-123-4567
555.123.4567
5551234567"""
pattern = re.compile(r"""(?P<area>\d{3}) \D*(?P<prefix>\d{3})\D*(?P<suffix>\d{4})""", re.VERBOSE)

normalize = []
for match in pattern.finditer(text):
    area = match.group("area")
    prefix = match.group("prefix")
    suffix = match.group("suffix")

normalize.append(f'{area}-{prefix}-{suffix}')
print(''.join(normalize))