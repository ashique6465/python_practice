import re 
def IP(test_ips):
    pattern = r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$'
    regex = re.compile(pattern)
    for ip in test_ips:
        print(f'{ip} => {bool(regex.match(ip))}')

test_ips = ["192.168.0.1", "10.0.0.255", "255.255.255.255", "256.100.50.25", "192.168.0", "abc.def.ghi.jkl"]

print(IP(test_ips))