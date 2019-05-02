This script predicts a Person Genre from the first (portuguese version only) name of that person, using Python and Sklearn.

using CONDA: create a environment from the YAML file:
```
conda env create -f envnome.yml
```
this will create a CONDA env named 'nomeenv'

OR install the dependencies through PIP:
```
pip install -r reqnome.txt
```


Open the 'Anaconda Prompt' and run out.py with your (Portuguese) name as the first argument:
```
python out.py "Maria"
```


Or run through Jupyter Notebook, open Anaconda Prompt:
```
conda activate nomeenv
jupyter notebook
```

Then open the NoteNome.ipynb