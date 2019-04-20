
#!/usr/bin/python3.6
# 8 Puzzle using A* algorithm misplaced pile huristic method
import os, sys
import copy
import traceback

class Node: 
    def __init__(self, data, f_val, level):
        self.data = data
        self.f_val = f_val
        self.level = level

    def find_blank(self,initial):
        #print("inside find")
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if initial[i][j] == 'b':
                    return i,j
                else:
                    continue
        
    def swap1(self,initial, x1,y1, x2, y2):
        if x2 > 0 and x2 < len(self.data) and y2 < len(self.data) and y2 > 0:
            temp =[]
            duplicate_data = copy.deepcopy(initial)
            temp = duplicate_data[x1][y1]
            duplicate_data[x1][y1] = duplicate_data[x2][y2]
            duplicate_data[x2][y2] = temp
            #print("duplicate_data: %s" %(duplicate_data))
            return duplicate_data
        else:
            return None


    def create_child(self):
        #print(self.data)
        x, y = self.find_blank(self.data)
        child = []
        value = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
        for i in value:
            swap1 = self.swap1(self.data,x,y,i[0],i[1])
            if swap1 is not None:
                child_nade = Node(swap1, 0,self.level+1)
                child.append(child_nade)
        #print("child: %s" %(child))
        return child

class puzzle:

    def __init__(self, mat_size):
        self.l = mat_size
        self.open1 = []
        self.closed = []

    def huristic1(self, initial, goal):             # misplaced pile
        
        h = 0
        #print("initial: %s" %(initial))
        for i in range(self.l):
            for j in range(self.l):
                #print(i,j)
                if initial[i][j] == 'b':
                    continue
                elif initial[i][j] != goal[i][j]:
                    h += 1
        
        return h

    def f(self,start,goal):
        #print("start.data: %s" %(start.data))
        #print(type(start))
        return self.huristic1(start.data, goal) + start.level

    def process(self):
        
        #print("inside process")
        initial = []
        goal = [] 
        for i in range(3):
            initial.append(input("enter initial matrix: ").split(" "))
        for j in range(3):
            goal.append(input("enter goal matrix: ").split(" "))
        start = Node(initial, 0, 0)
        #print(start.data)
        start.f_val = self.f(start, goal)
        self.open1.append(start)
        while True:
            
            cur = self.open1[0]
            self.open1 = []
            #print(cur)
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                    #print(" ")
            print("\n")
            print(" | ")
            print(" | ")
            # print(" -- ")
            print("\\\'/ \n")
            if self.huristic1(cur.data, goal) == 0:
                break
            for k in cur.create_child():
                k.f_val = self.f(k, goal)
                self.open1.append(k)
            self.closed.append(cur)
            if cur in self.open1:
                del self.open1[0]
            self.open1.sort(key = lambda x: x.f_val, reverse = False)
        # self.open1.sort(key = lambda x: x.f_val, reverse = false)
        

def main():
    p = puzzle(3)
    p.process()
   
   


if __name__ == '__main__':
    print("hello")
    main()
    
