# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <img src="images/AF_Symbol_New_Blue.png"  width="25%" align="left" border="4"><img src="images/Air_Force_Research_Laboratory.png"  width="20%" align="right" border="4">

# <headingcell level=1>

# Equations of Electrodynamics:
# 
# From Maxwell to Helmholtz

# <markdowncell>

# ###Dr. Daniel Cargill    (<a href="mailto:daniel.cargill@us.af.mil">daniel.cargill@us.af.mil</a>)
# 
# ###Tau Weekly Meeting: 10/??/14

# <markdowncell>

# ### This talk **focuses** on
# 
#  * #### Deriving Helmholtz from Maxwell
#  
#  
#  * #### Numerical/Analytical Solutions of Deterministic Helmholtz
#  
#  
#  * #### Numercial Methods for Stochastic Helmholtz
#  
#  
#  * #### Rates of Convergence
#     

# <codecell>

import numpy as np
import pandas as pd
import pandas.io.data as pdd
from urllib import urlretrieve
from IPython.display import HTML, Image
%matplotlib inline

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
# \newcommand\pddder[4]{\frac{\partial^3 #1}{\partial #2 \partial #3 \partial #4}}
# \let\truesum=\sum
# \def\sum{\mathop{\textstyle\truesum}\limits}
# \def\Re#1{\mathrm{Re}\hspace{-0.03in}\left[#1\right]}
# \def\Im#1{\mathrm{Im}\hspace{-0.03in}\left[#1\right]}
# \def\bigOh#1{O\hspace{-0.03in}\left(#1\right)}
# \def\littelOh#1{o\hspace{-0.03in}\left(#1\right)}
# \def\conj#1{\bar{#1}}
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
# \require{cancel}$$
# 
# 
# #####Maxwell's system in differential form:
# <table>
# <tr>
# <th>  Maxwell's Equations  </th> <th>  Constitutive Relations</th> <th>  Dielectric boundary conditions </th>
# <tr>
# <td> 
# \begin{equation}
# \begin{split}
# \nabla \cdot \vect{D} &= \rho_f\\ 
# \nabla \times \vect{E} &= -\pder{\vect{B}}{t} \\
# \nabla \cdot \vect{B} &= 0    \\
# \nabla \times \vect{H} &= \vect{J}_f + \pder{\vect{D}}{t}\\
# \end{split}
# \end{equation} 
# </td> 
# <td>   
# \begin{equation}
# \begin{split}
#   \vect{D} &= \epsilon_0 \vect{E} + \vect{P}( \vect{E})\\
#   \vect{H} &= \frac{1}{\mu_0} \vect{B} - \vect{M}(\vect{B})
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

# <markdowncell>

# #####Definitions:
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
# </table>

# <markdowncell>

#  #####Using the Constitutive Relations and taking **dot** products...
#  
#  
#  \begin{equation}
#    \vect{E} \cdot \left(\nabla \times \frac{1}{\mu_0} \vect{B}\right) - \frac{1}{\mu_0} \vect{B} \cdot \left(\nabla \times \vect{E}\right) =
#    \vect{E} \cdot \left(\nabla \times \vect{M}\right) +   \vect{E} \cdot \vect{J}_f +  \vect{E} \cdot \pder{\epsilon_0 \vect{E}}{t} +  \vect{E} \cdot\pder{\vect{P}}{t} + \frac{1}{\mu_0} \vect{B} \pder{\vect{B}}{t}
# \end{equation}
# 
# 
# #####or 
# 
# 
#  \begin{equation}
#   \pder{}{t}\left(\frac{\epsilon_0}{2}  \vect{E} \cdot \vect{E} + \frac{1}{2\mu_0}\vect{B}\cdot\vect{B}\right)
#   = -\nabla \cdot \left(\vect{E} \times \frac{1}{\mu_0} \vect{B}\right) - \vect{E} \cdot \left( \vect{J}_f + \pder{\vect{P}}{t} + \left(\nabla \times \vect{M}\right)\right)
# \end{equation}
# 
# 
# ##### produces conservation (energy density) equation!

# <markdowncell>

