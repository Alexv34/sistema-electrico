from typing import Literal
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from pylab import *


#interfaz

def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)

layout = [
    [sg.Text('Ingresa el valor de x'),sg.In(default_text='',size=(6,1), do_not_clear=True)],
    [sg.Text('Ingresa el valor de y'),sg.In(default_text='',size=(6,1), do_not_clear=True)],
    [sg.B('Graficar'), sg.B('Salir')],
    [sg.T('Controles:')],
    [sg.Canvas(key='controls_cv')],
    [sg.T('Grafico:')],
    [sg.Column(
        layout=[
            [sg.Canvas(key='fig_cv',
                       # Tamaño de interfaz
                       size=(600 , 400)
                       )]
        ],
        background_color='#DAE0E6',
        pad=(0, 0)
    )],
]



window = sg.Window('Cableado', layout)

#graficos

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Salir'):  # 
        break
    elif event is 'Graficar':
        # ------------------------------- Codigo de matplotlib
        plt.xlim(-1,10)
        plt.ylim(-1,10)
        plt.figure(1)
        fig = plt.gcf()
        DPI = fig.get_dpi()
        fig.set_size_inches(6, 4)
        x,y=np.linspace(0,10),np.linspace(0,10)
        # ------------------------------- marco cuadrado
        fig, ax = plt.subplots()
        ax.add_patch(
        patches.Rectangle(
            (0, 0),
            9,
            9,
            edgecolor = 'green',
            fill=False      
        ) )
        toma=(values[0],values[1])
        iluminacion=''
        y=0
        x=0
        plt.plot(toma,label='iluminacion',marker='*',linestyle='None',markersize=10)
        plt.plot(iluminacion,label='Toma corriente',marker='s',linestyle='None',markersize=10)
        plt.legend(loc="upper left")
        plt.plot(x, y,toma)
        plt.title('Cableado')
        plt.xlabel('X')
        plt.ylabel('Y')
        X,Y=np.meshgrid(x,y)
        # -------------------------------  controles
        draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)

window.close()