import colorama
import progressbar
import time

def tarea_super_lenta():
    time.sleep(2)

barra_progreso = progressbar.ProgressBar()

print colorama.Fore.GREEN

for n in barra_progreso(xrange(0, 10)):
    tarea_super_lenta()
