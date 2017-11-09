
def plotfig():
	global root,i,stockPrice, strike, volatility, timeToMature, riskfreeRate, dividend
	S=float(stockPrice.get())
	K=float(strike.get())
	sig=float(volatility.get())
	t=float(timeToMature.get())/365
	r=float(riskfreeRate.get())
	y=float(dividend.get())
	d1=(math.log(S*math.exp(-y*t)/K)+(r+sig**2/2)*t)/sig/math.sqrt(t)
	d2=d1-sig*math.sqrt(t)
	callPrice=S*math.exp(-y*t)*norm.cdf(d1)-K*math.exp(-r*t)*norm.cdf(d2)
	putPrice=K*math.exp(-r*t)*norm.cdf(-d2)-S*math.exp(-y*t)*norm.cdf(-d1)
	#print callPrice,putPrice

	labelCall=Label(root,text='Call Price: '+str(callPrice))
	labelCall.grid(row=i,column=1)
	j=i+1
	labelPut=Label(root,text='Put Price: '+str(putPrice))
	labelPut.grid(row=j,column=1)
	j=j+2

	label0=Label(root,text='Know the Greeks')
	j=j+1
	Si=np.linspace(K-50,K+50,100)
	d1i=(np.log(Si*math.exp(-y*t)/K)+(r+sig**2/2)*t)/sig/math.sqrt(t)
	deltaCall=math.exp(-y*t)*norm.cdf(d1i)
	deltaPut=-math.exp(-y*t)*(1-norm.cdf(d1i))
	gammaAll=norm.pdf(d1i)*math.exp(-y*t)/Si*sig*math.sqrt(t)
	thetaPut=-Si*norm.pdf(d1i)*sig*math.exp(-y*t)/2/math.sqrt(t)-y*Si*math.exp(-y*t)*norm.cdf(-d1i)+r*K*math.exp(-r*t)*norm.cdf(-d1i+sig*math.sqrt(t))
	f,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(10,4),dpi=100)
	ax1.plot(Si,deltaCall,'r')
	ax1.plot(Si,deltaPut,'b')
	ax1.set_ylabel(r'$\Delta$')
	ax1.set_xlabel('Spot Price [$]')
	ax1.legend(['Call','Put'],frameon=False)
	ax2.plot(Si,gammaAll,'k')
	ax2.set_ylabel(r'$\Gamma$')
	ax2.set_xlabel('Spot Price [$]')
	ax3.plot(Si,thetaPut,'k')
	ax3.set_ylabel(r'$\Theta$')
	ax3.set_xlabel('Spot Price [$]')
	f.tight_layout()
	canvas=FigureCanvasTkAgg(f,root)
	plot_widget=canvas.get_tk_widget()
	plot_widget.grid(row=j,column=1)

	Button(root, text='Quit', command=root.quit).grid(row=0, column=0)





# simple GUI
import numpy as np
import math
from scipy.stats import norm
from Tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# create the window
root = Tk()

# modify root window
root.title("Option Price Simulator")
root.geometry("1500x1000")


button1=Button(root,text="Run",command=plotfig)
button1.pack(side='top')
button1.grid(row=0,column=1)

i=1
stockPrice=Entry(root)
stockPrice.insert(END,'90')
stockPrice.grid(row=i,column=1)
labelStockPrice=Label(root,text='Stock Price [$]')
labelStockPrice.grid(row=i)
i=i+1
strike=Entry(root)
strike.insert(END,'100')
strike.grid(row=i,column=1)
labelStrike=Label(root,text='Strike Price [$]')
labelStrike.grid(row=i)
i=i+1
volatility=Entry(root)
volatility.insert(END,'1')
volatility.grid(row=i,column=1)
labelVolatility=Label(root,text='Stock Volatility [$]')
labelVolatility.grid(row=i)
i=i+1
timeToMature=Entry(root)
timeToMature.insert(END,'7')
timeToMature.grid(row=i,column=1)
labelTimeToMature=Label(root,text='Time to Maturity [day]')
labelTimeToMature.grid(row=i)
i=i+1
riskfreeRate=Entry(root)
riskfreeRate.insert(END,'0.05')
riskfreeRate.grid(row=i,column=1)
labelRiskfreeRate=Label(root,text='Risk-free Interest Rate [per year]')
labelRiskfreeRate.grid(row=i)
i=i+1
dividend=Entry(root)
dividend.insert(END,'0')
dividend.grid(row=i,column=1)
labelDividend=Label(root,text='Dividend [$]')
labelDividend.grid(row=i)
i=i+1

plotfig()

root.mainloop()



