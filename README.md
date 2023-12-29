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


### steps to download opensource LLMs to your laptop

- tbd (use LM Studio)

### steps to run these LLMs behind an (open-AI compatible) API

- tbd use LM Studio
- need to figure out how to run multiple LLMs together, local-ai didnt work, LM Studio doesn't allow it natively

### steps to kick off docker container for code execution

- this is where we will get the coder LLM (our AI software engineer) to run the code.
- I already have the Dockerfile in the root directory from the CLI run:
- now we build the image (this step takes a while)
	- `docker build -t autogen-project .`
````
(venv) tcm autonomous-product-team$ docker build -t autogen-project .
[+] Building 125.9s (5/9)                                                                               docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                    0.0s
 => => transferring dockerfile: 341B                                                                                    0.0s
 => [internal] load .dockerignore                                                                                       0.0s
 => => transferring context: 2B                                                                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.9.18-slim                                                   3.6s
 => [auth] library/python:pull token for registry-1.docker.io                                                           0.0s
 => [1/4] FROM docker.io/library/python:3.9.18-slim@sha256:96be08c44307e781fd9ce8e05b49c969b4cb902ec23594f904739c58d  122.3s
 => => resolve docker.io/library/python:3.9.18-slim@sha256:96be08c44307e781fd9ce8e05b49c969b4cb902ec23594f904739c58da3  0.0s
 => =>.....
 ```

 - now we run the image:
 	- `docker run -it -p 3010:3010 --rm --network host autogen-project`
 	- -it allows you to interact with the container
 	- --rm removes the container when it stops
 	- --network host allows the container to connect to localhost where I'm running the actual LLM (much faster on Apple metal than a tiny container)

