# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import HTML
from IPython.display import Image

# <markdowncell>

# MACROS FOR LATEX:
# \newcommand\der[2]{\frac{d{#1}}{d{#2}}}
# \newcommand\dder[2]{\frac{d^2{#1}}{d{#2}^2}}
# \newcommand\ddder[2]{\frac{d^3{#1}}{d{#2}^3}}
# \newcommand\pder[2]{\frac{\partial #1}{\partial #2}}
# \newcommand\ppder[2]{\frac{\partial^2 #1}{\partial #2^2}}
# \newcommand\pnder[3]{\frac{\partial^{#3} #1}{\partial #2^{#3}}}
# \newcommand\der[2]{\frac{d{#1}}{d{#2}}}
# \newcommand\dder[2]{\frac{d^2{#1}}{d{#2}^2}}
# \newcommand\ddder[2]{\frac{d^3{#1}}{d{#2}^3}}
# \newcommand\pder[2]{\frac{\partial #1}{\partial #2}}
# \newcommand\ppder[2]{\frac{\partial^2 #1}{\partial #2^2}}
# \newcommand\pnder[3]{\frac{\partial^{#3} #1}{\partial #2^{#3}}}
# \newcommand\pdder[3]{\frac{\partial^2 #1}{\partial #2 \partial #3}}
# \newcommand\pddder[4]{\frac{\partial^3 #1}{\partial #2 \partial #3 \partial #4}}
# \let\truesum=\sum
# \def\sum{\mathop{\textstyle\truesum}\limits}
# 
# \def\Re#1{\mathrm{Re}\hspace{-0.03in}\left[#1\right]}
# \def\Im#1{\mathrm{Im}\hspace{-0.03in}\left[#1\right]}
# \def\bigOh#1{O\hspace{-0.03in}\left(#1\right)}
# \def\littelOh#1{o\hspace{-0.03in}\left(#1\right)}
# \def\conj#1{\bar{#1}}
# 
# 
# \newcommand{\intl}[4]{\int_{#3}^{#4} #1 \, d #2}
# \def\Del#1{\Delta(#1)}
# \def\del#1{\delta\hspace{-0.03in}\left(#1 \right)}
# \def\Int#1#2{\left[\int #1 \, d#2\right]}
# \def\iint{\int \int}
# \def\dmin#1#2{\displaystyle{\min_{#1}}\hspace{-0.03in}\left(#2 \right)}
# \def\dmax#1#2{\displaystyle{\max_{#1}}\hspace{-0.03in}\left(#2 \right)}
# \def\dargmin#1#2{\displaystyle{{\mathrm{argmin}}_{#1}}\hspace{-0.03in}\left(#2 \right)}
# \def\dargmax#1#2{\displaystyle{{\mathrm{argmax}}_{#1}}\hspace{-0.03in}\left(#2 \right)}
# \def\vect#1{\mathbf{#1}}
# \def\gvect#1{\boldsymbol{#1}}
# \def\ip#1#2{\left \langle #1,#2 \right \rangle}
# \def\Ip#1#2{\Re{\int \conj{#1}\, #2 \,dt}}
# \def\adjoint#1{#1^{\dagger}}

# <headingcell level=1>

# 
# Equations of Electrodynamics

# <markdowncell>

# 
# <table>
# <tr>
# <th>  Maxwell's Equations  </th> <th>  Constitutive Relations: </th> <th>  Dielectric boundary conditions </th>
# <tr>
# <td> 
# \begin{equation}
# \begin{split}
# \nabla \cdot \vect{D} &= \rho_f \quad \quad  \nabla \times \vect{E} = -\pder{\vect{B}}{t} \\
# \nabla \cdot \vect{B} &= 0  \quad \quad   \nabla \times \vect{H} = \vect{J}_f + \pder{\vect{D}}{t}
# \end{split}
# \end{equation} 
# </td> 
# <td>   
# \begin{equation}
# \begin{split}
#   \vect{D} &= \epsilon_0 \vect{E} + \vect{P}\\
#   \vect{H} &= \frac{1}{\mu_0} \vect{B} - \vect{M} 
# \end{split}
# \end{equation} 
# </td> 
# <td> 
#  \begin{equation}
#   \vect{D}_{1}^{\perp}-\vect{D}_{2}^{\perp} = \sigma_f
# \end{equation}
# 
#  \begin{equation}
#    \vect{B}_{1}^{\perp}-\vect{B}_{2}^{\perp} = 0
# \end{equation}
# 
#  \begin{equation}
#   \vect{E}_{1}^{\parallel} -\vect{E}_{2}^{\parallel}   = 0 
# \end{equation}
# 
#  \begin{equation}
#   \vect{H}_{1}^{\parallel}-\vect{H}_{2}^{\parallel} = \vect{K}_f \times \hat{\vect{n}}
# \end{equation}
# </td> 
# </table>

