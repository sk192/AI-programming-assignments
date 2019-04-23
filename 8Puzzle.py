
#!/usr/bin/python3.6
# 8 Puzzle using A* algorithm misplaced pile huristic method
import os, sys
import copy
import traceback
import math
import datetime

class Node: 
	def __init__(self, data, f_val, level):
		self.data = data
		self.f_val = f_val
		self.level = level

	def find_blank(self,initial):
		for i in range(len(self.data)):
			for j in range(len(self.data)):
				if initial[i][j] == 'b':
					return i,j
				else:
					continue
		
	def swap1(self,initial, x1,y1, x2, y2):
		if x2 >= 0 and x2 < len(self.data) and y2 < len(self.data) and y2 >= 0:
			temp =[]
			duplicate_data = copy.deepcopy(initial)
			temp = duplicate_data[x1][y1]
			duplicate_data[x1][y1] = duplicate_data[x2][y2]
			duplicate_data[x2][y2] = temp
			return duplicate_data
		else:
			return None


	def create_child(self):
		x, y = self.find_blank(self.data)
		child = []
		value = [(x, y-1),(x, y+1),(x-1, y),(x+1, y)]
		for i in value:
			swap1 = self.swap1(self.data,x,y,i[0],i[1])
			if swap1 is not None:
				child_nade = Node(swap1, 0,self.level+1)
				child.append(child_nade)

		return child

