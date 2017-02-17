# coding=utf-8
str = """
rabb rākhā ! xudā hāfiz ! allā belī ! rām bhalī kare ! hāe rabbā !
"""
a = str.splitlines()
result =""
for words in a:
    result +=words + " "

print result
