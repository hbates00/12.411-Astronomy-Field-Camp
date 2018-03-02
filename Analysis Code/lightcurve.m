%Plots using subplots


hold on

subplot(5, 1, 1)
errorbar(JD1, Vmag1, err1, 'r.')
legend('J. Bouvier et al, 1993')
title('Long-Term Variability of HBC 379', 'fontsize', 18)
axis([2.446*10^6, 2.454*10^6, 12, 13])

set(gca, 'YDir', 'reverse')

subplot(5, 1, 2)
errorbar(JD2, Vmag2, err2, 'y.')
legend('F. J. Vrba et al, 1993a')
axis([2.446*10^6, 2.454*10^6, 12, 13])
set(gca, 'YDir', 'reverse')

subplot(5, 1, 3)
errorbar(JD3, Vmag3, err3, 'g.')
legend('F. J. Vrba et al, 1993b')
axis([2.446*10^6, 2.454*10^6, 12, 13])
ylabel('V Magnitude', 'fontsize', 18)
set(gca, 'YDir', 'reverse')

subplot(5, 1, 4)
errorbar(JD4, Vmag4, err4, 'b.')
legend('K. N. Grankin, 1998')
axis([2.446*10^6, 2.454*10^6, 12, 13])
set(gca, 'YDir', 'reverse')

subplot(5, 1, 5)
errorbar(JD5, Vmag5, err5, 'm.')
legend('K. N. Grankin et al, 2007')
axis([2.446*10^6, 2.454*10^6, 12, 13])
xlabel('Julian Date', 'fontsize', 18)
set(gca, 'YDir', 'reverse')

hold off


%% Plots all on one graph

hold on

set(gca, 'YDir', 'reverse')
title('Long-Term Variability of HBC 379', 'fontsize', 30)

green = [0/255, 150/255, 136/255]
grey = [120/255, 144/255, 156/255]
orange = [255/255, 171/255, 64/255]
blue = [77/255, 208/255, 225/255]
dkgrey = [48/255, 48/255, 48/255]

errorbar(JD1, Vmag1, err1, '.', 'Color', green, 'markersize', 30)
errorbar(JD3, Vmag3, err3, '.', 'Color', orange, 'markersize', 30)
errorbar(JD2, Vmag2, err2, '.', 'Color', grey, 'markersize', 30)
errorbar(JD4, Vmag4, err4, '.', 'Color', blue, 'markersize', 30)
errorbar(JD5, Vmag5, err5, '.', 'Color', dkgrey, 'markersize', 30)


xlabel('Julian Date', 'fontsize', 24)
ylabel('Vmag', 'fontsize', 24)
legend('J. Bouvier et al, 1993', 'F. J. Vrba et al, 1993b', 'F. J. Vrba et al, 1993a', 'K. N. Grankin, 1998', 'K. N. Grankin et al, 2008')

set(gca, 'fontsize', 18)

authors = ['J. Bouvier et al, 1993', 'F. J. Vrba et al, 1993a', 'F. J. Vrba et al, 1993b','K. N. Grankin, 1998', 'K. N. Grankin et al, 2007'];