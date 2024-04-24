import pandas as pd;
import matplotlib.pyplot as plt


visualise_data = pd.read_csv("result_data.csv", delimiter=",")

fig, ax1 = plt.subplots()

# Plot bars
ax1.bar(visualise_data['YEAR'], visualise_data['CAR'], label='CAR', color='red')
ax1.bar(visualise_data['YEAR'], visualise_data['BY_FOOT'], bottom=visualise_data['CAR'], label='FOOT', color='skyblue')
ax1.bar(visualise_data['YEAR'], visualise_data['BICYCLE'], bottom=visualise_data['CAR'] + visualise_data["BY_FOOT"], label='BICYCLE', color='green')
ax1.bar(visualise_data['YEAR'], visualise_data['PUBLIC_TRANSPORT'], bottom=visualise_data['CAR'] + visualise_data["BY_FOOT"] + visualise_data['BICYCLE'], label='PUBLIC TRANSPORT', color='orange')
ax1.bar(visualise_data['YEAR'], visualise_data['OTHER'], bottom=visualise_data['CAR'] + visualise_data["BY_FOOT"] + visualise_data['BICYCLE'] + visualise_data['PUBLIC_TRANSPORT'], label='OTHER', color='gray')


# labels and title for the first y-axis (left)
ax1.set_ylim(0, 100)
ax1.set_xlabel('Year')
ax1.set_ylabel('Percentage')
ax1.set_title('Percentage Distribution of Modes of Transport')

# secondary y-axis (right) for 'EMISSION'
ax2 = ax1.twinx()
ax2.plot(visualise_data['YEAR'], visualise_data['EMISSION'], color='blue', marker='o', linestyle='-', label='EMISSION')
ax2.set_ylabel('Emission (thousands of tons)')

# Set legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.savefig('output/transport_emission.png')

correlation = visualise_data['BICYCLE'].corr(visualise_data['EMISSION'])
print(correlation)

plt.figure(figsize=(8, 6))
plt.scatter(visualise_data['BICYCLE'], visualise_data['EMISSION'], color='blue')
plt.title('Correlation between BICYCLE and EMISSION')
plt.xlabel('BICYCLE')
plt.ylabel('EMISSION')
plt.grid(True)

# Annotate correlation coefficient
plt.text(visualise_data['BICYCLE'].min(), visualise_data['EMISSION'].max(), f'Correlation: {correlation:.2f}', verticalalignment='top')

plt.savefig('output/correlation.png')