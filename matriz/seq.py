import time
from matriz import *

tempo_total = 0
tempo_read = 0
tempo_print = 0

start = time.time()
matrizes = load_matrizes(0)
end = time.time()

tempo = end - start
tempo_read += tempo

a = matrizes[0]
b = matrizes[1]
resultado = fazer_matriz(len(a), len(b[0]))

log = open("log/seq/"+str(len(a))+".txt", "w")
log.write("read: "+str(tempo)) 
log.write("\n\n")

for x in range(1, 21):
	resultado = fazer_matriz(len(a), len(b[0]))
	
	start = time.time()
	multiplicar_matrizes(a, b, resultado)
	end = time.time()

	tempo = end - start
	tempo_total += tempo

	log.write("execute "+str(x)+": "+str(tempo)) 
	log.write("\n")

start = time.time()
print_matriz(resultado)
end = time.time()

tempo = end - start
tempo_print += tempo

log.write("\n")
log.write("print: "+str(tempo_print)) 
log.write("\n")

print(tempo_total)
log.write("\n")
log.write("Tempo total de execução: "+str(tempo_total))
log.write("\n")
log.write("Tempo medio de execução: "+str(tempo_total/20))
log.write("\n")
log.write("Tempo medio de execução + read + print: "+str((tempo_total/20) + tempo_read + tempo_print))
log.close()