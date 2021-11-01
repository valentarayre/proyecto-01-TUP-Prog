import re 
import json

def cambiar_numero(num):
    if len(num) == 0:
        return num
    else:
        if int(num[-1]) % 2 == 0:
            return cambiar_numero(num[:-1]) + "1"
        else:
            return cambiar_numero(num[:-1]) + "2"
def cambiar_numero2(num):
    if num == 0:
        return num
    else:        
        if (num % 10) % 2 == 0:            
            return cambiar_numero2(num // 10) * 10 + 1
        else:
            return cambiar_numero2(num // 10) * 10 + 2

def cambiar_lista(lista):
    if len(lista) <= 0:
        return lista
    else:        
        return cambiar_lista(lista[:-1]) + lista[-1]

def compara_list(list1, list2):
    #Si tienen distinto cantidad de elementos, son diferentes
    if len(list1) != len(list2):
        return False
    #Si las dos estan vacias son iguales
    if not (list1 and list2):
        return True
    # Compara los dos primeros elementos si son iguales
    if list1[0] != list2[0]:
        return False
    # llama de vuelta a la funcion sin el primer elemento de la lista
    return compara_list(list1[1:], list2[1:])

def divicion_ent(a,b):
    if a <= 0:
        return a
    else:
        return divicion_ent(a-b,b) +1

def calcular_pi(i):
    if i == 0:
        return 4
    else:
        return (4 * (-1)**i) * (1/(2*i+1)) + calcular_pi(i-1)
    
def mostrar_estacion(data):
    cont = 0
    for e in data:
        aux = e['nombre']
        print(f'{cont:>3d} : {aux:<20s}')
        cont +=1

    try:        
        selec = int(input('Seleccione la Opcion: '))    
        element = data[selec]    
        print('Cantidad de sensores de la estacion "{}": {}'.format(element["nombre"], len(element["sensor"])))
        for e in element["sensor"]:        
            print('{:<19s}: {}{}'.format(e["tipo"],e["medicion"],e["escala"]))
    except Exception: 
        print("No se encontro esa opcion o no es un numero valido")

def prom_voltaje(data):
    valores = []
    for e in data:
        acu= 0
        cant = len(e['bateria'])
        for valor in e['bateria']:
            acu += valor
        prom = acu/cant
        valores.append({'nombre':e['nombre'],'promedio': prom})    
    valores.sort(key = lambda valores: valores['promedio'])
    estacion = valores[0]
    print('La estacion con menos voltaje promedio es: {}, con un promedio de {}'.format(estacion['nombre'], estacion['promedio']))    



def menu():
    #expreciones_regulares()
    #num = 46579222    
    #print(cambiar_numero(str(num)))
    #print(cambiar_numero2(num))
    #l =  [ [1, 2, 3], [4, 5, 6], [7], [8] ]
    #print(cambiar_lista(l))
    """ l1 = [1,2,3,4]
    l2 = [1,2,3,4]
    print(compara_list(l1,l2))
    print(compara_list([],[])) """
    #print(divicion_ent(0,3))
    #print(calcular_pi(2))
    #json2 = open("estacion.json", "rt")

    #data = json.loads(json2.read())
    #mostrar_estacion(data)
    #prom_voltaje(data)
    print("Trabajo Integrador Valentin Tarayre")
    checkTema=True
    opciones = ("Expreciones Regulares","Recurcion","Colecciones","Formato de Intercambio de Datos")
    while(checkTema):
        try:
            print("Menu Opciones Tema: \n1 %s \n2 %s \n3 %s \n4 %s" %opciones)
            selecTema = int(input("Ingrese Numero de Opcion: "))
            if selecTema in [1,2,3,4]:
                checkTema= False
            else:
                print("Vuelva a ingresar la Opcion")
        except Exception:
            print("Error")
    print("\n\n")
    if selecTema is 1:
        print("%s" %opciones[0])
        print("   1- Matriculas\n   2- Menores a 1900")
        selecOpcion = int(input("Ingrese el numero: "))
        if selecOpcion in [1,2]:
            if selecOpcion is 1:
                print('^(L(V|Q)-[A-Z]{3})|(LV-(S|X|SX)\d{3})$')
            elif selecOpcion is 2:
                print('^((\d{1,3})|(1[0-8]\d\d))$')
        else:
            print("Error no existe Opcion")
            return 0


    


if __name__ == "__main__":
    menu()
else:
    print("run from import")