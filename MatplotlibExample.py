import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

def setup(layout=None):
    assert layout is not None
    
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(layout)
    return fig, ax

def get_signal():
    t = np.arange(0,2.5,.01)
    s = np.sin(5*np.pi*t)
    return t,s

def plot_signal(t,s):
    line, = axes.plot(t,s,linewidth=5,color='magenta')
    return line

def make_shadow(fig,axes,line,t,s):
    delta = 2/72 # number of points to move the shadow away
    offset= transforms.ScaledTranslation(delta,-delta,
                                         fig.dpi_scale_trans)
    # Deltas : 
    # 1st delta moves shadow left (negative) or right(positive)
    # 2nd delta moves shadow up (positive) or down (negative)
    offset_transform = axes.transData + offset
    # We plot the same data, but now using offset transform
    # zorder  -- to render it below the line
    axes.plot(t,s, linewidth = 5, color = 'gray',
             transform = offset_transform,
             zorder =.5 * line.get_zorder())
    
    
if __name__ =="__main__":
    fig,axes = setup(111)
    t, s =get_signal()
    line = plot_signal(t,s)
    make_shadow(fig,axes,line,t,s)
    axes.set_title('Shadow effect using an offset transform')
    plt.show()
    
    