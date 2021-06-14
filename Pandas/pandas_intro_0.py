# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 11:53
# @Author  : Hu-y
# @File    : pandas_intro_0.py
# 1.  How to import pandas and check the version?
import pandas as pd
import numpy as np
print(pd.__version__)
print(pd.show_versions(as_json=True))
"""
output:
0.20.3
{'system': {'commit': None, 'python': '3.6.3.final.0', 'python-bits': 64, 'OS': 'Windows', 'OS-release': '10', 'machine': 'AMD64', 'processor': 'Intel64 Family 6 Model 158 Stepping 9, GenuineIntel', 'byteorder': 'little', 'LC_ALL': 'None', 'LANG': 'None', 'LOCALE': 'None.None'}, 'dependencies': {'pandas': '0.20.3', 'pytest': '3.2.1', 'pip': '9.0.1', 'setuptools': '36.5.0.post20170921', 'Cython': '0.26.1', 'numpy': '1.13.3', 'scipy': '0.19.1', 'xarray': None, 'IPython': '6.1.0', 'sphinx': '1.6.3', 'patsy': '0.4.1', 'dateutil': '2.6.1', 'pytz': '2017.2', 'blosc': None, 'bottleneck': '1.2.1', 'tables': '3.4.2', 'numexpr': '2.6.2', 'feather': None, 'matplotlib': '2.1.0', 'openpyxl': '2.4.8', 'xlrd': '1.1.0', 'xlwt': '1.3.0', 'xlsxwriter': '1.0.2', 'lxml': '4.1.0', 'bs4': '4.6.0', 'html5lib': '0.999999999', 'sqlalchemy': '1.1.13', 'pymysql': None, 'psycopg2': None, 'jinja2': '2.9.6', 's3fs': None, 'pandas_gbq': None, 'pandas_datareader': None}}
None
"""

# 2.How to create a series from a list, numpy array and dict?