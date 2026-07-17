#                 IMPORT LIBRARIES

import streamlit as st
import pandas as pd


#                  LOAD DATASETS

# @st.cache_data(show_spinner=False)
def load_data():
    """
    Load Exoplanet and Asteroid datasets.

    Returns:
        exo_df (pd.DataFrame): Cleaned Exoplanet dataset
        asteroid_df (pd.DataFrame): Cleaned Asteroid dataset
    """

    exo_df = pd.read_csv(
        "Data/clean_2_exo_planet_data.csv"
    )

    asteroid_df = pd.read_csv(
        "Data/clean_Near_earth_object_data.csv"
    )



    mapping = {"Yes": 1, "No": 0}

    exo_df["habitable_zone_flag"] = exo_df["habitable_zone_flag"].str.strip().map(mapping)
    exo_df["multi_planet_system"] = exo_df["multi_planet_system"].str.strip().map(mapping)
    return exo_df, asteroid_df