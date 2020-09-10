import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import *


class Plotter:
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    
    experiment_name = ''

    grid = False

    def the_function(self, mul):
        return 3 * np.pi * np.e ** (-5 * np.sin(2 * np.pi * mul * self.t))

    def toggle_grid(self, event):
        self.grid = not self.grid
        print('grid', self.grid)
        self.ax.grid(self.grid)

    def save_csv(self, event):
        print(self.experiment_name+'.csv')
        pass

    def set_exp_name(self, val):
        self.experiment_name = val
        print('Changed name to', val)
    
    bounds = [0, 1]
    def zoom_lb(self, val):
        self.bounds[0] = val
        self.ax.set_xlim(self.bounds)
    
    def zoom_ub(self, val):
        self.bounds[1] = val
        self.ax.set_xlim(self.bounds)

    gui_objects = []

    data = []

    def receive_data(self, index, point):
        # plt.figure(1)
        self.ax.plot(index, point, 'ob-')
        plt.pause(0.05)

    def draw_gui(self):
        grid_btn = Button(plt.axes([0.7, 0.05, 0.15, 0.075]), 'Toggle Grid')
        grid_btn.on_clicked(self.toggle_grid)
        self.gui_objects.append(grid_btn)
        
        sfreq_b = Slider(plt.axes([0.25, 0.1, 0.2, 0.03]), 'LowerBound', 0.01, 5.0, valinit=0, valstep=0.1)
        sfreq_b.on_changed(self.zoom_lb)
        self.gui_objects.append(sfreq_b)
        
        sfreq_u = Slider(plt.axes([0.25, 0.05, 0.2, 0.03]), 'UpperBound', 0.01, 5.0, valinit=1, valstep=0.1)
        sfreq_u.on_changed(self.zoom_ub)
        self.gui_objects.append(sfreq_u)

        text_box = TextBox(plt.axes([0.3, 0.9, 0.45, 0.075]), 'Experiment name', initial=self.experiment_name)
        text_box.on_submit(self.set_exp_name)
        self.gui_objects.append(text_box)

        save_btn = Button(plt.axes([0.75, 0.9, 0.15, 0.075]), 'Save')
        save_btn.on_clicked(self.save_csv)
        self.gui_objects.append(save_btn)


    def init(self):
        self.t = np.arange(0.0, 1.0, 0.001)
        self.s = self.the_function(1)
        self.l, = plt.plot(self.t, self.s, lw=2)
        plt.ion()
        plt.show()
        plt.autoscale()
        self.draw_gui()



p = Plotter()
p.init()
for i in range(1000):
    p.receive_data(i/100.0, 3 * np.pi * np.e ** (-5 * np.sin(2 * np.pi * 1 * i/100.0)))
input()

