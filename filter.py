import pandas as pd
import gzip
import shutil


# we need data from 2010 - 2021

# ELECTRIC CAR + HYBRID CAR + PASSENGER_CAR
CO2_FOOTPRINT_GZ = "input/estat_env_ac_co2fp.tsv.gz"
# BYCYCLE VS. CAR (in %)
VERKEHRSMITTELWAHL = "input/verkehrsmittelwahl2021.csv"

with gzip.open('input/estat_env_ac_co2fp.tsv.gz', 'rb') as f_in:
    with open('input/unzip_estat_env_ac_co2fp.tsv', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

CO2_FOOTPRINT = "input/unzip_estat_env_ac_co2fp.tsv"

co2_footprint_data = pd.read_csv(CO2_FOOTPRINT,'\t')
# co2 emissions in households in austria in thousand tonnes of CO2 emissions
filtered_co2_footprint_data = co2_footprint_data[co2_footprint_data.iloc[:, 0].str.contains("AT,AT", na=False) & co2_footprint_data.iloc[:, 0].str.contains("HH", na=False)]

# for column in filtered_co2_footprint_data
emission = []
for i in range(1, len(filtered_co2_footprint_data.columns)):
    emission.append(filtered_co2_footprint_data.iloc[0, i])
print(emission)

emissions_data = {
    'YEAR': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'EMISSION': emission
}

# Convert the dictionary to a DataFrame
emission_df = pd.DataFrame(emissions_data)

# Write the DataFrame to a CSV file
emission_df.to_csv('output/emissions_data.csv', index=False)


verkehrsmittelwahl_data = pd.read_csv(VERKEHRSMITTELWAHL, ";")
filtered_verkehrsmittelwahl_data = verkehrsmittelwahl_data[['YEAR' , 'BICYCLE', 'CAR', 'PUBLIC_TRANSPORT', 'BY_FOOT']]
# in %
filtered_verkehrsmittelwahl_data = filtered_verkehrsmittelwahl_data[filtered_verkehrsmittelwahl_data['YEAR'] > 2009]

filtered_verkehrsmittelwahl_data['CAR'] = filtered_verkehrsmittelwahl_data['CAR'].str.replace(',', '.').astype(float)
filtered_verkehrsmittelwahl_data['BICYCLE'] = filtered_verkehrsmittelwahl_data['BICYCLE'].str.replace(',', '.').astype(float)
filtered_verkehrsmittelwahl_data['PUBLIC_TRANSPORT'] = filtered_verkehrsmittelwahl_data['PUBLIC_TRANSPORT'].str.replace(',', '.').astype(float)
filtered_verkehrsmittelwahl_data['BY_FOOT'] = filtered_verkehrsmittelwahl_data['BY_FOOT'].str.replace(',', '.').astype(float)
filtered_verkehrsmittelwahl_data['OTHER'] = 100 - filtered_verkehrsmittelwahl_data['CAR'] - filtered_verkehrsmittelwahl_data['BICYCLE'] - filtered_verkehrsmittelwahl_data['PUBLIC_TRANSPORT'] - filtered_verkehrsmittelwahl_data['BY_FOOT']


result_data = pd.merge(filtered_verkehrsmittelwahl_data, emission_df, on='YEAR')

result_data.to_csv('output/result_data.csv', index=False)