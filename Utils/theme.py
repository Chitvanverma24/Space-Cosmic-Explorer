import streamlit as st
import base64
from pathlib import Path
from textwrap import dedent


# PAGE CONFIG

def page_config(title):

    st.set_page_config(

        page_title=title,

        page_icon="🚀",

        layout="wide",

        initial_sidebar_state="expanded"

    )


# LOAD CSS

def load_css():

    css_path = Path("CSS/main.css")

    with open(css_path, encoding="utf-8") as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True

        )


# ============================================================================
# PAGE HEADER
#
# Premium hero-style page header used at the top of every page:
#   LEFT  — badge + title + subtitle (+ optional highlight chips)
#   RIGHT — cinematic SVG artwork (Assets/Hero/hero_planet.svg)
# Each page follows it with st.divider().
#
# NOTE 1: the HTML is dedented before st.markdown() renders it. Lines indented
# by 4+ spaces inside a Markdown string are treated as an indented CODE BLOCK,
# so indented HTML gets displayed as literal text instead of being rendered.
#
# NOTE 2: the artwork is embedded as a base64 data URI so the whole header is
# a single self-contained HTML block — no file-serving issues, and SVG SMIL
# animations (twinkling stars, drifting moons) still play inside the <img>.
# ============================================================================

@st.cache_data(show_spinner=False)
def _hero_art():

    art_path = Path("Assets/Hero/hero_planet.svg")

    if not art_path.exists():
        return ""

    encoded = base64.b64encode(art_path.read_bytes()).decode()

    return (
        '<div class="page-header-art">'
        f'<img src="data:image/svg+xml;base64,{encoded}" alt="" />'
        '</div>'
    )


def page_header(badge, title, subtitle, chips=None):

    chips_html = ""

    if chips:
        pills = "".join(
            f'<span class="page-chip">{chip}</span>' for chip in chips
        )
        chips_html = f'<div class="page-chips">{pills}</div>'

    st.markdown(
        dedent(f"""\
        <div class="page-header">
        <div class="page-header-content">
        <div class="page-badge">{badge}</div>
        <h1 class="page-title">{title}</h1>
        <p class="page-subtitle">{subtitle}</p>{chips_html}
        </div>{_hero_art()}
        </div>
        """),
        unsafe_allow_html=True,
    )


# SECTION HEADER

def section_header(title, subtitle=""):

    st.markdown(
        f"""
        <div class="section-header">

            <div>

                <div class="section-title">

                    {title}

                </div>

                <div class="section-description">

                    {subtitle}

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# DIVIDER

def divider():

    st.markdown("<hr>", unsafe_allow_html=True)


# EMPTY SPACE

def space(height=25):

    st.markdown(

        f"<div style='height:{height}px'></div>",

        unsafe_allow_html=True

    )


# FOOTER

def footer():

    st.markdown(
        """
        <div class="footer">

            <div class="footer-title">
                🪐 Space Cosmic Explorer
            </div>

            <div class="footer-description">

                Explore Exoplanets • Host Stars • Near-Earth Asteroids

            </div>

            <div class="footer-tech">

                Built with ❤️ using
                Python • Streamlit • Pandas • NumPy • Plotly

            </div>

            <div class="footer-copy">

                © 2026 Space Cosmic Explorer | Designed by Chitvan Verma

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
