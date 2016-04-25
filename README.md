# Help! They dumped a dataset on our doorstep...

...and want us to predict something. 

This repository contains the slides (PDF) and the Jupyter Notebook files that
were used in the DevCon 2016 presentation with the aforementioned title by
Richard Berendsen.

Note that you cannot actually run everything, as the data is not available. 
But you can use the code for your reference.

## Installation requirements

The next two steps assume you have the following setup installed:

1. An Anaconda Python 3 distribution
1. pandas (`conda install pandas`)
1. Jupyter (`conda install jupyter`)

## Step 1: Generate the notebooks

You will have to generate the Jupyter Notebooks (.ipynb files)
from the .py files in this repository. To do that, just call 

`config/py_to_notebook.sh`

## Step 2: open the notebooks

To open the notebooks, just type

`jupyter notebook`
