## Description

Downloads the Representative Market Rate Exchange (RMRE) from the [www.datos.gov.co](https://www.datos.gov.co) source. Allows setting the data series in time frequencies, splitting the time series through start and end functions, transforming the data set in log returns or levels, and making a Dynamic graph.

## Example

```bash
pip install cITMre=0.1.0
from citmre.citmre_fun import rmre_data

# Show full series dataset
rmre_serie = rmre_data()

# Show monthly dataset with Plotly Graph
rmre_splited = rmre_data(frequency=12, log_return=False, plot_data=True)

# Show quaterly log_return dataset with Plotly Graph
rmre_splited = rmre_data(frequency=4, log_return=True, plot_data=True, type="mean")

# Show splited log return dataset
rmre_splited = rmre_data('2000-01-01','2023-12-31', log_return=True)
#> "Warning: The information will be obtained from the next business day, as the desired date is a holiday or weekend."
```
<img src="https://i.ibb.co/mF5RLb1/README-example-2.png" alt="Example Image" style="width: 1000px; height: 360px;">