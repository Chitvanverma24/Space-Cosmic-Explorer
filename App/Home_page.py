#                 HOME DASHBOARD

import streamlit as st

from Utils.theme import page_header, section_header, footer
from Utils.data_load import load_data


#                    HOME PAGE

def home_page():

 
    # LOAD DATA
 

    exo, asteroid = load_data()


 
    # DASHBOARD CALCULATIONS
 

    total_exoplanets = len(exo)

    total_host_stars = exo["host_star"].nunique()

    total_asteroids = len(asteroid)

    average_temperature = exo["Planet_temperature"].mean()

    average_host_star_mass = exo["Host_star_mass"].mean()

    habitable_planets = exo["habitable_zone_flag"].sum()

    multi_planet_systems = exo["multi_planet_system"].sum()

    recent_discoveries = exo["Recent_discovery"].sum()

    closest_asteroid = asteroid.loc[
        asteroid["Distance_from_Earth"].idxmin(),
        "Asteroid_fullname"
    ]

    closest_distance = asteroid["Distance_from_Earth"].min()


 
    # DATASET SUMMARY CALCULATIONS
 

    total_planet_types = exo["planet_type"].nunique()

    total_discovery_methods = exo["discovery_method"].nunique()

    average_speed = asteroid["Relative Speed"].mean()

    brightest_asteroid = asteroid.loc[
        asteroid["Asteroid_brightness"].idxmin(),
        "Asteroid_fullname"
    ]

    minimum_distance = asteroid["Minimum_Distance_asteroid"].min()


 
    # PAGE HEADER
 

    page_header(
        "🚀 SPACE COSMIC EXPLORER",
        "🪐 Space Cosmic Explorer",
        "Explore Exoplanets, Host Stars and Near-Earth Asteroids across the Universe.",
        chips=[
            "🪐 25K+ Space Objects",
            "🛰 Real NASA Datasets",
            "🤖 AI-Powered Insights",
        ]
    )

    st.divider()

    #              DASHBOARD OVERVIEW
 

    st.header("📊 Dashboard Overview")

    st.write(
        "Quick summary of the complete Exoplanet and Asteroid datasets."
    )

    st.write("")

 
    # FIRST ROW
 

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🪐 Total Exoplanets",
            f"{total_exoplanets:,}"
        )

    with col2:

        st.metric(
            "⭐ Host Stars",
            f"{total_host_stars:,}"
        )

    with col3:

        st.metric(
            "☄ Total Asteroids",
            f"{total_asteroids:,}"
        )

    with col4:

        st.metric(
            "🌡 Avg Temperature",
            f"{average_temperature:.0f} K"
        )



    st.write("")


 
    # SECOND ROW
 

    col5, col6, col7, col8 = st.columns(4)

    with col5:

        st.metric(
            "🌍 Habitable Planets",
            f"{habitable_planets:,}"
        )

    with col6:

        st.metric(
            "🛰 Multi Planet Systems",
            f"{multi_planet_systems:,}"
        )

    with col7:

        st.metric(
            "✨ Recent Discoveries",
            f"{recent_discoveries:,}"
        )

    with col8:

        st.metric(
            "☄ Closest Asteroid",
            closest_asteroid.strip(),
        )
        st.caption(f"📏 Distance from Earth: {closest_distance:.3f} AU")
    st.divider()


     
    #          EXPLORE OUR DASHBOARDS
 

    st.header("🚀 Explore Our Dashboards")

    st.write(
        "Navigate through different modules of Space Cosmic Explorer."
    )

    st.write("")

    dashboard_data = [

        {
            "icon": "📊",
            "title": "Visualization Dashboard",
            "description": "Interactive charts and analytics for Exoplanets, Host Stars and Asteroids."
        },

        {
            "icon": "🪐",
            "title": "Exoplanet Explorer",
            "description": "Search and explore confirmed Exoplanets with detailed scientific information."
        },

        {
            "icon": "⭐",
            "title": "Host Star Observatory",
            "description": "Analyze Host Stars, stellar properties and planetary systems."
        },

        {
            "icon": "☄️",
            "title": "Asteroid Information Center",
            "description": "Explore Near-Earth Asteroids including speed, distance and brightness."
        },

        {
            "icon": "🤖",
            "title": "Planet Recommendation Engine",
            "description": "Get planet recommendations based on your preferred conditions."
        },

        {
            "icon": "🌌",
            "title": "Galactic Comparison Lab",
            "description": "Compare two exoplanets side-by-side using scientific parameters."
        },

        {
            "icon": "ℹ️",
            "title": "About Project",
            "description": "Learn about datasets, technologies and project objectives."
        }

    ]


    cols = st.columns(3)

    for index, dashboard in enumerate(dashboard_data):

        with cols[index % 3]:

            with st.container(border=True):

                st.subheader(
                    f"{dashboard['icon']} {dashboard['title']}"
                )

                st.write(
                    dashboard["description"]
                )

                st.button(
                    "Open Dashboard",
                    disabled=True,
                    key=f"dashboard_{index}"
                )

    

     
    #              LATEST DISCOVERIES
 

    st.header("🛰 Latest Discoveries")

    st.write(
        "Recently discovered exoplanets available in the dataset."
    )

    st.write("")

    latest_planets = (
        exo.sort_values(
            by="Discover_year",
            ascending=False
        )
        .head(3)
    )

    col1, col2, col3 = st.columns(3)

    columns = [col1, col2, col3]

    for column, (_, planet) in zip(columns, latest_planets.iterrows()):

        with column:

            with st.container(border=True):

                st.subheader(f"🪐 {planet['planet_name']}")

                st.write(
                    f"**⭐ Host Star :** {planet['host_star']}"
                )

                st.write(
                    f"**🌍 Planet Type :** {planet['planet_type']}"
                )

                st.write(
                    f"**📅 Discovery Year :** {int(planet['Discover_year'])}"
                )

                st.write(
                    f"**🌡 Temperature :** {planet['Planet_temperature']:.0f} K"
                )

                st.write(
                    f"**🛰 Orbit Period :** {planet['orbit_period_days']:.2f} Days"
                )

    st.divider()

     
    #               DATASET SUMMARY
 

    st.header("📊 Dataset Summary")

    st.write(
        "Quick overview of the Exoplanet and Asteroid datasets."
    )

    st.write("")

    left_col, right_col = st.columns(2)

 
    # EXOPLANET DATASET
 

    with left_col:

        with st.container(border=True):

            st.subheader("🪐 Exoplanet Dataset")

            st.write(f"**Total Exoplanets :** {total_exoplanets:,}")

            st.write(f"**Host Stars :** {total_host_stars:,}")

            st.write(f"**Habitable Planets :** {habitable_planets:,}")

            st.write(f"**Planet Types :** {total_planet_types}")

            st.write(f"**Discovery Methods :** {total_discovery_methods}")

            st.write(f"**Average Temperature :** {average_temperature:.0f} K")

            st.write(f"**Average Host Star Mass :** {average_host_star_mass:.2f} Solar Mass")


 
    # ASTEROID DATASET
 

    with right_col:

        with st.container(border=True):

            st.subheader("☄️ Asteroid Dataset")

            st.write(f"**Total Asteroids :** {total_asteroids:,}")

            st.write(f"**Closest Asteroid :** {closest_asteroid}")

            st.write(f"**Closest Distance :** {closest_distance:.6f} AU")

            st.write(f"**Average Speed :** {average_speed:.2f}")

            st.write(f"**Brightest Asteroid :** {brightest_asteroid}")

            st.write(f"**Minimum Distance :** {minimum_distance:.6f} AU")

    st.divider()



 
    #                     FOOTER
 

    st.caption(
        "© 2026 Space Cosmic Explorer | Developed by Chitvan Verma"
    )