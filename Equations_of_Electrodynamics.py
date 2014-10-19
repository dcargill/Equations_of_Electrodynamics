# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>


# <codecell>


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

Image('http://www.rp-photonics.com/img/resonator_mode_2.png')
#Image('images/resonator_mode_2.png')

# <headingcell level=3>

# Exercise

# <markdowncell>

# Trend-based investment strategy with the EURO STOXX 50 index:
# 
# * 2 trends 42d & 252d 
# * long, short, cash positions
# * no transaction costs
# 
# Signal generation:
# 
# * invest (go long) when the 42d trend is more than 100 points above the 252d trend
# * sell (go short) when the 42d trend is more than 20 points below the 252d trend
# * invest in cash (no interest) when neither of both is true

# <headingcell level=2>

# Historical Correlation between EURO STOXX 50 and VSTOXX

# <markdowncell>

# It is a stylized fact that stock indexes and related volatility indexes are **highly negatively correlated**. The following example analyzes this stylized fact based on the EURO STOXX 50 stock index and the VSTOXX volatility index using Ordinary Least-Squares regession (OLS).

# <markdowncell>

# First, we collect historical data for both the EURO STOXX 50 stock and the VSTOXX volatility index.

# <codecell>

import pandas as pd
import datetime as dt
from urllib import urlretrieve

# <codecell>

try:
    es_url = 'http://www.stoxx.com/download/historical_values/hbrbcpe.txt'
    vs_url = 'http://www.stoxx.com/download/historical_values/h_vstoxx.txt'
    urlretrieve(es_url, 'es.txt')
    urlretrieve(vs_url, 'vs.txt')
except:
    pass

# <markdowncell>

# The **EURO STOXX 50 data** is not yet in the right format. Some house cleaning is necessary (I).

# <codecell>

lines = open('es.txt').readlines()  # reads the whole file line-by-line

# <codecell>

lines[:5]  # header not well formatted

# <markdowncell>

# The **EURO STOXX 50 data** is not yet in the right format. Some house cleaning is necessary (II).

# <codecell>

lines[3883:3890]  # from 27.12.2001 additional semi-colon

# <markdowncell>

# The **EURO STOXX 50 data** is not yet in the right format. Some house cleaning is necessary (III).

# <codecell>

lines = open('es.txt').readlines()  # reads the whole file line-by-line
new_file = open('es50.txt', 'w')  # opens a new file
new_file.writelines('date' + lines[3][:-1].replace(' ', '') + ';DEL' + lines[3][-1])
    # writes the corrected third line (additional column name)
    # of the orginal file as first line of new file
new_file.writelines(lines[4:])  # writes the remaining lines of the orginal file

# <markdowncell>

# The **EURO STOXX 50 data** is not yet in the right format. Some house cleaning is necessary (IV).

# <codecell>

list(open('es50.txt'))[:5]  # opens the new file for inspection

# <markdowncell>

# Now, the data can be safely read into a DataFrame object.

# <codecell>

es = pd.read_csv('es50.txt', index_col=0, parse_dates=True, sep=';', dayfirst=True)

# <codecell>

del es['DEL']  # delete the helper column

# <codecell>

es.info()

# <markdowncell>

# The VSTOXX data can be read without touching the raw data.

# <codecell>

vs = pd.read_csv('vs.txt', index_col=0, header=2, parse_dates=True, sep=',', dayfirst=True)

# you can alternatively read from the Web source directly
# without saving the csv file to disk:
# vs = pd.read_csv(vs_url, index_col=0, header=2,
#                  parse_dates=True, sep=',', dayfirst=True)

# <markdowncell>

# We now **merge the data** for further analysis.

# <codecell>

import datetime as dt
data = pd.DataFrame({'EUROSTOXX' :
            es['SX5E'][es.index > dt.datetime(1999, 12, 31)]})
data = data.join(pd.DataFrame({'VSTOXX' :
            vs['V2TX'][vs.index > dt.datetime(1999, 12, 31)]}))
data.info()

# <markdowncell>

# Let's inspect the two time series.

# <codecell>

data.head()

# <markdowncell>

# A **picture** can tell almost the complete story.

# <codecell>

data.plot(subplots=True, grid=True, style='b', figsize=(10, 5))

# <markdowncell>

# We now generate **log returns** for both time series.

# <codecell>

rets = np.log(data / data.shift(1)) 
rets.head()

# <markdowncell>

# To this new data set, also stored in a DataFrame object, we apply **OLS**.

# <codecell>

xdat = rets['EUROSTOXX']
ydat = rets['VSTOXX']
model = pd.ols(y=ydat, x=xdat)
model

# <markdowncell>

# Again, we want to see how our results look graphically.

# <codecell>

