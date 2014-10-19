# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# IPython-fu: el camino de la "nbconversión".

# <markdowncell>

# <i class="icon-user icon-2x"><strong> [Damián Avila](http://www.damian.oquanta.info)</strong></i>
# 
# <i class="icon-twitter icon-2x"><strong> [@damian_avila](http://twitter.com/damian_avila)</strong></i>
# 
# <i class="icon-github icon-2x"><strong> [damianavila](https://github.com/damianavila)</strong></i>
# 
# <i class="icon-envelope-alt icon-2x"><strong> <a href="mailto:info@oquanta.info">info@oquanta.info</a></strong></i>

# <markdowncell>

# ## CHARLA:
# 
# ## [http://goo.gl/lwQtB0](http://goo.gl/lwQtB0)

# <headingcell level=2>

# 1. El notebook the IPython. 

# <markdowncell>

# <img src="figs/logo.png" />

# <markdowncell>

# ## [http://ipython.org/](http://ipython.org/)

# <headingcell level=3>

# ¿Qué es el  notebook the IPython?

# <markdowncell>

# >The goal of IPython is to create a comprehensive environment for interactive and exploratory computing.

# <markdowncell>

# Una herramienta para contar **historias**:
# 
# * metodologías
# * procedimientos
# * análisis

# <markdowncell>

# Técnicamente es una documento basado de JSON:

# <codecell>

from IPython.nbformat import current
with open('IPython_fu_talk.ipynb') as f:
    nb = current.read(f,'json')
    
nb.worksheets[0].cells[15:20]

# <markdowncell>

# * Genera archivos con la extensión `.ipynb` que se guardan en el directorio local.
# * En el notebook podemos almacenar:
#     * Código
#     * Texto (Markdown)
#     * Equaciones (LaTeX)
#     * Imágenes
#     * Videos
#     * HTML
# * Puede ser controlado por versiones.
# * Puede verse sin tener IPython instalado usando NBViewer: http://nbviewer.ipython.org/.
# * Puede ser exportado a otros formatos: Slides, HTML, Markdown, reStructured Text, LaTeX y PDF.

# <headingcell level=3>

# ¿Cuáles son sus características principales?

# <markdowncell>

# * Interactivo

# <markdowncell>

# * Exploratorio

# <markdowncell>

# * Colaborativo

# <markdowncell>

# * Abierto

# <headingcell level=2>

# 2. Instalando el notebook de IPython.

# <markdowncell>

# **¿Qué necesito para hacerlo andar?**
# 
# * Tornado
# * ZeroMQ/PyZMQ
# * Jinja2
# * Chrome, Firefox, Safari (WebSockets, Flexible Box Model)
# * Matplotlib para hacer figuras
# * En linux, mac `pip install ipython[all]` o desde el `source` en **github**.
# * Instalación fácil (incluyendo instaladores para win): Canopy, Anaconda, Python XY, WinPython, Pyzo
# * Online: Wakari

# <markdowncell>

# **¿Cómo lo hago andar?**
# 
# * `cd` en el directorio conteniendo los archivos `ipynb` y simplemente tipeamos:
# 
# ```
# (ipython_dev)damian@damian-Inspiron-1110:~$ ipython notebook
# 
# 2013-05-10 12:11:26.912 [NotebookApp] Using existing profile dir: u'/home/damian/.config/ipython/profile_default'
# 2013-05-10 12:11:26.937 [NotebookApp] Using MathJax from CDN: http://cdn.mathjax.org/mathjax/latest/MathJax.js
# 2013-05-10 12:11:26.984 [NotebookApp] The port 8888 is already in use, trying another random port.
# 2013-05-10 12:11:26.985 [NotebookApp] Serving notebooks from local directory: /home/damian
# 2013-05-10 12:11:26.985 [NotebookApp] The IPython Notebook is running at: http://127.0.0.1:8888/
# 2013-05-10 12:11:26.986 [NotebookApp] Use Control-C to stop this server and shut down all kernels.
# Se ha abierto una nueva ventana en la sesión actual del navegador.
# ```

# <headingcell level=3>

# Interfase de usuario.

# <markdowncell>

# * Dashboard
# * Menu
# * Barra de herramientas
# * Área del notebook y celdas

# <headingcell level=3>

# Tipo de celdas

