# Packages
import pandas as pd
import requests
import json
import numpy as np
import re
from datetime import datetime
import plotly.express as px

def rmre_data(start_date=None, end_date=None, log_return=False, plot_data=False, frequency=365, type="last_date"):

    def calculate_semester(date):
        if date.month <= 6:
            return f"{date.year}-1S"
        else:
            return f"{date.year}-2S"

    url = "https://www.datos.gov.co/resource/ceyp-9c7c.json?$limit=1000000"
    response = requests.get(url)
    json_data = response.json()
    df_data = pd.DataFrame(json_data)
    df_data['vigenciadesde'] = pd.to_datetime(df_data['vigenciadesde'], format='%Y-%m-%dT%H:%M:%S.%f')
    df_data['vigenciahasta'] = pd.to_datetime(df_data['vigenciahasta'], format='%Y-%m-%dT%H:%M:%S.%f')

    if start_date is None:
        start_date = df_data['vigenciadesde'].min().strftime('%Y-%m-%d')
    if end_date is None:
        end_date = df_data['vigenciahasta'].max().strftime('%Y-%m-%d')

    if not isinstance(start_date, str) or not re.match(r'^\d{4}-\d{2}-\d{2}$', start_date):
        raise ValueError("Error: 'start_date' should be in 'year-month-day' format")
    if not isinstance(end_date, str) or not re.match(r'^\d{4}-\d{2}-\d{2}$', end_date):
        raise ValueError("Error: 'end_date' should be in 'year-month-day' format")
    if start_date > end_date:
        raise ValueError("Error: 'start_date' is greater than 'end_date'")
    if type not in ["mean", "last_date"]:
        raise ValueError("Error: 'type' must be 'mean' or 'last_date'")

    df_filtered = df_data[(df_data['vigenciahasta'] >= start_date) & (df_data['vigenciahasta'] <= end_date)]
    df_filtered = df_filtered[['vigenciahasta', 'valor']]
    df_filtered['valor'] = pd.to_numeric(df_filtered['valor'], errors='coerce')
    df_filtered.dropna(inplace=True)
    df_filtered = df_filtered.rename(columns={'vigenciahasta': 'Date', 'valor': 'rmre'})
    df_filtered.reset_index(drop=True, inplace=True)

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')    

    if start_date.isoweekday() > 5 or end_date.isoweekday() > 5:
        print("Warning: The information will be obtained from the next business day, as the desired date is a holiday or weekend.")

    if log_return:
        df_filtered['log_return'] = np.log(df_filtered['rmre'] / df_filtered['rmre'].shift(1))
        df_filtered.dropna(inplace=True)

    if frequency == 365:
        if plot_data:
            fig = px.line(df_filtered, x='Date', y='log_return' if log_return else 'rmre',
                          title='Log Return' if log_return else 'RMRE')
            fig.show()
        return df_filtered.set_index('Date')['log_return' if log_return else 'rmre']

    elif frequency in [12, 4, 2]:
        if frequency == 12:
            df_filtered['Month'] = df_filtered['Date'].dt.to_period('M').astype(str)
        elif frequency == 4:
            df_filtered['Quarter'] = df_filtered['Date'].dt.to_period('Q').astype(str)
        elif frequency == 2:
            df_filtered['Semester'] = df_filtered['Date'].apply(calculate_semester)

        if log_return:
            result = df_filtered.groupby('Month' if frequency == 12 else 'Quarter' if frequency == 4 else 'Semester')[
                'log_return'].agg('mean' if type == 'mean' else 'last')
            result.dropna(inplace=True)
        else:
            result = df_filtered.groupby('Month' if frequency == 12 else 'Quarter' if frequency == 4 else 'Semester')[
                'rmre'].agg('mean' if type == 'mean' else 'last')

        result = result.rename('log_return' if log_return else 'rmre')

        if plot_data:
            y_column = 'rmre' if log_return == False else 'log_return'
            fig = px.line(result.reset_index(),
                          x='Month' if frequency == 12 else 'Quarter' if frequency == 4 else 'Semester',
                          y=y_column,
                          title='Mean Log Return' if type == 'mean' else 'Last Log Return')
            fig.show()

        return result
    else:
        raise ValueError("Error: Invalid 'frequency' argument. Should be one of 365 12, 4, or 2")