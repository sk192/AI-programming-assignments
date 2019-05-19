#!/usr/bin/python3
import os, sys, random
import copy
import traceback
import math
import datetime
from collections import OrderedDict
from operator import itemgetter  

def fitness_function(population, queen_loc):
	
	
	state_fitness_dict = {}
	#print("queen_loc length, population len: %s%s" %(len(queen_loc),len(population)))
	for i in range(len(queen_loc)):
		fitness = 0
		flag = False
		max_non_attacking_queens = 28
		#while j < len(queen_loc[i]) - 1 and k < len(queen_loc[i]):
		for j in range(len(queen_loc[i])-1):
			for k in range(j+1, len(queen_loc[i])):
				a = queen_loc[i][j]
				b = queen_loc[i][k]
				#print(a,b)
				x1 = a[0]
				y1 = a[1]
				x2 = b[0]
				y2 = b[1]
				#print(x1,y1,x2,y2)
				if (x1 == x2 and y1 != y2) or (x1 == y1 and x2 == y2) or (x1 != x2 and y1 == y2) or (x1 == y2 and x2 == y1) or (x1-1 == x2 and y1 + 1 == y2) or (abs(x1 - x2) == abs(y1 - y2)) or (x1 + 1 == x2 and y1 - 1 == y2):
					fitness += 1
				#print(fitness)
		fit = max_non_attacking_queens - fitness
		#print("i: %s" %(i))
		# p = population[i]
		# q = ''
		# for x in population[i]:
		# 	q = q + ''.join(str(x) )

		state_fitness_dict[population[i]] = fit

	return state_fitness_dict

def selection(fit):
	S = sum(fit.values())
	prob_selection = {}
	parent_selection = []
	# for i in range(len(population)):
	# 	partial_sum = random.randint(0,S)
	# 	for key in fit:
	# 		partial_sum = partial_sum + fit[key]
	# 		if partial_sum < S:
	# 			continue
	# 		else:
	# 			selection.append(key)
	# 			break
	previous_prob = 0.0
	for key in fit:
		previous_prob = previous_prob + (fit[key]/S)
		#print("previous_prob: %s" %(previous_prob))
		prob_selection[key] = previous_prob
	OrderedDict(sorted(prob_selection.items(), key= lambda x : x[1]))
	#print("------prob selection --------------: %s " %(prob_selection))
		#print("prob_selection: %s" %(prob_selection))
	#print("prob_selection: %s" %(prob_selection))
	for i in range(len(prob_selection)):
		r = random.uniform(0,1)
		#print("r: %s" %(r))
		for j in prob_selection:
			if r < prob_selection[j]:
				parent_selection.append(j)
				break
	print("parent_selection, length: %s%s" %(parent_selection, len(parent_selection)))
	return parent_selection


def crossover(p_sel):
	
	i = 0
	j = 1
	crossover = []
	while i < len(p_sel) - 1 and j < len(p_sel):
		c = random.randint(1,6)
		A = p_sel[i]
		B = p_sel[j]
		C = A[:c+1] + B[c+1:]
		D = B[:c+1] + A[c+1:]
		#print("A: %s" %(A))
		#print("B: %s" %(B))
		crossover.append(C)
		crossover.append(D)
		i += 2
		j += 2
	return crossover

def mutation(cross):
	prob = 0.05
	for i in range(len(cross)):
		n = random.uniform(0,1)
		if n < prob:
			print("-------------------------------------Mutation happened-------------------------: %s" %n)
			while True:
				r1 = str(random.randint(1,8))
				r2 = str(random.randint(1,8))
				if r1 in cross[i]:
					cr = cross[i].find(r1)
					clist = list(cross[i])
					clist[cr] = r2
					cross[i] = ''.join(clist)
					break
	return cross

def process(population):

	S= 0 
	
	
	for i in range(10):
		queen_loc = []
		z = 0
		k = 0
		states =[]
		while k < len(population):
			b = [] 
			for i in range(8):
				b.append(random.randint(1,8)) 
			k += 1
			states.append(b)
		#print("states: %s" %(states))
		#print("population: %s" %(population))
		while z < len(population):
			l = 0
			q_l = []
			while l < len(population[0]):
				q_l.append((int(population[z][l]),states[z][l]))
				l += 1
			#print(q_l)
			queen_loc.append(q_l)
			#print(queen_loc)
			z += 1
		print("===========new_population=======%s" %(population))
		print("Queen Location----------------%s" %(queen_loc))
		fit = fitness_function(population, queen_loc)
		print("fitness: %s" %(fit))
		if 28 in fit.values():
			print("---------------FOUND---------------")
			for key,value in fit.items():
				if value == 28:
					return key
		else: 
			p_sel = selection(fit)
			cross = crossover(p_sel)
			new_population = mutation(cross)
			print("new_population: %s" %(new_population))
			population = new_population
	print("Sorry could not find solution ")
	return population
		
	

if __name__ == '__main__':
	n = int(input("Enter number of states in population: "))
	
	population = []
	states = [] 

	k = 0
	while k < n:
		a = []
		for i in range(8):
			a.append(random.randint(1,8)) 
			#b.append(random.randint(1,8))
		population.append(a)
		#states.append(b)
		k += 1
	for i in range(len(population)):
		p = population[i]
		q = ''
		for x in population[i]:
			q = q + ''.join(str(x) )
		population[i] = q

	p = process(population)
	print(p)
