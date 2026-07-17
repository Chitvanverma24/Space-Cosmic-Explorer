#               ASTEROID INFORMATION CENTER

import streamlit as st
from Utils.data_load import load_data
from Utils.theme import page_header

def asteroid_page():

 
    #                   LOAD DATA
 

    exo, asteroid = load_data()

 
    #                  PAGE HEADER
 

    page_header(
        "🚀 SPACE COSMIC EXPLORER",
        "☄️ Asteroid Information Center",
        "Track Near-Earth Asteroids and explore their orbital characteristics."
    )
    st.divider()

 
    #                  SEARCH ASTEROID
 

    search_asteroid = st.text_input(
        "🔍 Search Asteroid", placeholder="Enter asteroid name..."
    )

 
    #                  SEARCH FILTER
 

    if search_asteroid:

        asteroid_filtered = asteroid[
            asteroid["Asteroid_fullname"].str.contains(
                search_asteroid, case=False, na=False
            )
        ]

    else:

        asteroid_filtered = asteroid.copy()

 
    #               TWO COLUMN LAYOUT
 

    left_panel, right_panel = st.columns([4, 1], gap="large")

    with left_panel:

     
        #            ASTEROID KPI CALCULATIONS
     

        total_asteroids = len(asteroid_filtered)

        average_speed = asteroid_filtered["Relative Speed"].mean()

        average_distance = asteroid_filtered["Distance_from_Earth"].mean()

        average_brightness = asteroid_filtered["Asteroid_brightness"].mean()

        latest_approach = asteroid_filtered["Closest Date to Earth"].max()

     
        #                    KPI CARDS
     

        kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

        with kpi1:

            st.metric(

                "☄️ Asteroids",

                f"{total_asteroids:,}"

            )

        with kpi2:

            st.metric(

                "Avg Speed km/h",

                f"{average_speed:.1f}"

            )

        with kpi3:

            st.metric(

                "Avg Distance AU",

                f"{average_distance:.2f}"

            )

        with kpi4:

            st.metric(

                "Avg Brightness",

                f"{average_brightness:.2f}"

            )

        with kpi5:

            st.metric(

                "Latest Approach",

                str(latest_approach)[:4]

            )

        st.divider()

     
        #                 SELECT ASTEROID
     

        st.subheader("☄️ Select Asteroid")

        asteroid_list = sorted(asteroid_filtered["Asteroid_fullname"].unique())

        selected_asteroid = st.selectbox(
            "Choose Asteroid", asteroid_list, label_visibility="collapsed"
        )

     
        #            SELECTED ASTEROID DATA
     

        asteroid_info = asteroid_filtered[
            asteroid_filtered["Asteroid_fullname"] == selected_asteroid
        ].iloc[0]

        st.divider()

     
        #            ASTEROID INFORMATION
     

        st.subheader("☄️ Asteroid Information")

        col1, col2 = st.columns(2)


     
        #            GENERAL INFORMATION
     

        with col1:

            st.markdown("### 🌍 General Information")

            st.write(f"**Asteroid Name :** {asteroid_info['Asteroid_fullname']}")

            st.write(f"**Asteroid ID :** {asteroid_info['Asteroid id']}")

            st.write(f"**Closest Approach :** {asteroid_info['Closest Date to Earth']}")

            st.write(f"**Brightness :** {asteroid_info['Asteroid_brightness']:.2f}")


     
        #              SPEED ANALYSIS
     

        with col2:

            st.markdown("### ⚡ Speed Analysis")

            st.write(f"**Relative Speed :** {asteroid_info['Relative Speed']:.2f} km/h")

            st.write(f"**Initial Speed :** {asteroid_info['Intial_speed']:.2f} km/h")

            if asteroid_info["Relative Speed"] >= asteroid_filtered["Relative Speed"].median():

                speed_status = "🚀 High Speed"

            else:

                speed_status = "🐢 Moderate Speed"

            st.write(f"**Speed Category :** {speed_status}")


        st.divider()


     
        #       DISTANCE & OBSERVATION DETAILS
     

        col3, col4 = st.columns(2)


     
        #            DISTANCE ANALYSIS
     

        with col3:

            st.markdown("### 📏 Distance Analysis")

            st.write(
                f"**Distance from Earth :** " f"{asteroid_info['Distance_from_Earth']:.6f} AU"
            )

            st.write(
                f"**Minimum Distance :** "
                f"{asteroid_info['Minimum_Distance_asteroid']:.6f} AU"
            )

            st.write(
                f"**Maximum Distance :** "
                f"{asteroid_info['Maximum_Distance_asteroid']:.6f} AU"
            )


     
        #          OBSERVATION DETAILS
     

        with col4:

            st.markdown("### 🔭 Observation Details")

            st.write(f"**Observation Date :** " f"{asteroid_info['Closest Date to Earth']}")

            st.write(f"**Asteroid ID :** " f"{asteroid_info['Asteroid id']}")

            if (
                asteroid_info["Distance_from_Earth"]
                <= asteroid_filtered["Distance_from_Earth"].median()
            ):

                status = "🟢 Close Approach"

            else:

                status = "🔵 Safe Distance"

            st.write(f"**Current Status :** {status}")


        st.divider()

    with right_panel:

     
        #                  QUICK FACTS
     

        # ===========================
        # QUICK FACTS
        # ===========================

        st.subheader("📌 Quick Facts")

        largest_asteroid = asteroid_filtered.loc[
            asteroid_filtered["Maximum_Distance_asteroid"].idxmax(),
            "Asteroid_fullname"
        ]

        closest_distance = asteroid_filtered["Distance_from_Earth"].min()

        fastest_speed = asteroid_filtered["Relative Speed"].max()

        brightest = asteroid_filtered["Asteroid_brightness"].max()

        earliest_record = asteroid_filtered["Closest Date to Earth"].min()

        latest_record = asteroid_filtered["Closest Date to Earth"].max()

        st.metric(
            "☄ Largest Asteroid",
            largest_asteroid
        )

        st.metric(
            "Closest Distance(AU)",
            f"{closest_distance:.5f}"
        )

        st.metric(
            "⚡ Fastest Speed",
            f"{fastest_speed:.0f}km/h"
        )

        st.metric(
            "💡 Max Brightest",
            f"{brightest:.4f}"
        )

        st.metric(
            "📅 Earliest Record",
            str(earliest_record)[:7]
        )

        st.metric(
            "📅 Latest Record",
            str(latest_record)[:7]
        )
    st.divider()


     
        #               DATASET STATISTICS
     

    st.subheader("📊 Statistics")

    fastest = asteroid_filtered.loc[
        asteroid_filtered["Relative Speed"].idxmax(),
        "Asteroid_fullname"
    ]

    nearest = asteroid_filtered.loc[
        asteroid_filtered["Distance_from_Earth"].idxmin(),
        "Asteroid_fullname"
    ]

    latest = asteroid_filtered["Closest Date to Earth"].max()

    st.write(f"**🚀 Fastest Asteroid :** {fastest}")

    st.write(f"**🌍 Nearest Asteroid :** {nearest}")

    st.write(f"**📅 Latest Approach :** {latest}")

    st.divider()


     
        #                  DID YOU KNOW
     

    st.subheader("☄️ Did You Know?")

    st.info(

        """
        NASA continuously tracks Near-Earth
        Asteroids to predict future close
        approaches and improve planetary
        defense strategies.
        """

    )

    st.divider()


     
        #                CENTER STATUS
     

    st.success("✅ Asteroid Center Ready")

    st.caption(

        "Search and asteroid selection update "
        "the information center instantly."

    )
