from pylab import *

#Individual author data combined into a single .dat firle
#Each data set separated by zeros
#Zeros also included in line 0 of .dat file and last line of .dat file
filedata = loadtxt('Data/K N Grankin 1998.dat',unpack=True)
jd = filedata[0]
vmag = filedata[1]
jd = reshape(jd,shape(jd)[0])
vmag = reshape(vmag,shape(vmag)[0])
err = np.zeros(len(jd))+0.03

#Identify where "separators" are, so as to identify which line elements of the input file to plot for each author
wherezeros = where(jd == 0.00)[0]

#import pdb; pdb.set_trace()
scatter_kwargs = {"zorder":100}
error_kwargs = {"lw":1.5, "zorder":0}
area = pi*(3)**2
colors = ['red','orange','green','blue','purple','yellow','cyan'] #Can add more colors depending on how many authors' data sets need to be visually represented in plot
authors = ['Author 1','Author 2','Author 3','Author 4','Author 5','Author 6','Author 7','Author 8']  #List of authors in order as found in input .dat file

fig1 = figure(num=None,figsize=(14,5.5),facecolor='w')
ax = subplot(111,Position=[0.08, 0.10, 0.70, 0.80])
title('HBC 437',fontsize=18)
ylabel('V [mag]',fontsize=16)
xlabel('JD + 2400000',fontsize=16)
xlim([min(jd[where(jd != 0.00)[0]])-75,max(jd)+75])
ylim([min(vmag[where(vmag != 0.00)[0]])-(max(err)+0.02),max(vmag)+(max(err)+0.02)])
for i in range(1,len(wherezeros)):
    plt.errorbar(jd[wherezeros[i-1]+1:wherezeros[i]],vmag[wherezeros[i-1]+1:wherezeros[i]],yerr=err[wherezeros[i-1]+1:wherezeros[i]],linestyle="None",color='#000000',**error_kwargs)
    scatter(jd[wherezeros[i-1]+1:wherezeros[i]],vmag[wherezeros[i-1]+1:wherezeros[i]],color=colors[i-1],edgecolors='#000000',s=area,label=authors[i-1],**scatter_kwargs)
legend(bbox_to_anchor=(1.18,1.02))
xticks(np.arange(min(jd[where(jd != 0.00)[0]]),max(jd)+1,200))
show()