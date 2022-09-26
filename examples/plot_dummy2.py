# -*- coding: utf-8 -*-
"""
Plot dummy 2
============
Yes
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Animator1D(animation.TimedAnimation):
    def __init__(self, N=256):
        up = np.linspace(0, 1, N//2)
        self.amplitudes = np.hstack([up, up[::-1]])
        self.t = np.linspace(0, 1, N, 0)

        fig, ax = plt.subplots(1, 1)
        y0 = self.cos(self.amplitudes[len(self.amplitudes)//2])
        self.lines = [ax.plot(self.t, y0)[0]]

        animation.TimedAnimation.__init__(self, fig, blit=True)

    def cos(self, a):
        return a * np.cos(2*np.pi * 4 * self.t)

    def _draw_frame(self, frame_idx):
        self.lines[0].set_data(self.t, self.cos(self.amplitudes[frame_idx]))
        self._drawn_artists = [*self.lines]

    def new_frame_seq(self):
        return iter(range(len(self.amplitudes)))

    def _init_draw(self):
        pass


ani = Animator1D(128)
ani.save('yes.gif', fps=30, savefig_kwargs=dict(pad_inches=0),
          writer='ffmpeg')
plt.close()
