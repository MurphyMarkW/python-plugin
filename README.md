python-plugin
=============

A minimalistic plugin system for python using decorators.

Example:
```
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
```
