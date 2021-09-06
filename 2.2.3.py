from MKT import *

axes = Axes(10, 'P/$P$', 'V/$V$', ltx=True, fontsize=26, yratio=0.5)

v1 = (2, '$V_0$')
v2 = (4, '$2V_0$')
v3 = (8, '$4V_0$')
p2 = (4, '$P_0$')
p1 = (2, r'$\frac{1}{2}P_0$')

state1 = State(axes, v=v1, p=p2, patch='$1$', patch_pos='TR')
state2 = State(axes, v=v2, p=p1, patch='$2$', patch_pos='TR')
state3 = State(axes, v=v3, p=p1, patch='$3$', patch_pos='TR')


axes.process(state1, state2)
axes.process(state2, state3)

axes.marker(state1, ms=7)
axes.marker(state2, ms=7)
axes.marker(state3, ms=7)

axes.line(state1, tp='xp')
axes.line(state1, tp='yp')
axes.line(state2, tp='xp')
axes.line(state2, tp='yp')
axes.line(state1, tp='yp')

#savefig('2.2.3.pdf')

show()
