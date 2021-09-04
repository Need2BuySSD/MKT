from MKT import *

axes = Axes(10, 'P/$P$', 'V/$V$', ltx=True, fontsize=26, yratio=0.8)

v1 = (2, '')
v2 = (8, '')
p1 = (2, '')
p2 = (7, '')

state1 = State(axes, v=v1, p=p2, patch='$1$', patch_pos='L', xtick=False, ytick=False)
state2 = State(axes, v=v2, p=p2, patch='$2$', patch_pos='R', xtick=False, ytick=False)
state3 = State(axes, v=v2, p=p1, patch='$3$', patch_pos='R', xtick=False, ytick=False)
state4 = State(axes, v=v1, p=p1, patch='$4$', patch_pos='L', xtick=False, ytick=False)

axes.process(state1, state2)
axes.process(state2, state3)
axes.process(state3, state4)
axes.process(state4, state1)

#savefig('9.24.pdf')
show()
