#               SPACE COSMIC EXPLORER
#                  MAIN CONTROLLER

import streamlit as st
from streamlit_option_menu import option_menu


# ---------------- THEME ---------------- #

from Utils.theme import (
    page_config,
    load_css,
    # show_sidebar_logo
)

# ---------------- PAGES ---------------- #

from App.Home_page import home_page
from App.visualization_page import visualization_page
from App.Exoplanet_Explorer import exoplanet_explorer_page
from App.Host_star import host_star_page
from App.Asteroid import asteroid_page
from App.Recommendation import planet_recommendation_page
from App.Comparison import galactic_comparison_page
from App.About import about_page


#               PAGE CONFIG

page_config("Space Cosmic Explorer")

load_css()


#               SIDEBAR

with st.sidebar:

    # show_sidebar_logo()

    st.image(
        "Assets/logo.png",
        use_container_width=True
    )
    selected = option_menu(
        menu_title=None,
        options=["Home", "Visualization", "Exoplanet Explorer",
                "Host Star Observatory", "Asteroid Information Center",
                "Planet Recommendation Engine", "Galactic Comparison Lab", "About"],
        icons=["house", "bar-chart", "globe", "stars", "stars",
            "robot", "layers", "info-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "6px !important",
                "background-color": "#0d0b1a",   # matches --sce-space-900, no more grey
            },
            "icon": {
                "color": "#49D6FF",              # cyan icons, matches --sce-cyan
                "font-size": "18px",
            },
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "4px 0px",
                "padding": "12px 14px",
                "border-radius": "10px",
                "color": "#C9C3E0",               # matches --sce-text-secondary
                "background-color": "transparent",
            },
            "nav-link:hover": {
                "background-color": "rgba(127, 90, 240, 0.16)",
            },
            "nav-link-selected": {
                "background-color": "#7F5AF0",    # matches --sce-purple
                "color": "#ffffff",
                "font-weight": "700",
            },
        }
    )

#                    PAGE ROUTER

pages = {
    "Home": home_page,
    "Visualization": visualization_page,
    "Exoplanet Explorer": exoplanet_explorer_page,
    "Host Star Observatory": host_star_page,
    "Asteroid Information Center": asteroid_page,
    "Planet Recommendation Engine": planet_recommendation_page,
    "Galactic Comparison Lab": galactic_comparison_page,
    "About": about_page,
}


#                 LOAD SELECTED PAGE

pages[selected]()
