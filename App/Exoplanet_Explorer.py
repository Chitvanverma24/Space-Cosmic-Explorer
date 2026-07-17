#                  IMPORT LIBRARIES

import streamlit as st
import pandas as pd
from Utils.theme import page_header
from Utils.data_load import load_data

#               EXOPLANET EXPLORER PAGE


def exoplanet_explorer_page():

    
    #                  LOAD DATA
    

    exo, asteroid = load_data()

    
    #                  PAGE HEADER
    

    page_header(
        "🪐 SPACE COSMIC EXPLORER",
        "🪐 Exoplanet Explorer",
        "Explore thousands of confirmed exoplanets beyond our Solar System."
    )

    st.divider()

    
    #                   SEARCH BAR
    

    search = st.text_input(

        "🔍 Search Exoplanet",

        placeholder="Enter planet name..."

    )

    # Search Filter

    if search:

        exo = exo[
            exo["planet_name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    # 
    # #                    FILTERS
    # 

    # planet_type = st.selectbox(

    #     "Planet Type",

    #     ["All"] + sorted(exo["planet_type"].unique())

    # )

    # discovery_method = st.selectbox(

    #     "Discovery Method",

    #     ["All"] + sorted(exo["discovery_method"].unique())

    # )

    # star_type = st.selectbox(

    #     "Host Star Type",

    #     ["All"] + sorted(exo["star_type"].unique())

    # )

    # distance_category = st.selectbox(

    #     "Distance Category",

    #     ["All"] + sorted(exo["Distance_category"].unique())

    # )

    # orbit_category = st.selectbox(

    #     "Orbit Category",

    #     ["All"] + sorted(exo["Orbit_category"].unique())

    # )

    # habitable = st.selectbox(

    #     "Habitable Zone",

    #     ["All", "Yes", "No"]

    # )

    # 
    # #                 APPLY FILTERS
    # 

    # exo = exo.copy()

    # if planet_type != "All":

    #     exo = exo[
    #         exo["planet_type"] == planet_type
    #     ]

    # if discovery_method != "All":

    #     exo = exo[
    #         exo["discovery_method"] == discovery_method
    #     ]

    # if star_type != "All":

    #     exo = exo[
    #         exo["star_type"] == star_type
    #     ]

    # if distance_category != "All":

    #     exo = exo[
    #         exo["Distance_category"] == distance_category
    #     ]

    # if orbit_category != "All":

    #     exo = exo[
    #         exo["Orbit_category"] == orbit_category
    #     ]

    # if habitable == "Yes":

    #     exo = exo[
    #         exo["habitable_zone_flag"] == 1
    #     ]

    # elif habitable == "No":

    #     exo = exo[
    #         exo["habitable_zone_flag"] == 0
    #     ]

    
    #                 MAIN LAYOUT
    

    left_panel, right_panel = st.columns(

        [4, 1],

        gap="large"

    )

    with left_panel:

     
        #                   KPI CALCULATIONS
     

        total_planets  = len(exo)

        average_radius = exo["planet_radius_earth"].mean()

        average_temperature = exo["Planet_temperature"].mean()

        average_orbit = exo["orbit_period_days"].mean()

        habitable_planets = (
            exo["habitable_zone_flag"] == 1
        ).sum()

     
        #                     KPI CARDS
     

        kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

        with kpi1:

            st.metric(
                "🪐 Exoplanets",
                f"{total_planets:,}"
            )

        with kpi2:

            st.metric(
                "🌍 Avg Radius",
                f"{average_radius:.1f}R⊕"
            )

        with kpi3:

            st.metric(
                "🌡 Avg Temp",
                f"{average_temperature:.0f} K"
            )

        with kpi4:

            st.metric(
                "🛰 Avg Orbit Day",
                f"{average_orbit:.0f}"
            )

        with kpi5:

            st.metric(
                "🌱 Habitable",
                f"{habitable_planets:,}"
            )

        st.divider()

     
        #                 PLANET SELECTOR
     

        st.subheader("🪐 Select Exoplanet")

        selected_planet = st.selectbox(

            "Choose a Planet",

            exo["planet_name"].sort_values().unique(),

            label_visibility="collapsed"

        )

        st.divider()

     
        #                 EXOPLANET DATABASE
     

        # st.subheader("📋 Exoplanet Database")

        # table = exo[

        #     [

        #         "planet_name",

        #         "host_star",

        #         "planet_type",

        #         "star_type",

        #         "Planet_temperature",

        #         "planet_radius_earth",

        #         "planet_mass_earth",

        #         "orbit_period_days",

        #         "Distance_category",

        #         "Discover_year"

        #     ]

        # ].copy()

        # table.columns = [

        #     "Planet Name",

        #     "Host Star",

        #     "Planet Type",

        #     "Star Type",

        #     "Temperature (K)",

        #     "Radius (R⊕)",

        #     "Mass (M⊕)",

        #     "Orbit (Days)",

        #     "Distance",

        #     "Discovery Year"

        # ]

        # st.dataframe(

        #     table,

        #     use_container_width=True,

        #     hide_index=True,

        #     height=450

        # )

        # st.divider()

     
        #              SELECTED PLANET DATA
     

        planet = exo[exo["planet_name"] == selected_planet].iloc[0]

     
        #                PLANET DETAILS
     

        st.subheader("🪐 Planet Information")

        col1, col2 = st.columns(2)

     
        #             GENERAL INFORMATION
     

        with col1:

            st.markdown("### 🌍 General Information")

            st.write(f"**Planet Name :** {planet['planet_name']}")

            st.write(f"**Host Star :** {planet['host_star']}")

            st.write(f"**Planet Type :** {planet['planet_type']}")

            st.write(f"**Star Type :** {planet['star_type']}")

            st.write(f"**Discovery Year :** {int(planet['Discover_year'])}")

     
        #           SCIENTIFIC PROPERTIES
     

        with col2:

            st.markdown("### 🔬 Scientific Properties")

            st.write(f"**Temperature :** {planet['Planet_temperature']:.0f} K")

            st.write(f"**Radius :** {planet['planet_radius_earth']:.2f} R⊕")

            st.write(f"**Mass :** {planet['planet_mass_earth']:.2f} M⊕")

            st.write(f"**Orbit Period :** {planet['orbit_period_days']:.2f} Days")

            st.write(f"**Distance Category :** {planet['Distance_category']}")

        st.divider()

     
#             DISCOVERY INFORMATION

        col3, col4 = st.columns(2)


        with col3:

            st.markdown("### 🔭 Discovery")

            st.write(f"**Method :** {planet['discovery_method']}")

            st.write(f"**Facility :** {planet['Discovery_facility']}")

            st.write(f"**Orbit Category :** {planet['Orbit_category']}")


     
        #                HABITABILITY
     

        with col4:

            st.markdown("### 🌱 Habitability")

            habitable = "✅ Yes" if planet["habitable_zone_flag"] == 1 else "❌ No"

            multi = "✅ Yes" if planet["multi_planet_system"] == 1 else "❌ No"

            st.write(f"**Habitable Zone :** {habitable}")

            st.write(f"**Multi Planet System :** {multi}")

            st.write(
                f"**Distance from Host Star :** " f"{planet['Distance_from_host_star']:.3f} AU"
            )


        st.divider()

    with right_panel:

     
        #                  FILTER PANEL
     

        # st.subheader("🎛 Explorer Filters")

        # st.success(
        #     f"Showing {len(exo):,} Exoplanets"
        # )

        # st.divider()

        # st.write("### 🌍 Current Filters")

        # st.write(f"**Planet Type :** {planet_type}")

        # st.write(f"**Discovery :** {discovery_method}")

        # st.write(f"**Star Type :** {star_type}")

        # st.write(f"**Distance :** {distance_category}")

        # st.write(f"**Orbit :** {orbit_category}")

        # st.write(f"**Habitable :** {habitable}")

        # st.divider()


     
        #                  QUICK FACTS
     

        # ===========================
        # QUICK FACTS
        # ===========================

        st.subheader("📌 Quick Facts")

        hottest_planet = exo.loc[
            exo["Planet_temperature"].idxmax(),
            "planet_name"
        ]

        coldest_planet = exo.loc[
            exo["Planet_temperature"].idxmin(),
            "planet_name"
        ]

        closest_planet = exo.loc[
            exo["Distance_from_earth"].idxmin(),
            "planet_name"
        ]

        largest_planet = exo.loc[
            exo["planet_radius_earth"].idxmax(),
            "planet_name"
        ]

        latest_discovery = int(exo["Discover_year"].max())

        st.metric(
            "🔥 Hottest Planet",
            hottest_planet[:6]
        )

        st.metric(
            "🧊 Coldest Planet",
            coldest_planet[:6]
        )

        st.metric(
            "🌍 Closest planet",
            closest_planet[:8]
        )

        st.metric(
            "🪐 Largest Planet",
            largest_planet[:7]
        )

        st.metric(
            "📅 Latest Discovery",
            latest_discovery
        )
    st.divider()

    #             DATASET STATISTICS
     
    st.subheader("📊 Statistics")

    st.write(
        f"**Newest Discovery :** "
        f"{int(exo['Discover_year'].max())}"
    )

    st.write(
        f"**Oldest Discovery :** "
        f"{int(exo['Discover_year'].min())}"
    )

    st.write(
        f"**Average Temperature :** "
        f"{exo['Planet_temperature'].mean():.0f} K"
    )

    st.write(
        f"**Average Radius :** "
        f"{exo['planet_radius_earth'].mean():.2f} R⊕"
    )

    st.write(
        f"**Average Mass :** "
        f"{exo['planet_mass_earth'].mean():.2f} M⊕"
    )

    st.write(
        f"**Average Orbit :** "
        f"{exo['orbit_period_days'].mean():.1f} Days"
    )

    st.divider()


     
    #                EXPLORER STATUS
     

    st.success("✅ Explorer Ready")

    st.caption(
        "Search and filters update the explorer instantly."
    )

        
 
    #                     FOOTER
 

    st.caption("© 2026 Space Cosmic Explorer | Developed by Chitvan Verma")