# <markdowncell>

# * Code
# * Markdown
# * Raw text
# * Heading

# <headingcell level=3>

# "Shortcuts" del teclado

# <markdowncell>

# * `Shift-Enter` para ejecutar una celda
# * `Ctrl-Enter` para ejecutar una celda y *quedarse* en esa misma celda.
# * `Alt-Enter` para ejecutar una celda e insertar una nueva celda por debajo de la *ejecutada*.
# * Todas las otras "shortcuts" tienen la forma: `Ctrl-m ?`
# * Si querés ver las "shortcuts" disponibles: `Ctrl-m h`

# <headingcell level=2>

# 3. Usando el notebook de IPython.

# <headingcell level=3>

# Trabajar con códido y correrlo:

# <markdowncell>

# El clásico `hola mundo`:

# <codecell>

print "Hola PyConAr 2013"

# <markdowncell>

# La representación de los objetos es más legible:

# <codecell>

from numpy.random import randn
data = {i : randn() for i in range(7)}
data

# <markdowncell>

# y contrasten contra la siguiente representación:

# <codecell>

>>> from numpy.random import randn
>>> data = {i : randn() for i in range(7)}
>>> print data # pequeña trampa para verlo como se vería en consola

# <markdowncell>

# Puedo probar "pedacitos" de código (por ejemplo de tutoriales):

# <codecell>

>>> the_world_is_flat = 1
>>> if the_world_is_flat:
...     print "Be careful not to fall off!"

# <codecell>

In [5]: [x*x for x in range(5)]

# <markdowncell>

# Puedo ver los errores o *tracebacks* de una manera simple y visualmente informativa:

# <codecell>

%run non_existent_file

# <codecell>

x = 1
y = 4
z = y/(1-x)

# <markdowncell>

# Otras ventajas a la hora de trabajar con código:
# 
# * Completado por Tab

# <codecell>

import scipy as sp

# <codecell>

sp.

# <markdowncell>

# * Ayuda integrada

# <codecell>

?

# <codecell>

def suma(a, b):
    """
    Demo de una función que suma cosas...
    """
    return a + b

# <codecell>

suma?

# <codecell>

suma??

# <markdowncell>

# * "Atajos" interactivos (aliases, magics)

# <codecell>

%magic

# <codecell>

%lsmagic

# <codecell>

%quickref

# <markdowncell>

# Pero tambien tenemos *cell magics* (`%%`) a través de las cuales el notebook soporta correr código en otros lenguajes (entre otras tareas:
# 
# * R
# * Octave
# * Cython
# * Bash
# * Perl
# * Ruby
# * etc.

# <markdowncell>

# y combinando *magics* las tareas son muy simples:

# <codecell>

%%bash
mkdir temporal/
touch temporal/mi_programa.py
cat temporal/mi_programa.py

# <codecell>

%%writefile temporal/mi_programa.py
def mi_funcion(x, y):
    """
    Demo
    """
    return x / y

x = 4
y = 2

resultado = mi_funcion(x, y)

# <codecell>

%run temporal/mi_programa.py

# <codecell>

resultado

# <markdowncell>

# Puedo interaccionar fácilmente con el sistema operativo:

# <codecell>

!pwd

# <codecell>

files = !ls
print "My current directory's files:"
print files

# <codecell>

!echo $files

# <codecell>

!echo {files[0].upper()}

# <markdowncell>

# Por ejemplo, puedo generar figuras programáticamente utilizando matplotlib:

# <codecell>

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3*np.pi, 500)
y = np.sin(x**2)

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('sin x^2')
axes.set_title('Una figura simple');

# <headingcell level=3>

# Documentar el flujo de trabajo.

# <markdowncell>

# El texto reendea vía `Markdown`, por ejemplo puedo tener *italica*, **enfásis** o linkear a [google](http://www.google.com).
# 
# Puedo hacer listas:
# 
# 1. primero
# 2. segundo
# 3. tercero
# 
# 
# * auto
# * biblicleta
# * moto

# <markdowncell>

# Puedo embeber código para demostración, por ejemplo, para Python:
# 
#     def f(x):
#         """a docstring"""
#         return x**2
# 
# o para otros lenguajes:
# 
#     if (i=0; i<n; i++) {
#       printf("hello %d\n", i);
#       x += 4;
#     }

