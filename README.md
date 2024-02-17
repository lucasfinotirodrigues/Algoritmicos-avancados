--EXERCÍCIO NÚMERO 1

CRIE UM PROGRAMA EM PYTHON QUE RESOLVA A SÉRIE DE FIBONNACCI
Serie de Fibonnacci: 0, 1, 1, 2, 3, 5, 8 ...



--EXERCÍCIO NÚMERO 2

SABE-SE QUE O NÚMERO 6 É UM NÚMERO PERFEITO, EXIBA OS OUTROS
PERFEITOS QUE EXISTEM ENTRE 1 E O NÚMERO INFORMADO PELO USUÁRIO.
Número perfeito: seus divisores naturais exceto ele somados são iguais ao
seu valor. 6 é divisível por 1, 2, 3 que somados resultam em 6.


--EXERCÍCIO NÚMERO 3

Crie um algoritmo que desenvolva o controle de uma sessão de teatro, contendo os seguintes quesitos:
O teatro deverá ter, no máximo, 40 linhas por 60 colunas (completando um total de 2400 cadeiras).
O usuário, ao iniciar o sistema deverá escolher o tamanho da sala (informando linha e coluna, respectivamente e o valor
de ingresso total.)

Deverá ser desenhado um menu, com as seguintes opções:
[1] - Iniciar o teatro: essa opção o usuário informa quantas linhas e colunas serão ocupadas, não podendo superar o total
de linhas e colunas determinadas para o tamanho do teatro e, também não poderá ser feito se outro espetáculo estiver
aberto.
[2] - Reservar lugar, informando linha e coluna. Se este lugar estiver livre, poderá ser reservado e colocado uma
informação que está reservado (para que futuramente não possa ser reservado novamente). Para reserva, deverá pagar
30% do valor total. Se estiver reservado, informar ao usuário e pedir novo conjunto de linha e coluna.


[3] - Comprar lugar. Verificar se lugar está livre, se tiver, cobrar valor cheio, se estiver reservado, cobrar valor
de 70% do valor cheio, já que para reservar, precisou pagar 30%.
[4] - Liberar lugar. Caso lugar esteja reservado ou comprado, trocar status para Livre e subtrair do sistema o
valor pago anteriormente (se reservado, subtrair 30% do valor cheio, se estiver vendido, subtrair 100% do
valor cheio).
[5] - Listar poltronas (assim o usuário poderá saber, quantos e quais locais estão livres, quais e quantos
reservados e quais e quantos vendidos).
[6] - Encerrar o espetáculo (essa opção só poderá ser utilizada se tivermos 60% + 1, da ocupação total do
teatro - posições vendidas. Neste momento, reservas não contam). Quando o espetáculo for encerrado,
deverá ser exibido o total de cadeiras vendidas (e o valor das vendas), o total de reserva (e o valor das
reservas), o total de cadeiras livres (e o valor que não foi recebido). Deverá também exibir ao final, a
totalização do espetáculo

Total Geral de Cadeiras: XXX
Total de Cadeiras Vazias: XXX
Total de Cadeiras Reservadas: XXX
Total de Cadeiras Vendidas: XXX
Total do Espetáculo em R$: 000.00
Total não recebido em R$: 000.00
Total em reservas R$: 000.00
[7] - Reiniciar o espetáculo (todas as variáveis deverão ser reiniciadas e as cadeiras do espetáculo, liberadas).
Boa diversão e lembre-se nada é tão ruim que não possa ser piorado.