# <headingcell level=5>

# The following table provides the meaning of each symbol and the SI unit of measure:

# <markdowncell>

# 
# <table>
# <tr>
# <th>  Symbol  </th> <th>   Meaning </th> <th>  SI unit of measure </th>
# </tr>
# <tr>
# <td> $$\vect{E}$$ </td> <td>  electric field</td> <td>   $$V/m$$ </td>
# </tr>
# <tr>
# <td> $$\vect{P}$$ </td> <td>   electric polarization </td> <td>  $$N/ (Vm)$$</td>  
# </tr>
# <tr>
# <td> $$\vect{D}$$ </td> <td>   electric displacement  </td> <td>  $$N/(Vm)$$ </td>
# </tr>
# <tr>
# <td> $$\vect{B}$$ </td> <td>   magnetic field </td> <td>    $$V s/m^2$$</td> 
# </tr>
# <tr>
# <td> $$\vect{M}$$ </td> <td>   magnetization </td> <td>    $$A/m$$ </td> 
# </tr>
# <tr>
# <td> $$\vect{H}$$ </td> <td>   magnetic displacement </td> <td>   $$A/m$$ </td> 
# </tr>
# <tr>
# <td> $$\vect{J}_f$$ </td> <td>   current density </td> <td>   $$C/(s m^2)$$ </td>
# </tr>
# <tr>
# <td> $$\vect{K}_f$$ </td> <td>   current surface density </td> <td>   $$C/ s m$$ </td> 
# </tr>
# <tr>
# <td> $$\rho_f$$ </td> <td>  charge density </td> <td>   $$C/ m^3$$</td> 
# </tr>
# <tr>
# <td> $$\sigma_f$$ </td> <td>   surface charge  density</td> <td>  $$C/ m^2$$</td> 
# </tr>
# <tr>
#  <td> $\epsilon_0 \approx 8.8 \times 10^{-12}$ </td> <td> permitting of free space </td> <td> $$C^2/(Nm^2)$$ </td> 
#  </tr>
# <tr>
# <td> $$\mu_0 \approx 4\pi \times 10^{-7}$$ </td> <td>  permeability of free space </td> <td>  $$V s / (A m) $$ </td> 
# </tr>
# <tr>
# <td> $$c  \approx 2.9 \times 10^{-8}$$ </td> <td>  speed of light in vac   </td> <td>  $$m/s$$</td> 

# <codecell>

Image('http://www.rp-photonics.com/img/resonator_mode_2.png')
#Image('images/resonator_mode_2.png')

# <headingcell level=5>

# Constitutive Relations:

# <markdowncell>

# 
#  \begin{equation}
#   \vect{D} = \epsilon_0 \vect{E} + \vect{P}
# \end{equation}
# 
#  \begin{equation}
#    \vect{H} = \frac{1}{\mu_0} \vect{B} - \vect{M} 
# \end{equation}

# <headingcell level=5>

# Dielectric boundary conditions:

# <markdowncell>

# $$\newcommand\der[2]{\frac{d{#1}}{d{#2}}}
# \newcommand\dder[2]{\frac{d^2{#1}}{d{#2}^2}}
# \newcommand\ddder[2]{\frac{d^3{#1}}{d{#2}^3}}
# \newcommand\pder[2]{\frac{\partial #1}{\partial #2}}
# \newcommand\ppder[2]{\frac{\partial^2 #1}{\partial #2^2}}
# \newcommand\pnder[3]{\frac{\partial^{#3} #1}{\partial #2^{#3}}}
# \newcommand\der[2]{\frac{d{#1}}{d{#2}}}
# \newcommand\dder[2]{\frac{d^2{#1}}{d{#2}^2}}
# \newcommand\ddder[2]{\frac{d^3{#1}}{d{#2}^3}}
# \newcommand\pder[2]{\frac{\partial #1}{\partial #2}}
# \newcommand\ppder[2]{\frac{\partial^2 #1}{\partial #2^2}}
# \newcommand\pnder[3]{\frac{\partial^{#3} #1}{\partial #2^{#3}}}
# \newcommand\pdder[3]{\frac{\partial^2 #1}{\partial #2 \partial #3}}
# \newcommand\pddder[4]{\frac{\partial^3 #1}{\partial #2 \partial #3 \partial #4}}$$
#  \begin{equation}
#   \vect{D}_{1}^{\perp}-\vect{D}_{2}^{\perp} = \sigma_f
# \end{equation}
# 
#  \begin{equation}
#    \vect{B}_{1}^{\perp}-\vect{B}_{2}^{\perp} = 0
# \end{equation}
# 
#  \begin{equation}
#   \vect{E}_{1}^{\parallel} -\vect{E}_{2}^{\parallel}   = 0 
# \end{equation}
# 
#  \begin{equation}
#   \vect{H}_{1}^{\parallel}-\vect{H}_{2}^{\parallel} = \vect{K}_f \times \hat{\vect{n}}
# \end{equation}

