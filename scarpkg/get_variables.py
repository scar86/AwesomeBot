import yaml


def get_info(var_file):
    
    with open(var_file, "r") as stream:
        INFO = yaml.load(stream)
    
    return INFO
