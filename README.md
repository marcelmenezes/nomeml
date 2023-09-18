This script predicts a Person Genre from the first (portuguese version only) name of that person, using Python 3.7.3 and Sklearn 0.20.3;
The model was trained from a dataset of 500k Names (treino/parte_nome_sexo.csv).

using CONDA: create a environment from the YAML file:
```
conda env create -f envnome.yml
```
this will create a CONDA env named 'nomeenv'

OR install the dependencies through PIP:
```
pip install -r reqnome.txt
```


1. Open the 'Anaconda Prompt' and run 'out.py' with your (Portuguese) name as the first argument:
```
python out.py "João"
```


--- OR --- 
2. Run through Jupyter Notebook, open Anaconda Prompt:
```
conda activate nomeenv
jupyter notebook
```

Then open the NoteNome.ipynb
