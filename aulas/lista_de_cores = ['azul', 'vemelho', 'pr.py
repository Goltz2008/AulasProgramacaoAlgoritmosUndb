cores = ["azul", "vemelho", "preto","macaco", 14 , 33, 88.67]
frutas = ["maca", "banana", "cacau", "acerola", "caju", "pitaya", "melancia"]



print("------------------------")

print(cores)
print("Primeiro", cores[0])
print("Ultimo", cores[-1])

print("------------------------")

coresNome = cores[1:4]
print(coresNome)

print("------------------------")

numerosLista = cores[4:7:1]
print(numerosLista)

print("------------------------")

meioLista = cores[2:5:1]
print(meioLista)

print("------------------------")

itensSep = cores[1:6:2]
print(itensSep)

print("------------------------")

invertList = cores[::-1]
print(invertList)

frutas.append("Kiwi")
print(frutas)
