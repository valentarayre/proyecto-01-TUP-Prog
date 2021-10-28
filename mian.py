import re 

#   Primer Eje

# La exprecion regular que encontre fue
# /^(L(V|Q)-[A-Z]{3})|(LV-(S|X|SX)\d{3})/
# ^((\d{1,3})|(1[0-8]\d\d))$


def expreciones_regulares():
    test = ["LV-QWE","LQ-ABE","LV-X443","LV-S586","LV-SX334","LA-123","LX-ABC","LV","LV-344"]
    exp = r'/^(L(V|Q)-[A-Z]{3})|(LV-(S|X|SX)\d{3})/'

    exp = re.compile(r'^(L(V|Q)-[A-Z]{3})|(LV-(S|X|SX)\d{3})')

    for e in test:    
        if exp.search(e) is not None:
            print("Es Correcta la Matricula:", e)
        else:
            print("No es Correcta la Matricula:", e) 

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
 
def main():
    #expreciones_regulares()
    #num = 46579222    
    #print(cambiar_numero(str(num)))
    #print(cambiar_numero2(num))
    #l =  [ [1, 2, 3], [4, 5, 6], [7], [8] ]
    #print(cambiar_lista(l))
    l1 = [1,2,3,4]
    l2 = [1,2,3,4]
    print(compara_list(l1,l2))
    print(compara_list([],[]))
    


if __name__ == "__main__":
    main()
else:
    print("run from import")