# Biblioteca do openCV
import cv2

# Variavel imagem usando a função imread() para ler a imagem
img = cv2.imread('.\imagem\imagem.jpg')

# Substituindo todos os pixels por Azul(Blue)

for y in range(0 , img.shape[0], 10): # Y percorre as linha;
    for x in range(0, img.shape[1], 10): # X percorre as colunas.
        img[y: y + 5, x: x + 5] = (0,255,255) # Quadrados amarelos.

# Mostrar a imagem usando o imshow()
cv2.imshow("Imagem Modificada", img)

# Esperar até pressionar qualquer botão... Esqueci de usar esse ele apareceu e sem ver nada ele ja sumiu
cv2.waitKey(0)
