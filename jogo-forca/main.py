from operator import index, le
from random import choice, randint
def init():
    words = []
    f = open('fuits.txt')
    for line in f:
        words.append(line.replace('\n',''))
    
    word = list(words[randint(0,len(words))])
    game_continue = True
    chances = 0
    painel = list(len(word)*'_')
    while game_continue:
        if chances==5:
            game_continue = False
        letter = input("Escolha uma letra:")
        print("Chances",1,'/',5)
        print("Forca:", painel )
        if letter in word:
            index = 0
            for lett in word:
                if lett == letter:
                    painel[index] = letter
                index+=1
        chances+=1
        print(painel)
if __name__=="__main__":
    init()