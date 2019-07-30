# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(req):
  return render(req, 'commathweb/index.html')

def decto32fp(req):
  if req.method == 'POST':
    d = float(req.POST.get('number'))
    nb = bin(int(d))
    lung = d - int(d)
    bilung=''
    while(lung!=0):
      lung*=2
      bilung = bilung+str(int(lung))
      lung -= int(lung)
    nb = nb[2:]
    e = len(nb)-1
    s = '0' if d >= 0 else '1'
    e += 127
    bie = bin(e)
    nbbilung = nb+bilung
    bie = bie[2:]
    nbbilung = nbbilung[1:]
    b = s+bie+nbbilung
    b = b + '0'*(32-len(b))
    dec = Convertback32(b)

    result = {
      'result' : b,
      'dec' : dec
    }

    return render(req, 'commathweb/dto32.html',result)
  else:
    return render(req, 'commathweb/dto32.html')

def decto64fp(req):
  if req.method == 'POST':
    d = float(req.POST.get('number'))
    nb = bin(int(d))
    lung = d - int(d)

    bilung=''

    count = 0
    while(lung!=0):
      lung*=2
      bilung = bilung+str(int(lung))
      lung -= int(lung)
      count += 1
      if count == 44 : break

    nb = nb[2:]
    e = len(nb)-1

    s = '0' if d >= 0 else '1'
    e += 1023
    bie = bin(e)

    nbbilung = nb+bilung
    bie = bie[2:]
    nbbilung = nbbilung[1:]
    bx = s+bie+nbbilung
    b = bx + '0'*(64-len(bx))
    dec = Convertback64(b)

    result = {
      'result' : b,
      'dec' : dec

    }
    return render(req, 'commathweb/dto64.html',result)
  else:
    return render(req, 'commathweb/dto64.html')

def Convertback32(x):
  x = str(x)
  s = int(x[0])
  e = int(x[1:9],2)
  f = 1+sum([ int(x[8+i])*2**-i for i in range(1,24) ])
  y = (-1)**s * 2**(e-127) * f
  return y

def Convertback64(x):
  x = str(x)
  s = int(x[0])
  e = int(x[1:12],2)
  f = 1+sum([int(x[11+i])*2**-i for i in range(1,53)])
  y = (-1)**s * 2**(e-1023) * f
  return y


def cal_solve(A, b):
    import numpy as np
    a,b = np.array(A), np.array(b)
    n= len(A[0])
    x = np.array([0]*n)

    for k in range(0, n-1):
        for j in range(k+1, n):
            if a[j,k] != 0.0:
                lam = a[j][k]/a[k][k]
                a[j,k:n] = a[j, k:n] - lam*a[k,k:n]
                b[j] = b[j] - lam*b[k]
    for k in range(n-1,-1,-1):
        x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]
    return x.flatten()

def solve(req):
  try:
    if req.method == 'POST':
      matrix_y=[]
      matrix_x=[]
      data= req.POST.get('number')
      sp = data.split('\n')
      for i in sp:
        y=[float( i.split('=')[-1] )]
        matrix_y.append(y)
        x = (i.split('=')[0]).split(',')
        matrix_x.append(list(map(float, x)))

      result=cal_solve(matrix_x,matrix_y)
  
      results = {
        'result':result
      }
      return render(req,'commathweb/solve.html',results)  
    else:
      return render(req,'commathweb/solve.html')
  except:
    err = "กรุณากรอกใหม่"
    text = {
      'text':err
    }
    return render(req,'commathweb/solve.html',text)
  