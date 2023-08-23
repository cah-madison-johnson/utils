#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from utils.DataMetrics import DataMetrics
import pandas as pd
class MatrixConsolidation(DataMetrics):
    def __init__(self, table_df, crt_dt_elem,nqnss_dt_elem, title):
        super().__init__(table_df, crt_dt_elem,nqnss_dt_elem)
        self.title = title
   


    def dq_df(self):
        return (super().def_cmplt_df()).mul(self.def_uniq_df())
    
    
    def dataset_score(self):
        result = {}
        result[self.title+'_SCORE']=[round(self.dq_df().mean().mean(),2) * 100]
        for elem in self.crt_dt_elem:
            result[elem+'_SCORE'] = [((self.dq_df()[elem].sum()) / len(self.dq_df())) * 100]        
        dataset_score = (pd.DataFrame(result)).reset_index(drop=True)
        
        return dataset_score
