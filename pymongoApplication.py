import datetime
import pymongo 
from pymongo import MongoClient

mongodb_url = "mongodb+srv://danielmarcosvilelarpa:B%40nana23@cluster0.r0wtpbk.mongodb.net/"

client = pymongo.MongoClient(mongodb_url)


# criar banco de dados
database_name = "Aplicacao"
db = client[database_name]

# coleção
collection_name = "bank"
bank_collection = db[collection_name]

# insert

cliente = {"nome": "Daniel Vilela", "cpf": 999999999, "endereco": "Rua João Perone"}
Conta = {"tipo": "poupança", "agencia":"0001-23", "num": 543-398}

result1 = bank_collection.insert_one(cliente)
result2 = bank_collection.insert_one(Conta)

if result1.inserted_id:
    print("Dados do clientes adicionados com sucesso.")
else:
    print("Falha ao adicionar dados do clientes.")

if result2.inserted_id:
    print("Dados da conta do clientes adicionados com sucesso.")
else:
    print("Falha ao adicionar dados da conta do clientes.") 


# find

result1 = bank_collection.find()
for document in result1:
    print(document)

    
client.close()