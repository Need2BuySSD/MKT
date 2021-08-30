import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams


class Axes():
    def __init__(self,length, y, x, linewidth=None, head_width=None, head_length=None, null=False, ltx=False, fontsize=18, equal_aspect=True, yratio=1):
        
        if linewidth is None:
            linewidth=length / 5
        if head_width is None:
            head_width=linewidth/8
        if head_length is None:
            head_length=linewidth/4
                
        if ltx:
            rc('text', usetex = True)
            rc('font', size = fontsize, family = 'serif')
            #rc('text.latex', preamble = r'\usepackage[utf8]{inputenc}')
            #rc('text.latex', preamble = r'\usepackage[english]{babel}')
        else:
            rc('text', usetex = False)
            rc('font', size = fontsize, family = 'serif')
        self.fig, self.surf = plt.subplots()
        if equal_aspect:
            self.surf.set_aspect('equal')
            
        if '/' in y:
            self.y = y.split('/')[0]
            self.y_tag = y.split('/')[1]
        else:
            self.y = y
            self.y_tag = y
        if '/' in x:
            self.x = x.split('/')[0]
            self.x_tag = x.split('/')[1]
        else:
            self.x = x
            self.x_tag = x
        self.length = length
        self.linewidth = linewidth
        self.yratio=yratio
        self.surf.axis('off')
        #self.surf.set_xlim([0, length])
        self.surf.set_ylim([-fontsize*0.04, length*yratio])
        self.surf.arrow(0, 0, 0, length*yratio, head_width=head_width, head_length=head_length, fc='k', lw=linewidth, clip_on=False)
        self.surf.arrow(0, 0, length, 0, head_width=head_width, head_length=head_length, fc='k', lw=linewidth, clip_on=False)
        self.surf.text(length, -linewidth/5, self.x_tag, ha='center', va='top', clip_on = False)
        self.surf.text(-linewidth/5, length*yratio, self.y_tag, ha='right', va='center', clip_on = False)
        if null:
            self.surf.text(-linewidth / 4, -linewidth / 4, '0', ha='center', clip_on=False)


    def process(self, state0, state1, lwmult=1, linestyle='-', arrow=True):
        linewidth = self.linewidth * lwmult        
        if self.x == 'P':
            x0 = state0.p[0]
            x1 = state1.p[0]
        elif self.x == 'V':
            x0 = state0.v[0]
            x1 = state1.v[0]
        elif self.x == 'T':
            x0 = state0.t[0]
            x1 = state1.t[0]
        if self.y == 'P':
            y0 = state0.p[0]
            y1 = state1.p[0]
        elif self.y == 'V':
            y0 = state0.v[0]
            y1 = state1.v[0]
        elif self.y == 'T':
            y0 = state0.t[0]
            y1 = state1.t[0]

        self.surf.plot((x0, x1), (y0, y1), str('k' + linestyle), linewidth = linewidth)
        if arrow:
            self.surf.arrow(x0, y0, (x1-x0)/2, (y1-y0)/2, fc='k', linewidth=linewidth, length_includes_head=False, head_width=linewidth/8, head_length=linewidth/8)
            
    def isothermal(self, state0, state1, lwmult=1, linestyle='-', arrow=True):
        linewidth = self.linewidth * lwmult          
        if state1 is not None:
            # X
            x0, y0 = state0.get_coords()
            x1, y1 = state1.get_coords()            
            if x0 > x1:
                rev = True
                x0, y0, x1, y1 = x1, y1, x0, y0
            # Y
            if x0 * y0 == x1 * y1:
                const = x0 * y0
                x = np.linspace(x0, x1)
                y = const / x
                self.surf.plot(x, y, color='black', linewidth=linewidth, linestyle=linestyle)
                if arrow:
                    if not rev:
                        x = ((x1 + x0) / 2 + (const/((y1 + y0) / 2))) / 2
                        self.surf.arrow(x, const/x, 0.00001, const/(x+0.00001)-const/x, fc='k', linewidth = linewidth, length_includes_head=False, head_width=linewidth/8, head_length=linewidth/8)
                    else:
                        x = ((x1 + x0) / 2 + (const/((y1 + y0) / 2))) / 2
                        self.surf.arrow(x, const/x, -0.00001, -(const/(x+0.00001)-const/x), fc='k', linewidth = linewidth, length_includes_head=False, head_width=linewidth/8, head_length=linewidth/8)                        
            else:
                raise RuntimeError('PV is not const')
        else:
            x0, y0 = state0.get_coords()
            const = x0 * y0
            x = np.linspace(const / (self.length * self.yratio)+0.01, self.length*0.99)
            y = const / x
            self.surf.plot(x, y, color='black', linewidth=linewidth, linestyle=linestyle)
            if arrow:
                x = x0
                self.surf.arrow(x, const/x, 0.00001, const/(x+0.00001)-const/x, fc='k', linewidth = linewidth, length_includes_head=False, head_width=linewidth / 4)

    def adiabatic(self, state0, state1, lwmult=1, linestyle='-', arrow=True): #NE RABOTAET
        linewidth = self.linewidth * lwmult
        if state1 is not None:
            x0, y0 = state0.get_coords()
            x1, y1 = state1.get_coords()
            if self.x == 'P' and not self.y == 'V':
                x0, y0, x1, y1 = y0, x0, y1, x1
            if x0 > x1:
                x0, y0, x1, y1 = x1, y1, x0, y0
            if state0.v is not None and \
               state0.p is not None and \
               state1.p is not None and \
               state1.p is not None:
                const = state0.p[0] * state0.v[0] ** (5/3) 
            else:
                raise RuntimeError('P or V is not defined')            
            x = np.linspace(x0, x1)
            y = const / (x)**5/3
            self.surf.plot(x, y, color='black', linewidth=linewidth, linestyle=linestyle)
            #if arrow:
            #    x = ((x1 + x0) / 2 + (const/((y1 + y0) / 2))) / 2
            #    axes.surf.arrow(x, const/x, 0.00001, const/(x+0.00001)-const/x, fc='k', linewidth = linewidth, length_includes_head=False, head_width=linewidth / 4)
        else:
            x0, y0 = state0.get_coords()
            if self.x == 'P' and not self.y == 'V':
                x0, y0 = y0, x0            
            if state0.v is not None and \
               state0.p is not None:
                const = (state0.p[0] * state0.v[0])**(5/3) 
            else:            
                raise RuntimeError('PV^Y is not defined')   
            x = np.linspace(0.01, self.length*0.99)
            y = const / (x)**5/3
            self.surf.plot(x, y, color='black', linewidth=linewidth, linestyle=linestyle) #A DALSHE RABOTAET

    def marker(self, state, ms=5):
        x, y = state.get_coords()
        self.surf.plot(x, y, '.', color = 'black', markersize=ms)

    def line(self, state, tp='0', linestyle='--'):
        x1, y1 = state.get_coords()
        if tp=='all':
            self.line(state, tp='0', linestyle='--')
            self.line(state, tp='xp', linestyle='--')
            self.line(state, tp='yp', linestyle='--')
        else:
            if str(tp) == '0':
                x0, y0 = 0, 0
            elif tp == 'xp':
                x0, y0 = 0, y1
            elif tp == 'yp':
                x0, y0 = x1, 0
            self.surf.plot((x0, x1), (y0, y1), 'k'+linestyle, linewidth = self.linewidth * 0.8)
    def lines(self, states, tp='0', linestyle='--'):
        for state in states:
            self.line(state, tp=tp, linestyle='--')
            
    def grid(self, step=1,  lwmult=0.25, linestyle='-'):
        linewidth = self.linewidth*lwmult
        for x in range(0, self.length+step, step):
            self.surf.plot((x, x), (0, int(self.length*self.yratio)), str('k' + linestyle), linewidth = linewidth)
        for y in range(0, int(self.length*self.yratio)+step, step):
            self.surf.plot((0, self.length), (y, y), str('k' + linestyle), linewidth = linewidth)

