def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    figurinhas_repetidas_maria= 0
    figurinhas_repetidas_joao = 0
    figurinhas_diferentes_maria = 0
    figurinhas_diferentes_joao =0
    figurinhas_trocaveis_total = 0
    
    
    for i in figurinhas_da_maria:
        for j in figurinhas_da_maria:
            if (i == j):
                figurinhas_repetidas_maria = figurinhas_repetidas_maria+ 1
            else:
                figurinhas_diferentes_maria = figurinhas_diferentes_maria + 1
    figurinhas_repetidas_maria = figurinhas_repetidas_maria - len(figurinhas_da_maria)
    
    
    for i in figurinhas_do_joao:
        for j in figurinhas_do_joao:
            if (i==j):
                figurinhas_repetidas_joao = figurinhas_repetidas_joao+1
            else:
                figurinhas_diferentes_joao = figurinhas_diferentes_joao + 1
    figurinhas_repetidas_joao = figurinhas_repetidas_joao - len(figurinhas_do_joao)
    
    
    
    figurinhas_trocaveis_total = figurinhas_repetidas_joao + figurinhas_repetidas_maria
    if (figurinhas_diferentes_maria == 2*len(figurinhas_da_maria)):
        figurinhas_trocaveis_total = len(figurinhas_da_maria)
    print(int(figurinhas_trocaveis_total))
    return figurinhas_trocaveis_total       




if __name__ == '__main__':
    A, B = input("Digite o numero total de figurinhas que Maria e Joao possuem (os numeros devem ser separados por um espaco em branco)\n").split(' ')

    figurinhas_da_maria = input("Quais sao as figurinhas de Maria?(separados por um espaco em branco)\n ").split(' ')
    
    figurinhas_do_joao = input("Quais sao as figurinhas e Joao?(separados por um espaco em branco)\n").split(' ')
    
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao)
