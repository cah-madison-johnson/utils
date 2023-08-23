#!/usr/bin/env python
# coding: utf-8
import numpy as np
class HelperFunctions:
    def __init__(self, table_df):
        self.table_df  = table_df 
# Completeness function    
    def mplct_cmpltnss_rule(self,d):
#         print(self.table_df)
    
        dat1 = d
        len_df = len(dat1)

        for col in dat1.columns:
            dat1[col] = 1 - (1 - np.where((dat1[col].isna()) | (dat1[col]==''),1,0).sum()/len_df)*np.where((dat1[col].isna()) | (dat1[col]==''),1,0)

        return dat1 

# Uniqueness function

    def mplct_nqnss_rule(self,d):
    
        dat1 = d
        len_df = len(dat1)

        for col in dat1.columns:
            dat1[col] = 1 - (dat1[col].nunique()/len_df)*(1 - dat1[col].nunique()/len_df)

        return dat1
