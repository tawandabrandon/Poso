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
		graphs = []

		ZESAbtn = Tk.Button(self, text="ZESA",command = lambda: showZESA())
		ZESAbtn.pack()

		AFDISbtn = Tk.Button(self, text="AFDIS",command = lambda: showAFDIS())
		AFDISbtn.pack()

def showZESA():
	print("Graph for ZESA")
	lines = None
	try:
	    file = open('ZESA.csv', mode='r')
	    print("Opening file for")
	    lines = file.readlines()
	except Exception as e:
	    print('Failed to load')
	else:
		print("Dataset successfully loaded for")

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

	plt.title('ZESA Stock Indicator')
	plt.ylabel('Stock Price')
	plt.xlabel('Date and Time')
	plt.plot(x,y)
	plt.show()

def showAFDIS():
	print("Graph for AFDIS")
	lines = None
	try:
	    file = open('AFDIS.csv', mode='r')
	    print("Opening file for AFDIS")
	    lines = file.readlines()
	except Exception as e:
	    print('Failed to load company data file')
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

	plt.title('AFDIS Stock Indicator')
	plt.ylabel('Stock Price')
	plt.xlabel('Date and Time')
	plt.plot(x,y)
	plt.show()

app = StockPriceApp()
app.mainloop()