# <markdowncell>

# Gracias a MathJax, se pueden incluir expresiones matemáticas `inline`: 
# $e^{i\pi} + 1 = 0$  o en `bloque`:
# 
# $$e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i$$

# <headingcell level=3>

# Si el navegador puede mostrarlo...

# <codecell>

from IPython.display import display

# <markdowncell>

# * Imágenes:

# <codecell>

from IPython.display import Image
Image(filename='pyconar2013_talks/figs/logo.png')

# <codecell>

from IPython.display import SVG
SVG(filename='pyconar2013_talks/figs/python-logo.svg')

# <markdowncell>

# * Video:

# <markdowncell>

# Puedo cargar y mostrar videos de Youtube, Vimeo, etc...

# <codecell>

from IPython.display import YouTubeVideo
YouTubeVideo('MIAKOMzRl1I')

# <markdowncell>

# * HTML

# <codecell>

from IPython.display import HTML

s = """<table>
<tr>
<th>Header 1</th>
<th>Header 2</th>
</tr>
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>"""

# <codecell>

h = HTML(s)
display(h)

# <markdowncell>

# * Sitios web:

# <codecell>

from IPython.display import IFrame
IFrame('http://www.damian.oquanta.info',1024,768)

# <markdowncell>

# * Música:

# <codecell>

%load soln/soundcloud.py

from IPython.display import HTML
h = HTML("""<iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F94543639"></iframe>""")
display(h)

# <markdowncell>

# * Javascript

# <codecell>

from IPython.display import Javascript

# fetch d3 from cloudflare
Javascript("""$.getScript('//cdnjs.cloudflare.com/ajax/libs/d3/3.2.2/d3.v3.min.js')""")

# <codecell>

%%html
<style type="text/css">

circle {
  fill: rgb(31, 119, 180);
  fill-opacity: .25;
  stroke: rgb(31, 119, 180);
  stroke-width: 1px;
}

.leaf circle {
  fill: #ff7f0e;
  fill-opacity: 1;
}

text {
  font: 10px sans-serif;
}

</style>

# <codecell>

%%javascript

// This unhides the output area
container.show();

// element is the jQuery element we will append to
var e = element.get(0);
    
var diameter = 600,
    format = d3.format(",d");

var pack = d3.layout.pack()
    .size([diameter - 4, diameter - 4])
    .value(function(d) { return d.size; });

var svg = d3.select(e).append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
  .append("g")
    .attr("transform", "translate(2,2)");

d3.json("files/flare.json", function(error, root) {
  var node = svg.datum(root).selectAll(".node")
      .data(pack.nodes)
    .enter().append("g")
      .attr("class", function(d) { return d.children ? "node" : "leaf node"; })
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  node.append("title")
      .text(function(d) { return d.name + (d.children ? "" : ": " + format(d.size)); });

  node.append("circle")
      .attr("r", function(d) { return d.r; });

  node.filter(function(d) { return !d.children; }).append("text")
      .attr("dy", ".3em")
      .style("text-anchor", "middle")
      .text(function(d) { return d.name.substring(0, d.r / 3); });
});

d3.select(self.frameElement).style("height", diameter + "px");

# <headingcell level=3>

# Cargar código remoto

# <codecell>

%load http://matplotlib.sourceforge.net/mpl_examples/api/collections_demo.py

# <codecell>

#!/usr/bin/env python
'''Demonstration of LineCollection, PolyCollection, and
RegularPolyCollection with autoscaling.

For the first two subplots, we will use spirals.  Their
size will be set in plot units, not data units.  Their positions
will be set in data units by using the "offsets" and "transOffset"
kwargs of the LineCollection and PolyCollection.

The third subplot will make regular polygons, with the same
type of scaling and positioning as in the first two.

The last subplot illustrates the use of "offsets=(xo,yo)",
that is, a single tuple instead of a list of tuples, to generate
successively offset curves, with the offset given in data
units.  This behavior is available only for the LineCollection.

'''

import matplotlib.pyplot as plt
from matplotlib import collections, transforms
from matplotlib.colors import colorConverter
import numpy as np

nverts = 50
npts = 100

# Make some spirals
r = np.array(range(nverts))
theta = np.array(range(nverts)) * (2*np.pi)/(nverts-1)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = list(zip(xx,yy))

