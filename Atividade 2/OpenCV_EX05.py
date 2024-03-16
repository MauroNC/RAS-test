# Biblioteca do openCV
import cv2

# Variavel imagem usando a função imread() para ler a imagem
img = cv2.imread('.\imagem\imagem.jpg')

# Substituindo todos os pixels por Azul(Blue)

for y in range(0 , img.shape[0]): # Y percorre as linha;
    for x in range(0, img.shape[1]): # X percorre as colunas.
        img[y, x] = (0,(x*y)%256,0)

# Mostrar a imagem usando o imshow()
cv2.imshow("Imagem Modificada", img)

# Esperar até pressionar qualquer botão... Esqueci de usar esse ele apareceu e sem ver nada ele ja sumiu
cv2.waitKey(0)
