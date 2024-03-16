# Exemplo 2: alterar individualmente cada pixel ou ler a informação individual do pixel

# Biblioteca do openCV
import cv2

# Variavel imagem usando a função imread() para ler a imagem
img = cv2.imread('.\imagem\imagem.jpg')

# Ler as informações da imagem
(b, g, r) = img[0, 0]

# Imprimir na tela tela as cores
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)