from pylab import *

#Input file has *NO* zeros separating the individual datasets.
#No title row, just the data
filedata = loadtxt('No Grankin.txt',unpack=True)
jd = filedata[0]
vmag = filedata[1]
err = np.zeros(len(jd))+0.03



Per = 5.6633
phasearray = jd
phase = zeros(len(phasearray))
for i in range(0,len(phasearray)):
    a = (phasearray[i] - phasearray[0])/Per
    phase[i] = a - int(a)
sortIndi = np.argsort(phase)
phases = phase[sortIndi]
magnitudes = vmag[sortIndi]
errors = err[sortIndi]

#days = linspace(min(jd),max(jd),100)
#phs = linspace(0,1,100)
#y = 0.25*cos((pi/2*days/Per)) + mean(magnitudes)

fig1 = figure(num=None,figsize=(10,5),facecolor='w')
title('Period = %s d' % round(Per,4))
ylabel('V (mag)',fontsize=16)
xlabel('Phase',fontsize=16)
xlim([min(phases)-0.025,max(phases)+0.025])
ylim([13.2,11])
scatter_kwargs = {"zorder":100}
error_kwargs = {"lw":2, "zorder":0}
area = pi*(3)**2
scatter(phases,magnitudes,color='blue',edgecolors='#000000',s=area,**scatter_kwargs)
errorbar(phases,magnitudes,yerr=errors,linestyle="None",color='#000000',**error_kwargs)
#plot(phs,y,'black')
show()