PI = 3.141592653589793236433850288 #constante pi
def funcion(n):
  if (n!=0):
    suma=0.0
    for i in range (1,n+1):
      a=(i-1.0)/n
      b=float(i)/n
      xi=(i-0.5)/n	
      fxi=4.0/(1.0 +xi*xi)
      suma= suma + fxi
    resultado=suma/n
    return resultado

n=int(raw_input('Valor de n:'))
m=int(raw_input('Valor de m:'))
resultados=[]
print funcion(n)
for j in range(1, m+1):
  pi= funcion(j*n)
  resultados= resultados + [pi]
print resultados