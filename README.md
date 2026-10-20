# Global City Distribution Analysis

## Research question
How are cities distributed across the globe, and which countries hold the
densest urban networks?

## Dataset
- **Source:** GeoNames "cities" dump (CC-BY 4.0) —
  https://download.geonames.org/export/dump/cities500.zip
- **Size:** 3,173,958 city records worldwide.
- **Fields:** country code, city name, region, population, latitude, longitude.
- **Usage permission:** Creative Commons Attribution 4.0 (free to use with attribution).

## Methods and tools
- **Language:** Python 3
- **Libraries:** pandas (data loading and aggregation), matplotlib (plotting)
- **Approach:** load and clean the city records, filter to populated cities,
  then build a global scatter plot and a country-level bar chart.

## Main findings
1. Populated cities cluster strongly along coastlines and in temperate
   latitudes, with dense bands across Europe, South Asia, and East Asia.
2. The United States, China, and India are among the countries with the
   largest recorded number of cities.

## Limitation
The population column is empty for roughly 98% of the records, so any
population-weighted analysis is limited to the small subset of cities that
report a population figure.

## How to run
1. Download `cities500.zip` from the GeoNames link above and extract
   `cities500.txt`, renaming it to `world_cities_pop.csv` in this folder.
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the analysis: `python analysis.py`
4. The script writes `city_scatter.png` and `city_histogram.png`.

## Visualizations
- `city_scatter.png` — global scatter of all populated cities.
- `city_histogram.png` — top 20 countries by number of cities.
