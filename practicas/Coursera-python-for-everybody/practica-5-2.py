'''
Escriba un programa que solicite repetidamente al usuario números enteros hasta que el usuario ingrese 'listo'.
Una vez que se ingrese "listo", imprima el mayor y el menor de los números. 
Si el usuario ingresa algo que no sea un número válido, 
descárguelo con un try / except y envíe un mensaje apropiado e ignore el número. 
Ingrese 7, 2, bob, 10 y 4 y haga coincidir la salida a continuación.
'''
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue
    
    
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    print (f"numero: {num}, mas grande: {largest}")

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    print(f"numero: {num}, mas pequeño: {smallest}")
    
    
print("Maximum", largest)
print('Minimum', smallest)