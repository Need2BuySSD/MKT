from MKT import *

axes = Axes(10, 'P/$P$', 'V/$V$', ltx=True, fontsize=32, yratio=0.8)

p1 = (2, '')
p2 = (6, '')
v1 = (1, '')
v2 = (9, '')
state1 = State(axes, p=p1, v=v1, xtick=False, ytick=False, patch='1', patch_pos='BL')
state2 = State(axes, p=p1, v=v2, xtick=False, ytick=False, patch='2', patch_pos='BR')
state3 = State(axes, p=p2, v=v2, xtick=False, ytick=False, patch='3', patch_pos='TR')
state4 = State(axes, p=p2, v=v1, xtick=False, ytick=False, patch='4', patch_pos='TL')

axes.process(state1,state2, lwmult=1.2)
axes.process(state2,state3, lwmult=1.2)
axes.process(state3,state4, lwmult=1.2)
axes.process(state4,state1, lwmult=1.2)

#savefig('8.31.pdf')
show()