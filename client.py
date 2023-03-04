#Aqui vocês irão colocar seu algoritmo de aprendizado
import connection as cn

state = cn.connect(2037)

acao = "right"
estado, recompensa = cn.get_state_reward(state, acao)

# Lendo o documento txt em formato de array
# com cada linha ocupando uma posição
f = open('resultado.txt', 'r')
linhas = f.readlines()
print(linhas[0])

# conversão das informações recebidas do estado de binario para decimal
# para calcular a posiçao na array
direcao = int(estado[7:], 2) 
print(int(estado[2:7], 2), direcao)

# posicao = (int(estado[2:7], 2)-1)*4 + direcao

f.close()