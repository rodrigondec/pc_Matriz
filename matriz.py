def fazer_matriz(linha, coluna, valor):
	matriz = []
	for x in xrange(0, linha):
		matriz.append([])
		for y in xrange(0, coluna):
			matriz[x].append(valor)
	return matriz

def seq(linha, coluna):
	a = fazer_matriz(linha, coluna, 1)
	b = fazer_matriz(linha, coluna, 1)

	resultado = fazer_matriz(len(a), len(b[0]), 0)

	for i in xrange(0, len(a)):
		for j in xrange(0, len(a[0])):
			for k in xrange(0, len(a)):
				resultado[i][j] += a[i][k] * b[k][j]

	print(resultado)

seq(2, 2)