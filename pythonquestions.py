# Estarei resolvendo algumas problemas de raciocinio lógico com o python. O objetivo aqui é inteiramente treinar meu raciocinio e a minha capacidade de transformar meu pensando em código. Já declaro de antemão que as minhas soluções não são as únicas possíveis, essa foi a minha maneira de fazer, caso queira compartilhar a sua, me chame no linkedin, será um prazer aprender contigo: https://www.linkedin.com/in/marcelolealgonzalez/

#Os problemas estão em espanhol e inglês 

#from msilib.schema import Error
import random
from tkinter import N

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
    return nova_frase

funcao_inversa('eu sou um gostosao')


# 7 - Define a function is_palindrome() that recognizes palindromes (that is, words that have the same appearance written inverted), example: is_palindrome ("radar") would have to return True.

def is_palindrome(sentence):
    palindromo = funcao_inversa(sentence)
    if palindromo == sentence: 
        return True
    else:
        return False

print(is_palindrome('aea'))



# 8 - Define a function overlay() that takes two lists and returns True if they have at least 1 member in common or returns False otherwise. Write the function using the nested for loop

def overlay(lista1, lista2):
    for elem in lista1:
        if elem in lista2:
            return True
    return False

#ou

def overlay2(lista1, lista2):
    for elem1 in lista1:
        for elem2 in lista2:
            if elem1 == elem2:
                return True
    return False

print("Listas com elementos em comum")
print(overlay([1,3,5,7,9,0],[2,6,6,8,8,0]))
print(overlay2([1,3,5,7,9,0],[2,6,6,8,8]))


# 9 - Define a function generate_n_characters() that takes an integer n and returns the character multiplied by n. For example: generate_n_characters(5, "x") should return "xxxxx".

def generate_n_characters(character, num):
    if (int(num)):
        return character*num

print(generate_n_characters("ma", 4))

#ou

def generate_n_characters2(character, num):
    string = ""
    for x in range(0, num):
        string += character
    return string

print(generate_n_characters2("fiu", 11))



# 10 - Define a histogram procedure() that takes a list of integers and prints a histogram to the screen. Example: procedure([4, 9, 7]) should print the following:

def procedure(lista):
    for elem in lista:
        print(elem*"*")

procedure([4, 3, 2])


#ou, se quiser com espaco entre as "barras"


def procedure2(lista):
    for elem in lista:
        histogram = elem*"*"
        print(f"{histogram}\n")

procedure2([4, 3, 2])