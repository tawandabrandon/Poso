from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot');

x = [2,4,6,8]
y = [7,3,8,3]

x2 = [1,3,5,7]
y2 = [6,7,2,6]

plt.bar(x,y,color='c', align = 'center')

plt.bar(x,y,color='g', align = 'center')

plt.title('Stock Indicator')
plt.ylabel('Stock Price')
plt.xlabel('Date and Time')

plt.show()
