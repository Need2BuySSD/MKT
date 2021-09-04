from MKT import *

axes = Axes(10, 'P/$P$', 'T/$T$', ltx=True, fontsize=32, yratio=0.7)

p1 = (3, '')
p2 = (5, '')
t1 = (2, '')
t2 = (7, '')
state1 = State(axes, p=p1, t=t1, xtick=False, ytick=False, patch='$1$', patch_pos='BB')
state2 = State(axes, p=p2, t=t2, xtick=False, ytick=False, patch='$2$', patch_pos='BR')

axes.process(state1, state2)

axes.marker(state1, ms=7)
axes.marker(state2, ms=7)


#savefig('8.27.pdf')
show()
