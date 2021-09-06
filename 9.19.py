from MKT import *

axes = Axes(10, 'P/$P$', 'V/$V$', ltx=True, fontsize=26, yratio=1)

v1 = (2, '$V_{1,2}$')
v2 = (8, '$V_{3,4}$')
p1 = (2, '$P_{1,4}$')
p2 = (8, '$P_{2,3}$')

state1 = State(axes, v=v1, p=p1, patch='$1$', patch_pos='TL')
state2 = State(axes, v=v1, p=p2, patch='$2$', patch_pos='TL')
state3 = State(axes, v=v2, p=p2, patch='$3$', patch_pos='R')
state4 = State(axes, v=v2, p=p1, patch='$4$', patch_pos='TR')

axes.process(state1, state2)
axes.process(state2, state3)
axes.process(state3, state4)
axes.process(state4, state1)
axes.isothermal(state2, None, arrow=False, lwmult=0.6)

axes.line(state1, tp='xp', linestyle='-')
axes.line(state1, tp='yp', linestyle='-')
axes.line(state2, tp='xp', linestyle='-')
axes.line(state4, tp='yp', linestyle='-')

#savefig('9.19.pdf')
show()
