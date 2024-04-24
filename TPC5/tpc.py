import json 
import ply.lex as lex

with open("stock.json", "r") as jsonfile:
    data = json.load(jsonfile)["stock"]

moedas = {
    "2e": 2.00,
    "1e": 1.00,
    "50c": 0.50,
    "20c": 0.20,
    "10c": 0.10,
    "5c": 0.05,
    "2c": 0.02,
    "1c": 0.01
}
saldo = 0

def to_int(s):
    
    res = None
    if(s in moedas):
        res = moedas[s]
    else:
        print("Moeda inválida")
        res = 0
    return res

def to_str(n):

    inteiro, decimal = str("{:.2f}".format(n)).split('.')
    return f"{inteiro}e{decimal}c"

tokens = (
    'LISTAR',
    'MOEDA',
    'DINHEIRO',
    'SELECIONAR',
    'PRODUTO',
    'VIRGULA',
    'PONTO',
    'SAIR'
)

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_DINHEIRO = r'\d{1,2}[ec]'
t_SELECIONAR = r'SELECIONAR'
t_PRODUTO = r'A\d{2}'
t_VIRGULA = r','
t_PONTO = r'\.'
t_SAIR = r'SAIR'

t_ignore = ' \t'


def t_error(t):
    print("Caractere inválido: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

on = True 

while on: 

    command = input(">> ")
    lexer.input(command)
    tok = lexer.token()
    if(tok.type == "SAIR"):
        on = False
    elif(tok.type == "MOEDA"):
        for tok in lexer:
            if(tok.type == "DINHEIRO"):
                saldo += to_int(tok.value)
        print("maq: Saldo = " + to_str(saldo))
    elif(tok.type == "LISTAR"):
        print (f"{'cod':<10} | {'nome':<20} | {'quantidade':<10} | {'preço':<10}")
        print("-" * 60 + "\n")
        for item in data:
            print(f"{item['cod']:<10} | {item['nome']:<20} | {item['quant']:<10} | {item['preco']:<10.2f}")
    elif(tok.type == "SELECIONAR"):
        tok = lexer.token()
        if(tok):
            if(tok.type == "PRODUTO"):
                for item in data:
                    if(item['cod'] == tok.value):
                        if(saldo >= item['preco'] and item['quant'] > 0):
                            item["quant"] -= 1
                            troco = saldo - item['preco']
                            print(f"maq: Troco = {to_str(saldo)}")
                            saldo = 0
                        else:
                            print("maq: Saldo insuficiente ou produto indisponível")
    else:
        print("Comando inválido")


with open ("stock.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)