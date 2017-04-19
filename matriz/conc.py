import time, logging
from matriz import fazer_matriz, load_matrizes, print_matriz
import threading
from threading import Thread

def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    # l.addHandler(streamHandler)    

def multiplicar(index):
	global resultado
	log_threads.info("thread "+threading.currentThread().getName()+" vai multiplicar o index "+str(index))
	for i in range(0, len(a)):
		for j in range(0, len(a[i])):
			resultado[i][j] += a[i][index] * b[index][j]
	log_threads.info("thread "+threading.currentThread().getName()+" terminou")

threads = []
    
def multiplicar_matrizes(qt_threads):
	global a
	global b
	global resultado
	for k in range(0, len(a)):
		t = Thread(name=str(k),target=multiplicar, args=(k,))
		threads.append(t)
		t.start()

tempo_total = 0
tempo_read = 0
tempo_print = 0

start = time.time()
matrizes = load_matrizes(6)
end = time.time()

tempo = end - start
tempo_read += tempo

a = matrizes[0]
b = matrizes[1]
resultado = fazer_matriz(len(a), len(b[0]))
tamanho_matriz = len(a)
qt_threads = tamanho_matriz

setup_logger("log_exec", "log/conc/"+str(tamanho_matriz)+"-"+str(qt_threads)+"_e.txt")
log_exec = logging.getLogger("log_exec")
setup_logger("log_threads", "log/conc/"+str(tamanho_matriz)+"-"+str(qt_threads)+"_t.txt")
log_threads = logging.getLogger("log_threads")

log_exec.info("read: "+str(tempo_read)+"\n")

qt_execucoes = 20
for x in range(0, qt_execucoes):

	start = time.time()
	multiplicar_matrizes(qt_threads)
	end = time.time()

	tempo = end - start
	tempo_total += tempo

	log_exec.info("execute "+str(x+1)+": "+str(tempo))

start = time.time()
print_matriz(resultado)
end = time.time()

tempo = end - start
tempo_print += tempo

log_exec.info("\nprint: "+str(tempo_print))

print(tempo_total)
log_exec.info("\nTempo total de execução: "+str(tempo_total))
log_exec.info("Tempo medio de execução: "+str(tempo_total/qt_execucoes))
log_exec.info("Tempo medio de execução + read + print: "+str((tempo_total/qt_execucoes) + tempo_read + tempo_print))