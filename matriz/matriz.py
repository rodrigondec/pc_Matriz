def load_matrizes(index):
	arquivos_matriz = [["a4x4.txt", "b4x4.txt"], ["a8x8.txt", "b8x8.txt"], ["a16x16.txt", "b16x16.txt"],  ["a32x32.txt", "b32x32.txt"], ["a64x64.txt", "b64x64.txt"], ["a128x128.txt", "b128x128.txt"], ["a256x256.txt", "b256x256.txt"], ["a512x512.txt", "b512x512.txt"], ["a1024x1024.txt", "b1024x1024.txt"], ["a2048x2048.txt", "b2048x2048.txt"]]

	arquivo_a = open("Matrizes/"+arquivos_matriz[index][0], 'r')
	arquivo_a.readline()
	matriz_a = []
	for linha in arquivo_a:
		matriz_a.append(linha.split())
	for i in range(0, len(matriz_a)):
		for j in range(0, len(matriz_a[i])):
			matriz_a[i][j] = int(matriz_a[i][j])
	arquivo_a.close()

	arquivo_b = open("Matrizes/"+arquivos_matriz[index][1], 'r')
	arquivo_b.readline()
	matriz_b = []
	for linha in arquivo_b:
		matriz_b.append(linha.split())
	for i in range(0, len(matriz_b)):
		for j in range(0, len(matriz_b[i])):
			matriz_b[i][j] = int(matriz_b[i][j])
	arquivo_b.close()

	return [matriz_a, matriz_b]

def fazer_matriz(linha, coluna):
	matriz = []
	for x in range(0, linha):
		matriz.append([])
		for y in range(0, coluna):
			matriz[x].append(0)
	return matriz

def multiplicar_matrizes(a, b, resultado):
	for i in range(0, len(a)):
		for j in range(0, len(a[i])):
			for k in range(0, len(a)):
				resultado[i][j] += a[i][k] * b[k][j]
	return resultado

def print_matriz(a):
	for i in range(0, len(a)):
		for j in range(0, len(a[i])):
			print(str(a[i][j])+" ", end='')
		print("\n")