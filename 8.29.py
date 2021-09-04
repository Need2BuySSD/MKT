from MKT import *

axes = Axes(8, 'P/$P$', 'V/$V$', ltx=True, fontsize=32, yratio=0.8)

v1 = (1, '')
v2 = (5, '')
p1 = (4, '')
p2 = (3, '')

state1 = State(axes, v=v1, p=p1, xtick=False, ytick=False, patch='$1$', patch_pos='BL')
state2 = State(axes, v=v2, p=p2, xtick=False, ytick=False, patch='$2$', patch_pos='BB')

axes.process(state1, state2)

axes.marker(state1, ms=7)
axes.marker(state2, ms=7)

axes.grid()

#savefig('8.29.pdf')
show()
