import os
import yaml
basepath = os.path.dirname(__file__)
cfg_file=os.path.abspath(os.path.join(basepath,"socib.yml"))
config = yaml.safe_load(open(cfg_file))

def get_waves_forecast_data(varname,str_date):
    from pydap.client import open_url
    from datetime import datetime as dt
    
    print varname
    print str_date
    date = dt.strptime(str_date,'%Y%m%d%H%M%S')
    waves_cfg = config['products']['modeling']['wave']
    url_base = waves_cfg['urls']['opendap']
    ncfile = waves_cfg['basename'] % str_date
    prefix = dt.strftime(date,'%Y/%m')
    url = '%s/%s/%s' % (url_base,prefix,ncfile)
    print url
    dataset = open_url(url)
    
    return dataset[varname]

def get_fixed_station_data(station,varname,str_date=None):
    from pydap.client import open_url
    from datetime import datetime as dt
    
    date = dt.strptime(str_date,'%Y%m%d%H%M%S')
    station_cfg = config['products']['observational']['fixed_estations'][station]
    ncfile = station_cfg['basename'] % 'latest'
    prefix = ''
    if(str_date is not None):
        ncfile = station_cfg['basename'] % dt.strftime(date,'%Y-%m')
        prefix = dt.strftime(date,'%Y')
    url_base = station_cfg['urls']['opendap']
    url = '%s/%s/%s' % (url_base,prefix,ncfile)
    print url
    dataset = open_url(url)
    
    return dataset[varname]
    