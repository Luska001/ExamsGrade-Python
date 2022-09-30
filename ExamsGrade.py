def addupList(myList):

    # função para somar todos as notas guardadas dentro do array.
    result = 0
    # variável result recebe valor inicial 0.
    for x in myList:
    # 'para cada x (elemento) dentro do parâmetro mylist (que será uma variável do programa).
        result = result + x
        # result recebe seu valor mais o elemento do array, como temos mais de um valor dentro do array usamos um loop, assim quando o primeiro elemento for somado ao result, ele passará para o próximo elemento, já que o anterior 'sumiu' do array, porque foi inserido na variável result.
    return result
    #ao final do loop, a função addupList irá retornar o valor da variável result.

count = 0
# contador que serve como parâmetro para a quantidade de notas.
conjunto_notas = []
# array responsável por armazenar as notas digitadas (Não possui tamanho pré-definido '[]', pois seu tamanho será dado pela quantidade de notas que o usuário digitará).

qt_notas = int(input('Quantas notas deseja inserir? '))
while qt_notas <= 1:
# se o usuário tentar digitar uma quantidade de notas iguais ou menores que 1, será feito um loop até que a quantidade seja aceitável, pois não se pode inserir uma quantidade de 0 ou menos notas, e também não se faz média de 1 nota.
    qt_notas = int(input('Quantidade de notas inválidas, Insira novamente: '))

while count < qt_notas:
# enquanto o valor da variável cont for menor ou igual a variável qt_notas o programa segue normalmente.
    notas = int(input('Digite a {}º nota: '.format(count+1)))
    conjunto_notas.append(notas)
    # a nota digitada pelo usuário é inserida dentro do array conjunto_notas.
    count += 1
    # a variável count recebe +1 ao seu valor atual, para que acompanhe a quantidade de notas que o usuário quer informar, assim, quando chegar ao número x de notas pedidas pelo usuário (guardada na variável qt-notas), o loop termina.

    while notas > 10:
        print('Nota inválida!')
        conjunto_notas.pop()
        # caso a nota que o usuário digitar seja maior que 10, o programa diz ser inválida e remove o número do array com a função .pop().
        count -= 1
        # a variável count perde -1 de seu valor atual, passando para o programa que aquela nota inválida foi excluída com o pop(), assim não contando como uma nota válida e não entrando para a contagem de notas inseridas.
        break
        # break quebra este while para não gerar um loop infinito, voltando para o while de cima, que irá pedir a nota novamente. 

conjunto = addupList(conjunto_notas)
# função addupList usa como parâmetro para seu funcionamento o array conjunto_notas.
# variável 'conjunto' recebe o valor da função adduppList, que somou os números do array, resultando na soma de todas as notas válidas digitas pelo usuário.
media = conjunto / qt_notas
# variável 'media' rececbe o valor da divisão entre as variáveis 'conjunto' e 'qt_notas'.

print('A média do aluno foi de {}'.format(media))
# mostra na tela a média do aluno calculada acima.