import time

tupla = tuple()

tupla = (1)

tupla = (1,)

tupla = 1, 2, 3

print(tupla)

print(tupla[1])

# tupla[0] = 100 #erro, pois não é possivel alterar

#manipulando dicionario
dic = {"semMundial" : "palmeiras", "1mundial" : "corinthias", "2Mundial" : "Sãopaulo"}

print(dic["semMundial"])

notas = {"mat": 5, "lp":10, "ef":8}

print(notas)
print(notas["lp"])

# print(notas["bio"])

print(dir(notas))

print(notas.values())

print(notas.keys())

print(len(notas))

for diciplina in notas.keys():
    print(diciplina)
time.sleep(3)