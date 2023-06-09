from IDS import IterativeDeepeningSearch
import  time
import numpy as np

start_time = time.time()


ids = IterativeDeepeningSearch( np.array([[0,4,2],[3,1,5],[7,8,6]]))
ids.Search()

print("time : "+str(time.time() - start_time))