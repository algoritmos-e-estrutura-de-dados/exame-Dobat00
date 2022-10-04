def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    figurinhas_trocaveis_maria = 0
    figurinhas_trocaveis_joao = 0
    figurinhas_trocaveis_total = 0
    figurinhas_diferentes_maria = 0
    figurinhas_diferentes_joao = 0
    quantidade_figurinhas_maria =0
    quantidade_figurinhas_joao = 0
    aux = 0

    
    for x in figurinhas_da_maria:
        quantidade_figurinhas_maria = quantidade_figurinhas_maria + 1
        for y in figurinhas_da_maria:
            if (x == y):
                figurinhas_trocaveis_maria = figurinhas_trocaveis_maria + 1
            else:
                figurinhas_diferentes_maria = figurinhas_diferentes_maria + 1

    figurinhas_trocaveis_maria = int(figurinhas_trocaveis_maria) - int(quantidade_figurinhas_maria)
    figurinhas_trocaveis_maria = figurinhas_trocaveis_maria/2
    figurinhas_diferentes_maria = figurinhas_diferentes_maria/2

    
    for x in figurinhas_do_joao:
        quantidade_figurinhas_joao = quantidade_figurinhas_joao + 1
        for y in figurinhas_do_joao:
            if (x == y):
                figurinhas_trocaveis_joao = figurinhas_trocaveis_joao + 1
            else:
                figurinhas_diferentes_joao = figurinhas_diferentes_joao + 1

    figurinhas_trocaveis_joao = int(figurinhas_trocaveis_joao) - int(quantidade_figurinhas_joao)
    figurinhas_trocaveis_joao = figurinhas_trocaveis_joao/2          
    figurinhas_diferentes_joao = figurinhas_diferentes_joao/2

    
    if (len(figurinhas_da_maria)> len(figurinhas_do_joao)):
        if (figurinhas_diferentes_maria == A):
            figurinhas_trocaveis_maria = A

    elif (len(figurinhas_da_maria)< len(figurinhas_do_joao)):
        if(figurinhas_diferentes_joao == B):
            figurinhas_trocaveis_joao = B

    
            
        

    figurinhas_trocaveis_total = figurinhas_trocaveis_maria+figurinhas_trocaveis_joao
    print(int(figurinhas_trocaveis_total))
    return figurinhas_trocaveis_total



if __name__ == '__main__':
    A, B = input("Digite o numero total de figurinhas que Maria e Joao possuem (os numeros devem ser separados por um espaco em branco)\n").split(' ')

    figurinhas_da_maria = input("Quais sao as figurinhas de Maria?(separados por um espaco em branco)\n ").split(' ')
    
    figurinhas_do_joao = input("Quais sao as figurinhas e Joao?(separados por um espaco em branco)\n").split(' ')
    
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao)
