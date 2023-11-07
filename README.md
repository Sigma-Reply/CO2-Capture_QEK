# Material Characterisation for CO2 Capture

## Files description

The algorithm consists in 3 parts:

1. Projection.ipynb explains the projection procedure in 2D
2. MOF_analysis.ipynb studies the dynamics of the molecular structure on a neutral atom device.
3. MOF-CO2/MofCO2.ipynb treats the classical regression algorithm


The code contained in MOF-CO2 is taken from ref [5] https://doi.org/10.1038/s42004-023-01009-x (https://github.com/ibarisorhan/MOF-CO2). The original notebook is indicated by "MofCo2_origin.ipynb",
while it has been restricted to the 38 MOF dataset of less than 25 atoms in  "MofCo2.ipynb". The decent accuracy obtained although the strong dataset reduction is interesting in the context of a POC.

The dataset study with statistics and plots can be found under DataSetStats-complexity.ipynb. It also contains a complexity analysis confronted to the dataset at hands which as been reported in the excel sheet.