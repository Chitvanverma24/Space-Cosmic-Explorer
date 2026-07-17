#               GALACTIC COMPARISON LAB

import streamlit as st
import pandas as pd
from Utils.data_load import load_data
from Utils.theme import page_header

def galactic_comparison_page():

 
    #                  LOAD DATA
 

    exo, asteroid = load_data()

 
    #                  PAGE HEADER
 

    page_header(
        "🚀 SPACE COSMIC EXPLORER",
        "⚖️ Galactic Comparison Lab",
        "Compare planets, host stars and asteroids side-by-side with interactive analysis."
    )

    st.divider()
 
    #              SELECT PLANETS
 

    col1, col2 = st.columns(2)

    planet_list = sorted(exo["planet_name"].unique())

    with col1:

        planet_1 = st.selectbox("🪐 Select Planet A", planet_list, index=0)

    with col2:

        planet_2 = st.selectbox("🌍 Select Planet B", planet_list, index=1)

 
    #               PLANET DATA
 

    planet_a = exo[exo["planet_name"] == planet_1].iloc[0]

    planet_b = exo[exo["planet_name"] == planet_2].iloc[0]

    st.divider()

 
    #             PLANET COMPARISON CARDS
 

    st.subheader("🪐 Planet Comparison")

    left_card, right_card = st.columns(2)

 
    #                 PLANET A CARD
 

    with left_card:

        st.markdown("## 🪐 Planet A")

        st.metric("Planet Name", planet_a["planet_name"])

        st.write(f"**Host Star :** {planet_a['host_star']}")

        st.write(f"**Planet Type :** {planet_a['planet_type']}")

        st.write(f"**Star Type :** {planet_a['star_type']}")

        st.write(f"**Discovery Year :** {int(planet_a['Discover_year'])}")

        st.write(f"**Temperature :** {planet_a['Planet_temperature']:.0f} K")

        st.write(f"**Radius :** {planet_a['planet_radius_earth']:.2f} R⊕")

        st.write(f"**Mass :** {planet_a['planet_mass_earth']:.2f} M⊕")

        st.write(f"**Orbit :** {planet_a['orbit_period_days']:.2f} Days")

        habitable_a = "✅ Yes" if planet_a["habitable_zone_flag"] == 1 else "❌ No"

        st.write(f"**Habitable :** {habitable_a}")

 
    #                 PLANET B CARD
 

    with right_card:

        st.markdown("## 🌍 Planet B")

        st.metric("Planet Name", planet_b["planet_name"])

        st.write(f"**Host Star :** {planet_b['host_star']}")

        st.write(f"**Planet Type :** {planet_b['planet_type']}")

        st.write(f"**Star Type :** {planet_b['star_type']}")

        st.write(f"**Discovery Year :** {int(planet_b['Discover_year'])}")

        st.write(f"**Temperature :** {planet_b['Planet_temperature']:.0f} K")

        st.write(f"**Radius :** {planet_b['planet_radius_earth']:.2f} R⊕")

        st.write(f"**Mass :** {planet_b['planet_mass_earth']:.2f} M⊕")

        st.write(f"**Orbit :** {planet_b['orbit_period_days']:.2f} Days")

        habitable_b = "✅ Yes" if planet_b["habitable_zone_flag"] == 1 else "❌ No"

        st.write(f"**Habitable :** {habitable_b}")

    st.divider()

 
    #               COMPARISON TABLE
 

    st.subheader("📊 Scientific Comparison")

    comparison = {
        "Property": [
            "Planet Type",
            "Host Star",
            "Star Type",
            "Discovery Year",
            "Temperature (K)",
            "Radius (R⊕)",
            "Mass (M⊕)",
            "Orbit Period (Days)",
            "Distance Category",
            "Habitable Zone",
        ],
        planet_a["planet_name"]: [
            planet_a["planet_type"],
            planet_a["host_star"],
            planet_a["star_type"],
            int(planet_a["Discover_year"]),
            f"{planet_a['Planet_temperature']:.0f}",
            f"{planet_a['planet_radius_earth']:.2f}",
            f"{planet_a['planet_mass_earth']:.2f}",
            f"{planet_a['orbit_period_days']:.2f}",
            planet_a["Distance_category"],
            "Yes" if planet_a["habitable_zone_flag"] == 1 else "No",
        ],
        planet_b["planet_name"]: [
            planet_b["planet_type"],
            planet_b["host_star"],
            planet_b["star_type"],
            int(planet_b["Discover_year"]),
            f"{planet_b['Planet_temperature']:.0f}",
            f"{planet_b['planet_radius_earth']:.2f}",
            f"{planet_b['planet_mass_earth']:.2f}",
            f"{planet_b['orbit_period_days']:.2f}",
            planet_b["Distance_category"],
            "Yes" if planet_b["habitable_zone_flag"] == 1 else "No",
        ],
    }

    comparison_df = pd.DataFrame(comparison)

    st.dataframe(comparison_df, use_container_width=True, hide_index=True)

    st.divider()

 
    #                WINNER ANALYSIS
 

    st.subheader("🏆 Winner Analysis")

    winner1, winner2 = st.columns(2)

 
    #            PHYSICAL PROPERTIES
 

    with winner1:

        st.markdown("### 🌍 Physical Properties")

        # Radius

        if planet_a["planet_radius_earth"] > planet_b["planet_radius_earth"]:

            radius_winner = planet_a["planet_name"]

        elif planet_b["planet_radius_earth"] > planet_a["planet_radius_earth"]:

            radius_winner = planet_b["planet_name"]

        else:

            radius_winner = "🤝 Tie"

        st.success(f"📏 Larger Planet : {radius_winner}")

        # Mass

        if planet_a["planet_mass_earth"] > planet_b["planet_mass_earth"]:

            mass_winner = planet_a["planet_name"]

        elif planet_b["planet_mass_earth"] > planet_a["planet_mass_earth"]:

            mass_winner = planet_b["planet_name"]

        else:

            mass_winner = "🤝 Tie"

        st.success(f"⚖ More Massive : {mass_winner}")

        # Temperature (Lower is Better)

        if planet_a["Planet_temperature"] < planet_b["Planet_temperature"]:

            temp_winner = planet_a["planet_name"]

        elif planet_b["Planet_temperature"] < planet_a["Planet_temperature"]:

            temp_winner = planet_b["planet_name"]

        else:

            temp_winner = "🤝 Tie"

        st.success(f"🌡 Cooler Planet : {temp_winner}")

 
    #            ORBITAL PROPERTIES
 

    with winner2:

        st.markdown("### 🛰 Orbital Properties")

        # Orbit Period

        if planet_a["orbit_period_days"] > planet_b["orbit_period_days"]:

            orbit_winner = planet_a["planet_name"]

        elif planet_b["orbit_period_days"] > planet_a["orbit_period_days"]:

            orbit_winner = planet_b["planet_name"]

        else:

            orbit_winner = "🤝 Tie"

        st.success(f"🛰 Longer Orbit : {orbit_winner}")

        # Discovery Year (Earlier is Better)

        if planet_a["Discover_year"] < planet_b["Discover_year"]:

            discovery_winner = planet_a["planet_name"]

        elif planet_b["Discover_year"] < planet_a["Discover_year"]:

            discovery_winner = planet_b["planet_name"]

        else:

            discovery_winner = "🤝 Tie"

        st.success(f"📅 Earlier Discovery : {discovery_winner}")

        # Habitable Zone

        if planet_a["habitable_zone_flag"] == 1 and planet_b["habitable_zone_flag"] == 0:

            habitability = planet_a["planet_name"]

        elif planet_b["habitable_zone_flag"] == 1 and planet_a["habitable_zone_flag"] == 0:

            habitability = planet_b["planet_name"]

        elif planet_a["habitable_zone_flag"] == 1 and planet_b["habitable_zone_flag"] == 1:

            habitability = "🤝 Both Habitable"

        else:

            habitability = "❌ Neither"

        st.success(f"🌱 Better Habitability : {habitability}")

    st.divider()

 
    #            FINAL COMPARISON VERDICT
 

    st.subheader("🤖 Final Comparison Verdict")

    score_a = 0
    score_b = 0

 
    # TEMPERATURE (Lower is Better)
 

    if planet_a["Planet_temperature"] < planet_b["Planet_temperature"]:
        score_a += 1

    elif planet_b["Planet_temperature"] < planet_a["Planet_temperature"]:
        score_b += 1

 
    # RADIUS (Larger is Better)
 

    if planet_a["planet_radius_earth"] > planet_b["planet_radius_earth"]:
        score_a += 1

    elif planet_b["planet_radius_earth"] > planet_a["planet_radius_earth"]:
        score_b += 1

 
    # MASS (Larger is Better)
 

    if planet_a["planet_mass_earth"] > planet_b["planet_mass_earth"]:
        score_a += 1

    elif planet_b["planet_mass_earth"] > planet_a["planet_mass_earth"]:
        score_b += 1

 
    # ORBIT PERIOD (Longer is Better)
 

    if planet_a["orbit_period_days"] > planet_b["orbit_period_days"]:
        score_a += 1

    elif planet_b["orbit_period_days"] > planet_a["orbit_period_days"]:
        score_b += 1

 
    # DISCOVERY YEAR (Earlier is Better)
 

    if planet_a["Discover_year"] < planet_b["Discover_year"]:
        score_a += 1

    elif planet_b["Discover_year"] < planet_a["Discover_year"]:
        score_b += 1

 
    # HOST STAR MASS (Higher is Better)
 

    if planet_a["Host_star_mass"] > planet_b["Host_star_mass"]:
        score_a += 1

    elif planet_b["Host_star_mass"] > planet_a["Host_star_mass"]:
        score_b += 1

 
    # HOST STAR RADIUS (Higher is Better)
 

    if planet_a["Host_star_radius"] > planet_b["Host_star_radius"]:
        score_a += 1

    elif planet_b["Host_star_radius"] > planet_a["Host_star_radius"]:
        score_b += 1

 
    # HOST STAR TEMPERATURE
    # Sun-like stars (≈5778 K) are preferred
 

    diff_a = abs(planet_a["Host_star_temp"] - 5778)
    diff_b = abs(planet_b["Host_star_temp"] - 5778)

    if diff_a < diff_b:
        score_a += 1

    elif diff_b < diff_a:
        score_b += 1

 
    # DISTANCE FROM HOST STAR
    # Habitable distance (≈1 AU) is preferred
 

    dist_a = abs(planet_a["Distance_from_host_star"] - 1)
    dist_b = abs(planet_b["Distance_from_host_star"] - 1)

    if dist_a < dist_b:
        score_a += 1

    elif dist_b < dist_a:
        score_b += 1

 
    # HABITABLE ZONE
    # Most Important (2 Points)
 

    if planet_a["habitable_zone_flag"] == 1 and planet_b["habitable_zone_flag"] == 0:
        score_a += 2

    elif planet_b["habitable_zone_flag"] == 1 and planet_a["habitable_zone_flag"] == 0:
        score_b += 2

 
    #             FINAL DECISION
 

    if score_a > score_b:

        winner = planet_a["planet_name"]
        loser = planet_b["planet_name"]

        st.success(f"🏆 Recommended Planet : **{winner}**")

        st.info(f"""
    ### 🌍 AI Comparison Summary

    **🏆 Winner : {winner}**

    **⭐ Final Score**

    - **{planet_a['planet_name']} : {score_a} Points**
    - **{planet_b['planet_name']} : {score_b} Points**

    ---

    ### 📊 Why {winner} Won?

    """)

        if planet_a["Planet_temperature"] < planet_b["Planet_temperature"]:
            st.write(f"✅ Cooler Planet (+1)")

        if planet_a["planet_radius_earth"] > planet_b["planet_radius_earth"]:
            st.write(f"✅ Larger Radius (+1)")

        if planet_a["planet_mass_earth"] > planet_b["planet_mass_earth"]:
            st.write(f"✅ Higher Mass (+1)")

        if planet_a["orbit_period_days"] > planet_b["orbit_period_days"]:
            st.write(f"✅ Longer Orbit (+1)")

        if planet_a["Discover_year"] < planet_b["Discover_year"]:
            st.write(f"✅ Earlier Discovery (+1)")

        if planet_a["Host_star_mass"] > planet_b["Host_star_mass"]:
            st.write(f"✅ More Massive Host Star (+1)")

        if planet_a["Host_star_radius"] > planet_b["Host_star_radius"]:
            st.write(f"✅ Larger Host Star (+1)")

        if abs(planet_a["Host_star_temp"] - 5778) < abs(planet_b["Host_star_temp"] - 5778):
            st.write(f"✅ More Sun-like Host Star (+1)")

        if abs(planet_a["Distance_from_host_star"] - 1) < abs(
            planet_b["Distance_from_host_star"] - 1
        ):
            st.write(f"✅ Better Orbital Distance (+1)")

        if planet_a["habitable_zone_flag"] == 1 and planet_b["habitable_zone_flag"] == 0:
            st.write(f"🌱 Habitable Zone (+2)")

        st.warning(f"""
    ### 📉 Why {loser} Lost?

    It achieved only **{score_b} points** because it performed worse in several scientific parameters compared to **{winner}**.
    """)


    elif score_b > score_a:

        winner = planet_b["planet_name"]
        loser = planet_a["planet_name"]

        st.success(f"🏆 Recommended Planet : **{winner}**")

        st.info(f"""
    ### 🌍 AI Comparison Summary

    **🏆 Winner : {winner}**

    **⭐ Final Score**

    - **{planet_b['planet_name']} : {score_b} Points**
    - **{planet_a['planet_name']} : {score_a} Points**

    ---

    ### 📊 Why {winner} Won?

    """)

        if planet_b["Planet_temperature"] < planet_a["Planet_temperature"]:
            st.write(f"✅ Cooler Planet (+1)")

        if planet_b["planet_radius_earth"] > planet_a["planet_radius_earth"]:
            st.write(f"✅ Larger Radius (+1)")

        if planet_b["planet_mass_earth"] > planet_a["planet_mass_earth"]:
            st.write(f"✅ Higher Mass (+1)")

        if planet_b["orbit_period_days"] > planet_a["orbit_period_days"]:
            st.write(f"✅ Longer Orbit (+1)")

        if planet_b["Discover_year"] < planet_a["Discover_year"]:
            st.write(f"✅ Earlier Discovery (+1)")

        if planet_b["Host_star_mass"] > planet_a["Host_star_mass"]:
            st.write(f"✅ More Massive Host Star (+1)")

        if planet_b["Host_star_radius"] > planet_a["Host_star_radius"]:
            st.write(f"✅ Larger Host Star (+1)")

        if abs(planet_b["Host_star_temp"] - 5778) < abs(planet_a["Host_star_temp"] - 5778):
            st.write(f"✅ More Sun-like Host Star (+1)")

        if abs(planet_b["Distance_from_host_star"] - 1) < abs(
            planet_a["Distance_from_host_star"] - 1
        ):
            st.write(f"✅ Better Orbital Distance (+1)")

        if planet_b["habitable_zone_flag"] == 1 and planet_a["habitable_zone_flag"] == 0:
            st.write(f"🌱 Habitable Zone (+2)")

        st.warning(f"""
    ### 📉 Why {loser} Lost?

    It achieved only **{score_a} points** because it performed worse in several scientific parameters compared to **{winner}**.
    """)


    else:

        st.warning(f"""
    ## 🤝 Comparison Result

    Both planets scored **{score_a} points**.

    Neither planet showed a clear scientific advantage based on the selected comparison parameters.

    This means both planets have nearly equal characteristics.
    """)
