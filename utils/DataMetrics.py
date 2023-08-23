#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import numpy as np

from utils.HelperFunctions import HelperFunctions

class DataMetrics(HelperFunctions):
    def __init__(self, table_df, crt_dt_elem,nqnss_dt_elem):
        super().__init__(table_df)
        self.crt_dt_elem = crt_dt_elem
        self.nqnss_dt_elem = nqnss_dt_elem
 
    def default_df(self):
        return pd.DataFrame(1, index=np.arange(len(self.table_df)), columns=(self.table_df).columns)
    
#     Missing Data Matrix
    def def_cmplt_df(self):
        cmplt_df = ((self.table_df).filter(self.crt_dt_elem).pipe(self.mplct_cmpltnss_rule))
        def_cmplt_df = self.default_df().copy()
        def_cmplt_df[self.crt_dt_elem] = cmplt_df 

        return def_cmplt_df
#     Uniqueness Data Matrix
    def def_uniq_df(self):
        def_uniq_df = self.default_df().copy()
        def_uniq_df[self.nqnss_dt_elem] = self.table_df.filter(self.nqnss_dt_elem).pipe(self.mplct_nqnss_rule)
        return def_uniq_df