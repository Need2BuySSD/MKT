from MKT import *

axes = Axes(10, 'P/$P$', 'V/$V$', ltx=True, fontsize=32, yratio=0.7)

v1 = (2, '$V_0$')
v2 = (8, '$3V_0$')
p1 = (2, '$P_0$')
p2 = (5, '$2P_0$')

state1 = State(axes, v=v1, p=p1, patch='$1$', patch_pos='BBL')
state2 = State(axes, v=v1, p=p2, patch='$2$', patch_pos='T')
state3 = State(axes, v=v2, p=p2, patch='$3$', patch_pos='R')

axes.process(state1, state2, arrow=False)
axes.process(state2, state3, arrow=False)
axes.process(state3, state1, arrow=False)

axes.marker(state1, ms=7)
axes.marker(state2, ms=7)
axes.marker(state3, ms=7)

axes.line(state1, tp='xp')
axes.line(state1, tp='yp')
axes.line(state2, tp='xp')
axes.line(state3, tp='yp')

savefig('9.28.pdf')
show()
