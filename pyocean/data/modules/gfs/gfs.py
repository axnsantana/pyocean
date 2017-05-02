import os
import yaml
basepath = os.path.dirname(__file__)
cfg_file=os.path.abspath(os.path.join(basepath,"gfs.yml"))
config = yaml.safe_load(open(cfg_file))
