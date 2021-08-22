for i in range(0,10,3):
    print(i)

for i in range(0,-6,-2):
    print(i)

print("While")
numero=0
while numero<=5:
    print(numero)
    numero=numero+1
else:
    print("Secuencia terminada")

#Funciones
def evaluar(cali):
    if cali>=8 and cali<9:
        print("SA")
    elif cali>=9 and cali<10:
        print('DE')
    elif  cali==10:
        print("AU")
    else:
        print("NA")

calificacion=input("Ingresa tu promedio: ")

if int(calificacion)>=8 and int(calificacion)<9:
        print("SA")
elif int(calificacion)>=9 and int(calificacion)<10:
        print('DE')
elif  int(calificacion)==10:
        print("AU")
else:
        print("NA")

calificacion=input("Ingresa tu promedio: ")
