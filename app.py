import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Multi-App Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS styling
st.markdown("""
<style>
    .stApp > header { visibility: hidden; }
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100%;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 8px 8px 0px 0px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0e1117;
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# 3. Web App Directory
APPS = [
    {
        "title": "📋 Noticeboard Dashboard",
        "url": "https://noticeboard-dashboard-2.streamlit.app/",
        "description": "Noticeboard & Task Tracking Dashboard"
    },
    {
        "title": "🐙 Octopus Tracker",
        "url": "https://octopus-tracker-1.streamlit.app/",
        "description": "Octopus Energy Tariff & Usage Tracker"
    },
    {
        "title": "📈 Global Indices",
        "url": "https://stocks-global-indices-noticeboard.netlify.app/",
        "description": "Global Stock Market Indices Noticeboard"
    },
    {
        "title": "🎴 Flashcards",
        "url": "https://flashcard-everywhere.netlify.app/",
        "description": "Flashcard Study & Review App"
    },
    {
        "title": "🔍 Data Quality",
        "url": "https://data-quality-dashboard-260913.streamlit.app/",
        "description": "Data Quality Analysis Dashboard"
    }
]

# 4. Sidebar Options
st.sidebar.title("🎛️ App Controls")
st.sidebar.markdown("---")

iframe_height = st.sidebar.slider(
    "📏 Frame Height (px)",
    min_value=600,
    max_value=1400,
    value=850,
    step=50,
    help="Adjust iframe height to fit your display size."
)

scrolling_enabled = st.sidebar.checkbox("📜 Enable Frame Scrolling", value=True)

st.sidebar.markdown("---")
st.sidebar.subheader("🔗 Direct External Links")
for app in APPS:
    st.sidebar.markdown(f"• [{app['title']}]({app['url']})")

# 5. Top Tab Bar & Embed Render
tab_titles = [app["title"] for app in APPS]
tabs = st.tabs(tab_titles)

for idx, tab in enumerate(tabs):
    app = APPS[idx]
    with tab:
        st.caption(f"📍 **{app['description']}** — [Open directly in new tab ↗]({app['url']})")
        
        # Streamlit embedded iframe component
        components.iframe(
            src=app["url"],
            height=iframe_height,
            scrolling=scrolling_enabled
        )
