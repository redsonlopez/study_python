vogais_1 = {'aeiou'} # sem uso do construtor
print("v_1", type(vogais_1), vogais_1)
vogais_2 = set('aeiouaaaaaa') # construtor com string
print("v_2", type(vogais_2), vogais_2)
vogais_3 = set(['a', 'e', 'i', 'o', 'u']) # construtor com lista
print("v_3", type(vogais_3), vogais_3)
vogais_4 = set(('a', 'e', 'i', 'o', 'u')) # construtor com tupla
print("v_4", type(vogais_4), vogais_4)

print(set('banana'))

