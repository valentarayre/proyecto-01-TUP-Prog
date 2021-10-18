import re

#   Primer Eje

# La exprecion regular que encontre fue
# /^(L(V|Q)-[A-Z]{3})|(LV-(S|X|SX)\d{3})/

test = ["LV-QWE","LQ-ABE","LV-X443","LV-S586","LV-SX334","LA-123","LX-ABC","LV","LV-344"]
exp = r'/^(L(V|Q)-[A-Z]{3})|(LV-(S|X|SX)\d{3})/'

exp = re.compile(r'^(L(V|Q)-[A-Z]{3})|(LV-(S|X|SX)\d{3})')

for e in test:    
    if exp.search(e) is not None:
        print("Es Correcta la Matricula:", e)
    else:
        print("No es Correcta la Matricula:", e)