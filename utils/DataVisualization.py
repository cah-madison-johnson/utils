#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# from utils.MatrixConsolidation import MatrixConsolidation
import pandas as pd
import plotly.graph_objects as go

class DataVisualization:
    def __init__(self, dataset_score,title):
        self.dataset_score = dataset_score
        self.title = title
        
   
    def fig_card(self):
        txt = "Dataset Score<br><span style='font-size:0.8em;color:gray'>{title}</span>"
    
        fig_card = go.Figure(go.Indicator(
        mode = "number",
        value = self.dataset_score.iloc[0].iloc[0],
        number = {'suffix': "%"},
        title = {"text": txt.format(title = self.title)},
        ))

        fig_card.update_layout(paper_bgcolor = "lightgray")

        fig_card.show()
        
