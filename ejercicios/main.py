# 1 - pedir el radio de un circulo y calcular su área a pi r^2
'''import math
radio=float(input('Ingrese el radio del circulo: '))
area= math.pi * (radio*radio)
print('El area del circulo es:',area)'''

# 2 - Pedir el radio de una circunferencia y calcular su longitud
'''import math
radio=float(input('Ingrese el radio de la circunferencia:'))
longitud= math.pi * (radio+radio)
print('La longitud de la circunferencia es:',longitud)'''

# 3 - Pedir dos numeros y mostrar la suma
'''n1=int(input('Ingrese primer numero: '))
n2=int(input('Ingrese segundo numero: '))
suma:int = n1+n2

print('La suma es:' ,suma)'''

# 4 - Pedir 3 numeros y mostrar la multipilacion entre ambos (a*b*c)
'''n1=int(input('Ingrese primer numero: '))
n2=int(input('Ingrese segundo numero: '))
n3=int(input('Ingrese tercer numero: '))

multiplicacion:int = n1*n2*n3

print('La multiplicacion entre los tres numeros es:' ,multiplicacion)'''

# 5 - Pedir el nombre y la edad de una persona y mostrar: Jacinto tiene 5 años
'''nombre=str(input('Ingrese su nombre:'))
edad=int(input('Ingrese su edad:'))
print(nombre, 'tiene', edad, 'años.')'''

# 6 - Pedir 3 numeros y mostrarlos ordenados de menor a mayor
'''n1=int(input('Ingrese primer numero:'))
n2=int(input('Ingrese segundo numero:'))
n3=int(input('Ingrese tercer numero:'))
numeros = [n1, n2, n3]
numeros.sort()
print('Numeros de menor a mayor:',numeros)'''

# 7 - Pedir un numero entre 0 y 9.999 y decir cuantas cifras tiene
'''num=int(input('Ingrese un numero entre 0 y 9.999: '))
if num<10:
    print('El numero',num, 'tiene 1 cifra')
else:
    if num<100:
        print('El numero',num,'tiene 2 cifras')
    else:
        if num<1000:
            print('El numero',num,'tiene 3 cifras')
        else:
            if num<10000:
                print('El numero', num,'tiene 4 cifras')
            else:
                if num<100000:
                    print('El numero',num,'tiene 5 cifras')'''

# 8 - Pedir un numero entre 1000 y 9.999, decir si es capicua.(se lee igual de derecha a izquierda)
'''num=int(input('Ingrese un numero entre 1000 y 9.999: '))
n4= num%10 # el % me da el residuo de la division entre el numero que el usuario ingresa y el 10
n3=int((num%100)/10)# int para que me de solo la parte entera del residuo de la division
n2=int((num%1000)/100)
n1=int((num-(num%1000)) / 1000)# ejemplo 4538 - (el residuo de 4538/1000 es 538) / 1000 , y el int me da la parte entera de esta cuenta.
if n1 == n4 and n2 == n3:
    print('El numero',num,'es capicua')
else:
    print('El numero',num,'no es capicua')'''

# 9 - Pedir una nota de 0 a 10 y mostrarla de la forma: insuficiente, suficiente, bien. usando if
'''nota=float(input('Ingrese su calificacion: '))
if nota<=4:
    print('Insuficiente')
else:
    if nota<=7:
        print('Bien')
    else:
        if nota<=10:
            print('Suficiente')'''

# 10 - Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta. Soponiendo todos los meses de 30 dias.
'''dia=int(input('Ingrese dia: '))
mes=int(input('Ingrese mes (en numero):'))
año=int(input('Ingrese año: '))
if dia<=30 and dia>0 and mes>0 and mes<13 and año>0:
    print('La fecha que ingreso es valida.')
else:
    print('La fecha que ingreso es invalida.')'''

