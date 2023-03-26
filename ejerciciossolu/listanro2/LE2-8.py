# 8.Genear una funcion rango hasta un numero maximo (10^5), con un step y agregar a una lista
# los numeros que cumplan las siguientes opciones , que sean primos
rango=range(1,100001,1)
primos=[]

def primo(n):
  if n==1:
       return False
  else:
    for i in range(2,n):
            if (n%i) == 0:
                return False
    return True
def main():
    for i in rango:
        if primo(i):
            primos.append(i)
            
    print("Primos")
    print(primos)

main()





