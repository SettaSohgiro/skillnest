
#declaraciones de variables

arr_estudiantes = []
arr_asignaturas = []
arr_est_asig = []

# funciones para el sistema de calificaciones

# funcion para validar el ingreso de numeros enteros
def validar_int(msn):
    if msn == "":
        msn = "Ingrese un numero : "

    while True:
        try:
            num = int(input(f"{msn}"))
            return num
        except ValueError:
            print("¡Error! Por favor, ingrese un número válido.")


def obtener_numero_estudiantes():
    # Pide al usuario el número de estudiantes y devuelve el valor
    # pregunta si quiere ingresar mas estudiantes

    if len(arr_estudiantes) > 0:
        print(f"ya se han ingresado los siguientes estudiantes : ")
        mostrar_estudiantes()       
        sin = input("si desea agregar mas estudiantes ingrese si : ")
        if sin.lower() == "si":
            agregar_estudiantes()
        else:
            menu_principal()
    else:
        agregar_estudiantes()

def agregar_estudiantes():
    #num_estudiantes =int(input("Ingrese el numero de estudiantes : "))
    # ingresa el primer estudiante a la lista ymuestra lo que ya estan en la lista
    num_estudiantes = validar_int("Ingrese el numero de estudiantes : ")
    print(f"numero de estudiante ingresado : {num_estudiantes}")
    for x in range(num_estudiantes):
        nombre = obtener_nombre_estudiante()
        promedio = 0
        estado = "pendiente"

        arr_estudiantes.append({
            'nombre': nombre,
            'promedio': promedio,
            'estado': estado
            })
    print(f"\nestudiantes ingresados : ")

    for estudiante in arr_estudiantes:
        print(f"nombre : {estudiante['nombre']}")

    #print("\nfalta agregar las asignaturas a los estudiantes y sus calificaciones")  

def obtener_nombre_estudiante():
    # Pide al usuario el nombre del estudiante y devuelve el valor
    nombre = input("Ingrese el nombre del estudiante : ")
    return nombre        


def mostrar_estudiantes():
    # Muestra los estudiantes ingresados
    if len(arr_estudiantes) > 0:
        print("\nEstudiantes ingresados:")
        for estudiante in arr_estudiantes:
            print(f"- {estudiante['nombre']}")
    else:
        print("No se han ingresado estudiantes aún.")        

# -----------------------------------------------------------------------------------------------------------------------        

def mostrar_asignaturas():
    # Muestra las asignaturas ingresadas
    if len(arr_asignaturas) > 0:
        print("\nAsignaturas ingresadas:")
        for asigna in arr_asignaturas:
            print(f"- {asigna['asignatura']}")
        print("\n")
    else:
        print("No se han ingresado asignaturas aún.")        


def obtener_numero_asignaturas():
    # Pide al usuario el número de asignaturas y devuelve el valor
    if len(arr_asignaturas) >0:
        print(f"ya se han ingresado las siguientes asignaturas : ")
        mostrar_asignaturas()       
        sin = input("si desea agregar mas asignaturas ingrese si : ")
        if sin.lower() == "si":
            agregar_asignaturas()
        else:
            menu_principal()
    else:
        agregar_asignaturas()


def agregar_asignaturas():
    #agrega asignaturas a la lista de asignaturas y muestra lo que ya estan en la lista

    num_asignaturas = validar_int("Ingrese el numero de asignaturas : ")
    #  print(f"numero de estudiante ingresado : {num_estudiantes}")
    for x in range(num_asignaturas):
        asignatura = obtener_nombre_asignatura()
        arr_asignaturas.append({
            'asignatura': asignatura
                })
        
    print(f"\nasignaturas ingresadas : ")

    for asign in arr_asignaturas:
        print(f"nombre asignatura : {asign['asignatura']}")


def obtener_nombre_asignatura():
    # Pide al usuario el nombre de la asignatura y devuelve el valor
    nom_asignatura = input("Ingrese el nombre de la asignatura : ")
    return nom_asignatura

