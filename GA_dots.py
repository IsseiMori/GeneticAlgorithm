import matplotlib.pyplot as plt
import random
import math
import copy
import numpy as np
import sys
from operator import itemgetter

#zero([0][0])~zero([4][9])
from numpy import *
dots = zeros((5, 11))
copy = zeros((5, 11))
copy2 = zeros(11)
copy3 = zeros(11)

endpoint = 1000
x = 0
gen = 0


#set random value minimum,maximum,amount
dots[0] = np.random.randint(-5,5,11)
dots[1] = np.random.randint(-5,5,11)
dots[2] = np.random.randint(-5,5,11)
dots[3] = np.random.randint(-5,5,11)
dots[4] = np.random.randint(-5,5,11)

def answer():
	for i in range(0, 5):
		difference = 0
		if dots[i][10] == 0:
			return 1
	return 0

def evaluate(array):
	for i in range(0, 5):
		difference = 0
		for j in range(0, 10):
			difference += fabs(array[i][j])
		array[i][10] = difference

def export(array):
	global x
	Y = [1,2,3,4,5,6,7,8,9,10,11]
	for i in range(0,5):
		#reset canvas
		plt.clf()

		#Set the range of the graph
		plt.xlim([-6,6])
		plt.ylim([0,11])

		plt.plot(array[i], Y, 'o')
		plt.savefig("pics/graph"+str(x)+".png")
		x +=1
		#plt.show()

#export()

def print_dots(array):
	for i in range(0, 5):
		print("array["+str(i)+"]="+str(array[i][10]))


#array, first array, second array, position
def change(array,a,b):
	print(a,b)
	for i in range(random.randint(3,7), 10):
		array[a][i], array[b][i] = array[b][i], array[a][i]

def mutation(array,a):
	dim  = random.randint(0,10)
	if dim == 10:
		sys.exit()
	array[a][dim] = random.randint(-5,5)

def birth(array,a,b,c):
	for i in range(0,10):
		if random.randint(0,1) == 1:
			array[c][i] = array[a][i]
		else:
			array[c][i] = array[b][i]

evaluate(dots)
while True:
	#print(dots)

	#print_dots(dots)
	copy = sorted(dots, key=lambda x:x[10])

	birth(copy,random.randint(0,2),random.randint(0,2),3)
	birth(copy,random.randint(0,2),random.randint(0,2),4)

	#change(copy,random.randint(0,4),random.randint(0,4))
	#change(copy,random.randint(0,4),random.randint(0,4))

	mutation(copy,random.randint(0,4))
	mutation(copy,random.randint(0,4))
	mutation(copy,random.randint(0,4))

	dots = copy

	evaluate(dots)
	#print_dots(dots)
	print(dots)

	#export(dots)
	
	#break when difference = 0
	if answer():
		print(gen)
		print("done")
		break

	#export()
	gen += 1
	if gen >=endpoint :
		sys.exit()


