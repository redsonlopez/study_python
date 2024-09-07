from collections import deque

# usa deque para criar uma fila
fila = deque(["abacate", "bola", "cachorro"])
print(fila)  # deque(['abacate', 'bola', 'cachorro'])

# adicionando um novo elemento
fila.append("dado") 
print(fila)  # deque(['abacate', 'bola', 'cachorro', 'dado'])

# Remove o primeiro elemento adicionado à fila.
fila.popleft()
print(fila)  # deque(['bola', 'cachorro', 'dado'])