import matplotlib.pyplot as plt
plt.plot(xdat, ydat, 'r.')
ax = plt.axis()  # grab axis values
x = np.linspace(ax[0], ax[1] + 0.01)
plt.plot(x, model.beta[1] + model.beta[0] * x, 'b', lw=2)
plt.grid(True)
plt.axis('tight')

# <markdowncell>

# Let us see if we can identify **systematics over time**. And indeed, during the crisis 2007/2008 (yellow dots) volatility has been more pronounced than more recently (red dots).

# <codecell>

import matplotlib as mpl
mpl_dates = mpl.dates.date2num(rets.index)
plt.figure(figsize=(8, 4))
plt.scatter(rets['EUROSTOXX'], rets['VSTOXX'], c=mpl_dates, marker='o')
plt.grid(True)
plt.xlabel('EUROSTOXX')
plt.ylabel('VSTOXX')
plt.colorbar(ticks=mpl.dates.DayLocator(interval=250),
          format=mpl.dates.DateFormatter('%d %b %y'))

# <headingcell level=3>

# Exercise

# <markdowncell>

# We want to test whether the EURO STOXX 50 and/or the VSTOXX returns are **normally distributed** or not (e.g. if they might have fat tails). We want to do a
# 
# * graphical illustration (using _**qqplot**_ of _**statsmodels.api**_) and a
# * statistical test (using _**normaltest**_ of _**scipy.stats**_)
# 
# Add on: plot a histogram of the log return frequencies and compare that to a normal distribution with same mean and variance (using e.g. _**norm.pdf**_ from _**scipy.stats**_)

# <headingcell level=2>

# Constant Proportion VSTOXX Investment

# <markdowncell>

# There has been a number of studies which have illustrated that **constant proportion investments in volatility derivatives** &ndash; given a diversified equity portfolio &ndash; might improve investment performance considerably. See, for instance, the study
# 
# <a href="http://www.eurexgroup.com/group-en/newsroom/60036/" target="_blank">The Benefits of Volatility Derivatives in Equity Portfolio Management</a>
# 
# We now want to replicate (in a simplified fashion) what you can flexibly test here on the basis of two backtesting applications for **VSTOXX-based investment strategies**:
# 
# <a href="http://www.eurexchange.com/vstoxx/app1/" target="_blank">Two Assets Backtesting</a>
# 
# <a href="http://www.eurexchange.com/vstoxx/app2/" target="_blank">Four Assets Backtesting</a>
# 

# <markdowncell>

# The strategy we are going to implement and test is characterized as follows:
# 
# * An investor has total wealth of say 100,000 EUR
# * He invests, say, 70% of that into a diversified equity portfolio
# * The remainder, i.e. 30%, is invested in the VSTOXX index directly
# * Through (daily) trading the investor keeps the proportions constant
# * No transaction costs apply, all assets are infinitely divisible

# <markdowncell>

# We already have the necessary data available. However, we want to drop 'NaN' values and want to **normalize the index values**.

# <codecell>

data = data.dropna()

# <codecell>

data = data / data.ix[0] * 100

# <codecell>

data.head()

# <markdowncell>

# First, the **initial invest**.

# <codecell>

invest = 100
cratio = 0.3
data['Equity'] = (1 - cratio) * invest / data['EUROSTOXX'][0]
data['Volatility'] = cratio * invest / data['VSTOXX'][0]

# <markdowncell>

# This can already be considered an **static** investment strategy.

# <codecell>

data['Static'] = (data['Equity'] * data['EUROSTOXX']
                + data['Volatility'] * data['VSTOXX'])

# <codecell>

data[['EUROSTOXX', 'Static']].plot(figsize=(10, 5))

# <markdowncell>

# Second, the dynamic strategy with **daily adjustments** to keep the value ratio constant.

# <codecell>

for i in range(1, len(data)):
    evalue = data['Equity'][i - 1] * data['EUROSTOXX'][i]
      # value of equity position
    vvalue = data['Volatility'][i - 1] * data['VSTOXX'][i]
      # value of volatility position
    tvalue = evalue + vvalue
      # total wealth 
    data['Equity'][i] = (1 - cratio) * tvalue / data['EUROSTOXX'][i]
      # re-allocation of total wealth to equity ...
    data['Volatility'][i] = cratio * tvalue / data['VSTOXX'][i]
      # ... and volatility position

# <markdowncell>

# Third, the **total wealth position**.

# <codecell>

data['Dynamic'] = (data['Equity'] * data['EUROSTOXX']
                + data['Volatility'] * data['VSTOXX'])

# <codecell>

data.head()

# <markdowncell>

# A brief check if the **ratios are indeed constant**.

# <codecell>

(data['Volatility'] * data['VSTOXX'] / data['Dynamic'])[:5]

# <codecell>

