## Getting started

The cITMre library—Colombian Index Tool (Market Rate Exchange)—responds to the researcher's 
economics and financial sciences needs to use the colombian Representative Market Rate Exchange. 
This package presents a practical solution for downloading the RMRE database. 

The tool allows us to obtain:

* Download the data series in daily, monthly, quarterly, and half-yearly frequencies.
* Can split the time series through start and end function
* Can transform the data set in log returns or level
* Can make a Dynamic graph through Plotly, or if is your preference can make a normal plot.

## Motivation

Obtaining information from the Colombian RMRE is relatively straightforward; the search in the 
official state database Portal de Datos Abiertos <www.datos.gov.co> allows the data to be 
downloaded in .xls or .csv. In economics or financial sciences, obtaining and loading this 
information into R can be frustrating, forcing many users to create a routine function linked 
to the database limited to the user's expertise. Thus, this tool aims to facilitate both the 
loading of data and the use of essential RMRE time series analysis tools.

Note: The information discounts weekends and holidays; the function approximates the nearest 
trade date.

## Parameters:

| Parameter     | Description                                                                                           | Default Value       |
|---------------|-------------------------------------------------------------------------------------------------------|---------------------|
| start_date    | An initial date in the "YYYY-MM-DD" type; by default, the series starts on the first date of the resource. | First day of the resource |
| end_date      | A final date in the "YYYY-MM-DD" form; by default, it shows the updated last date on the resource.    | Updated last date on the resource |
| log_return    | Show the log return of the RMRE (Representative Market Rate Exchange) dataset; if it is TRUE, show the log return dataset; if it is FALSE, show the level dataset; in default, show the level dataset. | FALSE |
| plot_data     | Show a Plotly linear graph data set; by default, the argument is false, and the graph is built in the Viewer option. You can use the basic plot if the user does not use the plot_data option. | FALSE |
| frequency     | Show frequencies for the data set in daily (365), month (12), quarter (4), and half-year (2); in default, the dataset is the daily frequency. | Daily (365) |
| type          | It works only with 12, 4, 2 frequencies, showing the dataset using the last date ("last_date") or doing a mean ("mean") in the frequency series. By default, the type is "last_date". | "last_date" by default |

## Applied Example

If you want to use `citmre`, perform the package installation process using `pip install 
cITMre=0.1.0` and load the `from citmre.citmre_fun import rmre_data`.
Once the package is installed, use the `rmre_data()` function to obtain the total RMRE series 
(the Colombian state has RMRE data since 1991-12-02); the data loaded is an XTS series.

``` bash
from citmre.citmre_fun import rmre_data
import pandas as pd
pd.head(rmre_data())
```

In economic or financial research, it is not necessary to take the whole time series; use 
`start_date` and `end_date` under the format "YYYYY-MM_DD" to obtain a specific start and 
end date. For example, we want to get the RMRE from March 18, 2005, to June 26, 2019, in an 
object called `data` simplifying function result.

data = rmre_data(start_date = "2005-03-18", end_date = "2019-06-26")
pd.head(data)

In some research, the historical volatility is expected to be analysed for advanced econometric
or financial studies. It is possible to use the function `log_return=TRUE` to change the series
to log return based on the formula: lr(RMRE) = ln(Present Value / Past Value), in Default the 
series is presented in level data.

data_log = rmre_data(start_date = "2005-03-18", end_date = "2019-06-26", log_return = true)
pd.head(data_log)
pd.tail(data_log)

On some occasions, economic or financial variables do not necessarily use the same time-frequency
of the daily series as in the RMRE. Colombia's GDP (Gross Domestic Product) is quarterly; therefore,
the RMRE daily series must be transformed into a quarterly one. The `frequency` function displays
the RMRE series in monthly (12), quarterly (4) and half-yearly (2) series. By default, the daily
series will be (365). Frequencies can also be transformed to log_return.

The `type` function can approximate the series on mean or last date data. When `type = "mean" is used,
the series gets the average value of the series in frequency. If `type = "last_date" is used, the 
last data of the series is used in frequency. By default, the `type` is set to `last_date`.

### Monthly RMRE
data_m = rmre_data(start_date = "1998-03-18", end_date = "2019-06-26",frequency = 12)
pd.head(data_m)
pd.tail(data_m)

### Quarterly RMRE
data_q = rmre_data(start_date = "1998-03-18", end_date = "2019-06-26",frequency = 4)
pd.head(data_q)
pd.tail(data_q)

### Half-year RMRE
data_s = rmre_data(start_date = "1998-03-18", end_date = "2019-06-26",frequency = 2, type = "mean")
pd.head(data_s)
pd.tail(data_s)

Finally, some researchers feel that displaying a dynamic graph increases the analysis and learning
methods, which is why the `plot_data` option can display a Plotly line graph, allowing the user to
analyse the data through the Viewer. This option works well
with the other options of the `rmre_data` function.

### Monthly RMRE
rmre_data(start_date = "1998-03-18", end_date = "2019-06-26",frequency = 12, plot_data = true)

# Final considerations

This tool can be used for time series analysis with an xts class condition; therefore, the user can
transform the series to ts if any tool conflicts with an xts series.

## References
Source: Portal de Datos Abiertos <www.datos.gov.co> 