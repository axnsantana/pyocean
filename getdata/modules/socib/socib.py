import os
import yaml
basepath = os.path.dirname(__file__)
cfg_file=os.path.abspath(os.path.join(basepath,"socib.yml"))
config = yaml.safe_load(open(cfg_file))

def get_waves_forecast_data(varname):
    from pydap.client import open_url
    from datetime import datetime as dt
    
    date = dt.strptime('20160828000000','%Y%m%d%H%M%S')
    waves_cfg = config['products']['modeling']['wave']
    url_base = waves_cfg['urls']['opendap']
    ncfile = dt.strftime(date,'%Y/%m/sapo_ib_swan_%Y%m%d%H%M%S.nc')
    url = '%s/%s' % (url_base,ncfile) 
    dataset = open_url(url)
    
    return dataset[varname]

