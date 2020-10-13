#Biblioteca utilizada para criar o Histograma
import matplotlib.pyplot as hist

#inicia os valores iniciais dos pixels
pixels = []
mValue = 0

#Inicia o loop para inclusão dos Valores
i = 0
#Input dos valores
while i < 20:
    nun = input('Digite o Valor para a posição: %d Do vetor de Pixels\r\n' % i)
    try:
        #Caso converter um numero para float, irá retornar um erro
        value = int(nun)
        pixels.append(value)
        #Aqui irá salvar o maior valor inserido
        if(mValue < value):
            #Valor limite de intensidade
            mValue = value
        #Acrescenta a variavel contadora
        i = i + 1
    except ValueError:
        #Caso digitar algum valor invalido, o programa irá pedir para digitar um valor valido
        print('Valor Invalido, favor digitar um valor númerico que seja valido!')

# Resultado de pixels da imagem (N) (conforme solicitado no trabalho)
N = 20

#Controi a tabela que irá ficar com o histograma
hist.xlabel('Intensidade')
hist.ylabel('Repetições')
hist.title('Histograma da Imagem')

resultado = pixels #Prepara o Vetor resultado

#Graus de intensidade que cada pixel pode atribuir
L = mValue + 1

#Inicia o Vetor com o resultado do Histograma
#Com posições de 0 até até maior grau de intensidade da imagem
histog = []
for i in range(L):
    histog.append(0)
#Histograma do resultado
histogResu = []
for i in range(L):
    histogResu.append(0)

#Constroi o histograma dos inputs
for i in range(20):
    k = pixels[i]
    histog[k] = histog[k] + 1

#Monta Histograma Acumulado
histAcumulado = []
for i in range(L):
    #Pega quantidade no Histograma original
    valorAcumulado = histog[i]
    if(i > 0):
        #Pega o Ultimo valor adicionado e acrecenta
        valorAcumulado = valorAcumulado + histAcumulado[i - 1]
    histAcumulado.append(valorAcumulado)

#Constroi o Pk, divisão do histograma acumulado pelo número de Pixels
Pk = []
for i in range(L):
    resul = histAcumulado[i]/N
    Pk.append(resul)

#Constroi o K' que é resultado de Pk * variações de intensidade
kLine = []
for i in range(L):
    resul = round(Pk[i]*mValue)
    kLine.append(resul)

for i in range(20):
    #Pixel Atual
    valueAtual = pixels[i]
    #Novo Valor
    newValor = kLine[valueAtual]
    resultado[i] = newValor

#Constroi o histograma do resultado final
for i in range(20):
    k = resultado[i]
    histogResu[k] = histogResu[k] + 1

#Coloca o histograma original e o resultado na tabela criada
hist.plot(histogResu, color='blue')
hist.plot(histog, color='black')
hist.show()
