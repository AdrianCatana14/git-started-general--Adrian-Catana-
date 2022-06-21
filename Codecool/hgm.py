import random
import sys
from ascii_hangman import HANGMANPICS

print(""" 
 _                Welcome to                                    
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                    __/ |                      
                   |___/       """)
print("\n")

name = input("What's your name? ")
print("\n")
print(f"Hello {name}, let's play!")
print("\n")

print("1. Easy 2. Medium 3. Hard 4. Quit")
difficulty = input("Select your difficulty")
lives = 7
if difficulty == '1':
    lives = 7



# 1. fac rost de un cuvant pe care sa il ghicesc
# aflu numarul total de linii din fisierul meu
# generez un numar aleatoriu intre 0 si numarul maxim de linii
# citesc din fisier linia aleasa
random_word_number = 4
#citesc din fisier linia continuta in valoarea random_word_number
word_to_guess = ()
already_tried_letters = []
# 2. afisez cu "_" fiecare litera neghicita
# parcurg litera cu litera cuvantul aflat in variabila word_to_guess


# 3. cerem o litera pentru a fi ghicita
tried_letter = input("Introduceti o litera")
already_tried_letters.append(tried_letter)
# 4. daca am nimerit litera sa se afle in cuvantul  nostru atunci inlocuim acel _ cu litera respectiva
if tried_letter in word_to_guess:
    #parcurg fiecare litera din variabila  word_to_guess
    #atunci litera pe care o parcurg face parte din already_tried_letters afisez acea litera, altfel afisez "_"
# 4.0 Daca nu am nimerit litera scade nr vieti si afiseaza hangman
if tried_letter not in word_to_guess:
    lives -= 1 # lives = lives - 1
    

# 4.1 daca aceasta litera este deja inclusa in lista de litere incercate atunci repetam pasul 3
if tried_letter in already_tried_letters:
    print("You already tried this letter")
    print(already_tried_letters)
# 4.2 daca ce am introdus nu este o litere si in schimb este cuvantul quit termin fortat programul 
if tried_letter == "quit":
    #break
# 5. daca nu am nimerit litera scade nr de vieti si afiseaza printr o spanzuratoare si afisam o lista cu literele gresite 

# 6. repetam pasii 2-4 pana am ghicit cuvantul sau am terminat jocul
