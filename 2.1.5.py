from MKT import *

axes = Axes(10, 'P/$p$', 'V/$V$', ltx=True, yratio=0.5, null=True, fontsize=25)

p1 = (1, '')
p2 = (4.5, '')
v1 = (2, '')
v2 = (9, '')
state1 = State(axes, p=p1, v=v1, xtick=False, ytick=False, patch='$1$', patch_pos='BR')
state2 = State(axes, p=p2, v=v1, xtick=False, ytick=False, patch='$2$', patch_pos='T')
state3 = State(axes, p=p2, v=v2, xtick=False, ytick=False, patch='$3$', patch_pos='R')

axes.process(state1, state2, arrow=False)
axes.process(state2, state3, arrow=False)
axes.process(state3, state1, arrow=False)

axes.marker(state1, ms=7)
axes.marker(state2, ms=7)
axes.marker(state3, ms=7)

axes.line(state1, 'yp')
axes.line(state1, '0')
axes.line(state2, 'xp')

#savefig('2.1.5.pdf')
show()
