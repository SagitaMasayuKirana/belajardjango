import re

pattern = r'\w+'

teks = ' This is string! Yes, this is string. And 123 is number. '

x = re.findall(pattern, teks)

print(x)