from IDS import IterativeDeepeningSearch
import time

start_time = time.time()

ids = IterativeDeepeningSearch('arad','bucharest')
ids.Search()

print("time : " + str(time.time() - start_time))