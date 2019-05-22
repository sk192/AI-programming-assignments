# 8 queen problem using genetic algorithm. initial state: Place the queens from leftmost columns on the board, one queen per column. Goal state: Queens on the board such that none are attacking.


#!/usr/bin/python3
import os, sys, random
import copy
import traceback
import math
import datetime
from collections import OrderedDict
from operator import itemgetter  
import matplotlib.pyplot as plt

def fitness_function(population, queen_loc): 		# caluculate the number of non attacaking pair of queens as fitness value
	state_fitness_dict = []
	for i in range(len(queen_loc)):
		fitness = 0
		flag = False
		max_non_attacking_queens = 28
		for j in range(len(queen_loc[i])-1):
			for k in range(j+1, len(queen_loc[i])):
				a = queen_loc[i][j]
				b = queen_loc[i][k]
				x1 = a[0]
				y1 = a[1]
				x2 = b[0]
				y2 = b[1]
				if (x1 == x2 and y1 != y2) or (x1 == y1 and x2 == y2) or (x1 != x2 and y1 == y2) or (x1 == y2 and x2 == y1) or (x1-1 == x2 and y1 + 1 == y2) or (abs(x1 - x2) == abs(y1 - y2)) or (x1 + 1 == x2 and y1 - 1 == y2):
					fitness += 1
		fit = max_non_attacking_queens - fitness
		state_fitness_dict.append((population[i],fit))
	return state_fitness_dict

def selection(fit):									# Used roulette wheel selection method. 
	S=0
	for k in fit: 
		S = S + k[1]
	prob_selection = []
	parent_selection = []
	previous_prob = 0.0
	for key in fit:											
		previous_prob = previous_prob + (key[1]/S)			# calculate probability of every state and add with previous state probability
		prob_selection.append((key[0], previous_prob))
	sorted(prob_selection, key= itemgetter(1))
	for i in range(len(prob_selection)):				# Select the parents whose probability is greater than randomly selected number i.e. r 
		r = random.uniform(0,1)
		for j in prob_selection:
			if r < j[1]:
				parent_selection.append(j[0])
				break
	return parent_selection


def crossover(p_sel):
	
	i = 0
	j = 1
	crossover = []
	while i < len(p_sel) - 1 and j < len(p_sel):
		c = random.randint(1,6)								# select the crossover point randomly.
		A = p_sel[i]
		B = p_sel[j]
		C = A[:c+1] + B[c+1:]								# Generate child.
		D = B[:c+1] + A[c+1:]
		crossover.append(C)
		crossover.append(D)
		i += 2
		j += 2
	return crossover

def mutation(cross):									# Mutation will happen if n < prob.							
	prob = 0.05									
	for i in range(len(cross)):
		n = random.uniform(0,1)
		if n < prob:
			while True:									
				r1 = str(random.randint(1,8))
				r2 = str(random.randint(1,8))
				if r1 in cross[i]:
					cr = cross[i].find(r1)
					clist = list(cross[i])
					clist[cr] = r2							# replace the randomly selected number with other number.
					cross[i] = ''.join(clist)
					break
	return cross

def process(population):
	ar =[]
	S= 0 
	count = 0
	avg_fitness = []
	generation_population = []
	for i in range(100):
		generation_population.append(i+1)
		count += 1
		queen_loc = []
		#print("population : %s" %(population))
		z = 0
		while z < len(population):
			l = 0
			q_l = []
			while l < len(population[0]):					# this loop will create the 2-D queen loaction to calulate the fitness function.
				q_l.append((int(population[z][l]),l+1))     # queen location is like (row, column). Suppose state in population is '13246587', 
				l += 1										# then the representation will be (1,1),(3,2),(2,3),(4,4),(6,5),(5,6),(8,7),(7,8).
			queen_loc.append(q_l)				
			z += 1
		fit = fitness_function(population, queen_loc)
		sum1 = 0
		for i in range(len(fit)):
			sum1 = sum1 + fit[i][1]
		avg = sum1 / len(fit)
		avg_fitness.append(avg)
		#print("----------Avg: %s" %(avg))  
		for h in fit:
			if 28 == h[1]:				
				print("---------------FOUND THE OUTPUT------------")
				plt.title("Size_of_population = {%s}, Solved_in_genereation = {%s}" %(len(population),count))     # code to draw the graph
				plt.plot(generation_population, avg_fitness)
				plt.ylabel("Average fitness per geneartion ")
				plt.xlabel("Number of generations ")
				plt.yticks(range(0,30,2))
				plt.xticks(range(0,100,10))
				plt.ylim(0,28)
				plt.tight_layout()
				plt.show()
				print("Found at generation: %s" %(count))
				#return  h[0]
				ar.append(h[0])
		if len(ar) != 0:
			print("The state of non attacking queens is: ")
			return ar
		
		p_sel = selection(fit)
		cross = crossover(p_sel)
		new_population = mutation(cross)
		population = new_population
	print("Sorry could not find solution in 100 iterations...Try again ")
	plt.title("Size_of_population = {%s}, Solved_in_genereation = {%s}" %(len(population),count))
	plt.plot(generation_population, avg_fitness)
	plt.ylabel("Average fitness per geneartion ")
	plt.xlabel("Number of generations ")
	plt.yticks(range(0,30,2))
	plt.xticks(range(0,100,10))
	plt.ylim(0,28)
	plt.tight_layout()
	plt.show()

	return None
		
if __name__ == '__main__':
	n = int(input("Enter number of states in population (population size): "))
	
	population = []
	states = [] 

	k = 0
	while k < n:
		a = []
		for i in range(8):
			a.append(random.randint(1,8)) 
		population.append(a)
		k += 1
	for i in range(len(population)):
		p = population[i]
		q = ''
		for x in population[i]:
			q = q + ''.join(str(x) )
		population[i] = q

	p = process(population)
	print(p)
