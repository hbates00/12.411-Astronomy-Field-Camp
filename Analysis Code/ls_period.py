from pylab import *
from astroML.time_series import lomb_scargle

#Input file has *NO* zeros separating the individual datasets.
#No title row, just the data
filedata = loadtxt('Data/no Grankin.txt',unpack=True)
jd = filedata[0]
vmag = filedata[1]
jd = reshape(jd,shape(jd)[0])
vmag = reshape(vmag,shape(vmag)[0])
err = np.zeros(len(jd))+0.03

#Looping through different resolutions to give you an idea of how the sampling resolution can affect the resulting power spectrum.
#Too coarse of sampling results in potentially not identifying important signals within the data
#Too fine of sampling may drown out the true signal amongst false signals in the power spectrum.  
for i in range(181,182): #range(min resolution test, max resolution test):
    diffs = diff(sort(jd))
    Pmin = 2*min(diffs) #Minimum guess for period = twice the smallest sequential time difference between observations
    Pmax = 60 #Maximum guess for period
    Resolution = i  #Frequency sampling resolution (higher isn't always better)
    period = linspace(Pmin,Pmax,Resolution) # Choose a period grid   <<<444,485>>>
    ang_freqs = 2*pi/period

    #####################################################
    power = lomb_scargle(jd,vmag,err,ang_freqs)
    N = len(jd)
    #####################################################

    fig1 = figure(num=None,figsize=(12,6),facecolor='w')
    title('Lomb-Scargle (Res = %d)'%i,fontsize=24)
    ylabel('Power',fontsize=20)
    xlabel('Period [d]',fontsize=20)
    #xlim([1.5,25])
    #ylim([0,0.125])
    plot(period,power,'-',color='#0066cc',lw=1.5)
    #annotate(s='%0.4f' % Pdiffs,fontsize=18,xy=([22,0.8]),xytext=(22,0.8))
    #plot(perbin,powbin,'-',color='#00e600',lw=2)
    xticks(np.arange(0, max(period)+1, 5.0))
    show()