# Make some offsets
rs = np.random.RandomState([12345678])
xo = rs.randn(npts)
yo = rs.randn(npts)
xyo = list(zip(xo, yo))

# Make a list of colors cycling through the rgbcmyk series.
colors = [colorConverter.to_rgba(c) for c in ('r','g','b','c','y','m','k')]

fig, axes = plt.subplots(2,2)
((ax1, ax2), (ax3, ax4)) = axes # unpack the axes


col = collections.LineCollection([spiral], offsets=xyo,
                                transOffset=ax1.transData)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans)  # the points to pixels transform
    # Note: the first argument to the collection initializer
    # must be a list of sequences of x,y tuples; we have only
    # one sequence, but we still have to put it in a list.
ax1.add_collection(col, autolim=True)
    # autolim=True enables autoscaling.  For collections with
    # offsets like this, it is neither efficient nor accurate,
    # but it is good enough to generate a plot that you can use
    # as a starting point.  If you know beforehand the range of
    # x and y that you want to show, it is better to set them
    # explicitly, leave out the autolim kwarg (or set it to False),
    # and omit the 'ax1.autoscale_view()' call below.

# Make a transform for the line segments such that their size is
# given in points:
col.set_color(colors)

ax1.autoscale_view()  # See comment above, after ax1.add_collection.
ax1.set_title('LineCollection using offsets')


# The same data as above, but fill the curves.
col = collections.PolyCollection([spiral], offsets=xyo,
                                transOffset=ax2.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)  # the points to pixels transform
ax2.add_collection(col, autolim=True)
col.set_color(colors)


ax2.autoscale_view()
ax2.set_title('PolyCollection using offsets')

# 7-sided regular polygons

col = collections.RegularPolyCollection(7,
                                        sizes = np.fabs(xx)*10.0, offsets=xyo,
                                        transOffset=ax3.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)  # the points to pixels transform
ax3.add_collection(col, autolim=True)
col.set_color(colors)
ax3.autoscale_view()
ax3.set_title('RegularPolyCollection using offsets')


# Simulate a series of ocean current profiles, successively
# offset by 0.1 m/s so that they form what is sometimes called
# a "waterfall" plot or a "stagger" plot.

nverts = 60
ncurves = 20
offs = (0.1, 0.0)

yy = np.linspace(0, 2*np.pi, nverts)
ym = np.amax(yy)
xx = (0.2 + (ym-yy)/ym)**2 * np.cos(yy-0.4) * 0.5
segs = []
for i in range(ncurves):
    xxx = xx + 0.02*rs.randn(nverts)
    curve = list(zip(xxx, yy*100))
    segs.append(curve)

col = collections.LineCollection(segs, offsets=offs)
ax4.add_collection(col, autolim=True)
col.set_color(colors)
ax4.autoscale_view()
ax4.set_title('Successive data offsets')
ax4.set_xlabel('Zonal velocity component (m/s)')
ax4.set_ylabel('Depth (m)')
# Reverse the y-axis so depth increases downward
ax4.set_ylim(ax4.get_ylim()[::-1])


plt.show()



# <codecell>

#!/usr/bin/env python
'''Demonstration of LineCollection, PolyCollection, and
RegularPolyCollection with autoscaling.

For the first two subplots, we will use spirals.  Their
size will be set in plot units, not data units.  Their positions
will be set in data units by using the "offsets" and "transOffset"
kwargs of the LineCollection and PolyCollection.

The third subplot will make regular polygons, with the same
type of scaling and positioning as in the first two.

The last subplot illustrates the use of "offsets=(xo,yo)",
that is, a single tuple instead of a list of tuples, to generate
successively offset curves, with the offset given in data
units.  This behavior is available only for the LineCollection.

'''

import matplotlib.pyplot as plt
from matplotlib import collections, transforms
from matplotlib.colors import colorConverter
import numpy as np

nverts = 50
npts = 100

# Make some spirals
r = np.array(range(nverts))
theta = np.array(range(nverts)) * (2*np.pi)/(nverts-1)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = list(zip(xx,yy))

# Make some offsets
rs = np.random.RandomState([12345678])
xo = rs.randn(npts)
yo = rs.randn(npts)
xyo = list(zip(xo, yo))

