import sys

def getdata(module_name,function_name,*args,**kargs):
    import importlib
    try:
        module = importlib.import_module(module_name)
        return getattr(module,function_name)(*args,**kargs)
    except Exception, e:
        print( "<p>Error: %s</p>" % e )
        
    return