def mostrar_asignaturas():
    # Muestra las asignaturas ingresadas
    if len(arr_asignaturas) > 0:
        print("\nAsignaturas ingresadas:")
        for asigna in arr_asignaturas:
            print(f"- {asigna['asignatura']}")
        print("\n")
    else:
        print("No se han ingresado asignaturas aún.")        


# -----------------------------------------------------------------------------------------------------------------------
def agregar_asignaturas_o_calificaciones():
    # Agrega asignaturas o calificaciones a los estudiantes

    if len(arr_estudiantes) > 0 and len(arr_asignaturas) > 0:
        print(f"Desea agregar asignaturas o calificaciones a los estudiantes : ")
        while True:
    
            subopcion = submenu1() 
            if subopcion == "1":
                print("agregar notas") 
                obtener_calificaciones()

            elif subopcion == "2":
                print("agregar asignaturas")
                agregar_asignaturas_estudiantes()
            elif subopcion == "3":
                break    
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

    else:
        print("Primero debe ingresar estudiantes y asignaturas para agregar asignaturas o calificaciones a los estudiantes")
        menu_principal()



def obtener_rango_calificaciones(asig, nom_est):
    # Pide al usuario las calificaciones para cada asignatura y las devuelve en una lista
    while  True:
        #calificacion = int(input(f"Ingrese la calificacion del 1 al 10 para la asignatura {asig} del estudiante {nom_est} : "))
        calificacion = validar_int(f"Ingrese la calificacion del 1 al 10 para la asignatura {asig} del estudiante {nom_est} : ")
        if calificacion >= 1 and calificacion <= 10:
            return calificacion
          
        else:
            print("calificacion no valida, por favor ingrese una calificacion del 1 al 10")
            


def obtener_calificaciones():
    # Agrega calificaciones a los estudiantes

    mostrar_estudiantes_con_asignaturas()
    nom_est = input("Ingrese el nombre del estudiante al que desea agregar calificaciones : ")
    if nom_est in [est['nombre'] for est in arr_est_asig]:
        for est in arr_est_asig:
            if est['nombre'] == nom_est:
                arr_carga = est[nom_est+'_asig']
                for asig in arr_carga:
           #         print(f"asignatura : {asig['asignatura']} - calificacion : {asig['calificacion']}")
                    calificacion = obtener_rango_calificaciones(asig['asignatura'], nom_est)
                    asig['calificacion'] = calificacion
                # est[nom_est+'_asig'] = arr_carga


        # nom_asig = input(f"Cual es la asignatura que desea agregar calificaciones al estudiante {nom_est} :")
        # if nom_asig in [est['asignatura'] for est in arr_est_asig]:
        #     arr_est_asig[nom_asig] = input(f"Ingrese la calificacion para la asignatura {nom_asig} del estudiante {nom_est} : ")
    else:
        print(f"el estudiante no existe, por favor ingrese un estudiante valido")    

    print(f"\ncalificaciones agregadas a los estudiantes : {arr_est_asig}")    

def agregar_asignaturas_estudiantes():
    # Agrega calificaciones a los estudiantes
    
    mostrar_estudiantes()
    mostrar_asignaturas()
    nom_est = input("Ingrese el nombre del estudiante : ")
    nom_asig = input("Ingrese el nombre de la asignatura que desea agregar : ")
    if nom_est in [est['nombre']for est in arr_est_asig]:
        for est in arr_est_asig:
            #print("est : ",est['nombre']," - ",est[nom_est+'_asig'])
            print("for est : ",est)
            if est['nombre'] == nom_est:
                arr_carga = est[nom_est+'_asig']
                if nom_asig in [est_carga['asignatura'] for est_carga in arr_carga]:
                    print(f"la asignatura ya se ha agregado al estudiante")
                else:
         #           print(f"no existe la asignatura")   
                    arr_carga.append({
                        'asignatura': nom_asig, 
                        'calificacion': 0
                    })
                print("arr_carga : ", arr_carga,nom_est+'_asig')            
                est[nom_est+'_asig'] = arr_carga
    else:
        print(f"Ingrese una asignarura para el estudiante {nom_est} : ")   
        arr_est_asig.append({
            'nombre': nom_est, 
            nom_est+'_asig': [{
                'asignatura': nom_asig,
                'calificacion': 0
            }]
})
    

    print(f"\nAsignaturas agregadas a los estudiantes : {arr_est_asig}")    