# ##### Using the Constitutive Relations and taking **cross** products...
#  
#  
# \begin{equation}
#  \begin{split}
#    \epsilon_0 \nabla \cdot \vect{E} +\nabla \cdot \vect{P} &= \rho_f \\
#   \nabla \times \nabla \times \vect{E} & = - \mu_0\pder{\vect{J}_f}{t} -  \mu_0\pder{\left(\nabla \times \vect{M}\right)}{t} - \mu_0 \epsilon_0 \ppder{\vect{E}}{t} -\mu_0\ppder{\vect{P}}{t}\\
#    \nabla \cdot \vect{B} &= 0  \\
#    \nabla \times \nabla \times \vect{B} &= \mu_0\nabla \times \nabla \times \vect{M} + \mu_0 \nabla \times \vect{J}_f -  \mu_0 \epsilon\ppder{\vect{B}}{t}  +\mu_0 \pder{\left(\nabla \times\vect{P}\right)}{t}
#  \end{split}
# \end{equation}
# 
# 
# ##### and using  $\nabla \times \nabla \times\vect{A} = -\nabla^2\vect{A} + \nabla (\nabla \cdot \vect{A})$...
# 
# \begin{equation}
#  \begin{split}
#    \nabla \cdot \vect{E} &= \frac{\rho_f}{\epsilon_0} - \frac{1}{\epsilon_0} \nabla \cdot \vect{P} \\
#   \nabla^2 \vect{E} - \mu_0 \epsilon_0 \ppder{\vect{E}}{t} &= \mu_0\pder{\vect{J}_f}{t} + \mu_0\pder{\left(\nabla \times \vect{M}\right)}{t} + \frac{\nabla \rho_f}{\epsilon_0} - \frac{1}{\epsilon_0} \nabla \left(\nabla \cdot \vect{P} \right) + \mu_0\ppder{\vect{P}}{t}\\
#    \nabla \cdot \vect{B} &= 0  \\
#    \nabla^2\vect{B} - \mu_0 \epsilon_0 \ppder{\vect{B}}{t} &= -\mu_0\nabla \times \nabla \times \vect{M} - \mu_0 \nabla \times \vect{J}_f   - \mu_0 \pder{\left(\nabla \times\vect{P}\right)}{t}
#  \end{split}
# \end{equation}
# 
# ##### produces wave equations!

# <markdowncell>

#  #####Lets make some assumptions...
#  
#  * Non-magnetic medium with no free charge: $ \rho_f = 0$, $\vect{J}_f = \vect{0}$, $\vect{M} = \vect{0}$
# 
# \begin{equation}
#  \begin{split}
#    \nabla \cdot \vect{E} &= \xcancel{\frac{\rho_f}{\epsilon_0}} - \frac{1}{\epsilon_0} \nabla \cdot \vect{P} \\
#   \nabla^2 \vect{E} - \mu_0 \epsilon_0 \ppder{\vect{E}}{t} &= \xcancel{\mu_0\pder{\vect{J}_f}{t}} + \xcancel{\mu_0\pder{\left(\nabla \times \vect{M}\right)}{t}} + \xcancel{\frac{\nabla \rho_f}{\epsilon_0}} - \frac{1}{\epsilon_0} \nabla \left(\nabla \cdot \vect{P} \right) + \mu_0\ppder{\vect{P}}{t}\\
#    \nabla \cdot \vect{B} &= 0  \\
#    \nabla^2\vect{B} - \mu_0 \epsilon_0 \ppder{\vect{B}}{t} &= \xcancel{-\mu_0 \nabla \times \nabla \times \vect{M}} - \xcancel{\mu_0 \nabla \times \vect{J}_f}   - \mu_0 \pder{\left(\nabla \times\vect{P}\right)}{t}
#  \end{split}
# \end{equation}

# <markdowncell>

#  #####Lets make some assumptions...
#  
#  * Non-magnetic medium with no free charge: $ \rho_f = 0$, $\vect{J}_f = \vect{0}$, $\vect{M} = \vect{0}$
# 
#  * Instantious and isotropic polarization: $\vect{P}(\vect{E}) = \epsilon_0   \chi(\vect{r},t)   \vect{E}$
#  
#  \begin{equation}
#  \begin{split}
#    \nabla \cdot \vect{E} &= -\chi\nabla \cdot  \vect{E} -  \vect{ \nabla\chi} \cdot  \vect{E}  \\
#   \nabla^2 \vect{E} - \frac{1}{c^2} \ppder{\vect{E}}{t} &= - \nabla \left(\nabla \cdot  \chi \vect{E} \right) + \frac{1}{c^2} \ppder{ \chi \vect{E}}{t}\\
#    \nabla \cdot \vect{B} &= 0  \\
#    \nabla^2\vect{B} - \frac{1}{c^2}\ppder{\vect{B}}{t} &=    -\frac{1}{c^2} \pder{\left(\nabla \times \chi \vect{E}\right)}{t}
#  \end{split}
# \end{equation}
#  
# 
# 

# <codecell>


