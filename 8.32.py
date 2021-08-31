from MKT import *

axes = Axes(10, 'P/$P$', 'V/$V$', ltx=True, fontsize=32, yratio=0.8)

p1 = (12/9, '')
p2 = (6, '')
v1 = (2, '')
v2 = (9, '')
state1 = State(axes, p=p1, v=v1, xtick=False, ytick=False, patch='1', patch_pos='BL')
state2 = State(axes, p=p2, v=v1, xtick=False, ytick=False, patch='2', patch_pos='TL')
state3 = State(axes, p=p1, v=v2, xtick=False, ytick=False, patch='3', patch_pos='R')

axes.process(state1,state2, lwmult=1.2)
axes.isothermal(state2, state3, lwmult=1.2)
axes.process(state3,state1, lwmult=1.2)

#savefig('8.32.pdf')
show()