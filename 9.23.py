from MKT import *

axes = Axes(10, 'P/$P$', 'V/$V$', ltx=True, fontsize=26, yratio=0.8)

v1 = (2, '$V_0$')
v2 = (8, '$2V_0$')
p1 = (2, '$P_0$')
p2 = (6, '$2P_0$')

state1 = State(axes, v=v1, p=p1, patch='$1$', patch_pos='TL')
state2 = State(axes, v=v1, p=p2, patch='$2$', patch_pos='T')
state3 = State(axes, v=v2, p=p2, patch='$3$', patch_pos='R')
state4 = State(axes, v=v2, p=p1, patch='$4$', patch_pos='R')

axes.process(state1, state2, lwmult=1.5)
axes.process(state2, state3, lwmult=1.5)
axes.process(state3, state4, lwmult=1.5)
axes.process(state4, state1, lwmult=1.5)

axes.line(state1, tp='xp', linestyle='-')
axes.line(state1, tp='yp', linestyle='-')
axes.line(state2, tp='xp', linestyle='-')
axes.line(state4, tp='yp', linestyle='-')

#savefig('9.23.pdf')
show()
