import streamlit as st
from Utils.theme import page_header


def about_page():

    #                 PAGE HEADER

    page_header(
        "🚀 SPACE COSMIC EXPLORER",
        "ℹ️ About <span>Space Cosmic Explorer</span>",
        "An interactive Space Analytics Platform built to explore Exoplanets, "
        "Host Stars and Near-Earth Asteroids using real NASA datasets — through "
        "beautiful visualizations, intelligent recommendations and interactive dashboards."
    )

    st.divider()

    #                    PROJECT STATS

    stat1, stat2, stat3, stat4, stat5 = st.columns(5)


    with stat1:

        st.metric(

            label="🪐 Interactive Dashboards",

            value="7+"

        )

        st.caption("Complete Analytics Pages")

    

    with stat2:

        st.metric(

            label="🛰 NASA Datasets",

            value="2"

        )

        st.caption("Exoplanets + Asteroids")

    

    with stat3:

        st.metric(

            label="🌌 Space Objects",

            value="25K+"

        )

        st.caption("Planets & Asteroids")



    with stat4:

        st.metric(

            label="✅ Reliable Data",

            value="100%"

        )

        st.caption("Official NASA Sources")



    with stat5:

        st.metric(

            label="⚡ Built With",

            value="Streamlit"

        )

        st.caption("Fast • Interactive • Modern")

    st.divider()

  
    #                 MISSION • OFFER • DATA SOURCE

    mission_col, offer_col, data_col = st.columns([1.25,1,1])

   
    #                     OUR MISSION

    with mission_col:

        st.subheader("🎯 Our Mission")

        st.write("""

    To empower students, researchers and space
    enthusiasts by transforming complex NASA
    astronomical datasets into beautiful,
    interactive and easy-to-understand dashboards.

    Our goal is to make space exploration
    accessible for everyone through modern
    visual analytics and AI-powered insights.

    """)

        st.image(

            "Assets/About/mission.png",

            use_container_width=True

        )



    #                    WHAT WE OFFER

    with offer_col:

        st.subheader("⭐ What We Offer")

        st.write("✅ Explore thousands of confirmed exoplanets")

        st.write("✅ Analyze host star properties")

        st.write("✅ Monitor Near-Earth asteroids")

        st.write("✅ Compare planetary systems")

        st.write("✅ AI-powered planet recommendations")

        st.write("✅ Interactive visual dashboards")

        st.write("✅ Real NASA datasets")



 
    #                     DATA SOURCES

    with data_col:

        st.subheader("🗂 Data Sources")

        st.info("""

    ### NASA Exoplanet Archive

    Confirmed Exoplanets

    Host Star Properties

    Planet Characteristics

    """)

        st.info("""

    ### NASA Near Earth Object Database

    Asteroid Details

    Close Approaches

    Orbital Information

    """)

    st.divider()



    #         TECHNOLOGIES • USERS • CREATOR

    tech_col, users_col, creator_col = st.columns([1.15,1,1])


    #                 TECHNOLOGIES USED

    with tech_col:

        st.subheader("💻 Technologies Used")

        # tech1, tech2, tech3 = st.columns(3)

        # with tech1:

        st.info("🐍\n\nPython")

        st.info("📊\n\nPandas")

        # with tech2:

        st.info("🚀\n\nStreamlit")

        st.info("🔢\n\nNumPy")

        # with tech3:

        st.info("📈\n\nPlotly")

        st.info("🌐\n\nHTML / CSS")


    
    #                  WHO CAN USE THIS

    with users_col:

        st.subheader("👨‍🚀 Who Can Use This?")

        st.success("🎓 Students")

        st.caption(
            "Learn Space Science using interactive dashboards."
        )

        st.success("🔬 Researchers")

        st.caption(
            "Analyze NASA datasets quickly."
        )

        st.success("👨‍🏫 Educators")

        st.caption(
            "Teach astronomy with beautiful visualizations."
        )

        st.success("🌌 Space Enthusiasts")

        st.caption(
            "Explore the universe like a professional."
        )

    #                  ABOUT CREATOR

    with creator_col:

        st.subheader("👨‍💻 About The Creator")

        st.markdown("""
            <div style="
            text-align:center;
            font-size:90px;
            padding:15px;
            border:2px solid #7F5AF0;
            border-radius:50%;
            width:120px;
            height:120px;
            margin:auto;
            display:flex;
            align-items:center;
            justify-content:center;
            ">

            👤

            </div>
            """, unsafe_allow_html=True
        )

        st.markdown("### Chitvan Verma")

        st.write("🎓 B.Tech CSE (AI/ML Engineering)")

        st.write("""
            Passionate about

            • Artificial Intelligence

            • Data Science

            • Interactive Dashboard Development
            """
        )

        st.divider()

        st.write("📧 chitvanverma555@gmail.com")

        st.write("💻 GitHub : https://github.com/Chitvanverma24")

        st.write("🔗 LinkedIn : https://www.linkedin.com/in/chitvan-verma-803008395/")


  
    #                     QUICK PROJECT INFO

    st.subheader("🚀 Project Highlights")

    high1, high2, high3 = st.columns(3)

    with high1:

        st.success("""
    ### 📊 Interactive Analytics

    ✔ Exoplanet Explorer

    ✔ Host Star Observatory

    ✔ Asteroid Information Center

    ✔ Visualization Dashboard

    ✔ Planet Recommendation Engine

    ✔ Galactic Comparison Lab
    """)

    with high2:

        st.info("""
    ### 🤖 AI Powered Features

    ✔ Smart Planet Recommendation

    ✔ Intelligent Planet Comparison

    ✔ Scientific Property Analysis

    ✔ NASA Dataset Insights

    ✔ Interactive User Experience
    """)

    with high3:

        st.warning("""
    ### 🌌 Future Improvements

    ⭐ AI Chat Assistant

    ⭐ Live NASA API Integration

    ⭐ Real-Time Space Updates

    ⭐ 3D Planet Visualization

    ⭐ Advanced AI Analytics
    """)

    st.divider()


    
    #                  NASA DISCLAIMER
    

    st.info("""

    ### 🛰 Data Disclaimer

    This project is developed purely for educational and learning purposes.

    All astronomical information used in this dashboard is collected from publicly available NASA datasets, including:

    • NASA Exoplanet Archive

    • NASA Near-Earth Object (NEO) Database

    This dashboard does not represent an official NASA product.

    """)

    
    #                      FOOTER
    

    st.divider()

    left, center, right = st.columns([2,2,2])

    with left:

        st.caption(
            "🛰 Data sourced from NASA Exoplanet Archive & JPL Small-Body Database"
        )

    with center:

        st.caption(
            "🚀 Space Cosmic Explorer • Version 1.0"
        )

        st.caption(
            "Built with ❤️ using Streamlit"
        )

    with right:

        st.caption(
            "Keep Exploring • Keep Discovering 🌌"
        )

    st.markdown(
        "<center><h5>© 2026 Space Cosmic Explorer | Developed by Chitvan Verma</h5></center>",
        unsafe_allow_html=True
    )