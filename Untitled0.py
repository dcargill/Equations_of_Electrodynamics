# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

profile_dir = get_ipython().profile_dir.location
profile_dir

# <codecell>

IPython.html.nbextensions.check_nbextension('IPython-notebook-extensions-master/slidemode/main.js')

# <codecell>

import IPython

# <codecell>

%%javascript
IPython.load_extensions('IPython-notebook-extensions-master/slidemode/main');

# <codecell>


