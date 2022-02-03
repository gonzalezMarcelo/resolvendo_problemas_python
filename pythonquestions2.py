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




# 5 - Build a small program that converts binary numbers to integers.

def converts_binary_to_integer(sequencia):
    sequencia = str(sequencia)
    decimal = 0
    exp = len(sequencia) - 1
    for numero in sequencia:
        decimal = decimal + (int(numero)*2**(exp))
        exp -= 1
    
    return decimal


print(converts_binary_to_integer(1000))



# 6 - Write a small program where:
# - The current year is entered.
# - Enter the name and year of birth of three people.
# - It is calculated how old they will be during the current year.
# - It is printed on the screen.

# def calculando_idade():
#     current_year = input("Ponha o ano de seu desejo: ")
#     for i in range(3):
#         name = input("Insira o nome: ")
#         ano_de_nascimento = input("Insira o ano de nascimento: ")
#         idade = int(current_year) - int(ano_de_nascimento)

#         print(f"O {name} estará com {idade} anos") 
                

# calculando_idade()


# 7 - Define a tuple with 10 ages of people.
# Print the number of people aged over 20.
# You can vary the exercise so that it is the user who enters the ages.

def aged_over_twenty(lista):
    count = 0
    for elem in lista:
        if elem > 20:
            count += 1 
        
    return count

print(aged_over_twenty([20, 30, 40, 50, 60, 70, 80, 10, 14, 15, 16]))





# 8 - Define a list with a set of names, print the number of names beginning with the letter a. You can also make the user choose the letter to search for. (a little more exciting)

def name_start(lista, letra):
    count = 0
    for elem in lista:
        elem = elem.lower()
        if elem[0] == letra:
            count += 1 
    
    return count

print(name_start(["marcelo", "ana", "carlos", "joao", "jose", "alberto", "alice"], "a"))



# 9 - Create a function count_vowels(), which receives a word and counts how many letters "a" it has, how many letters "e" it has and so on until all the vowels are completed.
# The user can be made to choose the word.

def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letra in word:
        if letra in vowels:
            count += 1

    return count

print(count_vowels("paralelepipedo"))


# jeito certo

def count_vowels2(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    dictionary = {}
    for letra in word:
       if letra in vowels:
           if letra not in dictionary:
               dictionary[letra] = 1
           else:
                dictionary[letra] += 1
    
    return dictionary

print(count_vowels2("paralelepipedo"))

print(count_vowels2("jurema"))
