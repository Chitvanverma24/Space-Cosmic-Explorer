#               PLANET RECOMMENDATION ENGINE

import os
import streamlit as st
from Utils.data_load import load_data
from Utils.theme import page_header

def planet_recommendation_page():

 
    #                    LOAD DATA
 

    exo, asteroid = load_data()


    
    # RESET HANDLER
    

    if st.session_state.get("reset_filters", False):

        st.session_state["planet_type"] = "All"
        st.session_state["habitable"] = "All"
        st.session_state["star_type"] = "All"
        st.session_state["distance"] = "All"
        st.session_state["temperature"] = 800

        st.session_state["reset_filters"] = False

 
    #                   PAGE HEADER
 

    page_header(
        "🚀 SPACE COSMIC EXPLORER",
        "🤖 Planet Recommendation Engine",
        "Discover planets intelligently using AI-powered recommendation techniques."
    )

    st.divider()

 
    #               SEARCH PREFERENCES
 

    st.subheader("🪐 Search Preferences")

    col1, col2, col3, col4, col5 = st.columns(5)

   

    with col1:

        planet_type = st.selectbox(

            "🪐 Planet Type",

            ["All"] + sorted(exo["planet_type"].dropna().unique()),
            key ="planet_type"

        )

   

    with col2:

        habitable = st.selectbox(

            "🌱 Habitable Zone",

            ["All", "Yes", "No"],
            key ="habitable"

        )

   

    with col3:

        star_type = st.selectbox(

            "⭐ Star Type",

            ["All"] + sorted(exo["star_type"].dropna().unique()),
            key ="star_type"

        )

   

    with col4:

        distance = st.selectbox(

            "🌌 Distance Category",

            ["All"] + sorted(exo["Distance_category"].dropna().unique()),
            key ="distance"

        )

   

    with col5:

        max_temp = int(exo["Planet_temperature"].max())

        temperature = st.slider(

            "🌡 Maximum Temperature",

            0,

            max_temp,

            800,
            key ="temperature"
        )

    st.divider()

 
    #             APPLY FILTERS
 

    filtered = exo.copy()

    if planet_type != "All":

        filtered = filtered[
            filtered["planet_type"] == planet_type
        ]

    if habitable != "All":

        value = 1 if habitable == "Yes" else 0

        filtered = filtered[
            filtered["habitable_zone_flag"] == value
        ]

    if star_type != "All":

        filtered = filtered[
            filtered["star_type"] == star_type
        ]

    if distance != "All":

        filtered = filtered[
            filtered["Distance_category"] == distance
        ]

    filtered = filtered[
        filtered["Planet_temperature"] <= temperature
    ]

 
    #            RESULT INFORMATION
 

    st.success(

        f"✨ We found **{len(filtered)}** planets matching your preferences."

    )

    st.divider()



     
    #           AI MATCH SCORE CALCULATION
 

    if len(filtered) == 0:

        st.warning("No planets match your selected preferences.")

        return

    recommendations = filtered.copy()

    recommendations["Match_Score"] = 0

 
    #               PLANET TYPE MATCH
 

    if planet_type != "All":

        recommendations.loc[
            recommendations["planet_type"] == planet_type,
            "Match_Score"
        ] += 25


 
    #               HABITABLE ZONE
 

    if habitable != "All":

        value = 1 if habitable == "Yes" else 0

        recommendations.loc[
            recommendations["habitable_zone_flag"] == value,
            "Match_Score"
        ] += 30


 
    #                 STAR TYPE
 

    if star_type != "All":

        recommendations.loc[
            recommendations["star_type"] == star_type,
            "Match_Score"
        ] += 15


 
    #              DISTANCE CATEGORY
 

    if distance != "All":

        recommendations.loc[
            recommendations["Distance_category"] == distance,
            "Match_Score"
        ] += 15


 
    #             TEMPERATURE BONUS
 

    recommendations["Match_Score"] += (
        (
            temperature
            - recommendations["Planet_temperature"]
        ).clip(lower=0)
        / max(temperature, 1)
        * 15
    ).astype(int)


 
    #             RECENT DISCOVERY BONUS
 

    recommendations["Match_Score"] += (
        recommendations["Recent_discovery"] * 5
    )


 
    #             MULTI PLANET BONUS
 

    recommendations["Match_Score"] += (
        recommendations["multi_planet_system"] * 5
    )


 
    #             LIMIT SCORE
 

    recommendations["Match_Score"] = (
        recommendations["Match_Score"]
        .clip(0, 100)
        .astype(int)
    )


 
    #               SORT RESULTS
 

    recommendations = recommendations.sort_values(

        by="Match_Score",

        ascending=False

    ).reset_index(drop=True)


 
    #                  TOP RESULTS
 

    top_planets = recommendations.head(5)


     
    #             TOP RECOMMENDED PLANETS
 

    left_panel, right_panel = st.columns([3, 1], gap="large")

    with left_panel:

        st.subheader("⭐ Top Recommended Planets")

        
        #      IMAGE MAPPING (PLANET TYPE → IMAGE)
        



        
        image_map = {

            "Gas Giant": "Assets/Planets/Gas_Giant.png",

            "Mini-Neptune": "Assets/Planets/Mini_Neptune.png",

            "Neptune-like": "Assets/Planets/Neptune_Like.png",

            "Sub-Earth": "Assets/Planets/Sub_Earth.png",

            "Super-Earth": "Assets/Planets/Super_Earth.png",

            "Super-Jupiter": "Assets/Planets/Super_Jupiter.png",

            "Unknown": "Assets/Planets/Unknown.png"
        }
        # st.write(image_map.keys())

        
        #          SHOW TOP 5 RECOMMENDATIONS
        

        for _, planet in top_planets.iterrows():
            

            planet_type_name = str(planet["planet_type"]).strip()

            img = image_map.get(

                planet_type_name,

                "Assets/Planets/Unknown.png"

            )

            card1, card2, card3 = st.columns([1.2, 2.6, 1])

           
            # IMAGE
           

            with card1:

                if os.path.exists(img):

                    st.image(img, use_container_width=True)

           
            # PLANET DETAILS
           

            with card2:

                st.markdown(
                    f"## {planet['planet_name']}"
                )

                st.write(
                    f"**⭐ Host Star :** {planet['host_star']}"
                )

                st.caption(
                    planet["planet_type"]
                )

                st.write(
                    f"🌌 Distance : {planet['Distance_category']}"
                )

                st.write(
                    f"🌡 Temperature : {planet['Planet_temperature']:.0f} K"
                )

                hz = "Yes" if planet["habitable_zone_flag"] == 1 else "No"

                st.write(
                    f"🌱 Habitable : {hz}"
                )

                st.write(
                    f"📅 Discovery : {int(planet['Discover_year'])}"
                )

           
            # MATCH SCORE
           

            with card3:

                score = int(planet["Match_Score"])

                st.metric(

                    "Match",

                    f"{score}%"

                )

                # ------------------------------------------

                if score >= 95:

                    stars = "★★★★★"

                    quality = "Excellent"

                elif score >= 85:

                    stars = "★★★★☆"

                    quality = "Great"

                elif score >= 75:

                    stars = "★★★☆☆"

                    quality = "Good"

                elif score >= 60:

                    stars = "★★☆☆☆"

                    quality = "Average"

                else:

                    stars = "★☆☆☆☆"

                    quality = "Low"

                st.success(quality)

                st.write(stars)

            st.divider()

 
    #                 RIGHT SIDE PANEL
 

    with right_panel:

        
        #           PREFERENCE SUMMARY
        

        st.subheader("👤 Preference Summary")

        st.write(f"**🪐 Planet Type :** {planet_type}")

        st.write(f"**🌱 Habitable :** {habitable}")

        st.write(f"**⭐ Star Type :** {star_type}")

        st.write(f"**🌌 Distance :** {distance}")

        st.write(f"**🌡 Max Temperature :** {temperature} K")

        st.divider()

        
        #            MATCH INSIGHT
        

        st.subheader("📊 Match Insight")

        best_score = int(top_planets.iloc[0]["Match_Score"])

        st.metric(

            "Overall Match",

            f"{best_score}%"

        )

        if best_score >= 90:

            st.success(
                "Excellent match based on your selected preferences."
            )

        elif best_score >= 75:

            st.info(
                "Very good planetary candidates were found."
            )

        elif best_score >= 60:

            st.warning(
                "Some planets partially satisfy your preferences."
            )

        else:

            st.error(
                "Only weak matches were found."
            )

        st.divider()

        
        #             WHY THESE PLANETS?
        

        st.subheader("💡 Why These Planets?")

        reasons = []

        if planet_type != "All":

            reasons.append("✔ Preferred planet type")

        if habitable != "All":

            reasons.append("✔ Habitable zone preference")

        if star_type != "All":

            reasons.append("✔ Preferred host star")

        if distance != "All":

            reasons.append("✔ Preferred distance category")

        reasons.append("✔ Temperature within selected range")

        reasons.append("✔ AI Match Score ranking")

        for reason in reasons:

            st.write(reason)

        st.divider()

        
        #               RESET BUTTON
        

        if st.button("🔄 Reset Preferences", use_container_width=True):

            st.session_state["reset_filters"] = True

            st.rerun()


     
        #              BEST RECOMMENDATION HIGHLIGHT
     

        st.divider()

        st.subheader("🏆 Best Planet Recommendation")

        best_planet = top_planets.iloc[0]

        highlight1, highlight2 = st.columns([3, 1])

        with highlight1:

            st.success(
                f"""
                ### 🌍 {best_planet['planet_name']}

                This planet achieved the **highest AI Match Score**
                based on your selected preferences.
                """
            )

            st.write(f"⭐ **Host Star :** {best_planet['host_star']}")
            st.write(f"🪐 **Planet Type :** {best_planet['planet_type']}")
            st.write(f"🌱 **Habitable :** {'Yes' if best_planet['habitable_zone_flag']==1 else 'No'}")
            st.write(f"🌡 **Temperature :** {best_planet['Planet_temperature']:.0f} K")
            st.write(f"📅 **Discovery Year :** {int(best_planet['Discover_year'])}")
        st.divider()


 
    #             VIEW ALL MATCHES
 

    st.subheader("📋 View All Recommended Planets")

    display_columns = [

        "planet_name",
        "planet_type",
        "host_star",
        "star_type",
        "Planet_temperature",
        "Distance_category",
        "Match_Score"
    ]

    table = top_planets[display_columns].copy()

    table.columns = [

        "Planet Name",
        "Planet Type",
        "Host Star",
        "Star Type",
        "Temperature (K)",
        "Distance",
        "Match Score"
    ]

    st.dataframe(

        table,

        use_container_width=True,

        hide_index=True

    )

    st.divider()


 
    #            AI RECOMMENDATION SUMMARY
 

    st.subheader("🤖 AI Recommendation Summary")

    st.info(

        f"""
        ### Recommendation Complete

        Our recommendation engine analyzed your selected preferences and ranked confirmed exoplanets using a weighted scoring system.

        ### Selection Criteria

        ✅ Planet Type

        ✅ Habitable Zone

        ✅ Host Star Type

        ✅ Distance Category

        ✅ Temperature Range

        ### Best Recommended Planet

        **{best_planet['planet_name']}**

        with an overall match score of

        # ⭐ {int(best_planet['Match_Score'])}%

        This planet is currently the closest scientific match to your selected preferences.
        """

    )

    st.divider()


     
        #                  FOOTER
     

    st.caption(
        "Recommendation results are generated using scientific properties "
           "available in the confirmed exoplanet dataset."
    )