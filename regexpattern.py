import re

def substring_regex(text):
    m = re.search('(?<=- )\d+.*', text) #(?<=- )stars with '- '; \d+ = number digits; .* = end of string
    if m:
        found = m.group(0)
        return found
    else:
        return "not found"

def start_end(text):
    m = re.search(r'\w+.\w+', text) #search both side of .
    if m:
        found = m.group(0)
        return found
    else:
        return "no found"

def start_end_email(text):
    m = re.search(r'\w+.\w+\w+@\w+\w+.\w+', text) #search email
    if m:
        found = m.group(0)
        return found
    else:
        return "no found"
#text = "$0 - 199.99";
#substring_regex(text)


print start_end("$0 - 199.99")

#print start_end_email("blaa timo.kuisma@sci.fi blaa blaa")
