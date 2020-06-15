mkdir tools

virtualenv tools/kernswitch-env

source tools/kernswitch-env/bin/activate

pip install -r requirements.txt

deactivate
