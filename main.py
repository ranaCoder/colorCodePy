R = float(input("Enter value of R : "))
G = float(input("Enter value of G : "))
B = float(input("Enter value of B : "))


r = R/255
g= G/255
b = B/255
w = max(r,g,b)
if ((R==0 and G==0 and B == 0 ) and (R<=255 and G<=255 and B<=255 )):
  C = 0
  M =0
  Y = 0
  K = 1
else:
  C= (w -R/255)/w
  M= (w -G/255)/w
  Y= (w -B/255)/w
  K = 1-w
  print(C)
  print(M)
  print(Y)
  print(K)
  
  