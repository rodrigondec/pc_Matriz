import time
from matriz import *

matrizes = load_matrizes(8)
a = matrizes[0]
b = matrizes[1]

resultado = fazer_matriz(len(a), len(b[0]))
log = open("log/seq/"+str(len(a))+".txt", "w")
tempo_total = 0
for x in range(0, 30):
	start = time.time()
	multiplicar_matrizes(a, b, resultado)
	end = time.time()
	tempo = end - start
	tempo_total += tempo
	log.write(str(tempo)) 
	log.write("\n")

print(tempo_total)
log.write("\n")
log.write("Tempo total: "+str(tempo_total))
log.write("\n")
log.write("Tempo medio: "+str(tempo_total/30))
log.close()