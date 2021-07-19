# listas
animais = [1, 2, 3]
print(animais)

animais = ['Cachorro', 'Gato', 12345, 6.5]
print(animais)

print(animais[0])

print(animais[3])

animais[0] = 'Papagaio'
print(animais)

animais.remove('Gato')
print(animais)

print(len(animais))
print(animais)

print('Gato' in animais)

print('Gato' not in animais)

lista = [500, 30, 300, 80, 10]

print(max(lista))
print(min(lista))

animais.append('Leão')
print(animais)

animais.extend(['Cobra', 'Cachorro'])
print(animais)

print(animais.count('Cachorro'))

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)


# tuplas
tp = ('Banana', 'Maça', 10, 50)

print(tp[0])

print(tp.count('Maça'))

print(tp[0:2])


# dicionarios
dc = {'Maça': 10, 'Laranja': 15, 'Maça': 20, 'Uva': 5}

print(dc['Maça'])

dc['Maça'] = 25

chaves = dc.keys()
print(chaves)

valores = dc.values()
print(valores)

dc.setdefault('Limão', 22)
print(dc)

dc.setdefault('Laranja', 20)
print(dc)

