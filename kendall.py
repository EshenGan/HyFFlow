import tkinter as tk
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_pdf import PdfPages
from tkinter import filedialog




def kendallshow(result):
    ax = plt.subplot()
    ax.axis('off')
    ax.set_title('Man-Kendall Test')
    
    table = ax.table(cellText = result.values, colLabels = result.columns, loc = 'center')
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(1.2,2.5)
    