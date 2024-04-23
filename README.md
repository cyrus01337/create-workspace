# Setup
```sh
pyenv virtualenv 3.12.2 "$(basename $PWD)"
pyenv local "3.12.2/envs/$(basename $PWD)"
python -m pip install -U pip
pip install -r requirements.txt
```
