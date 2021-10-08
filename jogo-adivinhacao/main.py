from operator import le
import random

def init():
    dict_levels = {1:20, 2:10, 3:5} 
    painel = '''
    ************************************
    * Bem-Vindo ao jogo de Adivinhação *
    ************************************
    '''
    choices = '''
    Escolha um nível de dificuldade: 
    1) Fácil
    2) Médio
    3) Difícil
    '''
    congratulations = "Parabéns vc venceu! 🥳"
    print(painel)
    level = int(input(choices))
    
    while level not in [1,2,3]:
        print("Opção inválida, escolha novamente")
        level = int(input(choices))
    
    number = random.randint(0,100)
    game_continue = True
    chances = 0
    while game_continue:
        chances+=1
        if dict_levels[level] == chances:
            print("Vc perdeu!")
            game_continue=False
        number_choice = int(input("Escolha um número entre 0 e 100\n"))
        if number_choice == number:
            game_continue=False
            print(congratulations)
        else:
            
            if number_choice < number:
                print("O número escolhido é menor")
            else:
                print("O número escolhido é maior")

if __name__=='__main__':
    init()