# 11 - Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta. Con meses de 28, 30 y 31 dias. sin años bisiestos.
'''def comprobar_fecha(año, mes, dia):

    dia=int(input('Ingrese dia: '))
    mes=int(input('Ingrese mes (en numero): '))
    año=int(input('Ingrese año: '))

    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]# Array que almacenara los dias que tiene cada mes

    if ((año % 4 == 0 and año % 100 != 0) or año % 400 == 0):  # Comprobar si el ano es bisiesto y anadir dia en febrero en caso afirmativo
        dias_mes[1] += 1

    if (mes < 1 or mes > 12): # Comprobar que el mes sea valido
        return False

    mes -= 1
    if (dia <= 0 or dia > dias_mes[mes]):# Comprobar que el dia sea valido
        return False

    return True  # Si ha pasado todas estas condiciones, la fecha es valida

correcta = comprobar_fecha(2000, 2, 29)

# Mostrar el resultado:
if (correcta):
    print("\n\nLa fecha ingresada es CORRECTA\n")

else:
    print("\n\nLa fecha ingresada es FALSA\n")'''

# 12 - Pedir el dia, mes y año de una fecha correcta y mostrar la fecha del dia siquiente. Suponer que todos los meses tienen 30 dias.
'''def dia_siguiente(dia, mes, año):
        dia = int(input('Ingrese dia: '))
        mes = int(input('Ingrese mes (en numero): '))
        año = int(input('Ingrese año: '))

        if mes in (1,2,3,4,5,6,7,8,9,10,11,12):
            dias_mes=30

            if dia < dias_mes:
                dia += 1
            else:
                dia=1
                if mes == 12:
                    mes =1
                    año += 1
                else:
                    mes +=1
            return (dia, mes, año)

print ('El dia siguiente a la fecha que ingreso es:', dia_siguiente(2, 3, 2020)'''

# 13 - Idem que el ejercicio 12 suponiendo que cada mes tiene un numero distinto de dias (suponer que febrero tiene siempre 28 dias)
'''def dia_siguiente(dia, mes, año):
        dia = int(input('Ingrese dia: '))
        mes = int(input('Ingrese mes (en numero): '))
        año = int(input('Ingrese año: '))

        if mes in (1,3,5,7,8,10,12):
            dias_mes = 31
        elif mes == 2:
            dias_mes = 28
        else:
            dias_mes = 30

        if dia < dias_mes:
            dia += 1
        else:
            dia = 1
            if mes == 12:
                mes = 1
                año += 1
            else:
                mes += 1
        return (dia, mes, año)


print('El dia siguiente a la fecha que ingreso es:', dia_siguiente(2, 3, 2020))'''

# 14 - Diseña una aplicacion que muestre las tablas de multiplicar del 1 al 10
'''tabla_desde = 1 #tablas del 1
tabla_hasta = 10 #al 10
desde = 1 #multiplicaciones desde el 1
hasta = 10 #hasta el 10

for factor1 in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {factor1}:') #mostramos una cabecera para cada tabla
	for factor2 in range(desde, hasta + 1):
		print(f'{factor1} x {factor2} = {factor1 * factor2}')
	print() #línea en blanco al final de cada tabla'''

# 15 - Realizar un programa que nos pida un numero n, y nos diga cuantos numeros hay entre 1 y n
'''num=int(input('Ingrese un numero: '))
suma = 0
for i  in range(num):
    suma=suma+1
print("Entre 1 y",num,'hay',suma, 'numeros')'''

# 16 - Realizar un programa que cuente la cantidad de numeros pares desde 1 hasta un numero ingresado por el usuario.
'''numero = int(input("Ingrese Numero: "))
start = 1
print('Numeros pares desde 1 hasta', numero, ':')

for num in range(start, numero + 1):

    if num % 2 == 0:
        print(num, end=" ")'''

