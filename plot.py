import pandas as pd
from matplotlib import pyplot as plt
x = [1,2,34]
y = [1,12,25]
z = [10,5,0]
plt.title('Attendance')
# plt.xlabel("days")
# plt.ylabel("date")
# plt.plot(x,y)
# plt.plot(x,z)
# plt.legend(["this is Y","This is Z"])
# plt.show()

left = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13] 
  
# heights of bars 
height = [36, 40, 5,1,22,12,21,46,66,44,77,77,10] 
  
# labels for bars 
tick_label = ['1', '2', '3', '4', '5','6','7','8','9','10','11','12','13'] 
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'green']) 
  
plt.xlabel('Days') 
plt.ylabel('Date') 
plt.show()