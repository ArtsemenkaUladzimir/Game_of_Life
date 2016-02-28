import matplotlib

matplotlib.use('TKAgg')
from matplotlib import pyplot as plt
from matplotlib import animation


def animate(game):
    fig = plt.figure()
    ax = plt.axes(xlim=(-1, game.config.width), ylim=(-1, game.config.height))
    plt.gca().invert_yaxis()
    line, = ax.plot([], [], 'g^')

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,

    # animation function.  This is called sequentially
    def animate(i):
        active = game.get_active()
        game.next_generation()
        line.set_data(active)
        return line,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=100, interval=200, blit=True)

    plt.show()
