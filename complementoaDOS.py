def binarizar(decimal):
    binario = ''
    N=decimal
    while decimal//2!=0:
        a=decimal % 2
        binario = str(a) + binario
        q = decimal // 2
        decimal=q
    return str(decimal) + binario

def complemento(numero,longitud):
    if numero<0:
        conv=2**longitud+numero
        result=binarizar(conv)
        print(result)
    else:
        result = binarizar(numero)
        print(result)



complemento(-15,8)