# <markdowncell>

#  \begin{equation}
#    \nabla \times \vect{E} = -\pder{\vect{B}}{t} 
# \end{equation}
# 
# 
#  \begin{equation}
#    \nabla \cdot \vect{B} = 0 
# \end{equation}
# 
# \begin{equation}
# \nabla \times \frac{1}{\mu_0} \vect{B} = \nabla \times \vect{M} +  \vect{J}_f + \pder{\epsilon_0 \vect{E}}{t} +\pder{\vect{P}}{t} 
# \end{equation}

# <markdowncell>

# Dotting \eqref{equ:CR_Maxwell_2} by $\frac{1}{\mu_0} \vect{B}$ and \eqref{equ:CR_Maxwell_4} by $\vect{E}$ and subtracting gives
#  \begin{equation}
#    \vect{E} \cdot \left(\nabla \times \frac{1}{\mu_0} \vect{B}\right) - \frac{1}{\mu_0} \vect{B} \cdot \left(\nabla \times \vect{E}\right) =
#    \vect{E} \cdot \left(\nabla \times \vect{M}\right) +   \vect{E} \cdot \vect{J}_f +  \vect{E} \cdot \pder{\epsilon_0 \vect{E}}{t} +  \vect{E} \cdot\pder{\vect{P}}{t} + \frac{1}{\mu_0} \vect{B} \pder{\vect{B}}{t}
# \end{equation}
# or 
#  \begin{equation}
#    -\nabla \cdot \left(\vect{E} \times \frac{1}{\mu_0} \vect{B}\right)
#  = \vect{E} \cdot \vect{J}_f +  \frac{\epsilon_0}{2}  \pder{\vect{E} \cdot \vect{E}}{t} +  \vect{E} \cdot\pder{\vect{P}}{t} + \vect{E} \cdot \left(\nabla \times \vect{M}\right)  + \frac{1}{2\mu_0}\pder{\vect{B}\cdot\vect{B}}{t} 
# \end{equation}
# or 
#  \begin{equation}
#   \pder{}{t}\left(\frac{\epsilon_0}{2}  \vect{E} \cdot \vect{E} + \frac{1}{2\mu_0}\vect{B}\cdot\vect{B}\right)
#   = -\nabla \cdot \left(\vect{E} \times \frac{1}{\mu_0} \vect{B}\right) - \vect{E} \cdot \left( \vect{J}_f + \pder{\vect{P}}{t} + \left(\nabla \times \vect{M}\right)\right)
# \end{equation}
# 
# 
# \begin{equation}
#  \begin{split}
#    \epsilon_0 \nabla \cdot \vect{E} +\nabla \cdot \vect{P} &= \rho_f \\
#   \nabla \times \nabla \times \vect{E} & = - \mu_0\pder{\vect{J}_f}{t} - \mu_0\pder{\nabla \times \vect{M}}{t} - \mu_0 \epsilon_0 \ppder{\vect{E}}{t} -\mu_0\ppder{\vect{P}}{t}\\
#    \nabla \cdot \vect{B} &= 0  \\
#     \nabla \times \nabla \times \vect{B} &= \mu_0\nabla \times \nabla \times \vect{M} + \mu_0 \nabla \times \vect{J}_f -  \mu_0 \epsilon_0 \ppder{\vect{B}}{t}  + \mu_0 \pder{\nabla \times\vect{P}}{t}
#  \end{split}
# \end{equation}
# Using $\nabla \times \nabla \times\vect{A} = -\nabla^2\vect{A} + \nabla (\nabla \cdot \vect{A})$:
# \begin{equation}
#  \begin{split}
#     \nabla \cdot \vect{E} &= \frac{\rho_f}{\epsilon_0} - \frac{1}{\epsilon_0} \nabla \cdot \vect{P} \\
#   \nabla^2 \vect{E} - \mu_0 \epsilon_0 \ppder{\vect{E}}{t} &= \mu_0\pder{\vect{J}_f}{t} + \mu_0\pder{\nabla \times \vect{M}}{t} + \frac{\nabla \rho_f}{\epsilon_0} - \frac{1}{\epsilon_0} \nabla \left(\nabla \cdot \vect{P} \right) + \mu_0\ppder{\vect{P}}{t}\\
#    \nabla \cdot \vect{B} &= 0  \\
#    \nabla^2\vect{B} - \mu_0 \epsilon_0 \ppder{\vect{B}}{t} &= -\mu_0\nabla \times \nabla \times \vect{M} - \mu_0 \nabla \times \vect{J}_f   - \mu_0 \pder{\left(\nabla \times\vect{P}\right)}{t}
#  \end{split}
# \end{equation}

