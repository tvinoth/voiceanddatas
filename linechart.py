import matplotlib.pyplot as plt 
  
# x axis values 
x = [1,2,3,4,5,6] 
# corresponding y axis values 
y = [1,0,1,1,1,0] 
  
# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 
  
# setting x and y axis range 
# plt.ylim(1,8) 
# plt.xlim(1,8) 
  
# naming the x axis 
plt.xlabel('date') 
# naming the y axis 
plt.ylabel('days') 
  
# giving a title to my graph 
plt.title('Attendance!') 
  
# function to show the plot 
plt.show() import datetime  
