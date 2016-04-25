# Configuration

## Jupyter Notebook
Following the blog post on:

https://unsupervised.blogs.balabit.com/2015/08/how-to-version-control-ipython-3-jupyter-notebooks/

, retrieved Apr 25 2016, we copy-pasted a modified version stored in this directory (config/ipython_notebook_config.txt) of the online file:

https://github.com/balabit/ipython3-versioncontrol/blob/b9f25bad4d4cb06c34402f7156412dad96efbfa4/ipython_notebook_config.txt

into ~/.jupyter/jupyter_notebook_config.py; you can download the original to check what we changed.

This will take care of saving .py versions of your .ipynb files in a format
that can subsequently be transformed back to .ipynb files.

The reverse conversion is done using a modified version of the script py_to_notebook_v4.py, which was downloaded from:

https://github.com/balabit/ipython3-versioncontrol/blob/b9f25bad4d4cb06c34402f7156412dad96efbfa4/py_to_notebook_v4.py

The modified version is in config/py_to_notebook_v4.py, you can download the original if you want to check what we changed.

To run py_to_notebook_v4.py for all python files in this repository, we provided a convenience script: config/py_to_notebook.sh
