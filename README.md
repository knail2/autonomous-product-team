# Autonomous Product Team
using [autogen](https://microsoft.github.io/autogen) to set up a multi-agent team of specialized LLMs which mimic a product development and research team ...


### steps to set up the jupyter notebooks locally in a virtual environment:


- install [python](https://www.python.org/downloads/)
- clone this repo and change directory to come into it
- initiate a python virtual environment:
	- `python -m venv venv`
- activate the venv:
	- `. venv/bin/activate`
	- prompt should show (venv) ...
- install the required python libraries
	- `pip install -r requirements.txt`
- (optional) set up jupyter extensions:
	- `jupyter contrib nbextension install --user`
	- dark mode:
		- `jt -t onedork -fs 95 -altp -tfs 11 -nfs 115 -cellw 88% -T`
	- reset dark mode:
		- `jt -r`
	- the article is [here](https://towardsdatascience.com/supercharging-jupyter-notebooks-e22f5ad7ca18)
	- the documentation for the extensions [here](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/)
- run the notebooks:
	- `cd notebook # to save the notebooks here`
	- `jupyter notebook`
