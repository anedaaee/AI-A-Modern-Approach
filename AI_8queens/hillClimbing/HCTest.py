from HC import HillClimbing
import time
start_time = time.time()

x = HillClimbing([4,5,6,3,4,5,6,5])

x.climb()
print("time : " + str(time.time() - start_time))