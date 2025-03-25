import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import pandas as pd
import numpy as np
import rasterio as rasterio 



class Climatechangeanalysis:
    def __init__(self, temperature_excel_file, shp_file_path, precip_for_climate):
        self.administrative_boundaries = gpd.read_file(shp_file_path)
        self.temperature_data = pd.read_excel(temperature_excel_file) 
        src = rasterio.open(precip_for_climate)
        self.precipitation_data = src.read(1) 
        
    '''def info_climatechange(self):
        #This function
        # Extract available years from the dataset
        available_years = [int(col) for col in self.temperature_data.columns[2:] if str(col).isdigit()]

        # Define groups dynamically
        groups = {"Before 2011": [year for year in available_years if year < 2011]}

        # Create decade groups
        for year in range(2011, max(available_years) + 1, 10):
            decade_label = f"{year}-{min(year+9, max(available_years))}"
            groups[decade_label] = [y for y in available_years if year <= y < year + 10]

        # Compute averages
        grouped_avg = pd.DataFrame()
        grouped_avg["District"] = self.temperature_data["District Name"]
        grouped_avg["Before 2011"] = self.temperature_data["2011"]
        
        for group, years in groups.items():
            year_cols = [str(year) for year in years]
            grouped_avg[group] = self.temperature_data[year_cols].mean(axis=1)

        # Merge with geographic data
        merged_data = self.administrative_boundaries.merge(grouped_avg, left_on='DISTRICT', right_on='District', how='left')

        # Create subplots
        fig, axes = plt.subplots(5, 2, figsize=(15, 25))
        axes = axes.flatten()  # Flatten the 5x2 array to 1D for easier iteration

        # Plot each time period in a separate subplot
        for i, (group_name, _) in enumerate(groups.items()):
            if i >= len(axes):  # Ensure we don't exceed subplot count
                break
                
            ax = axes[i]
            merged_data.plot(column=group_name, cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, legend_kwds={'label': "Temperature (°C)"})
            ax.set_title(f'Avg Temperature {group_name}', fontsize=10)
            ax.set_axis_off()

        plt.tight_layout()
        plt.show()

        #Precipitation analysis for climate change analysis over time
        plt.figure(figsize = (8,8))
        plt.imshow(self.precipitation_data, cmap = 'cool')
        plt.colorbar(label = 'Precipitation Index')
        plt.title('Climate analysis of Nepal')
        plt.show()'''

    def EDA_analysis(self):
        selected_districts = ["BANKE", "KATHMANDU", "KASKI", "MUSTANG"]

#  Reshape data from wide to long format
        melted_data = pd.melt(
            self.temperature_data,
            id_vars=["District Name"],
            var_name="Year",
            value_name="Temperature",
            value_vars=[col for col in self.temperature_data.columns if col != "District Name"]
        )

# Convert Year to numeric (assuming columns are named '1981', '1982', etc.)
        melted_data["Year"] = pd.to_numeric(melted_data["Year"], errors='coerce')

# Filter for selected districts
        melted_data = melted_data[melted_data["District Name"].isin(selected_districts)]

# 2. Create multivariate scatterplot
        plt.figure(figsize=(14, 8))

# Option A: Color-coded by district with regression lines
        sns.lmplot(
            data=melted_data,
            x="Year",
            y="Temperature",
            hue="District Name",
            height=8,
            aspect=1.5,
            scatter_kws={"s": 60, "alpha": 0.7},
            line_kws={"lw": 2}
        )

        plt.title("Temperature Trends Across Selected Districts", fontsize=16, pad=20)
        plt.xlabel("Year", fontsize=14)
        plt.ylabel("Temperature (°C)", fontsize=14)
        plt.grid(alpha=0.3)

# Add correlation annotations
        for district in selected_districts:
            subset = melted_data[melted_data["District Name"] == district]
            corr = subset[["Year", "Temperature"]].corr().iloc[0, 1]
            plt.text(
                subset["Year"].median(),
                subset["Temperature"].max() - 0.5,
                f"{district}: r = {corr:.2f}",
                ha="center",
                bbox=dict(facecolor='white', alpha=0.8)
            )
        
        plt.tight_layout()
        plt.show()

climatedata = Climatechangeanalysis(
    'nepal_climate_data/data/District_avg_annual_temp_nepal.xlsx', 
    'nepal_climate_data/data/Local Unit/local_unit.shp',
    'nepal_climate_data/nepal_precipitation_2020.tif'
)
#climatedata.info_climatechange()
climatedata.EDA_analysis()