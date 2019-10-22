import matplotlib.pyplot as plt 
  
# x-axis values 
x = [1,2,3,4,5,6,7,8,9,10] 
# y-axis values 
y = [1,1,1,0,1,1,1,0,1,1] 
  
# plotting points as a scatter plot 
plt.scatter(x, y, label= "present", color= "green",  
            marker= "*", s=30) 
  
# x-axis label 
plt.xlabel('date') 
# frequency label 
plt.ylabel('days') 
# plot title 
plt.title('Attendance') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show()