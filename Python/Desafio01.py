mensagem = "A"

d1 = "#B"
d2 = "%s"
d3 = "9g"

remetente = d1
destinatario = d2

dispositivo_recebendo = d2

def aplicacao(info):
    return "[APLICAÇÃO] " + info

def apresentacao(info):
    return "[APRESENTAÇÃO] " + info

def sessao(info):
    return "[SESSÃO] " + info

def transporte(info):
    return "[TRANSPORTE] " + info

def rede(info, remetente, destinatario):
    return f"[REDE {remetente}->{destinatario}] " + info

def enlace(info):
    return "[ENLACE DE DADOS] " + info

def fisica(info):
    return "[FÍSICA] " + info

def binario(texto):
    binario = ""

    for char in texto:
        binario += format(ord(char), "08b")

    return binario

def unfisica(info):
    return info.replace("[FÍSICA] ", "")

def unenlace(info):
    return info.replace("[ENLACE DE DADOS] ", "")

def unrede(info, remetente, destinatario):
    return info.replace(f"[REDE {remetente}->{destinatario}] ", "")

def untransporte(info):
    return info.replace("[TRANSPORTE] ", "")

def unsessao(info):
    return info.replace("[SESSÃO] ", "")

def unapresentacao(info):
    return info.replace("[APRESENTAÇÃO] ", "")

def unaplicacao(info):
    return info.replace("[APLICAÇÃO] ", "")

def texto(binario):
    texto = ""

    for i in range(0, len(binario), 8):
        texto += chr(int(binario[i:i+8], 2))

    return texto

print(mensagem)

dado = aplicacao(mensagem)
print(dado)

dado = apresentacao(dado)
print(dado)

dado = sessao(dado)
print(dado)

dado = transporte(dado)
print(dado)

dado = rede(dado, remetente, destinatario)
print(dado)

dado = enlace(dado)
print(dado)

dado = fisica(dado)
print(dado)

print()

dado = binario(dado)
print(dado)

print()

if dispositivo_recebendo == destinatario:
    dado = texto(dado)
    print(dado)

    dado = unfisica(dado)
    print(dado)

    dado = unenlace(dado)
    print(dado)

    dado = unrede(dado, remetente, destinatario)
    print(dado)

    dado = untransporte(dado)
    print(dado)

    dado = unsessao(dado)
    print(dado)

    dado = unapresentacao(dado)
    print(dado)

    dado = unaplicacao(dado)
    print(dado)
else:
    print("Destinatário incorreto.")