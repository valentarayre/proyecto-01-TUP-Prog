import json

""" def cambiar_numero_string(num):
	if len(num) == 0:
		return num
	else:
		if int(num[-1]) % 2 == 0:
			return cambiar_numero_string(num[:-1]) + "1"
		else:
			return cambiar_numero_string(num[:-1]) + "2" """
def cambiar_numero(num):
	#Devuelve el numero cuando se haya cambiado al completo
	if num == 0:
		return num
	else:
		#si el numero es par se agrega 1 o sino 2
		#Modulo de 10 devuelve el ultimo numero y ese numero comprobamos si es par o no
		if (num % 10) % 2 == 0:            
			return cambiar_numero(num // 10) * 10 + 1
		else:
			return cambiar_numero(num // 10) * 10 + 2

def cambiar_lista(lista):
	#devuelve la lista vacia
	if len(lista) <= 0:
		return lista
	else:
		#llama a la funcion devolviendo la lista menos el ultimo elemento y se agrega a la cola el ultimo momento
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
	#Se le resta el divisor y se le suma 1, contanto las veces que se dividio
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
	print("Trabajo Integrador Valentin Tarayre")
	checkTema=True
	opciones = ("Expreciones Regulares","Recurcion","Colecciones","Formato de Intercambio de Datos")
	try:
		while(checkTema):            
			print("Menu Opciones Tema: \n1 %s \n2 %s \n3 %s \n4 %s" %opciones)
			selecTema = int(input("Ingrese Numero de Opcion: "))
			if selecTema in [1,2,3,4]:
				checkTema= False
			else:
				print("Vuelva a ingresar la Opcion")
		
		if selecTema == 1:
			print("%s" %opciones[0])
			print("   1- Matriculas\n   2- Menores a 1900")
			selecOpcion = int(input("Ingrese el numero: "))
			if selecOpcion in [1,2]:
				if selecOpcion == 1:
					print('^(L(V|Q)-[A-Z]{3})|(LV-(S|X|SX)\d{3})$')
				elif selecOpcion == 2:
					print('^((\d{1,3})|(1[0-8]\d\d))$')
			else:
				print("Error no existe Opcion")
				return 0
		elif selecTema == 2:
			print("%s" %opciones[1])
			print("        1- Cambio de numeros\n	2- Convertir listas en lista\n	3- Dos Lista Iguales\n	4- Divicion de numeros")
			selecOpcion = int(input("Ingrese el numero: "))
			print('\n')
			if selecOpcion in [1,2,3,4]:
				if selecOpcion == 1:
					num = input("Ingrese numero a probar: ")
					print("El numero {} se transformo en {}".format(num,cambiar_numero(num)))
				elif selecOpcion == 2:
					l =  [ [1, 2, 3], [4, 5, 6], [7], [8] ]
					print("La lista {} se transforma a {}".format(l, cambiar_lista(l)))
				elif selecOpcion == 3:
					l1 = [1,2,3,4]
					l2 = [1,2,3,4]
					print(compara_list(l1,l2))
				elif selecOpcion == 4:                    
					a = int(input("Primer Numero: "))
					b = int(input("Divisor Numero: "))                    
					if b > 0:
						print("{} / {} = {}".format(a,b,divicion_ent(a,b)))
					else:
						print("Ingrese un divisor mayor a 0")
			else:
				print("Error no existe Opcion")
				return 0
		elif selecTema == 3:			
			n_pi = int(input("Ingrese el numero: "))
			print("Con n {} Veces, resulto el numero: {}".format(n_pi,calcular_pi(n_pi)))			
		elif selecTema == 4:
			print("%s" %opciones[1])
			print("        1- Mostrar estaciones\n	2- Estacion menor bateria")
			selecOpcion = int(input("Ingrese el numero: "))
			
			if selecOpcion in [1,2]:
				with open('estacion.json', 'rt') as file:
					data = json.loads(file.read())
					if selecOpcion == 1:
						mostrar_estacion(data)
					elif selecOpcion == 2:
						prom_voltaje(data)
			else:
				print("Error no existe Opcion")
				return 0

	except ValueError:
			print("Error Solamente se acepta numeros")

	


if __name__ == "__main__":
	menu()
else:
	print("run from import")