# 17 - Realizar un programa que cuente la cantidad de numeros pares entre dos ingresados por el usuario y ademas muestre la suma de dichos numeros.
'''numero1=int(input('Ingrese un numero: '))
numero2=int(input('Ingrese otro numero: '))
suma=0

for num in range (numero1,numero2 + 1):
    if num % 2 ==0:
        suma = suma + 1
        print(num,end=' ')
print('\nentre', numero1, 'y', numero2,'hay', suma, 'numeros pares.')

print('\nLa suma entre ellos es: ')
nuevonum=0
for num in range (numero1, numero2+1):
    if num % 2 ==0:
        nuevonum= nuevonum+num
print(nuevonum)'''

# 18 - Realizar un juego del ahorcado en python. El juego es de a dos personas. El verdugo y el ahorcado. Siempre seran palabras de 6 caracteres. En caso de ser menos las ultimas letras seran gionoes.
'''palabraIngresada=""

print("Eres el verdugo, ingrese la palabra secreta que debe adivinar el ahorcado")
verdugo=str(input("(debe ocupar 6 caracteres,si es menor a 6, en las últimas letras ingrese guiones para completar): "))

#La función list() toma una cadena como argumento y la convierte en una lista. Cada carácter de la cadena se convierte
# en el elemento individual de la lista.
palabraSecreta= list(verdugo)

# Verificamos que la palabra esté correctamente ingresada
#la función len() se usa para obtener el número de elementos en la lista de palabraSecreta

while len(palabraSecreta) != 6 :
        palabraSecreta = str(input("Verdugo ingrese una palabra que contenga 6 caracteres y si es menor a 6, recuerde completar con guiónes al final de la palabra: "))

vidas = 6
while vidas > 0:
    fallas=0
    #Recorremos la lista que contiene la palabra secreta, se tendrá en cuenta el guión
    for letras in palabraSecreta:
        #Verficamos si la letra está dentro de la palabra secreta
        if letras in palabraIngresada:
            #Imprimimos en una linea
            print(letras, end= "")
        else:
            #Imprime "_" si no encuentra la letra dentro de la palabra secreta
            print("_", end="")
            #sumamos una falla
            fallas+=1
    #cuando no tenga fallas el ahorcado salva su vida
    if fallas ==0:
        print (" Muy Bien! Te salvaste")
        break

    letraIngresada=str(input("Eres el ahorcado. Intenta adivinar la palabra secreta para salvar tu vida. Ingrese una letra: "))
    #Vamos añadiendo la letra que introduce el usuario dentro de la variable de "palabraIngresada"
    palabraIngresada += letraIngresada

    #Busca si no está la letra dentro de la palabra a través del "not in"
    if letraIngresada not in palabraSecreta:
        #Si no está la letra en la palabra
        vidas -=1
        print("Te equivocaste")
        print (f"Tienes {vidas} vidas")
    if vidas == 0:
        print ("Te ahorcaron. Qué mal!")'''


