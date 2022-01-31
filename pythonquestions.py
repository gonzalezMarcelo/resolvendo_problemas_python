# Estarei resolvendo algumas problemas de raciocinio lógico com o python. O objetivo aqui é inteiramente treinar meu raciocinio e a minha capacidade de transformar meu pensando em código. Já declaro de antemão que as minhas soluções não são as únicas possíveis, essa foi a minha maneira de fazer, caso queira compartilhar a sua, me chame no linkedin, será um prazer aprender contigo: https://www.linkedin.com/in/marcelolealgonzalez/

#Os problemas estão em espanhol mesmo 

import random

#  1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def maior_numero(num1, num2):
    if (num1 > num2):
        return num1
    else:
        return num2

print(maior_numero(10, 11))


# 2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    elif (num2 > num1 and num2 > num3):
        return num2
    else:
        return num3

print(max_de_tres(1, 100, 3))


#ou

def max_de_tres2(num1, num2, num3):
    a = maior_numero(num1, num2)
    b = maior_numero(num3, a)
    return b

print(max_de_tres2(100, 20,400))



# 3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def tamanho_lista(lista):
    tamanho = 0
    for elem in lista:
        tamanho += 1 
    return tamanho

lista_teste = [0, 5, 6, 6, 7, 7, 5, 4, 3, 2, 7, 5,3,5]

print(tamanho_lista(lista_teste))

#testando resposta
print(len(lista_teste))




# 4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def eh_vogal(elem):
    lista_vogal = ["a", "e", "i", "o", "u"]
    if elem in lista_vogal:
        return True
    else:
        return False

print(eh_vogal("u"))




# 5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def somando_numeros(lista):
    resultado = 0
    for elem in lista:
        resultado += elem
    return resultado

print("Essa é a função somatória")
print(somando_numeros(lista_teste))
print(sum(lista_teste))



def multiplicado_numeros(lista):
    resultado = lista[0]
    x = 1
    while x in range(1, len(lista)):
        resultado = resultado * lista[x]
        x += 1
        print(resultado)
        

print("Multiplicando")
multiplicado_numeros([9, 2, 1])

# 6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def funcao_inversa(frase):
    tamanho_lista = -(len(frase) - 1)
    nova_frase = str()
    for elem in range(tamanho_lista,1):
        elem = abs(elem)
        nova_frase += frase[elem]
    print(nova_frase)

funcao_inversa('eu sou um gostosao')
