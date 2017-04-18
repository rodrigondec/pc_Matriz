import time
from matriz import *

matrizes = load_matrizes(6)
a = matrizes[0]
b = matrizes[1]

resultado = fazer_matriz(len(a), len(b[0]))
log = open("log/seq/"+str(len(a))+".txt", "w")
for x in range(0, 30):
	start = time.time()
	multiplicar_matrizes(a, b, resultado)
	end = time.time()
	log.write(str(end - start)) 
	log.write("\n")