# 19 - Pedir tres notas numerica entera entre 1 y 10 y mostrar dicha nota de la forma: Uno, Dos, Tres... Realizarlo con for e if.
'''nota1=int(input('Ingrese 1er nota: '))
nota2=int(input('Ingrese 2da nota: '))
nota3=int(input('Ingrese 3er nota: '))

for i in range (1,11):
    if nota1 == 1:
        print('Uno')
        break
    elif nota1 == 2:
        print('Dos')
        break
    elif nota1  == 3:
        print('Tres')
        break
    elif nota1  == 4:
        print('Cuatro')
        break
    elif nota1 == 5:
        print('Cinco')
        break
    elif nota1  == 6:
        print('Seis')
        break
    elif nota1  == 7:
        print('Siete')
        break
    elif nota1  == 8:
        print('Ocho')
        break
    elif nota1  == 9:
        print('Nueve')
        break
    elif nota1 == 10:
        print('Diez')
        break

for i in range (1,11):
    if nota2 == 1:
        print('Uno')
        break
    elif nota2 == 2:
        print('Dos')
        break
    elif nota2  == 3:
        print('Tres')
        break
    elif nota2  == 4:
        print('Cuatro')
        break
    elif nota2 == 5:
        print('Cinco')
        break
    elif nota2  == 6:
        print('Seis')
        break
    elif nota2  == 7:
        print('Siete')
        break
    elif nota2  == 8:
        print('Ocho')
        break
    elif nota2  == 9:
        print('Nueve')
        break
    elif nota2 == 10:
        print('Diez')
        break

for i in range (1,11):
    if nota3 == 1:
        print('Uno')
        break
    elif nota3 == 2:
        print('Dos')
        break
    elif nota3  == 3:
        print('Tres')
        break
    elif nota3  == 4:
        print('Cuatro')
        break
    elif nota3 == 5:
        print('Cinco')
        break
    elif nota3  == 6:
        print('Seis')
        break
    elif nota3  == 7:
        print('Siete')
        break
    elif nota3  == 8:
        print('Ocho')
        break
    elif nota3  == 9:
        print('Nueve')
        break
    elif nota3 == 10:
        print('Diez')
        break'''


#20 Realizar un programa que calcule todos los multiplos de 3 entre dos numeros ingresados por el usuario.
'''numero1=int(input('Ingrese un numero: '))
numero2=int(input('Ingrese un numero mayor al amterior numero: '))
suma=0
print('Numeros multiplos de 3:')

for num in range(numero1, numero2 + 1 ) :

    if num % 3 == 0:
        suma=suma+1

        print(num, end=" ")
print('\nEntre', numero1, 'y', numero2, 'hay', suma, 'numeros multiplos de 3.')'''

# 21 - Realizar un programa que sume los numeros ingresados por teclado mientras que el numero ingresado no sea 0
'''num1= int(input('Ingrese un numero: '))
num2= int(input('Ingrese otro numero: '))

if num1 and num2 !=0:
   print('El resultado de la suma de ambos numeros es: ' ,num1+num2)

else:
    print('Debe ingresar numeros diferentes a 0')'''


# 22 - Realizar un programa que multiplique los numeros ingresados por teclado mientras que el numero ingresado no sea 0
'''num1= int(input('Ingrese un numero: '))
num2= int(input('Ingrese otro numero: '))

if num1 and num2 !=0:
   print('El resultado de la multiplicacion de ambos numeros es: ' ,num1*num2)

else:
    print('Debe ingresar numeros diferentes a 0')'''

# 23 - Realizar una calculadora con menu. El menu contendra las 4 operaciones basicas y una opcion para salir. Al salir del programa se mostrara el resultado final del calculo.
'''print('************ Bienvenida/o ***************')
print(' Opcion 1: Sumar \n Opcion 2: Restar \n Opcion 3: multiplicar  \n Opcion 4: Dividir \n Opcion 0: salir \n ')
opc=int(input('Ingrese una opcion: '))

while opc  !=0 :
    num1 = int(input('Ingrese primer numero: '))
    num2 = int(input('Ingrese segundo numero: '))

    if opc == 1:
        print('\nEl resultado es:' ,num1 + num2)
    elif opc ==2:
        print('\nEl resultado es:' ,num1 - num2)
    elif opc ==3:
        print('\nEl resultado es:' ,num1 * num2)
    elif opc ==4:
        print('\nEl resultado es:' ,num1 / num2)
    else:
        print('\nPor favor ingrese una opcion correcta')

    print(' \n Opcion 1: Sumar \n Opcion 2: Restar \n Opcion 3: multiplicar  \n Opcion 4: Dividir \n Opcion 0: salir \n ')
    opc = int(input('Ingrese una opcion: '))'''



# 24 - Dibuja un cuadrado de n elementos de lado utilizando * (astericos)
'''lado=int(input('Ingrese numero para el lado del cuadrado: '))

for i in range(lado):
    print ('* ' * lado)'''