import streamlit as st

# Set page configuration for full-width layout
st.set_page_config(
    page_title="Unified Analytics Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for UI enhancements and smooth tab spacing
st.markdown("""
<style>
    /* Reduce top and bottom padding for max iframe viewing area */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100%;
    }

    /* Style navigation tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f8f9fa;
        padding: 8px 12px;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }

    .stTabs [data-baseweb="tab"] {
        height: 42px;
        border-radius: 6px;
        padding: 0px 16px;
        font-weight: 500;
        color: #495057;
        transition: all 0.2s ease-in-out;
    }

    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: #1f2937 !important;
        font-weight: 700 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08) !important;
    }
</style>
""", unsafe_allow_html=True)

# Registry of apps to display in top tabs
APPS = [
    {
        "title": "Noticeboard Dashboard",
        "icon": "📌",
        "url": "https://noticeboard-dashboard-2.streamlit.app/",
        "description": "Centralized noticeboard and dashboard feeds."
    },
    {
        "title": "Octopus Tracker",
        "icon": "🐙",
        "url": "https://octopus-tracker-1.streamlit.app/",
        "description": "Energy tariff and usage tracking dashboard."
    },
    {
        "title": "Global Indices",
        "icon": "📈",
        "url": "https://stocks-global-indices-noticeboard.netlify.app/",
        "description": "Real-time stock market indices and overview."
    },
    {
        "title": "Flashcards",
        "icon": "🗂️",
        "url": "https://flashcard-everywhere.netlify.app/",
        "description": "Everywhere interactive flashcard learning tool."
    },
    {
        "title": "Data Quality Dashboard",
        "icon": "🛡️",
        "url": "https://data-quality-dashboard-260913.streamlit.app/",
        "description": "Data validation, checks, and quality analytics."
    }
]

with st.sidebar:
    st.title("⚙️ Portal Controls")
    st.markdown("Access all consolidated tools in one place.")
    
    st.divider()
    
    # Adjustable iframe height
    iframe_height = st.slider("Iframe Height (px)", min_value=500, max_value=1200, value=850, step=50)
    
    if st.button("🔄 Refresh Application", use_container_width=True):
        st.rerun()

    st.divider()
    
    # Direct links to external apps
    st.markdown("### 🔗 Direct Links")
    for app in APPS:
        st.markdown(f"• [{app['icon']} {app['title']}]({app['url']})")

    st.caption("Built with Streamlit • Native `st.iframe` Portal")

st.markdown("## 🌐 Unified Application Hub")

tab_labels = [f"{app['icon']} {app['title']}" for app in APPS]
tabs = st.tabs(tab_labels)

for i, tab in enumerate(tabs):
    app = APPS[i]
    with tab:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.caption(f"**Description:** {app['description']}")
        with col2:
            st.markdown(f"<p style='text-align: right;'><a href='{app['url']}' target='_blank'>↗ Open in new tab</a></p>", unsafe_allow_html=True)

        # Native Streamlit iframe component
        st.iframe(
            src=app["url"],
            height=iframe_height,
            scrolling=True
        )
