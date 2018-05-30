from matplotlib import pyplot as plt
from matplotlib import style
from datetime import datetime

print('***********************************************')
print('Welcome to the Plotter')
print('')

path = raw_input('Please enter the name of the dataset: \n')
try:
    file = open(path, mode='r')

    lines = file.readlines()
except Exception as e:
    print('Failed to load %s :\n %s' % (path,e))
else:
	print("Dataset successfully loaded")

data = []
lines.pop(0)

for l in lines:
    date = datetime.strptime(l.replace('\n','').split(',')[0],'%m/%d/%Y')
    value = float(l.replace('\n','').split(',')[1])

    data.append([date,value])

style.use('ggplot')

x = []
y = []

for point in data:
	x.append(point[0])
	y.append(point[1])

plt.title('Stock Indicator')
plt.ylabel('Stock Price')
plt.xlabel('Date and Time')

while(True):
	cmd = int(input('Please enter a number to select a Chart Type: \n1. Line \n2. Bar\n3. Exit\n'))
	if cmd == 1:
		plt.plot(x,y)
		plt.show()
	elif cmd == 2:
		plt.bar(x,y,color='c', align = 'center')
		plt.show()
	elif cmd == 3:
		exit()
	else:
		print('Invalid input, please try again')