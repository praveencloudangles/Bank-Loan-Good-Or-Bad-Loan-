from data_cleaning import data_cleaning
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.graph_objects as go
import io
from PIL import Image

a = []
def data_vis():
    data = data_cleaning()
    print(data)

    column=list(data.columns)
    column_to_remove = ["loan_condition_cat", "term_cat", "recoveries", "interest_payment_cat", "application_type_cat", "annual_inc", "dti"]
    for col_to_remove in column_to_remove:
        column.remove(col_to_remove)

    print(column)

    for i in column:
        fig = px.histogram(data, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        # fig.show()
        fig.write_image(f"{i}_hist.jpg")
        # a.append(fig)
    for i in column:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        fig.write_image(f"{i}.jpg")
        # a.append(fig)

    columns_to_remove=["loan_condition_cat","term_cat", "recoveries", "interest_payment_cat", "application_type_cat", "annual_inc", "dti", "emp_length_int", "grade_cat", "total_rec_prncp"]
    df=data.drop(columns=columns_to_remove,axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    # fig.show()
    fig.write_image("img.jpg")


    return data

data_vis()