# Make a list of colors cycling through the rgbcmyk series.
colors = [colorConverter.to_rgba(c) for c in ('r','g','b','c','y','m','k')]

fig, axes = plt.subplots(2,2)
((ax1, ax2), (ax3, ax4)) = axes # unpack the axes


col = collections.LineCollection([spiral], offsets=xyo,
                                transOffset=ax1.transData)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans)  # the points to pixels transform
    # Note: the first argument to the collection initializer
    # must be a list of sequences of x,y tuples; we have only
    # one sequence, but we still have to put it in a list.
ax1.add_collection(col, autolim=True)
    # autolim=True enables autoscaling.  For collections with
    # offsets like this, it is neither efficient nor accurate,
    # but it is good enough to generate a plot that you can use
    # as a starting point.  If you know beforehand the range of
    # x and y that you want to show, it is better to set them
    # explicitly, leave out the autolim kwarg (or set it to False),
    # and omit the 'ax1.autoscale_view()' call below.

# Make a transform for the line segments such that their size is
# given in points:
col.set_color(colors)

ax1.autoscale_view()  # See comment above, after ax1.add_collection.
ax1.set_title('LineCollection using offsets')


# The same data as above, but fill the curves.
col = collections.PolyCollection([spiral], offsets=xyo,
                                transOffset=ax2.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)  # the points to pixels transform
ax2.add_collection(col, autolim=True)
col.set_color(colors)


ax2.autoscale_view()
ax2.set_title('PolyCollection using offsets')

# 7-sided regular polygons

col = collections.RegularPolyCollection(7,
                                        sizes = np.fabs(xx)*10.0, offsets=xyo,
                                        transOffset=ax3.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)  # the points to pixels transform
ax3.add_collection(col, autolim=True)
col.set_color(colors)
ax3.autoscale_view()
ax3.set_title('RegularPolyCollection using offsets')


# Simulate a series of ocean current profiles, successively
# offset by 0.1 m/s so that they form what is sometimes called
# a "waterfall" plot or a "stagger" plot.

nverts = 60
ncurves = 20
offs = (0.1, 0.0)

yy = np.linspace(0, 2*np.pi, nverts)
ym = np.amax(yy)
xx = (0.2 + (ym-yy)/ym)**2 * np.cos(yy-0.4) * 0.5
segs = []
for i in range(ncurves):
    xxx = xx + 0.02*rs.randn(nverts)
    curve = list(zip(xxx, yy*100))
    segs.append(curve)

col = collections.LineCollection(segs, offsets=offs)
ax4.add_collection(col, autolim=True)
col.set_color(colors)
ax4.autoscale_view()
ax4.set_title('Successive data offsets')
ax4.set_xlabel('Zonal velocity component (m/s)')
ax4.set_ylabel('Depth (m)')
# Reverse the y-axis so depth increases downward
ax4.set_ylim(ax4.get_ylim()[::-1])


plt.show()



# <headingcell level=3>

# Reendeo de LaTeX:

# <codecell>

from IPython.display import Latex
Latex(r"""\begin{eqnarray}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, 
\frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\
\nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, 
\frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} & = 0 
\end{eqnarray}""")

# <headingcell level=3>

# Pandas

# <codecell>

import pandas
pandas.set_option('display.notebook_repr_html', True)

# <codecell>

%%writefile data.csv
Date,Open,High,Low,Close,Volume,Adj Close
2012-06-01,569.16,590.00,548.50,584.00,14077000,581.50
2012-05-01,584.90,596.76,522.18,577.73,18827900,575.26
2012-04-02,601.83,644.00,555.00,583.98,28759100,581.48
2012-03-01,548.17,621.45,516.22,599.55,26486000,596.99
2012-02-01,458.41,547.61,453.98,542.44,22001000,540.12
2012-01-03,409.40,458.24,409.00,456.48,12949100,454.53

# <codecell>

df = pandas.read_csv('data.csv')
df

# <headingcell level=3>

# The IPython kernel/client model

# <codecell>

%connect_info

# <codecell>

%qtconsole

# <headingcell level=2>

# 4. `nbconvert`

# <headingcell level=3>

# Intro...

# <markdowncell>

