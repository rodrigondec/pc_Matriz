import time, logging
from matriz import fazer_matriz, load_matrizes, print_matriz
import threading
from threading import Thread

index_matrizes = 7
qt_execucoes = 1
# divisor_threads = 128
# qt_threads = int(tamanho_matriz/divisor_threads)
qt_threads = 64

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

def multiplicar(indexes):
	global resultado
	log_threads.info("thread "+threading.currentThread().getName()+" vai multiplicar os indexes "+str(indexes))
	for index in indexes:
		for i in range(0, len(a)):
			for j in range(0, len(a[i])):
				resultado[i][j] += a[i][index] * b[index][j]
	log_threads.info("thread "+threading.currentThread().getName()+" terminou")

threads = []
    
def multiplicar_matrizes(indexes_por_thread):
	global a
	global b
	global resultado
	
	for k in range(0, len(a), indexes_por_thread):
		indexes = []
		for i in range(k, (k+indexes_por_thread)):
			indexes.append(i)
		t = Thread(name=str(k),target=multiplicar, args=(indexes,))
		threads.append(t)
		t.start()

	for thread in threads:
		thread.join()

tempo_total = 0
tempo_read = 0
tempo_print = 0

start = time.time()
matrizes = load_matrizes(index_matrizes)
end = time.time()

tempo = end - start
tempo_read += tempo

a = matrizes[0]
b = matrizes[1]
resultado = fazer_matriz(len(a), len(b[0]))
tamanho_matriz = len(a)
# qt_threads = int(tamanho_matriz/divisor_threads)

setup_logger("log_exec", "log/conc/"+str(tamanho_matriz)+"-"+str(qt_threads)+"_e.txt")
log_exec = logging.getLogger("log_exec")
setup_logger("log_threads", "log/conc/"+str(tamanho_matriz)+"-"+str(qt_threads)+"_t.txt")
log_threads = logging.getLogger("log_threads")

log_exec.info("read: "+str(tempo_read)+"\n")

indexes_por_thread = int(len(a)/qt_threads)

for x in range(0, qt_execucoes):
	resultado = fazer_matriz(len(a), len(b[0]))
	log_threads.info("execute "+str(x+1))

	start = time.time()
	multiplicar_matrizes(indexes_por_thread)
	end = time.time()

	tempo = end - start
	tempo_total += tempo

	log_exec.info("execute "+str(x+1)+": "+str(tempo))
	log_threads.info("")


start = time.time()
print_matriz(resultado)
end = time.time()

tempo = end - start
tempo_print += tempo

log_exec.info("\nprint: "+str(tempo_print))

print(tempo_total)
print(str(len(a))+"-"+str(qt_threads))
log_exec.info("\nTempo total de execução: "+str(tempo_total))
log_exec.info("Tempo medio de execução: "+str(tempo_total/qt_execucoes))
log_exec.info("Tempo medio de execução + read + print: "+str((tempo_total/qt_execucoes) + tempo_read + tempo_print))