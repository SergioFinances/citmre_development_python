## Desciption

The Colombian Index Tool (Market Rate Exchange) package downloads the 
Colombian Market Rate from the source: [Portal de Datos Abiertos](https://www.datos.gov.co/Econom-a-y-Finanzas/TRM/ceyp-9c7c/data), for
direct use in Python.

<img src="https://i.ibb.co/s6db4M4/logo.png" width="100">

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