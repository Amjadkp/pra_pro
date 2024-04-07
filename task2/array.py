import numpy as np
import time

start_time=time.time()
ar=np.random.randint((1000,1000))
time_taken= time.time()-start_time
print("time taken = ",time_taken)

#converting into bit
start_time=time.time()
ar_bytes=ar.tobytes()
time_taken=time.time()-start_time
print("time taken = ",time_taken)

#converting bytes into array datatypes
start_time=time.time()
ar2=np.frombuffer(ar_bytes,dtype=ar.dtype)
time_taken=time.time()-start_time
print("time taken = ",time_taken)
