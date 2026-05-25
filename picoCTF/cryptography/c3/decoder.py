import sys
chars = ""
from fileinput import input
for line in input():
  chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

flag = ""

prev = 0
for char in chars:
  encoded = lookup2.index(char)
  cur = (encoded + prev) % 40
  flag += lookup1[cur]
  prev = cur

sys.stdout.write(flag)