class puzzle:

	def __init__(self, mat_size):
		self.l = mat_size
		self.open1 = []
		self.closed1 = []
		self.visited_node_data1 = []
		self.open2 = []
		self.closed2 = []
		self.visited_node_data2 = []
		self.open3 = []
		self.closed3 = []
		self.visited_node_data3 = []

	def huristic1(self, initial, goal):             # misplaced pile
		
		h = 0
		for i in range(self.l):
			for j in range(self.l):
				if initial[i][j] == 'b':
					continue
				elif initial[i][j] != goal[i][j]:
					h += 1
		
		return h
	def huristic2(self, initial, goal):				# manhattan distance
		sum2 = []
		initial_dict = {}
		goal_dict = {}
		for i in range(self.l):
			for j in range(self.l):
				key = initial[i][j]
				value = (i,j)
				key1 = goal[i][j]
				value1 = (i,j)
				initial_dict[key] = value
				goal_dict[key1] = value1
		for key in initial_dict:
			if key in goal_dict:
				x2 = goal_dict[key][0]
				y2 = goal_dict[key][1]
			x1 = initial_dict[key][0]
			y1 = initial_dict[key][1]
			sum1 = (abs(x1 - x2) + abs(y1 - y2))
			sum2.append(sum1)
		return sum(sum2)
	
	def huristic3(self, initial, goal):			# Euclidean distance
		# sum3 = []
		# initial_dict = {}
		# goal_dict = {}
		# for i in range(self.l):
		# 	for j in range(self.l):
		# 		key = initial[i][j]
		# 		value = (i,j)
		# 		key1 = goal[i][j]
		# 		value1 = (i,j)
		# 		initial_dict[key] = value
		# 		goal_dict[key1] = value1
		# for key in initial_dict:
		# 	if key in goal_dict:
		# 		x2 = goal_dict[key][0]
		# 		y2 = goal_dict[key][1]
		# 	x1 = initial_dict[key][0]
		# 	y1 = initial_dict[key][1]
		# 	sum1 = math.sqrt(abs((x1 - x2)^2 + (y1 - y2)^2))
		# 	sum3.append(sum1)
		# return sum(sum3)
		h1 = self.huristic1(initial,goal)
		h2 = self.huristic2(initial,goal)
		compsite = max(h1,h2)
		return compsite



	def h1f(self,start,goal):
		return self.huristic1(start.data, goal) + start.level
	
	def h2f(self,start,goal):
		return self.huristic2(start.data, goal) + start.level


	def h3f(self,start,goal):
		return self.huristic3(start.data, goal) + start.level

	def process1(self, initial, goal):

		print("\n heusristic 1 misplaced tiles method: \n")
		start = Node(initial, 0, 0)
		start.f_val = self.h1f(start, goal)
		self.open1.append(start)
		count = 0
		cur = self.open1[0]
		
		while self.huristic1(cur.data, goal) != 0 :
			
			
			#self.open1 = []
			for i in cur.data:
				for j in i:
					print(j, end=" ")
			if self.huristic1(cur.data, goal) == 0:
				break
			print("\n")
			print(" | ")
			print(" | ")
			print("\\\'/ \n")
		
			for k in cur.create_child():

				if k.data not in self.visited_node_data1:
					k.f_val = self.h1f(k, goal)
					self.open1.append(k)
			self.closed1.append(cur)
			self.visited_node_data1.append(cur.data)
			count += 1
			#if cur in self.open1:
			del self.open1[0]
			self.open1.sort(key = lambda x: x.f_val, reverse = False)
			cur = self.open1[0]
			if count <= 100:
				continue
			else:
				print("Sorry no solution found..we reached leaf node: ")
				break
		for i in cur.data:
			for j in i:
				print(j, end=" ")
		print("\nprocess1 number of moves:%s" %(count))
		
	def process2(self, initial, goal):
		print("\n heuristic2 Manhattan distance method: \n")

		start = Node(initial, 0, 0)
		start.f_val = self.h2f(start, goal)
		self.open2.append(start)
		count = 0
		cur = self.open2[0]
		
		while self.huristic2(cur.data, goal) != 0 :
			
			
			#self.open1 = []
			for i in cur.data:
				for j in i:
					print(j, end=" ")
			if self.huristic2(cur.data, goal) == 0:
				break
			print("\n")
			print(" | ")
			print(" | ")
			print("\\\'/ \n")
		
			for k in cur.create_child():
				if k.data not in self.visited_node_data2:
					k.f_val = self.h2f(k, goal)
					self.open2.append(k)
			self.closed2.append(cur)
			self.visited_node_data2.append(cur.data)
			count += 1
			#if cur in self.open1:
			del self.open2[0]
			self.open2.sort(key = lambda x: x.f_val, reverse = False)
			cur = self.open2[0]
			if count <= 100:
				continue
			else:
				print("Sorry no solution found: ")
				break
		for i in cur.data:
			for j in i:
				print(j, end=" ")

		print("\nprocess2 number of moves:%s" %(count))

	def process3(self, initial, goal):

		print("\n Composite Heuristic3 method: \n ")
	
		start = Node(initial, 0, 0)
		start.f_val = self.h3f(start, goal)
		self.open3.append(start)
		count = 0
		cur = self.open3[0]
		
		while self.huristic3(cur.data, goal) != 0 :
			#self.open1 = []
			for i in cur.data:
				for j in i:
					print(j, end=" ")
			if self.huristic3(cur.data, goal) == 0:
				break
			print("\n")
			print(" | ")
			print(" | ")
			print("\\\'/ \n")
		
			for k in cur.create_child():
				if k.data not in self.visited_node_data3:
					k.f_val = self.h3f(k, goal)
					self.open3.append(k)
			self.closed3.append(cur)
			self.visited_node_data3.append(cur.data)
			count += 1
			#if cur in self.open1:
			del self.open3[0]
			self.open3.sort(key = lambda x: x.f_val, reverse = False)
			cur = self.open3[0]
			if count <= 100:
				continue
			else:
				print("Sorry no solution found..: ")
				break
		for i in cur.data:
			for j in i:
				print(j, end=" ")
		print("\nprocess3 number of moves:%s" %(count))
		

def main():
	
	p = puzzle(3)
	initial = []
	goal = [] 
	for i in range(3):
		initial.append(input("enter initial matrix: ").split(" "))
	for j in range(3):
		goal.append(input("enter goal matrix: ").split(" "))
	print("\n8 Puzzle problem using A* algorithm: \n")

	print("Initial Matrix: %s" %(initial))
	print("\nGoal Matrix: %s" %(goal))

	start_time = datetime.datetime.now()
	p.process1(initial,goal)
	finish_time = datetime.datetime.now()
	print("\n\nprocess1 execution time: %s" %(finish_time - start_time))

	start_time = datetime.datetime.now()
	p.process2(initial,goal)
	finish_time = datetime.datetime.now()
	print("\n\nprocess2 execution time: %s" %(finish_time - start_time ))


	start_time = datetime.datetime.now()
	p.process3(initial, goal)
	finish_time = datetime.datetime.now()
	print("\n\nprocess3 execution time: %s" %(finish_time - start_time))

if __name__ == '__main__':
	main()
	
