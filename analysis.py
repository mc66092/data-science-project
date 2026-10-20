#!/usr/bin/env python3
"""Global City Distribution Analysis

Loads the GeoNames "cities" dataset (world_cities_pop.csv) and produces two
visualizations: a global scatter of populated cities and a bar chart of the
countries with the most cities.

Dataset source (GeoNames, CC-BY 4.0):
https://download.geonames.org/export/dump/cities500.zip
Place the extracted `cities500.txt` (renamed to `world_cities_pop.csv`) in
this folder, or set WORLD_CITIES_PATH to its location.
"""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WORLD_CITIES_PATH = os.environ.get("WORLD_CITIES_PATH", "world_cities_pop.csv")

COLUMNS = ["Country", "City", "AccentCity", "Region", "Population", "Latitude", "Longitude"]


def load(path):
    df = pd.read_csv(path, usecols=COLUMNS, low_memory=False)
    df["lat"] = df["Latitude"].astype(float)
    df["lon"] = df["Longitude"].astype(float)
    return df


def main():
    df = load(WORLD_CITIES_PATH)
    print(f"Loaded {len(df):,} city records")

    # Keep only cities with a recorded population for the scatter plot.
    populated = df[df["Population"] > 0].copy()
    print(f"Populated cities: {len(populated):,}")

    # --- Visualization 1: global scatter of populated cities ---
    fig, ax = plt.subplots(figsize=(11, 6), dpi=110)
    ax.scatter(
        populated["lon"], populated["lat"],
        s=0.4, c="tab:blue", alpha=0.35, linewidths=0,
    )
    ax.set_title("Global Distribution of Populated Cities")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_xlim(-180, 180)
    ax.set_ylim(-60, 85)
    fig.tight_layout()
    fig.savefig("city_scatter.png")
    plt.close(fig)

    # --- Visualization 2: countries with the most cities ---
    top = df["Country"].value_counts().head(20).sort_values()
    fig, ax = plt.subplots(figsize=(9, 7), dpi=110)
    ax.barh(top.index, top.values, color="tab:green")
    ax.set_title("Top 20 Countries by Number of Cities")
    ax.set_xlabel("Number of cities")
    fig.tight_layout()
    fig.savefig("city_histogram.png")
    plt.close(fig)

    print("Wrote city_scatter.png and city_histogram.png")


if __name__ == "__main__":
    main()
