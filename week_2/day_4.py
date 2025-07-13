#text="This is regex"
#pattern=r"[a-z]"
#matches=re.search(pattern,text)
#print(matches)pip install
import re
#text="This is regex"
#pattern=r"[a-z]"
#matches=re.search(pattern,text)
#print(matches)
#pattern=r"\+d{3}\s\d{3}\s\d{3}\s\d{3}"
#text="my phone number is +254 712 345 678" 
#matches=re.findall(pattern,text)
#print(matches)
#number= +254 321 765 546 and (+234)-123-456-245
#pattern=r"\(?\+\)?\-?\d{3}\-?\d{3}\-?\d{3}\-?\d{3}"
#matches=re.findall(pattern, text)
#print(matches)

#pattern=r"[a-zA-Z0-9-_?]+\@[a-zA-Z]+\.com"
#email="clare@gmail.com or clare@YAhoo.com or clare2?0@yAhoo.com"
#matches=re.findall(pattern, email)
#print(matches)

text="This is regex"
#pattern=r"[a-z]"
#matches=re.findall(pattern,text)
#print(matches)
#pattern=r"[a-z]+"
#matches=re.search(pattern,text)
#print(matches)

#text="ab aab abc aaabb"
#pattern=r"a.b"
#matches=re.findall(pattern,text)
#print(matches)

number="+254 702 345 678"
#pattern=r"\+\d{3}\s\d{3}\s\d{3}\s\d{3}"
#matches=re.findall(pattern,number)
#print(matches)

#for groupings use the re.search
#pattern=r"(\+\d{3})\s(\d{3})\s(\d{3})\s(\d{3})"
#matches=re.search(pattern,number)
#print(matches.group(0))
#print(matches.group(1))
#print(matches.group(2))
#print(matches.group(3))
#print(matches.group(4))

#number="(+254) 701 234 567 or +254 701 234 567"
#pattern=r"\(?\+\d{3}\)?\s\d{3}\s\d{3}\s\d{3}"
#matches=re.findall(pattern,number)
#print(matches)



