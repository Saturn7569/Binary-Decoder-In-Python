import os
os.system("cls")
txt=[]
while True:
  b=input("Enter A Binary Number: ")
  if b=="exit": break
  if len(b)!=8:
    print("invalid input length")
    continue
  i = 7
  d=0
  p=1
  while i>-1:
    if b[i]=="1":
      d+=p
    p*=2
    i-=1
  print(b,"=",d,"=",chr(d))
  txt.append(chr(d))
os.system("cls")
txtP=""
for i in txt:
  txtP+=i
print(txtP)
input("Type Anything To Terminate: ")
os.system("cls")
