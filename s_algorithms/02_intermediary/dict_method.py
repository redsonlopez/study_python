##
# Metodos de dicionários
##

contatos= {
        "redsonlopez@gmail.com": {"nome": "Hedson", "telefone": "(31)98704-3337"},
        "line_charada@hotmart.com": {"nome": "Aline", "telefone": "(11)98504-9996"},
}
print(contatos["redsonlopez@gmail.com"]) # {'nome': 'Hedson', 'telefone': '(31)98704-3337'}
print()

copia= contatos.copy()
copia["redsonlopez@gmail.com"]= {"nome": "Red"}
print(copia["redsonlopez@gmail.com"]) # {'nome': 'Red'}
print()

usuarios= contatos.copy()
contatos.clear()
print(contatos) # {}
print()

chaves_1= dict.fromkeys(["nome", "telefone"])
chaves_2= dict.fromkeys(["nome", "telefone"], "vazio")
print(chaves_1) # {'nome': None, 'telefone': None}
print(chaves_2) # {'nome': 'vazio', 'telefone': 'vazio'}
print()

# print(contatos["chave"]) # KeyError
print(copia.get("chave")) # None
print(copia.get("chave", {})) # {}
print(copia.get("chave", {"vazio"})) # {'vazio'}
print(copia.get("redsonlopez@gmail.com", {})) # {'nome': 'Red'}
print(copia.get("line_charada@hotmart.com")) # {'nome': 'Aline', 'telefone': '(11)98504-9996'}
print()

print(copia.items()) # dict_items([('redsonlopez@gmail.com', {'nome': 'Red'}), ('line_charada@hotmart.com', {'nome': 'Aline', 'telefone': '(11)98504-9996'})])
print()

print(copia.pop("redsonlopez@gmail.com")) # {'nome': 'Red'}
print(copia.pop("redsonlopez@gmail.com", {})) # {}
print()

print(usuarios.popitem()) # ('line_charada@hotmart.com', {'nome': 'Aline', 'telefone': '(11)98504-9996'})
#print(usuarios.popitem()) # ('redsonlopez@gmail.com', {'nome': 'Hedson', 'telefone': '(31)98704-3337'})
# print(usuarios.popitem()) # KeyError
print()

contato= {"nome": "Hedson", "telefone": "(31)98704-3337"}
print(contato.setdefault("nome", "João")) # "Hedson"
print(contato) # {'nome': 'Hedson', 'telefone': '(31)98704-3337'}
print(contato.setdefault("idade", 28)) # 28
print(contato) # {'nome': 'Hedson', 'telefone': '(31)98704-3337', 'idade': 28}
print()

contatos.update({"redsonlopez@gmail.com": {"nome": "Red"}})
contatos.update({"line_charada@hotmart.com": {"nome": "Aline", "telefone": "(11)98504-9996"}})
print(contatos)
print()

print(contatos.values())
print()

print("redsonlopez@gmail.com" in contatos)
print("charlotte@yahoo.com" in contatos)
print("idade" in contatos["redsonlopez@gmail.com"])
print("telefone" in contatos["line_charada@hotmart.com"])
print()

del contatos["redsonlopez@gmail.com"]["nome"]
del contatos["line_charada@hotmart.com"]
print(contatos)