# * `NBConvert` es una biblioteca de *reciente* (`tech preview`) incorporación al núcleo de IPython, y que permite la *nbconversión* de los notebooks de IPython a otros formatos tales como: `html`, `latex`, `markdown`, `python`, `rst` y  `slides`.
# 
# * Esta biblioteca esta basada en el sistema de `templates` de Jinja, por lo que modificar los nbconversores (o escribir el propio) no debería generar mayores dificultades.

# <markdowncell>

# Para utilizarlo desde la linea de comandos:
# 
# `$ ipython nbconvert <optiones y argumentos>`
# 
# y para solicitar ayuda: 
# 
# `$ ipython nbconvert --help` (y si querés más detalle: `--help-all`).

# <codecell>

%%bash
ipython nbconvert  IPython_fu_talk.ipynb --to html

# <headingcell level=3>

# Slides

# <markdowncell>

# Este nbconversor genera una presentacion HTML basada en la popular bibloteca Reveal.js
# 
# * Slides (horizontales).
# * Subslides (verticales).
# * Fragmentos.
# * Transiciones.
# * Temas.
# * Notas.
# * Exportacion a pdf.

# <codecell>

%%bash
ipython nbconvert IPython_fu_talk.ipynb --to slides

# <markdowncell>

# Más info: [http://www.damian.oquanta.info/categories/reveal.html](http://www.damian.oquanta.info/categories/reveal.html)

# <headingcell level=3>

# Usando la api de `nbconvert`... para bloguear con IPython y Nikola.

# <markdowncell>

# Podemos tomar como ejemplo el plugin `ipynb` presente en Nikola:
# 
# ```
# def compile_html(self, source, dest, is_two_file=True):
#         if flag is None:
#             req_missing(['ipython>=1.0.0'], 'build this site (compile ipynb)')
#         makedirs(os.path.dirname(dest))
#         HTMLExporter.default_template = 'basic'
#         c = Config(self.site.config['IPYNB_CONFIG'])
#         exportHtml = HTMLExporter(config=c)
#         with codecs.open(dest, "w+", "utf8") as out_file:
#             with codecs.open(source, "r", "utf8") as in_file:
#                 nb = in_file.read()
#                 nb_json = nbformat.reads_json(nb)
#             (body, resources) = exportHtml.from_notebook_node(nb_json)
#             out_file.write(body)
# ```            

# <markdowncell>

# <iframe src="http://www.damian.oquanta.info/posts/blogging-with-nikola-and-ipython.html" width="1024" height="768"></iframe>

# <headingcell level=2>

# 5. Discusión.

# <markdowncell>

# El notebook de IPython provee toda la infraestructura para:

# <markdowncell>

# 1- Obtener **datos**.

# <markdowncell>

# 2- **Procesar** los datos obtenidos.

# <markdowncell>

# 3- **Visualizar** los datos procesados

# <markdowncell>

# 4- **Elaborar** una **historia**  que se **sustenta** en los datos analizados.

# <markdowncell>

# 5- **Comunicar** dicha **historia** (junto con los **datos** y las **visualizaciones** obtenidas).

# <headingcell level=2>

# 6. El fututo del notebook the IPython

# <markdowncell>

# Para conocer en forma detallada lo lineamientos a futuro: 
# 
# [https://github.com/ipython/ipython/wiki/Roadmap:-IPython](https://github.com/ipython/ipython/wiki/Roadmap:-IPython)
# 
# * Soporte para multiusuarios
# * Soporte para múltiples directorios
# * Widgets interactivos (js)
# * Exportación mejorada de los notebook a otros formatos
# * Modo presentación
# 
# Y no se olviden de pasear por la galería de notebooks de IPython disponible en: 
# 
# [https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)

# <markdowncell>

# <i class="icon-thumbs-up icon-2x"><strong> [¡GRACIAS!](¡GRACIAS!)</strong></i>
# 
# <i class="icon-user icon-2x"><strong> [Damián Avila](http://www.damian.oquanta.info)</strong></i>
# 
# <i class="icon-twitter icon-2x"><strong> [@damian_avila](http://twitter.com/damian_avila)</strong></i>
# 
# <i class="icon-github icon-2x"><strong> [damianavila](https://github.com/damianavila)</strong></i>
# 
# <i class="icon-envelope-alt icon-2x"><strong> <a href="mailto:info@oquanta.info">info@oquanta.info</a></strong></i>

# <codecell>


