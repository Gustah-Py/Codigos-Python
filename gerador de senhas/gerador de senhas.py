import random

senha = ""

caracteres = "iefyug2w3qyguedguygfc"

for digito in range(3):
    aleatorio = random.choice(caracteres)
    senha += aleatorio
    
    print("-" * 20)
    print(senha)
    print("-" * 20)   