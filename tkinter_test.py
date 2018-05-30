from matplotlib import pyplot as plt
from matplotlib import style
from datetime import datetime
import Tkinter as Tk
#from tkinter import Tk
import matplotlib 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
from matplotlib import style
import matplotlib.animation as animation
from datetime import datetime
import numpy as np
import pandas as pd



LARGE_FONT = ("Verdana",12)
style.use("ggplot");

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

try:
	companies = open("companies.txt", mode='r').readlines()
	for line in companies:
		companies[companies.index(line)] = line.replace('\n','')
except Exception as e:
	raise

def animate(company):
	path = company+".csv"
	lines = open(path, mode='r').readlines()

	data = []
	lines.pop(0)

	for l in lines:
		date = datetime.strptime(l.replace('\n','').split(',')[0],'%m/%d/%Y')
		value = float(l.replace('\n','').split(',')[1])

		data.append([date,value])

	xlist = []
	ylist = []

	for point in data:
		xlist.append(point[0])
		ylist.append(point[1])

	#plt.title('Stock Indicator')
	#plt.ylabel('Stock Price')
	#plt.xlabel('Date and Time')

	a.clear()
	a.plot(xlist, ylist)


class StockPriceApp(Tk.Tk):
	def __init__(self, *args, **kwargs):
		Tk.Tk.__init__(self, *args, **kwargs)

		Tk.Tk.iconbitmap(self, default="Stocks.ico" )
		Tk.Tk.wm_title(self, "Stock Trading App")

		container = Tk.Frame(self)
		container.pack(side="top", fill = "both",expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.startFrame = StartPage(container, self) #intial page we run on

		self.startFrame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.startFrame
		frame.tkraise()

class StartPage(Tk.Frame):
	def __init__(self, parent, controller):

		Tk.Frame.__init__(self,parent)
		label = Tk.Label(self, text = "Choose Which StockTrend to Follow", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		for company in getCompanies():
			button = Tk.Button(self, text=company,command = lambda: showGraph(company))
			button.pack()

def showGraph(company):
	lines = None
	try:
	    file = open(company+'.csv', mode='r')
	    lines = file.readlines()
	except Exception as e:
	    print('Failed to load %s :\n %s' % (company,e))
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

	plt.title(company + 'Stock Indicator')
	plt.ylabel('Stock Price')
	plt.xlabel('Date and Time')

	plt.plot(x,y)
	plt.show()

def getCompanies():
	companies = None
	try:
		companies = open('companies.txt',mode='r').readlines()
	except Exception as e:
		raise

	companyList = []
	for c in companies:
		companyList.append(c.replace('\n',''))

	return companyList

app = StockPriceApp()
app.mainloop()