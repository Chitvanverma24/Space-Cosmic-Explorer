#                 HOST STAR OBSERVATORY

import streamlit as st
from Utils.data_load import load_data
from Utils.theme import page_header

def host_star_page():

 
    #                  LOAD DATA
 

    exo, asteroid = load_data()

 
    #                 PAGE HEADER
 

    page_header(
        "🪐 SPACE COSMIC EXPLORER",
        "⭐ Host Star Observatory",
        "Analyze host stars and discover the stellar environments where planets form."
    )

    st.divider()

 
    #                  SEARCH HOST STAR
 

    search_star = st.text_input(
        "🔍 Search Host Star", placeholder="Enter host star name..."
    )

 
    #                 SEARCH FILTER
 

    if search_star:

        exo_filtered = exo[
            exo["host_star"].str.contains(search_star, case=False, na=False)
        ]

    else:

        exo_filtered = exo.copy()

 
    #              TWO COLUMN LAYOUT
 

    left_panel, right_panel = st.columns([4, 1], gap="large")

    with left_panel:

     
        #               HOST STAR KPI CALCULATIONS
     

        total_host_stars = exo_filtered["host_star"].nunique()

        average_star_temp = exo_filtered["Host_star_temp"].mean()

        average_star_mass = exo_filtered["Host_star_mass"].mean()

        average_star_radius = exo_filtered["Host_star_radius"].mean()

        multi_planet_systems = (
            exo_filtered["multi_planet_system"] == 1
        ).sum()

     
        #                   KPI CARDS
     

        kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

        with kpi1:

            st.metric(

                "⭐ Host Stars",

                f"{total_host_stars:,}"

            )

        with kpi2:

            st.metric(

                "🌡 Avg Temp",

                f"{average_star_temp:.0f}K"

            )

        with kpi3:

            st.metric(

                "☀ Avg Mass M☉",

                f"{average_star_mass:.2f}"

            )

        with kpi4:

            st.metric(

                "🔵 Avg Radius R☉",

                f"{average_star_radius:.2f}"

            )

        with kpi5:

            st.metric(

                "🪐Multi Planets",

                f"{multi_planet_systems:,}"

            )

        st.divider()

     
        #                 SELECT HOST STAR
     

        st.subheader("⭐ Select Host Star")

        host_star_list = sorted(exo_filtered["host_star"].unique())

        selected_star = st.selectbox(
            "Choose Host Star", host_star_list, label_visibility="collapsed"
        )

     
        #            SELECTED HOST STAR DATA
     

        star = exo_filtered[exo_filtered["host_star"] == selected_star].iloc[0]

        st.divider()

     
        #              HOST STAR INFORMATION
     

        st.subheader("⭐ Host Star Information")

        col1, col2 = st.columns(2)

     
        #             GENERAL INFORMATION
     

        with col1:

            st.markdown("### 🌍 General Information")

            st.write(f"**Host Star :** {star['host_star']}")

            st.write(f"**Star Type :** {star['star_type']}")

            st.write(f"**Distance Category :** {star['Distance_category']}")

            st.write(f"**Age :** {star['Host_star_age']:.2f} Billion Years")

            st.write(f"**Discovery Year :** {int(star['Discover_year'])}")

     
        #             STELLAR PROPERTIES
     

        with col2:

            st.markdown("### 🔬 Stellar Properties")

            st.write(f"**Temperature :** {star['Host_star_temp']:.0f} K")

            st.write(f"**Mass :** {star['Host_star_mass']:.2f} M☉")

            st.write(f"**Radius :** {star['Host_star_radius']:.2f} R☉")

        st.divider()

     
        #          PLANETARY SYSTEM & DISCOVERY
     

        col3, col4 = st.columns(2)

     
        #             PLANETARY SYSTEM
     

        with col3:

            st.markdown("### 🪐 Planetary System")

            st.write(f"**Number of Planets :** {int(star['Number_of_planets'])}")

            st.write(f"**Number of Stars :** {int(star['Number_of_stars'])}")

            multi = "✅ Yes" if star["multi_planet_system"] == 1 else "❌ No"

            st.write(f"**Multi Planet System :** {multi}")

            habitable = "✅ Yes" if star["habitable_zone_flag"] == 1 else "❌ No"

            st.write(f"**Habitable Planet :** {habitable}")

     
        #              DISCOVERY INFORMATION
     

        with col4:

            st.markdown("### 🔭 Discovery")

            st.write(f"**Method :** {star['discovery_method']}")

            st.write(f"**Facility :** {star['Discovery_facility']}")

            st.write(f"**Orbit Category :** {star['Orbit_category']}")

            recent = "✅ Recent" if star["Recent_discovery"] == 1 else "📜 Older"

            st.write(f"**Recent Discovery :** {recent}")

        st.divider()
    st.divider()
    with right_panel:

     
        #                  QUICK FACTS
     

        # ===========================
        # QUICK FACTS
        # ===========================

        st.subheader("📌 Quick Facts")

        hottest_star = exo_filtered.loc[
            exo_filtered["Host_star_temp"].idxmax(),
            "host_star"
        ]

        coolest_star = exo_filtered.loc[
            exo_filtered["Host_star_temp"].idxmin(),
            "host_star"
        ]

        closest_star = exo_filtered.loc[
            exo_filtered["Distance_from_earth"].idxmin(),
            "host_star"
        ]

        largest_radius = exo_filtered["Host_star_radius"].max()

        oldest_star = exo_filtered["Host_star_age"].max()

        st.metric(
            "🔥 Hottest Star",
            hottest_star
        )

        st.metric(
            "🧊 Coolest Star",
            coolest_star[:7]
        )

        st.metric(
            "🌍 Closest Host Star",
            closest_star[:8]
        )

        st.metric(
            "☀ Largest Radius",
            f"{largest_radius:.1f} R☉"
        )

        st.metric(
            "Oldest Star(B Years)",
            f"{oldest_star:.4f} "
        )
    st.divider()
    #                 DATASET STATISTICS


    st.subheader("📊 Statistics")

    st.write(
        f"**Newest Discovery :** "
        f"{int(exo_filtered['Discover_year'].max())}"
    )

    st.write(
        f"**Oldest Discovery :** "
        f"{int(exo_filtered['Discover_year'].min())}"
    )

    st.write(
        f"**Average Age :** "
        f"{exo_filtered['Host_star_age'].mean():.2f} Billion Years"
    )

    st.write(
        f"**Most Common Star Type :** "
        f"{exo_filtered['star_type'].mode()[0]}"
    )

    # st.divider()

     
        #                 STAR FACT
     

    st.subheader("🌟 Did You Know?")

    most_common = exo_filtered["star_type"].mode()[0]

    st.info(

        f"⭐ Most confirmed exoplanets in the current "
        f"selection orbit **{most_common}** stars."

    )

     
        #               OBSERVATORY STATUS
     

    st.success("✅ Observatory Ready")

    st.caption(

        "Search and star selection update "
        "the observatory instantly."

    )
