# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Example IPython slideshow
# ==========================
# Melissa Gymrek
# --------------
# 01/13/14

# <markdowncell>

# Here's an example formatted table
# =========================

# <codecell>

from ipywidgets import *
import pandas as pd
from prettytable import PrettyTable
from reportlab.platypus.tables import TableStyle

df = pd.DataFrame({"x":[1,2,3], "y":[6,4,3], "z":["testing","pretty","tables"], "f":[0.023432, 0.234321,0.5555]})
pt = PrettyTable(df, tstyle=TableStyle(theme="theme1"), center=True)
cs = CellStyle()
cs.set("background-color", "pink")
cs.set("color", "purple")
pt.set_cell_style(style=cs)
pt.update_cell_style(cols=[0], format_function=lambda x: "%.3f"%x)
pt

# <markdowncell>

# Try clicking on the table to see the code!

# <markdowncell>

# Example build table
# ===================
# 
# Right click on the table to see the animation. Left click to see the code. Click "a" and "r" to (a)dvnce and (r)everse through the animation.

# <codecell>

pt = PrettyTable(df, tstyle=TableStyle(theme="theme1"), center=True)

def f1(pt):
    pt.update_cell_style(rows=[1], cols=[1], color="red", background_color="white")
    
def f2(pt):
    pt.update_cell_style(rows=[0], font_weight="bold")
StaticBuildTable(pt, [f1, f2], rightclick=True, center=True)

# <markdowncell>

# Example build figure
# ======================
# Right click on the figure to see the animation. Left click to see the code. Click "a" and "r" to (a)dvnce and (r)everse through the animation.

# <codecell>

def init(ax):
    ax.set_xlim(left=0, right=1)
    ax.set_ylim(bottom=0, top=1)
    
def f1(ax):
    ax.axhline(y=0.5, color="red")
    
def f2(ax):
    ax.axvline(x=0.5, color="purple")
    
def f3(ax):
    ax.plot([0,1],[0,1], color="blue")
StaticBuildFigure([f1,f2,f3], apply_to_all=init, center=True, rightclick=True)

