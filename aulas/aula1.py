
exx001
#Determine o sucesso e o antecessor de um número
N1= int (input("Digite um número"))
N2=N1+1
N3=N1-1
print(f"O sucessor é {N2}")
print(f"O antecessor é {N3}")

ex002
#Calcule o perímetro de um quadrado
L=float(input("Digite o valor de um lado"))
P=4*L
print(f"\n\t Quando o lado do quadrado é {L:.2f} o perímetro é {P:.2f}")

ex003
#Determine a área de um triangulo
H=float(input("Qual a altura do seu triangulo"))
B=float(input("Qual é a base do seu triangulo"))
A=(B*H)/2
print(f"A área do triangulo é {A:.1f}")

ex004
#Calcule o volume do cubo
A=float(input("Qual é a aresta do cubo"))
V=A**3
print(f"O volume do cubo é{V:.1f}")

ex005
#Elabore um programa que dada uma distância percorrida em quilometros,em km,bem como o total de combustivel gasto,em L,informe o consumo do veiculo 
C=float(input("Determine o combustivel gasto em L"))
D=float(input("Determine a distancia percorrida em km"))
CF=D/C
print(f"O consumo final do veiculo é {CF:.2f}")

ex006
#Faça um programa que dadas as medidas de uma sala em metro,comprimento e largura, bem como o preço do metro quadrado do carpete,informe o custo total para forrar o piso da sala
L=float(input("Determine a largura"))
C=float(input("Determine o comprimento"))
P=float(input("Determine o preço de m2"))
A=C*L
CT=A/P
print(f"O custo total é {CT:.2f}")

ex007
#Leia o salário mensal atual de um funcionário e o percentual de reajuste e determine o valor do novo sálario
P=float(input("Determine a porcentagem"))
SA=float(input("Determine o valor do sálario atual"))
R=(P/100)*SA
VS=SA+R
print(f"O valor do novo sálario é {VS:.2f}")

ex008
#O índice de massa corpórea (IMC) de uma pessoa é igual ao peso,em quiogramas,dividido pelo quadrado de sua altura,em m.construa um programa que dado o peso e a altura de uma pessoa indorme o valor do IMC
H=float(input("Determine a sua altura,em m"))
P=float(input("Determine um peso,em kg"))
IMC=P/2**H
print(f"O IMC é {IMC:.2f}")

ex009
#Uma certa importancia sera dividida entre tres ganhadores de um concurso.Elabore um programa que dado o valor do concurso em reais ele calcule e imprima quantia ganha por cada um dos jogadores
Q=float(input("Determine a quantia do concurso"))
G1=(46/100)*Q
G2=(32/100)*Q
G3=(22/100)*Q
print (f"O ganhador um ganhará {G1:.2f}")
print (f"O ganhador dois ganhará {G2:.2f}")
print (f"O ganhador três ganhará {G3:.2f}")

ex010
#Exercício 9 AULA 
VC=int(input("Digite o valor da compra"))
VP=int(input("Digite o valor pago pelo cliente"))
troco=VP-VC
print(f"Cédulas de R$ 20,00 = {troco//20}")
troco=troco % 20
print(f"Cédulas de R$ 10,00 = {troco//10}")
troco=troco % 10
print(f"Cédulas de R$ 5,00 = {troco//5}")
print=troco % 5
print (f"Cédulas de R$ 1,00 = {troco}")