def mostrar_estudiantes_con_asignaturas():
    # Muestra las asignaturas ingresadas
    if len(arr_est_asig) > 0:
        print("\nAsignaturas ingresadas:")
        for asigna in arr_est_asig:
# print(f"- {asigna['asignatura']}")
            print(f"- {asigna}")
        print("\n")
    else:
        print("No se han ingresado asignaturas aún.")        

# -----------------------------------------------------------------------------------------------------------------------

def calcular_promedio(estu):
    # Calcula y devuelve el promedio de las calificaciones
    suma = 0
    largo = 0
    prom = 0
    for estprom in arr_est_asig:
        #print(f"estprom : {estprom} - estu : {estu}")
        if estprom['nombre'] == estu:
            if estu+'_asig' in estprom:    
                largo = len(estprom[estu+'_asig'])
                for calif in estprom[estu+'_asig']:
                    suma += calif['calificacion']
    if suma > 0:
       # suma / largo if estprom[estu+'_asig'] else 0                
        prom = suma / largo

    return prom

def determinar_estado(promedio):
    # Determina si el estudiante ha aprobado o reprobado basándose en el promedio
    if promedio >= 6:
        return "aprobado"
    else:
        return "reprobado"

# -----------------------------------------------------------------------------------------------------------------------

def imprimir_resumen():
# Imprime un resumen con el nombre de los estudiantes, su promedio y su estado
    if len(arr_estudiantes) > 0:
        print("\n----------------------------------------------------------------------------------------")
        print("                           Reporte de los estudiantes                                \n")
        print("----------------------------------------------------------------------------------------\n")
        for estudiante in arr_estudiantes:
          #  print(f"array estudiantes : {estudiante}")
            prom = calcular_promedio(estudiante['nombre'])
          #  print(f"promedio : {prom}")
            estudiante['promedio'] = prom
            estado = determinar_estado(prom)
            estudiante['estado'] = estado
            if estudiante['promedio'] == 0 or estudiante['estado'] == "pendiente":
                print(f"nombre estudiante : {estudiante['nombre']} - promedio : {estudiante['promedio']} - estado : {estudiante['estado']} - falta agregar datos")
            else:    
                print(f"nombre estudiante : {estudiante['nombre']} - promedio : {estudiante['promedio']} - estado : {estudiante['estado']}")   
        print("\n----------------------------------------------------------------------------------------\n")        
    else:
        print("No se han ingresado estudiantes aún.")        
            
    while True:
      #  print("break")
        break        

def menu_principal():
    print("\nSistema de Calificaciones 1.0\n")
    print(" Opciones disponibles:")
    print(" 1. Agregar numero de estudiantes ")
    print(" 2. Agregar asignaturas ")
    print(" 3. Agregar asignaturas o calificaciones a los estudiantes ")
    print(" 4. Mostrar estudiantes")
    print(" 5. Salir")
    opt = input("Seleccione una opcion : ")
    return opt

#programacion del sistema de calificaciones


#----------------------------------------------------------------------------------------
#---------------------------- submenu agregar calificaciones y asignaturas -----------------------------------------


def submenu1():
    print("\nSistema de Calificaciones 1.0\n")
    print(" Opciones disponibles:")
    print(" 1. Agregar calificaciones a estudiantes ")
    print(" 2. Agregar asignaturas a estudiantes ")
    print(" 3. Salir")
    opt = input("Seleccione una opcion : ")
    return opt



#----------------------------------------------------------------------------------------
#---------------------------- Menu principal del sistema de calificaciones -----------------------------------------
while True:
    
    opcion = menu_principal() 
    if opcion == "1":
        obtener_numero_estudiantes()
    elif opcion == "2":
        obtener_numero_asignaturas()
    elif opcion == "3":
        agregar_asignaturas_o_calificaciones()
    elif opcion == "4":
        imprimir_resumen()
    elif opcion == "5":
        break    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")



