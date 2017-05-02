import os
import sys
import pkgutil

def getdata(module_name,function_name,*args,**kargs):
    import importlib
    try:
        module = importlib.import_module(module_name)
        return getattr(module,function_name)(*args,**kargs)
    except Exception, e:
        print( "<p>Error: %s</p>" % e )

    return

def list_modules():
    pkgpath = "%s/%s" % (os.path.dirname(__file__), 'modules')
    return [name for _, name, _ in pkgutil.walk_packages([pkgpath])]
