from IDSAStar import IterativeDeepeningSearchAStar
import time

start_time = time.time()

idsa = IterativeDeepeningSearchAStar('arad','bucharest')
idsa.Search()

print("time : " + str(time.time() - start_time))