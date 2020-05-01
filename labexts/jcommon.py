import os, sys, re, importlib, json, datetime, glob, platform, matplotlib, dateutil
import numpy as np
from IPython.display import HTML
import pandas as pd
from datetime import timedelta;
from collections import defaultdict
from pylab import rcParams
import matplotlib.pyplot as plt
import urllib.request;
from random import randint
from collections import defaultdict
from pylab import rcParams
rcParams['figure.figsize'] = 13, 5
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_colwidth', 1024)
pd.set_option('display.max_rows', 6)

params = {'legend.fontsize': 'small',
          'figure.figsize': (4, 3),
          'axes.titlesize':'medium',
         'axes.labelsize': 'x-small',
         'xtick.labelsize':'x-small',
         'ytick.labelsize':'x-small'}
matplotlib.pyplot.rcParams.update(params)

#-----------------------------------------------------------------------------------
class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]
#-----------------------------------------------------------------------------------
def readFile(file):
    with open(file, "rb") as f:
        c = f.read().decode().replace('\r\n', '\n')
        return c;
#-----------------------------------------------------------------------------------
def jlog(*args, debug=False, end=' ', **kwargs):
    if (not debug or 'debug' in kwargs and not kwargs(debug) ):
        return;

    for a in args:
        print(a, end=end)
    for k,v in kwargs.items():
        print ("%s = %s" % (k, v))
#-----------------------------------------------------------------------------------
