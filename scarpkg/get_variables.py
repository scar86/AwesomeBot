import yaml
import os
from log import logMsg

def get_info(var_file=None):
    if not var_file:
        var_file=os.environ['HOME']+"/.variables.yaml"
    
    with open(var_file, "r") as stream:
        INFO = yaml.load(stream)
    
    return INFO


def save_info(filePath,order):
    
    if os.path.isfile(filePath):
        os.remove(filePath)
        
    stream = file(filePath, "w")
    yaml.dump(order,stream)
    stream.close()
