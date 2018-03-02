 pro v111_light

; code to plot VSB 111 light curve and best fit

; SZK+LAP 12-6&7-2012

; SZK+LAP 12-19-12

; edited by LAP 3-23-13

d=read_array('v111_bin_phot.txt',/double)
s=d(0:2,*)
p=3.74
r=s
ph=((r(0,*)-r(0,13))/p)-fix((r(0,*)-r(0,13))/p) ;pixel 13 corresponds to
;peak in light curve fit so phasing to that (technially, the min)
res=bsort(ph,sph)

n=dblarr(3,46)
n(0,*)=sph
n(1,*)=s(1,res)
n(2,*)=s(2,res)

x =  n(0,*)
y =  n(1,*)
x = x * 2 * !pi
rx=reform(x)
ry=reform(y)
ws=1.0/(n(2,*)^2)          ;Weights
weights=reform(ws)
 a=[-.0335, 43.7613, 12.595]        ;Initial guess
 yfit=curvefit(rx,ry,weights,a,sigma,function_name='sineFunct5')
 print, 'Function parameters: ', a
 print, yfit

; define array of radians, zero to 2*pi:

xx=findgen(1000.)/158.996

; plot data and curve

loadct,2

!x.style=1
!y.style=1

plot,n(0,*),reverse(n(1,*)),psym=4,yrange=[12.67,12.57],symsize=2., $
ytitle='V (mag)',xtitle='Phase',charsize=1.6,charthick=2.3, $
ythick=3,xthick=3,thick=3,xrange=[-.04,1.04]

oploterr,n(0,*),n(1,*),n(2,*),3
oplot, xx/(2.*!pi), ((a(0) * sin(xx + a(1))) + a(2)),color=80,thick=3

end
