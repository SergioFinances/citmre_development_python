## cITMre

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

## Parameters

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

data = rmre_data(plot_data= True)
data.head()

#>Date
#>1991-12-02    643.42
#>1991-12-03    639.22
#>1991-12-04    635.70
#>1991-12-05    631.51
#>1991-12-06    627.16
```

<img src="https://i.ibb.co/mF5RLb1/README-example-2.png" alt="Example Image" style="width: 1000px; height: 360px;">

In economic or financial research, it is not necessary to take the whole time series; use 
`start_date` and `end_date` under the format "YYYYY-MM_DD" to obtain a specific start and 
end date. For example, we want to get the RMRE from March 18, 2005, to June 26, 2019, in an 
object called `data` simplifying function result.

``` bash
data = rmre_data(start_date = "2005-03-18", end_date = "2019-06-26", plot_data= True)
data.head()

#>Date
#>2005-03-18    2374.46
#>2005-03-22    2371.43
#>2005-03-23    2361.78
#>2005-03-28    2382.30
#>2005-03-29    2397.25
```

<img src="https://i.ibb.co/Q99x7Ny/mkdocs-example2.png" alt="Example Image" style="width: 1000px; height: 360px;">

In some research, the historical volatility is expected to be analysed for advanced econometric
or financial studies. It is possible to use the function `log_return=TRUE` to change the series
to log return based on the formula: $ lr(RMRE) = ln(\frac{Present~value}{Past~Value}) $, in Default the 
series is presented in level data.

``` bash
data_log = rmre_data(start_date = "2005-03-18", end_date = "2019-06-26", log_return = True, plot_data= True)
print(data_log.head())
print(data_log.tail())

#>Date
#>2005-03-22   -0.001277
#>2005-03-23   -0.004078
#>2005-03-28    0.008651
#>2005-03-29    0.006256
#>2005-03-30   -0.001641
#>Name: log_return, dtype: float64

#>Date
#>2019-06-19   -0.006609
#>2019-06-20   -0.004934
#>2019-06-21   -0.014541
#>2019-06-25   -0.003391
#>2019-06-26   -0.001261
#>Name: log_return, dtype: float64
```

<img src="https://i.ibb.co/9WFDPTj/mkdocs-example3.png" alt="Example Image" style="width: 1000px; height: 360px;">

On some occasions, economic or financial variables do not necessarily use the same time-frequency
of the daily series as in the RMRE. Colombia's GDP (Gross Domestic Product) is quarterly; therefore,
the RMRE daily series must be transformed into a quarterly one. The `frequency` function displays
the RMRE series in monthly (12), quarterly (4) and half-yearly (2) series. By default, the daily
series will be (365). Frequencies can also be transformed to log_return.

The `type` function can approximate the series on mean or last date data. When `type = "mean" is used,
the series gets the average value of the series in frequency. If `type = "last_date" is used, the 
last data of the series is used in frequency. By default, the `type` is set to `last_date`.

``` bash
### Monthly RMRE
data = rmre_data(start_date = "2005-03-18", end_date = "2019-06-26", plot_data= True, frequency = 12)
print(data.head())
print(data.tail())

#>Date
#>2005-03-18    2374.46
#>2005-03-22    2371.43
#>2005-03-23    2361.78
#>2005-03-28    2382.30
#>2005-03-29    2397.25
#>Name: rmre, dtype: float64

#>Date
#>2019-06-19    3264.98
#>2019-06-20    3248.91
#>2019-06-21    3202.01
#>2019-06-25    3191.17
#>2019-06-26    3187.15
#>Name: rmre, dtype: float64
```

<img src="https://i.ibb.co/yktpcRY/mkdocs-example4.png" alt="Example Image" style="width: 1000px; height: 360px;">

``` bash
### Quarterly RMRE
data_q = rmre_data(start_date = "2005-03-18", end_date = "2019-06-26", plot_data= True, frequency = 4)
print(data_q.head())
print(data_q.tail())

#>Quarter
#>2005Q1    2376.48
#>2005Q2    2331.81
#>2005Q3    2289.61
#>2005Q4    2282.35
#>2006Q1    2289.98

#>Name: rmre, dtype: float64
#>Quarter
#>2018Q2    2945.09
#>2018Q3    2989.58
#>2018Q4    3275.01
#>2019Q1    3190.94
#>2019Q2    3187.15
#>Name: rmre, dtype: float64
```

<img src="https://i.ibb.co/3Ffh5Gs/mkdocs-example5.png" alt="Example Image" style="width: 1000px; height: 360px;">

``` bash
### Half-year RMRE
data_s = rmre_data(start_date = "2005-03-18", end_date = "2019-06-26", plot_data= True, frequency = 2)
print(data_s.head())
print(data_s.tail())

#>Semester
#>2005-1S    2331.81
#>2005-2S    2282.35
#>2006-1S    2633.12
#>2006-2S    2233.31
#>2007-1S    1958.09
#>Name: rmre, dtype: float64

#>Semester
#>2017-1S    3038.26
#>2017-2S    2971.63
#>2018-1S    2945.09
#>2018-2S    3275.01
#>2019-1S    3187.15
#>Name: rmre, dtype: float64
```

<img src="https://i.ibb.co/9W33HWZ/mkdocs-example6.png" alt="Example Image" style="width: 1000px; height: 360px;">

## Final considerations

This tool can be used for time series analysis with an xts class condition; therefore, the user can
transform the series to ts if any tool conflicts with an xts series.

## References

Source: [Portal de Datos Abiertos](http://www.datos.gov.co/)