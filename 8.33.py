from MKT import *

axes = Axes(10, 'P/$P$', 'V/$V$', ltx=True, fontsize=32)

p1 = (2, '')
p2 = (8, '')
v1 = (1.5, '')
v2 = (6, '')
state1 = State(axes, p=p1, v=v1, xtick=False, ytick=False, patch='$1$', patch_pos='BR')
state2 = State(axes, p=p2, v=v2, xtick=False, ytick=False, patch='$2$', patch_pos='R')

axes.process(state1, state2)

axes.marker(state1, ms=7)
axes.marker(state2, ms=7)

axes.line(state1, '0')

#savefig('8.33.pdf')
show()
