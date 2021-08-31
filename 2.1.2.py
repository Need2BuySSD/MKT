from MKT import *

axes = Axes(10, 'P/$p$', 'V/$V$', ltx=True, fontsize=32)

p1 = (4, '$p_1$')
p2 = (8, '1,5$p_1$')
v1 = (4, '')
v2 = (8, '')
state1 = State(axes, p=p1, v=v1, xtick=False)
state2 = State(axes, p=p2, v=v1, xtick=False)
state3 = State(axes, p=p2, v=v2, xtick=False)

axes.process(state1,state2, arrow=False)
axes.process(state2,state3, arrow=False)
axes.process(state3,state1, arrow=False)

axes.marker(state1, ms=7)
axes.marker(state2, ms=7)
axes.marker(state3, ms=7)

axes.line(state1, 'all')
axes.line(state2, 'xp')

#savefig('2.1.2.pdf')
show()