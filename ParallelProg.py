import multiprocessing
import os


print("--------Parallel programming: Pool class-------- ")
def square(n):
	print("Worker process id for{0}:{1}".format(n,os.getpid()))
	return(n*n);
	
if __name__=="__main__":
	
	#input list
	arr=[1,2,3,4,5]

	#creating a Pool Object
	p = multiprocessing.Pool()

	#map list to target function
	result = p.map(square,arr)
	
	print("Square of each elements: ")
	print(result)
