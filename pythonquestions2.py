#Essa é a continuação da saga dos problemas sendo resolvido com python. Caso não esteja ciente, estou resolvendo problemas lógicos com python, a fim de me desenvolver mais na linguagem e testar minha capacidade de transformar pensando em código. Estas soluções não são as únicas possíveis, mas eu fiz assim. 

#OBS: Os problemas estão em inglês

# 1 - The max() function from exercise 1 (first part) and the max_of_three() function from exercise 2 (first part), will only work for 2 or 3 numbers. Suppose we have more than 3 numbers or we don't know how many numbers there are. Write a max_in_list() function that takes a list of numbers and returns the largest.

from itertools import count


def max_in_list2(lista):
    inicio = 0
    for elem in lista:
        if elem > inicio:
            inicio = elem
    
    return inicio

print(max_in_list2([9,5,6,7,4,2,7,8,12]))




# 2 - Write a longest() function that takes a list of words and returns the longest.

def longest(lista):
    maior_atual = ""
    for word in lista:
        if len(word) > len(maior_atual):
            maior_atual = word
    
    return maior_atual

print(longest(["coco", "xixi", "jumento", "carlos", "marcelo"]))



# 3 - Write a function filter_words() that takes a list of words and an integer n, and returns words that have more than n characters.

def filter_words(lista, n):
    palavras_maior_q_n = []
    for elem in lista:
        if len(elem) > n:
            palavras_maior_q_n.append(elem)
    
    return palavras_maior_q_n

print(filter_words(["coco", "xixi", "jumento", "carlos", "marcelo"], 6))



# 4 - Write a program that tells the user to enter a string. The program has to evaluate the string and say how many uppercase letters it has.

def uppercase_count(string):
    count = 0
    for x in string:
        if x.isupper():
            count += 1

    return count

print(uppercase_count("eUnAoSEioooooooooI"))
