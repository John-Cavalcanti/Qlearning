#Aqui vocês irão colocar seu algoritmo de aprendizado
import connection as cn

state = cn.connect(2037)

# variavel da proxima ação
acao = "right"
estado, recompensa = cn.get_state_reward(state, acao)

# abrindo documento
f = open('resultado.txt', 'r')

# calculo da linha do arquivo resultado.txt a ser modificada
posicao = int(estado[2:7], 2)*4 + int(estado[7:], 2) 

# Armazenando as linhas do arquivo em uma array
resultados = f.readlines()

# armazenando linha selecionada e recebendo valores separadamente
linha = resultados[posicao]
numeros = linha.split(" ")

# novo valor
novo_valor = "5"

# substituindo o valor de acordo com a ação correspodente
if acao == "left":
    atual = novo_valor+ " " + numeros[1] + " " + numeros[2]
elif acao == "jump":
    atual = numeros[0] + " " + novo_valor + " " + numeros[2]
elif acao == "right":
    atual = numeros[0]+ " " + numeros[1] + " " + novo_valor + "\n"
    atual = atual.replace(r"\n", "\n")

# reescrevendo a linha selecionada
resultados[posicao] = atual

# reescrevendo documento com a array modificada
f = open('resultado.txt', 'w')
f.writelines(resultados)

# fechando documento 
f.close()