# <markdowncell>

# MACROS FOR LATEX:
# $$\newcommand\der[2]{\frac{d{#1}}{d{#2}}}
# \newcommand\dder[2]{\frac{d^2{#1}}{d{#2}^2}}
# \newcommand\ddder[2]{\frac{d^3{#1}}{d{#2}^3}}
# \newcommand\pder[2]{\frac{\partial #1}{\partial #2}}
# \newcommand\ppder[2]{\frac{\partial^2 #1}{\partial #2^2}}
# \newcommand\pnder[3]{\frac{\partial^{#3} #1}{\partial #2^{#3}}}
# \newcommand\der[2]{\frac{d{#1}}{d{#2}}}
# \newcommand\dder[2]{\frac{d^2{#1}}{d{#2}^2}}
# \newcommand\ddder[2]{\frac{d^3{#1}}{d{#2}^3}}
# \newcommand\pder[2]{\frac{\partial #1}{\partial #2}}
# \newcommand\ppder[2]{\frac{\partial^2 #1}{\partial #2^2}}
# \newcommand\pnder[3]{\frac{\partial^{#3} #1}{\partial #2^{#3}}}
# \newcommand\pdder[3]{\frac{\partial^2 #1}{\partial #2 \partial #3}}
# \newcommand\pddder[4]{\frac{\partial^3 #1}{\partial #2 \partial #3 \partial #4}}$$
# \let\truesum=\sum
# \def\sum{\mathop{\textstyle\truesum}\limits}
# 
# \def\Re#1{\mathrm{Re}\hspace{-0.03in}\left[#1\right]}
# \def\Im#1{\mathrm{Im}\hspace{-0.03in}\left[#1\right]}
# \def\bigOh#1{O\hspace{-0.03in}\left(#1\right)}
# \def\littelOh#1{o\hspace{-0.03in}\left(#1\right)}
# \def\conj#1{\bar{#1}}
# 
# 
# \newcommand{\intl}[4]{\int_{#3}^{#4} #1 \, d #2}
# \def\Del#1{\Delta(#1)}
# \def\del#1{\delta\hspace{-0.03in}\left(#1 \right)}
# \def\Int#1#2{\left[\int #1 \, d#2\right]}
# \def\iint{\int \int}
# \def\dmin#1#2{\displaystyle{\min_{#1}}\hspace{-0.03in}\left(#2 \right)}
# \def\dmax#1#2{\displaystyle{\max_{#1}}\hspace{-0.03in}\left(#2 \right)}
# \def\dargmin#1#2{\displaystyle{{\mathrm{argmin}}_{#1}}\hspace{-0.03in}\left(#2 \right)}
# \def\dargmax#1#2{\displaystyle{{\mathrm{argmax}}_{#1}}\hspace{-0.03in}\left(#2 \right)}
# $$\def\vect#1{\mathbf{#1}}$$
# \def\gvect#1{\boldsymbol{#1}}
# \def\ip#1#2{\left \langle #1,#2 \right \rangle}
# \def\Ip#1#2{\Re{\int \conj{#1}\, #2 \,dt}}
# \def\adjoint#1{#1^{\dagger}}
# 

# <codecell>


# <codecell>


# <codecell>


