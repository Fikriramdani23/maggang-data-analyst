def fpb(a,b):
  if b == 0:
    return a;  
  else: 
    return fpb(b,a%b)

def kpk(a,b):
  kpk=int(a*b/fpb(a,b))
  return kpk

a = int(input('masukan angka ke-1 :'))
b= int(input('masukan angka ke-2:'))

print('FPB dari',a,'dan',b,'adalah',fpb(a,b))
print('KPK dari',a,'dan',b,'adalah',kpk(a,b))