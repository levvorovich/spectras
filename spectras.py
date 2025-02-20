import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal 
print("Current folder:", os.getcwd())
line_count = 0
line_count_background=0
with open("Graphs of Spectras\PPMA_A4_250nm_graph.txt", "r") as file:
    for line in file:
        line_count +=1

with open("Graphs of Spectras\\background_graph.txt", "r") as file:
    for line_br in file:
        line_count_background +=1

x_array_pmma = []
y_array_pmma= []
i_start = 0
with open("Graphs of Spectras\PPMA_A4_250nm_graph.txt", "r") as file:
    
    for line in file:
        if line[0].isdigit():
            print("found")
            for line in file:
                numbers_pmma= line.split()
                x_array_pmma.append(float(numbers_pmma[0]))
                y_array_pmma.append(float(numbers_pmma[1]))
            
            break
        else:
            i_start +=1
print(i_start)
x_array_background = []
y_array_background= []
with open("Graphs of Spectras\\background_graph.txt", "r") as file:
    for line_br in file:
        if line_br[0].isdigit():
            for line_br in file:
                numbers_br= line_br.split()
                x_array_background.append(float(numbers_br[0]))
                y_array_background.append(float(numbers_br[1]))
array_final=[]                
for i in range(line_count-i_start-1):
    array_final.append([])
    array_final[i].append(str(x_array_pmma[i]))
    # print(x_array_pmma[i])
    for j in range(1):
        array_final[i].append(str(y_array_pmma[i]-y_array_background[i]))





for i in range(200):
    print(array_final[i])


# print(line_count_background)
# print(line_count)

with open("new_data.txt", "w") as file:
    for i in range(line_count-i_start-1):
        file.write(" ".join(array_final[i]) + "\n")
x_arr=[]
y_arr=[]
for x in range(len(array_final)):
    x_arr.append(float(array_final[x][0]))
for y in range(len(array_final)):    
    y_arr.append(float(array_final[y][1]))

plt.plot(x_arr, y_arr)

plt.show()

m=3
lambda_2=470
lambda_3=550
n=1.49
d=(m*lambda_2-(m+1)*lambda_3)/(2*n)  
print("thickness of pmma",d)
