# Packages
import pandas as pd
import requests
import json
import numpy as np
import re
from datetime import datetime
import plotly.express as px

def rmre_data(start_date=None, end_date=None, log_return=False, plot_data=False, frequency=365, type="last_date"):

    """
    The cITMre library—Colombian Index Tool (Market Rate Exchange)—responds to the researcher's economics and financial sciences needs to use the colombian Representative Market Rate Exchange. This package presents a practical solution for downloading the RMRE database. 

    The tool allows us to obtain:

    * Download the data series in daily, monthly, quarterly, and half-yearly frequencies.
    * Can split the time series through start and end function
    * Can transform the data set in log returns or level
    * Can make a Dynamic graph through Plotly, or if is your preference can make a normal plot.

    # Motivation

    Obtaining information from the Colombian RMRE is relatively straightforward; the search in the official state database Portal de Datos Abiertos <www.datos.gov.co> allows the data to be downloaded in .xls or .csv. In economics or financial sciences, obtaining and loading this information into R can be frustrating, forcing many users to create a routine function linked to the database limited to the user's expertise. Thus, this tool aims to facilitate both the loading of data and the use of essential RMRE time series analysis tools.

    Note: The information discounts weekends and holidays; the function approximates the nearest trade date.

    # Parameters:

    * start_date An initial date in the "YYYY-MM-DD" type; by default, the series starts on the first date of the resource
    * end_date A final date in the "YYYY-MM-DD" form; by default, it shows the updated last date on the resource.
    * log_return Show the log return of the RMRE (Representative Market Rate Exchange) dataset; if it is TRUE, show the log return dataset; if it is FALSE, show the level dataset; in default, show the level dataset
    * plot_data Show a Plotly linear graph data set; by default, the argument is false, and the graph is built in the Viewer option. You can use the basic plot if the user does not use the plot_data option.
    * frequency Show frequencies for the data set in daily (365), month (12), quarter (4), and half-year (2); in default, the dataset is the daily frequency.
    * type It works only with 12,4,2 frequencies, showing the dataset using the last date ("last_date") or doing a mean ("mean") in the frequency series. By default, the type is "last_date".

    # Applied Example

    If you want to use `citmre`, perform the package installation process using `pip install cITMre=0.1.0` and load the `from citmre.citmre_fun import rmre_data`.
    Once the package is installed, use the `rmre_data()` function to obtain the total RMRE series (the Colombian state has RMRE data since 1991-12-02); the data loaded is an XTS series.

    from citmre.citmre_fun import rmre_data
    import pandas as pd
    pd.head(rmre_data())

    In economic or financial research, it is not necessary to take the whole time series; use `start_date` and `end_date` under the format "YYYYY-MM_DD" to obtain a specific start and end date. For example, we want to get the RMRE from March 18, 2005, to June 26, 2019, in an object called `data` simplifying function result.

    data = rmre_data(start_date = "2005-03-18", end_date = "2019-06-26")
    pd.head(data)

    In some research, the historical volatility is expected to be analysed for advanced econometric or financial studies. It is possible to use the function `log_return=TRUE` to change the series to log return based on the formula: lr(RMRE) = ln(Present Value / Past Value), in Default the series is presented in level data.

    data_log = rmre_data(start_date = "2005-03-18", end_date = "2019-06-26", log_return = true)
    pd.head(data_log)
    pd.tail(data_log)

    On some occasions, economic or financial variables do not necessarily use the same time-frequency of the daily series as in the RMRE. Colombia's GDP (Gross Domestic Product) is quarterly; therefore, the RMRE daily series must be transformed into a quarterly one. The `frequency` function displays the RMRE series in monthly (12), quarterly (4) and half-yearly (2) series. By default, the daily series will be (365). Frequencies can also be transformed to log_return.

    The `type` function can approximate the series on mean or last date data. When `type = "mean" is used, the series gets the average value of the series in frequency. If `type = "last_date" is used, the last data of the series is used in frequency. By default, the `type` is set to `last_date`.

    ##Monthly RMRE
    data_m = rmre_data(start_date = "1998-03-18", end_date = "2019-06-26",frequency = 12)
    pd.head(data_m)
    pd.tail(data_m)

    ##Quarterly RMRE
    data_q = rmre_data(start_date = "1998-03-18", end_date = "2019-06-26",frequency = 4)
    pd.head(data_q)
    pd.tail(data_q)

    ##Half-year RMRE
    data_s = rmre_data(start_date = "1998-03-18", end_date = "2019-06-26",frequency = 2, type = "mean")
    pd.head(data_s)
    pd.tail(data_s)

    Finally, some researchers feel that displaying a dynamic graph increases the analysis and learning methods, which is why the `plot_data` option can display a Plotly line graph, allowing the user to analyse the data through the Viewer (See https://plotly.com/r/line-charts/>). This option works well with the other options of the `rmre_data` function.

    ##Monthly RMRE
    rmre_data(start_date = "1998-03-18", end_date = "2019-06-26",frequency = 12, plot_data = true)

    # Final considerations

    This tool can be used for time series analysis with an xts class condition; therefore, the user can transform the series to ts if any tool conflicts with an xts series.

    # References
    Source: Portal de Datos Abiertos <www.datos.gov.co>   

    """

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
            
            fig.update_layout(autosize=True)
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
            fig.update_layout(autosize=True)
            fig.show()

        return result
    else:
        raise ValueError("Error: Invalid 'frequency' argument. Should be one of 365 12, 4, or 2")