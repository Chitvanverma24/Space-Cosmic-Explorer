#                  IMPORT LIBRARIES
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from Utils.theme import page_header


from Utils.data_load import load_data

#            VISUALIZATION DASHBOARD


def visualization_page():

 
    #                 LOAD DATA
 

    exo, asteroid = load_data()

 
    #             PAGE HEADER
 

    page_header(
        "🛰️ SPACE COSMIC EXPLORER",
        "📊 Visualization Dashboard",
        "Explore interactive visualizations for Exoplanets, Host Stars and "
        "Near-Earth Asteroids through premium analytics and AI-powered insights."
    )

    st.divider()

 
    #              SIDEBAR FILTERS
 

    st.sidebar.header("🎛 Dashboard Filters")

    planet_type = st.sidebar.multiselect(
        "Planet Type",
        options=sorted(exo["planet_type"].unique()),
        default=sorted(exo["planet_type"].unique()),
    )

    discovery_method = st.sidebar.multiselect(
        "Discovery Method",
        options=sorted(exo["discovery_method"].unique()),
        default=sorted(exo["discovery_method"].unique()),
    )

    star_type = st.sidebar.multiselect(
        "Star Type",
        options=sorted(exo["star_type"].unique()),
        default=sorted(exo["star_type"].unique()),
    )

 
    #              APPLY FILTERS
 

    exo_filtered = exo[
        (exo["planet_type"].isin(planet_type))
        & (exo["discovery_method"].isin(discovery_method))
        & (exo["star_type"].isin(star_type))
    ]

    asteroid_filtered = asteroid.copy()

 
    #                OPTION MENU
 

    selected_tab = option_menu(
        menu_title=None,
        options=[
            "🪐 Exoplanets",
            "⭐ Host Stars",
            "☄ Asteroids",
            "💡 Top Insights",
        ],
        icons=["globe", "star", "brightness-high" , "lightbulb"],
        orientation="horizontal",
        default_index=0,
    )

 
    #                EXOPLANETS TAB
 

    if selected_tab == "🪐 Exoplanets":

        st.subheader("🪐 Exoplanet Analytics")

        st.caption(
            "Explore the confirmed exoplanet dataset through interactive visualizations."
        )

        st.divider()

        
        # KPI CALCULATIONS
        

        total_planets = len(exo_filtered)

        habitable_planets = exo_filtered["habitable_zone_flag"].sum()

        average_temperature = exo_filtered["Planet_temperature"].mean()

        latest_discovery = exo_filtered["Discover_year"].max()

        
        # KPI ROW
        

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("🪐 Total Exoplanets", f"{total_planets:,}")

        with col2:
            st.metric("🌍 Habitable Planets", f"{habitable_planets:,}")

        with col3:
            st.metric("🌡 Average Temperature", f"{average_temperature:.0f} K")

        with col4:
            st.metric("📅 Latest Discovery", int(latest_discovery))

        st.divider()

        # ========= Graphs will start here in Part 2 =========

     
        # FIRST ROW OF CHARTS
     

        graph1, graph2 = st.columns(2)

     
        # GRAPH 1
        # Exoplanets Discovered Over Time
     

        with graph1:

            yearly_discoveries = (
                exo_filtered.groupby("Discover_year")
                .size()
                .reset_index(name="Total Exoplanets")
                .sort_values("Discover_year")
            )

            fig = px.line(
                yearly_discoveries,
                x="Discover_year",
                y="Total Exoplanets",
                markers=True,
                title="Exoplanets Discovered Over Time",
            )

            fig.update_layout(
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                title_font=dict(size=22),
                coloraxis_showscale=False,
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 2
        # Planet Type Distribution
     

        with graph2:

            planet_types = exo_filtered["planet_type"].value_counts().reset_index()

            planet_types.columns = ["Planet Type", "Count"]

            fig = px.pie(
                planet_types,
                names="Planet Type",
                values="Count",
                hole=0.55,
                title="Planet Type Distribution",
            )

            fig.update_layout(
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                title_font=dict(size=22),
                coloraxis_showscale=False,
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # SECOND ROW OF CHARTS
     

        graph3, graph4 = st.columns(2)

     
        # GRAPH 3
        # Exoplanets by Host Star Type
     

        with graph3:

            star_distribution = exo_filtered["star_type"].value_counts().reset_index()

            star_distribution.columns = ["Star Type", "Total Exoplanets"]

            fig = px.bar(
                star_distribution,
                x="Total Exoplanets",
                y="Star Type",
                orientation="h",
                text="Total Exoplanets",
                title="Exoplanets by Host Star Type",
                color="Total Exoplanets",
                color_continuous_scale="Viridis",
            )

            fig.update_traces(textposition="outside")

            fig.update_layout(
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                title_font=dict(size=22),
                coloraxis_showscale=False,
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 4
        # Distance Category Distribution
     

        with graph4:

            distance_category = (
                exo_filtered["Distance_category"].value_counts().reset_index()
            )

            distance_category.columns = ["Distance Category", "Count"]

            fig = px.bar(
                distance_category,
                x="Distance Category",
                y="Count",
                text="Count",
                title="Distance Category Distribution",
                color="Count",
                color_continuous_scale="Plasma",
            )

            fig.update_traces(textposition="outside")

            fig.update_layout(
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                title_font=dict(size=22),
                coloraxis_showscale=False,
            )

            st.plotly_chart(fig, use_container_width=True)

        # Third Row of charts
        graph5,graph6 = st.columns(2)

        # Graph 5
        with graph5:
         
            # HABITABLE PLANETS BY PLANET TYPE
         

            habitable = (exo_filtered[exo_filtered["habitable_zone_flag"] == 1].groupby("planet_type").size().reset_index(name="Habitable Planets"))

            fig = px.bar(

                habitable,

                x="planet_type",

                y="Habitable Planets",

                text_auto=True,

                color="Habitable Planets",

                color_continuous_scale="Greens",

                title="Habitable Planets by Planet Type"

            )

            fig.update_layout(

                template="plotly_dark",

                height=430,

                plot_bgcolor="#111827",

                paper_bgcolor="#111827",

                font=dict(color="white"),

                coloraxis_showscale=False,

                xaxis_title="Planet Type",

                yaxis_title="Number of Habitable Planets"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with graph6:
         
            # HABITABLE STATUS BY STAR TYPE
         

            star_habitable = (exo_filtered.groupby(["star_type", "habitable_zone_flag"]).size().reset_index(name="Count"))

            star_habitable["habitable_zone_flag"] = (star_habitable["habitable_zone_flag"].map({1: "Habitable",0: "Non-Habitable"}))

            fig = px.bar(

                star_habitable,

                x="star_type",

                y="Count",

                color="habitable_zone_flag",

                barmode="group",

                text_auto=True,

                color_discrete_sequence=[
                    "#00E676",
                    "#FF5252"
                ],

                title="Habitable vs Non-Habitable Planets by Star Type"
            )

            fig.update_layout(

                template="plotly_dark",

                height=430,

                plot_bgcolor="#111827",

                paper_bgcolor="#111827",

                font=dict(color="white"),

                xaxis_title="Star Type",

                yaxis_title="Number of Planets"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

         
            #                     FOOTER
         

 
    #                HOST STARS TAB
 

    elif selected_tab == "⭐ Host Stars":

        st.subheader("⭐ Host Star Analytics")

        st.caption(
            "Analyze stellar properties, classifications and planetary host systems."
        )

        st.divider()

        
        # KPI CALCULATIONS
        

        total_host_stars = exo_filtered["host_star"].nunique()

        average_temperature = exo_filtered["Host_star_temp"].mean()

        average_mass = exo_filtered["Host_star_mass"].mean()

        most_common_star = exo_filtered["star_type"].mode()[0]

        
        # KPI ROW
        

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric("⭐ Host Stars", f"{total_host_stars:,}")

        with col2:

            st.metric("🌡 Avg Temperature", f"{average_temperature:.0f} K")

        with col3:

            st.metric("⚖ Avg Mass", f"{average_mass:.2f} M☉")

        with col4:

            st.metric("🌟 Common Star Type", most_common_star[:6])

        st.divider()

        # ========= Graphs start below =========

     
        # FIRST ROW OF CHARTS
     

        graph1, graph2 = st.columns(2)

     
        # GRAPH 1
        # Host Star Type Distribution
     

        with graph1:

            star_distribution = exo_filtered["star_type"].value_counts().reset_index()

            star_distribution.columns = ["Star Type", "Count"]

            fig = px.bar(
                star_distribution,
                x="Count",
                y="Star Type",
                orientation="h",
                text="Count",
                title="Host Star Type Distribution",
                color="Count",
                color_continuous_scale="Viridis",
            )

            fig.update_traces(textposition="outside")

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                coloraxis_showscale=False,
                yaxis_title="",
                xaxis_title="Number of Host Stars",
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 2
        # Host Star Temperature Distribution
     

        with graph2:

            fig = px.histogram(
                exo_filtered,
                x="Host_star_temp",
                nbins=30,
                title="Host Star Temperature Distribution",
                color_discrete_sequence=["#FFB74D"],
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                xaxis_title="Temperature (K)",
                yaxis_title="Number of Host Stars",
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # SECOND ROW OF CHARTS
     

        graph3, graph4 = st.columns(2)

     
        # GRAPH 3
        # Host Star Mass Distribution
     

        with graph3:

            fig = px.histogram(
                exo_filtered,
                x="Host_star_mass",
                nbins=30,
                title="Host Star Mass Distribution",
                color_discrete_sequence=["#00E5FF"],
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                xaxis_title="Host Star Mass (Solar Mass)",
                yaxis_title="Number of Host Stars",
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 4
        # Host Star Radius Distribution
     

        with graph4:

            fig = px.histogram(
                exo_filtered,
                x="Host_star_radius",
                nbins=30,
                title="Host Star Radius Distribution",
                color_discrete_sequence=["#7C4DFF"],
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                xaxis_title="Host Star Radius (Solar Radius)",
                yaxis_title="Number of Host Stars",
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # THIRD ROW OF CHARTS
     

        graph5, graph6 = st.columns(2)

     
        # GRAPH 5
        # Host Star Mass vs Radius
     

        with graph5:

            fig = px.scatter(
                exo_filtered,
                x="Host_star_mass",
                y="Host_star_radius",
                color="star_type",
                hover_name="host_star",
                size="Host_star_radius",
                title="Host Star Mass vs Radius",
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                xaxis_title="Mass (Solar Mass)",
                yaxis_title="Radius (Solar Radius)",
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 6
        # Host Star Age Distribution
     

        with graph6:

            fig = px.histogram(
                exo_filtered,
                x="Host_star_age",
                nbins=30,
                title="Host Star Age Distribution",
                color_discrete_sequence=["#FF9800"],
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                xaxis_title="Host Star Age (Billion Years)",
                yaxis_title="Number of Host Stars",
            )

            st.plotly_chart(fig, use_container_width=True)
           
 
    #                 ASTEROIDS TAB
 

    elif selected_tab == "☄ Asteroids":

        st.subheader("☄ Asteroid Analytics")

        st.caption(
            "Explore Near-Earth Asteroids through speed, distance and brightness analysis."
        )

        st.divider()

        
        # KPI CALCULATIONS
        

        total_asteroids = len(asteroid_filtered)

        average_speed = asteroid_filtered["Relative Speed"].mean()

        closest_asteroid = asteroid_filtered.loc[
            asteroid_filtered["Distance_from_Earth"].idxmin(), "Asteroid_fullname"
        ]

        brightest_asteroid = asteroid_filtered.loc[
            asteroid_filtered["Asteroid_brightness"].idxmin(), "Asteroid_fullname"
        ]

        
        # KPI ROW
        

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric("☄ Total Asteroids", f"{total_asteroids:,}")

        with col2:

            st.metric("🚀 Avg Speed", f"{average_speed:.2f}")

        with col3:

            st.metric("📍 Closest Asteroid", closest_asteroid.strip())

        with col4:

            st.metric("💡 Brightest Asteroid", brightest_asteroid[:14])

        st.divider()

     
        # FIRST ROW OF CHARTS
     

        graph1, graph2 = st.columns(2)

     
        # GRAPH 1
        # Relative Speed by Brightness Quartiles
     

        with graph1:

            brightness_df = asteroid_filtered.copy()

            brightness_df["Brightness Quartile"] = pd.qcut(
                brightness_df["Asteroid_brightness"],
                q=4,
                labels=["Q1 (Brightest)", "Q2", "Q3", "Q4 (Dimmest)"],
            )

            speed_summary = (
                brightness_df.groupby("Brightness Quartile")["Relative Speed"]
                .mean()
                .reset_index()
            )

            fig = px.bar(
                speed_summary,
                x="Brightness Quartile",
                y="Relative Speed",
                text_auto=".2f",
                title="Average Relative Speed by Brightness Quartile",
                color="Relative Speed",
                color_continuous_scale="Turbo",
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                xaxis_title="Brightness Quartile",
                yaxis_title="Average Relative Speed",
                coloraxis_showscale=False,
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 2
        # Relative Speed vs Distance
     

        with graph2:

            fig = px.scatter(
                asteroid_filtered,
                x="Distance_from_Earth",
                y="Relative Speed",
                size="Asteroid_brightness",
                color="Relative Speed",
                hover_name="Asteroid_fullname",
                title="Relative Speed vs Distance",
                color_continuous_scale="Turbo",
            )

            fig.update_traces(
                marker=dict(opacity=0.75, line=dict(width=1, color="white"))
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                xaxis_title="Distance From Earth (AU)",
                yaxis_title="Relative Speed (km)",
                coloraxis_colorbar_title="Speed",
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 3
        # Asteroid Brightness Distribution
     

        graph3, graph4 = st.columns(2)

        with graph3:

            fig = px.box(
                asteroid_filtered,
                y="Asteroid_brightness",
                points="outliers",
                title="Asteroid Brightness Distribution",
                color_discrete_sequence=["#FFD54F"],
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                xaxis_title="",
                yaxis_title="Brightness (Absolute Magnitude)",
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 4
        # Relative Speed Trend
     

        with graph4:

            area_df = asteroid_filtered.copy()

            # Convert to datetime
            area_df["Closest Date to Earth"] = pd.to_datetime(
                area_df["Closest Date to Earth"]
            )

            # Extract Year
            area_df["Year"] = area_df["Closest Date to Earth"].dt.year

            # Average Speed per Year
            area_df = area_df.groupby("Year")["Relative Speed"].mean().reset_index()

            fig = px.area(
                area_df,
                x="Year",
                y="Relative Speed",
                title="Average Relative Speed Over Time",
                color_discrete_sequence=["#00E5FF"],
            )

            fig.update_traces(line=dict(width=3))

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                xaxis_title="Year",
                yaxis_title="Average Relative Speed",
            )

            st.plotly_chart(fig, use_container_width=True)
         

    elif selected_tab == "💡 Top Insights":
     
        # TOP INSIGHTS
     

        st.markdown("## 💡 Top 10 Scientific Insights")

        st.caption(
        """
            Discover the most important patterns,
            trends and scientific observations
            from the Exoplanet and Near-Earth
            Asteroid datasets.
        """
        )

        st.divider()

     
        # INSIGHT SUMMARY
     

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric("🪐 Total Exoplanets", f"{len(exo_filtered):,}")

        with col2:

            st.metric("⭐ Host Stars", f"{exo_filtered['host_star'].nunique():,}")

        with col3:

            st.metric("☄ Asteroids", f"{len(asteroid_filtered):,}")

        with col4:

            st.metric("🌍 Habitable Planets", f"{(exo_filtered['habitable_zone_flag']==1).sum():,}")

        st.divider()

     
        # GRAPH 1
        # TOP 10 FASTEST ASTEROIDS
     

        graph1, graph2 = st.columns(2)

        with graph1:

            fastest = asteroid_filtered.nlargest(10, "Relative Speed").sort_values(
            "Relative Speed"
            )

            fig = px.bar(
                fastest,
                x="Relative Speed",
                y="Asteroid_fullname",
                orientation="h",
                text_auto=".2f",
                color="Relative Speed",
                color_continuous_scale="Turbo",
                title="Top 10 Fastest Asteroids",
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                coloraxis_showscale=False,
                xaxis_title="Relative Speed",
                yaxis_title="Asteroid",
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 2
        # TOP 10 DISCOVERY YEARS
     
        with graph2:

            discovery = (
            exo_filtered.groupby("Discover_year")
            .size()
            .reset_index(name="Discoveries")
            .sort_values("Discoveries", ascending=False)
            .head(10)
            .sort_values("Discover_year")
            )

            fig = px.bar(
                discovery,
                x="Discover_year",
                y="Discoveries",
                text_auto=True,
                color="Discoveries",
                color_continuous_scale="Viridis",
                title="Top 10 Years with Most Exoplanet Discoveries",
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                coloraxis_showscale=False,
                xaxis_title="Discovery Year",
                yaxis_title="Number of Discoveries",
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 3
        # TOP 10 HOTTEST EXOPLANETS
     

        graph3, graph4 = st.columns(2)

        with graph3:

            hottest = exo_filtered.nlargest(10, "Planet_temperature").sort_values(
            "Planet_temperature"
            )

            fig = px.bar(
                hottest,
                x="Planet_temperature",
                y="planet_name",
                orientation="h",
                text_auto=".0f",
                color="Planet_temperature",
                color_continuous_scale="Reds",
                title="Top 10 Hottest Exoplanets",
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                coloraxis_showscale=False,
                xaxis_title="Temperature (K)",
                yaxis_title="Planet",
            )

            st.plotly_chart(fig, use_container_width=True)

     
        # GRAPH 4
        # TOP 10 COLDEST EXOPLANETS
     

        with graph4:

            coldest = exo_filtered.nsmallest(10, "Planet_temperature").sort_values(
                "Planet_temperature", ascending=False
            )

            fig = px.bar(
                coldest,
                x="Planet_temperature",
                y="planet_name",
                orientation="h",
                text_auto=".0f",
                color="Planet_temperature",
                color_continuous_scale="Blues",
                title="Top 10 Coldest Exoplanets",
            )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                plot_bgcolor="#111827",
                paper_bgcolor="#111827",
                font=dict(color="white"),
                coloraxis_showscale=False,
                xaxis_title="Temperature (K)",
                yaxis_title="Planet",
            )

            st.plotly_chart(fig, use_container_width=True)

