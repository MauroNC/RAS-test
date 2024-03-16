'''

Vamos rodar nosso primeiro programa.
Um “Alô mundo!” da visão computacional onde iremos apenas abrir uma arquivo de imagem
do disco e exibi-lo na tela. Feito isso o código espero o pressionamento de uma tecla para
fechar a janela e encerrar o programa.

não sei se esse seria o exemplo, mas fiz esse mesmo
'''

# Biblioteca do openCV
import cv2

# Variavel imagem usando a função imread() para ler a imagem
img = cv2.imread('.\imagem\imagem.jpg')

# Dimensões da imagem
print('Largura em pixels: ', end='')
print(img.shape[1])
print('Altura em pixels: ', end='')
print(img.shape[0])
print('Qtde de canais: ', end='')
print(img.shape[2])

# Mostra a imagem com a função imshow
cv2.imshow("Teste", img)

# Espera pressionar qualquer tecla
cv2.waitKey(0)

# Salvar a imagem no disco com função imwrite() segui o exemplo, não do pq isso, mas não qual de usar isso
# pelo menos para o exemplo...
cv2.imwrite("saida.jpg", img)
