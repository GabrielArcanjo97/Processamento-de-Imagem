#Biblioteca utilizada para abrir a imagem
import cv2
#Biblioteca utilizada para criar o histograma
import matplotlib.pyplot as hist

#Abre a imagemPI
img = cv2.imread('imagem1.jpg')
cv2.imshow("Original", img)

#Resultado
imgResul = img

#Inicia o Vetor com o resultado do histograma com posições de 0 até 255 que dá um total de 256
histo = []
for i in range(256):
    histo.append(0)

#Histograma da imagem final (resultado)
histoResult = []
for i in range(256):
    histoResult.append(0)

#Guarda info da imagem
larg = img.shape[1]
altu = img.shape[0]


# Quatidade de pixels da Imagem (N)
N = altu * larg
#Graus de intensidade que cada pixel pode ter
L = 256
#0 até 255

#Desenha o histograma
for colum in range(altu):
    for line in range(larg):
        #Pega o resultado da intensidade que está na posição 0
        #Conta quantas vezes aquela mesma intensidade aparece na imagem
        K = img[colum][line][0]
        histo[K] = histo[K] + 1

#Controi a tabela que permanecerá com o histograma
hist.xlabel("Intensidade")
hist.ylabel("Repetições")
hist.title("Histograma da Imagem")

#Constroi o Histograma Acumulado
histAcumu = []
for i in range(256):
    #vai pegar a quantidade no histograma original
    valorAcumu = histo[i]
    if(i > 0):
        #Irá pega o ultimo valor adicionado e acrescentar
        valorAcumu = valorAcumu + histAcumu[i - 1]
    histAcumu.append(valorAcumu)

#Constroi o Pk divisão do histograma acumulado pelo número de Pixels da imagem
Pk = []
for i in range(256):
    resul = histAcumu[i]/N
    Pk.append(resul)

#construir o K' que é resultado de Pk * Variações de intensidade (Pk * 255)
kLine = []
for i in range(256):
    resul = Pk[i]*L
    kLine.append(resul)

#Constroi uma nova imagem trocando o valor de K por K'
for line in range(larg):
    for colum in range(altu):
        #Atual valor de Pixels
        resulAtual = img[colum][line][0]
        #Novo Valor
        newValor = kLine[resulAtual]
        #Acrescenta intensidade para cada 1 das 3 camadas BGR
        for c in range(3):
            imgResul[colum][line][c] = newValor

#Monta o resultado do histograma
for line in range(larg):
    for colum in range(altu):
        #Pega o valor da intensidade na posição 0 pois ele retorna no padrão BGR e queremos só 1 das camadas
        #Para contar quantas vezes aquela intensidade aparece na imagem
        K = imgResul[colum][line][0]
        histoResult[K] = histoResult[K] + 1

#Adiciona histogramas Origem e Resultado na "Tabela" criada
hist.plot(histoResult, color="black")
hist.plot(histo, color="red")

cv2.imshow("Resultado", imgResul)
hist.show()