class State():
    def __init__(self, axes, p=None, v=None, t=None, patch=None, patch_pos='T', xtick=True, ytick=True):
        self.axes = axes
        linewidth = axes.linewidth
        tb = axes.length/20
        x = 0
        y = 0
        k = 1
        if p is None:
            self.v = (k * v[0], v[1])
            self.t = (k * t[0], t[1])
            self.p = (None, None)
        elif v is None:
            self.p = (k * p[0], p[1])
            self.t = (k * t[0], t[1])
            self.v = (None, None)
        elif t is None:
            self.p = (k * p[0], p[1])
            self.v = (k * v[0], v[1])
            self.t = (None, None)
        else:
            self.p = (k * p[0], [1])
            self.v = (k * v[0], v[1])
            self.t = (k * t[0], t[1])
            
        if xtick:
            axes.surf.text(self.get_coords()[0], -tb, self.get_patches()[0], ha='center', va='top', clip_on=False)
            axes.surf.plot((self.get_coords()[0], self.get_coords()[0]), (-tb / 3, tb / 3), 'k-', linewidth=linewidth, clip_on=False)
        if ytick:
            axes.surf.text(-tb, self.get_coords()[1], self.get_patches()[1], ha='right', va='center', clip_on=False)
            axes.surf.plot((-tb / 3, tb / 3), (self.get_coords()[1], self.get_coords()[1]), 'k-', linewidth=linewidth, clip_on=False)
        if patch is not None:
            x, y = self.get_coords()
            for pos in patch_pos:
                if 'T' in pos:
                    y += tb
                if 'B' in pos:
                    y -= tb
                if 'L' in pos:
                    x -= tb
                if 'R' in pos:
                    x += tb
            axes.surf.text(x, y, patch, ha='center', va='center', clip_on=False)

    def get_coords(self):
        # Y
        if self.axes.y == 'P':
            y = self.p[0]
        elif self.axes.y == 'V':
            y = self.v[0]
        elif self.axes.y == 'T':
            y = self.t[0]
        # X
        if self.axes.x == 'V':
            x = self.v[0]
        elif self.axes.x == 'P':
            x = self.p[0]
        elif self.axes.x == 'T':
            x = self.t[0]
        return (x, y)

    def get_patches(self):
        # Y
        if self.axes.y == 'P':
            patch_y = self.p[1]
        elif self.axes.y == 'V':
            patch_y = self.v[1]
        elif self.axes.y == 'T':
            patch_y = self.t[1]
        # X
        if self.axes.x == 'V':
            patch_x = self.v[1]
        elif self.axes.x == 'P':
            patch_x = self.p[1]
        elif self.axes.x == 'T':
            patch_x = self.t[1]
        return (patch_x, patch_y)


def show():
    plt.show()
def savefig(fname):
    plt.savefig(fname)