(data['Equity'] * data['EUROSTOXX'] / data['Dynamic'])[:5]

# <markdowncell>

# Let us inspect the performance of the strategy.

# <codecell>

data[['EUROSTOXX', 'Dynamic']].plot(figsize=(10, 5))

# <headingcell level=3>

# Exercise

# <markdowncell>

# Write a Python function which allows for an **arbitrary but constant ratio** to be invested in the VSTOXX index and which returns net performance values (in percent) for the constant proportion VSTOXX strategy.
# 
# Add on: find the ratio to be invested in the VSTOXX that gives the maximum performance.

# <headingcell level=2>

# Analyzing High Frequency Data

# <markdowncell>

# Using standard Python functionality and pandas, the code that follows reads **intraday, high-frequency data** from a Web source, plots it and resamples it.

# <codecell>

try:
    url = 'http://hopey.netfonds.no/posdump.php?'
    url += 'date=%s%s%s&paper=AAPL.O&csv_format=csv' % ('2014', '03', '12')
    # you may have to adjust the date since only recent dates are available
    urlretrieve(url, 'aapl.csv')
except:
    pass

# <codecell>

AAPL = pd.read_csv('aapl.csv', index_col=0, header=0, parse_dates=True)

# <codecell>

AAPL.info()

# <markdowncell>

# The **intraday evolution** of the Apple stock price.

# <codecell>

AAPL['bid'].plot()

# <codecell>

AAPL = AAPL[AAPL.index > dt.datetime(2014, 3, 12, 10, 0, 0)]
  # only data later than 10am at that day

# <markdowncell>

# A **resampling of the data** is easily accomplished with pandas.

# <codecell>

# this resamples the record frequency to 5 minutes, using mean as aggregation rule
AAPL_5min = AAPL.resample(rule='5min', how='mean').fillna(method='ffill')
AAPL_5min.head()

# <markdowncell>

# Let's have a graphical look at the new data set.

# <codecell>

AAPL_5min['bid'].plot()

# <markdowncell>

# With pandas you can easily apply **custom functions** to time series data.

# <codecell>

AAPL_5min['bid'].apply(lambda x: 2 * 530 - x).plot()
  # this mirrors the stock price development at 

# <headingcell level=2>

# Why Python for Financial Analytics & Visualization?

# <markdowncell>

# 10 years ago, Python was considered **exotic** in the analytics space &ndash; at best. Languages/packages like R and Matlab dominated the scene. Today, Python has become a **major force in financial analytics & visualization** due to a number of characteristics:
# 
#  * **syntax**: Python syntax is pretty close to the symbolic language used in mathematical finance (also: symbolic Python with SymPy)
#  * **multi-purpose**: prototyping, development, production, sytems administration &ndash; Python is one for all
#  * **libraries**: there is a library for almost any task or problem you face
#  * **efficiency**: Python speeds up all IT development tasks for analytics applications and reduces maintenance costs
#  * **performance**: Python has evolved from a scripting language to a 'meta' language with bridges to all high performance environments (e.g. LLVM, multi-core CPUs, GPUs, clusters)
#  * **interoperalbility**: Python seamlessly integrates with almost any other language and technology
#  * **interactivity**: Python allows domain experts to get closer to their business and financial data pools and to do real-time analytics
#  * **collaboration**: solutions like Wakari with IPython Notebook allow the easy sharing of code, data, results, graphics, etc.
#  

# <markdowncell>

# <img src="CA_logo.png" alt="Continuum Analytics" width="20%" align="right" border="4"><br><br><br><br>

# <headingcell level=2>

# Continuum Analytics Europe GmbH &ndash; Python Data Exploration & Visualization

# <markdowncell>

# **Continuum Analytics Inc.** &ndash; the company Web site
# 
# <a href="http://www.continuum.io" target="_blank">www.continuum.io</a>
# 
# **Dr. Yves J. Hilpisch** &ndash; my personal Web site
# 
# <a href="http://www.hilpisch.com" target="_blank">www.hilpisch.com</a>
# 
# **Python for Finance** &ndash; my NEW book (out as Early Release)
# 
# <a href="http://shop.oreilly.com/product/0636920032441.do" target="_blank">Python for Finance (O'Reilly)</a>
# 
# **Derivatives Analytics with Python** &ndash; my current book
# 
# <a href="http://www.derivatives-analytics-with-python.com" target="_blank">www.derivatives-analytics-with-python.com</a>
#     
# **Contact Us**
# 
# <a href="mailto:yves@continuum.io">yves@continuum.io</a> | <a href="mailto:europe@continuum.io">europe@continuum.io</a>
# | <a href="http://twitter.com/dyjh" target="_blank">@dyjh</a> | <a href="http://twitter.com/ContinuumIO" target="_blank">@ContinuumIO</a>

