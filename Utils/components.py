#               SPACE COSMIC EXPLORER
#                  COMPONENTS.PY

import streamlit as st
from textwrap import dedent


#                  PAGE TITLE

def page_title(title: str, subtitle: str = ""):

    st.markdown(
        dedent(f"""
        <div class="page-header">

            <h1 class="page-title">
                {title}
            </h1>

            <p class="page-subtitle">
                {subtitle}
            </p>

        </div>
        """),
        unsafe_allow_html=True
    )


#                SECTION TITLE

def section_title(title: str, description: str = ""):

    st.markdown(
        dedent(f"""
        <div class="section-header">

            <div class="section-title">

                {title}

            </div>

            <div class="section-description">

                {description}

            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


#                 SUB SECTION

def sub_section(title: str):

    st.markdown(
        dedent(f"""
        <div class="sub-section">

            {title}

        </div>
        """),
        unsafe_allow_html=True
    )


#                    DIVIDER

def divider():

    st.markdown(
        dedent("""
        <div class="space-divider"></div>
        """),
        unsafe_allow_html=True
    )


#                     BADGE

def badge(text: str):

    st.markdown(
        dedent(f"""
        <span class="space-badge">

            {text}

        </span>
        """),
        unsafe_allow_html=True
    )


#                    INFO CHIP

def info_chip(icon: str, text: str):

    st.markdown(
        dedent(f"""
        <div class="info-chip">

            <span class="chip-icon">
                {icon}
            </span>

            <span class="chip-text">
                {text}
            </span>

        </div>
        """),
        unsafe_allow_html=True
    )


#                    STAT CHIP

def stat_chip(icon: str, text: str):

    st.markdown(
        dedent(f"""
        <div class="stat-chip">

            <span class="stat-icon">

                {icon}

            </span>

            <span class="stat-text">

                {text}

            </span>

        </div>
        """),
        unsafe_allow_html=True
    )

#                   METRIC CARD

def metric_card(
    title: str,
    value,
    icon: str = "📊",
    subtitle: str = "",
    color: str = "#49D6FF"
):

    st.markdown(
        dedent(f"""
        <div class="metric-card">

            <div class="metric-icon" style="color:{color};">
                {icon}
            </div>

            <div class="metric-title">
                {title}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-subtitle">
                {subtitle}
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


#                  DASHBOARD CARD

def dashboard_card(
    icon: str,
    title: str,
    description: str,
    button_text: str = "Explore →"
):

    st.markdown(
        dedent(f"""
        <div class="dashboard-card">

            <div class="dashboard-icon">

                {icon}

            </div>

            <div class="dashboard-title">

                {title}

            </div>

            <div class="dashboard-description">

                {description}

            </div>

            <div class="dashboard-button">

                {button_text}

            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


#                    GLASS CARD

def glass_card(
    title: str,
    content: str
):

    st.markdown(
        dedent(f"""
        <div class="glass-card">

            <div class="glass-title">

                {title}

            </div>

            <div class="glass-content">

                {content}

            </div>

        </div>
        """),
        unsafe_allow_html=True
    )

#                  FEATURE CARD

def feature_card(
    icon: str,
    title: str,
    description: str
):

    st.markdown(
        dedent(f"""
        <div class="feature-card">

            <div class="feature-icon">

                {icon}

            </div>

            <div class="feature-title">

                {title}

            </div>

            <div class="feature-description">

                {description}

            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


#                    INFO CARD

def info_card(
    title: str,
    content: str
):

    st.markdown(
        dedent(f"""
        <div class="info-card">

            <div class="info-title">

                {title}

            </div>

            <div class="info-content">

                {content}

            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


#                QUICK INSIGHT CARD

def quick_insight_card(
    title: str,
    value,
    icon: str = "✨"
):

    st.markdown(
        dedent(f"""
        <div class="quick-card">

            <div class="quick-icon">

                {icon}

            </div>

            <div class="quick-title">

                {title}

            </div>

            <div class="quick-value">

                {value}

            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


#              RECENT DISCOVERY CARD

def recent_discovery_card(
    planet_name: str,
    host_star: str,
    planet_type: str,
    discovery_year
):

    st.markdown(
        dedent(f"""
        <div class="discovery-card">

            <div class="discovery-planet">

                🪐 {planet_name}

            </div>

            <div class="discovery-item">

                ⭐ <strong>Host Star</strong><br>
                {host_star}

            </div>

            <div class="discovery-item">

                🌍 <strong>Planet Type</strong><br>
                {planet_type}

            </div>

            <div class="discovery-item">

                📅 <strong>Discovery Year</strong><br>
                {discovery_year}

            </div>

        </div>
        """),
        unsafe_allow_html=True
    )

