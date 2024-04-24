This README serves as a quick start guide and describes the fields and values of the input files as well as the produced output csv files. The descriptions have been adapted from the respective resources.

# Run the project

# Data Description
## Input

### verkehrsmittelwahl2021.csv
- NUTS1: AT1 for Eastern Austria  
- NUTS2: AT13 for Federal State Vienna
- NUTS3: AT130 for City of Vienna
- DISTRICT_CODE: 9 for Vienna
- SUB_DISTRICT_CODE: 0 as not used
- YEAR: Year for which the share applies
- BICYCLE: Share of bicycles
- BY_FOOT: Share of pedestrians
- CAR: Share of cars
- MOTORCYCLE: Share of motorcycles
- PUBLIC_TRANSPORT: Share of public transport

### estat_env_ac_co2fp.tsv

- C_ORIG: place of origin, where the emissions take place
- NACE_R2: economic activity which actually emits CO2 emissions
- C_DEST: the geographical entity where the final demand (or consumption) takes place
- NA_ITEM: this dimension denotes the type of final demand in the country of destination causing the carbon footprint. This dimension distinguishes 5 categories of final demand: final consumption expenditure of general government, final consumption expenditure of households, final consumption expenditure of NPISH, gross fixed capital formation, changes in inventories and acquisitions less disposals of valuables. For private households, this category is not applicable
- TIME: reference years covered by the dataset, starting from 2010
- FREQ: time frequency, data are annual
- UNIT: thousand tonnes of CO2 emissions


## Output

### emissions_data.csv
- YEAR: Year for which the emission applies
- EMISSION: thousand tonnes of CO2 emissions in Austrian households

### result_data.csv
- YEAR: Year for which the emission and shares apply
- BICYCLE: Share of bicycles
- CAR: Share of cars
- PUBLIC_TRANSPORT: Share of public transport 
- BY_FOOT: Share of pedestrians
- OTHER: Share of rest of means of transports
- EMISSION: thousand tonnes of CO2 emissions in Austrian households