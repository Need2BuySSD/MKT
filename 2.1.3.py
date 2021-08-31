from MKT import *

axes = Axes(10, 'P/$p$', 'V/$V$', ltx=True, fontsize=32)

p1 = (4, '$p_0$')
p2 = (8, '$4p_0$')
v1 = (4, '$V_0$')
v2 = (8, '$2V_0$')
state1 = State(axes, p=p2, v=v1, patch='1', patch_pos='T')
state2 = State(axes, p=p1, v=v2, patch='2', patch_pos='R')

axes.process(state1,state2, arrow=False)

axes.marker(state1, ms=7)
axes.marker(state2, ms=7)

axes.line(state1, 'xp')
axes.line(state2, 'xp')
axes.line(state1, 'yp')
axes.line(state2, 'yp')

#savefig('2.1.3.pdf')
show()
