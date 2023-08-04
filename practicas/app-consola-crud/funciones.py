
# LISTAR DATOS
def listar_cursos(cursos):
    print("\nCursos: \n")
    contador=1
    for cur in cursos:
        datos = "{}. Código: {} | Nombre: {} ({} créditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print(" ")


# PEDIR DATOS PARA REGISTRO
def pedir_datos_registro():
    # Validación del código ingresado, debiendo ser de 6 números
    codigo_correcto = False
    while not codigo_correcto:
        codigo = input("Ingrese código del curso: ")
        if len(codigo) == 6:
            codigo_correcto = True
        else:
            print("Código incorrecto, debe tener 6 dígitos.")
    nombre = input("Ingrese nombre del curso: ")
    # Validación del número de créditos para que no se ingrese text, debe ser número entero
    creditos_correcto = False
    while not creditos_correcto:
        creditos = (input("Ingrese número de créditos del curso: "))
        if creditos.isnumeric():
            if int(creditos) > 0:
                creditos_correcto = True
                creditos = int(creditos)
            else:
                print("Los créditos deben ser mayor a 0")
        else:
            print("Créditos incorrectos, debe ser un número únicamente.")
    curso = (codigo, nombre, creditos)
    return curso


# PEDIR DATOS PARA ACTUALIZAR
def pedir_datos_actualizacion(cursos):
    listar_cursos(cursos)
    existe_codigo = False
    codigo_editar = input("Ingrese el código del que desea actualizar: ")
    for cur in cursos:
        if cur[0] == codigo_editar:
            existe_codigo = True
            break
    if existe_codigo:
        nombre = input("Ingrese nuevo nombre para el curso: ")
        # Validación del número de créditos para que no se ingrese text, debe ser número entero
        creditos_correcto = False
        while not creditos_correcto:
            creditos = input("Ingrese número de créditos del curso a modificar: ")
            if creditos.isnumeric():
                if int(creditos) > 0:
                    creditos_correcto = True
                    creditos = int(creditos)
                else:
                    print("Los créditos deben ser mayor a 0")
            else:
                print("Créditos incorrectos, debe ser un número únicamente.")
        curso = (codigo_editar, nombre, creditos)
    else:
        curso = None
    return curso


# PEDIR DATOS PARA ELIMINAR
def pedir_datos_eliminacion(cursos):
    listar_cursos(cursos)
    existe_codigo = False
    codigo_eliminar = input("Ingrese el código del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == codigo_eliminar:
            existe_codigo = True
            break
    if not existe_codigo:
        codigo_eliminar = ""

    return codigo_eliminar



