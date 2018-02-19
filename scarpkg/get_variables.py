import yaml
import os

def get_info(var_file=None):
    if not var_file:
        var_file=os.environ['HOME']+"/.variables.yaml"
    
    with open(var_file, "r") as stream:
        INFO = yaml.load(stream)
    
    return INFO
