# -*- coding: utf-8 -*-

# Set up the variables we'll use
uni_greeting = u'Hi, my name is %s.'
utf8_greeting = uni_greeting.encode('utf-8')
print utf8_greeting

uni_name = u'José'  # Note the accented e.
utf8_name = uni_name.encode('utf-8')
print utf8_name

# Plugging a Unicode into another Unicode works fine
print uni_greeting % uni_name

#Plugging UTF-8 into another UTF-8 string works too
print utf8_greeting % utf8_name


# You can plug Unicode into a UTF-8 byte sequence...
print utf8_greeting % uni_name  # UTF-8 invisibly decoded into Unicode; note the return type

# But plugging a UTF-8 string into a Unicode doesn't work so well...
#print uni_greeting % utf8_name  # Invisible decoding doesn't work in this direction
'''Traceback (most recent call last):
  File "C:/Users/Timo/Desktop/Robot Framework/Robot Framework/mysql_connection/unicode.py", line 23, in <module>
    print uni_greeting % utf8_name  # Invisible decoding doesn't work in this direction
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)
'''

# Unless you plug in ASCII-compatible data, that is.
print uni_greeting % u'Bob'.encode('utf-8')

# And you can forget about string interpolation completely if you're using UTF-16
#uni_greeting.encode('utf-16') % uni_name
'''
Traceback (most recent call last):
  File "C:/Users/Timo/Desktop/Robot Framework/Robot Framework/mysql_connection/unicode.py", line 34, in <module>
    uni_greeting.encode('utf-16') % uni_name
ValueError: unsupported format character ' ' (0x0) at index 33 '''

# Well, you can interpolate utf-16 into utf-8 because these are just byte sequences
#print utf8_greeting % uni_name.encode('utf-16')  # But this is a useless mess


