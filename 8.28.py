from MKT import *

axes = Axes(10, 'V/$V$', 'T/$T$', ltx=True, fontsize=32, yratio=0.7)

v1 = (3, '')
v2 = (5, '')
t1 = (2, '')
t2 = (7, '')
state1 = State(axes, v=v1, t=t1, xtick=False, ytick=False, patch='$1$', patch_pos='BB')
state2 = State(axes, v=v2, t=t2, xtick=False, ytick=False, patch='$2$', patch_pos='BR')

axes.process(state1, state2)

axes.marker(state1, ms=7)
axes.marker(state2, ms=7)


#savefig('8.28.pdf')
show()
