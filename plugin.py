import logging

class pluginmeta(type):
  '''
  Metaclass type that introduces the 'plugins' namespace dict.
  '''
  __plugins = dict()

  def __init__(cls,name,bases,dct):
    super(pluginmeta,cls).__init__(name,bases,dct)

  def __call__(cls,*args,**kwargs):
    new = type.__call__(cls,*args,**kwargs)
    new.spaces = args
    return new

  def __getitem__(self,key):
    return pluginmeta.__plugins[key]

  def __setitem__(self,key,val):
    pluginmeta.__plugins[key] = val

  def __delitem__(self,key):
    del pluginmeta.__plugins[key]

  def __iter__(self):
    return pluginmeta.__plugins.__iter__()

  def __len__(self):
    return len(pluginmeta.__plugins)

  def __contains__(self,item):
    return item in pluginmeta.__plugins

  def __str__(self):
    return str(pluginmeta.__plugins)

  def items(self):
    return pluginmeta.__plugins.items()

  def keys(self):
    return pluginmeta.__plugins.keys()

class plugin(object):
  '''
  A simple plugins decorator.
  Decorator takes a namespace as input.

  Example:
    @plugin('omg')
    def hai():
      ...

    @plugin('ican','haz')
    def cheeseburger():
      ...
    
    plugin
    {
      'omg': {'hai': <function hai at ...>},
      'ican': {'cheeseburger': <function cheeseburger at ...>},
      'haz': {'cheeseburger': <function cheeseburger at ...>},
    }
  '''
  __metaclass__ = pluginmeta

  def __init__(self,*spaces): pass

  def __call__(self,f):
    for space in self.spaces:
      try: plugin[space][f.__name__] = f
      except KeyError: plugin[space] = {f.__name__ : f}
    return f
