# encoding=utf-8
import io

f = io.open("abc.txt","wt", encoding="utf-8")

f.write(u"hello world ")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()

print(text)