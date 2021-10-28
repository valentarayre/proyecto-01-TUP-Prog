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

def main():
    #expreciones_regulares()
    num = 46579222
    
    #print(cambiar_numero(str(num)))
    print(cambiar_numero2(num))


if __name__ == "__main__":
    main()
else:
    print("run from import")