import random

def init():
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
    print(painel)
    level = int(input(choices))
    while level not in [1,2,3]:
        print("Opção inválida, escolha novamente")
        level = int(input(choices))
        
    
if __name__=='__main__':
    init()