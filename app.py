import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Unified Analytics & Tools Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Remove padding around main container for maximum iframe space */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100%;
    }

    /* Style the tabs header */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f8f9fa;
        padding: 8px 12px;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    .stTabs [data-baseweb="tab"] {
        height: 45px;
        white-space: pre-wrap;
        border-radius: 6px;
        padding: 0px 16px;
        font-weight: 500;
        color: #495057;
        background-color: transparent;
        transition: all 0.2s ease-in-out;
    }

    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: #1f2937 !important;
        font-weight: 700 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08) !important;
    }

    /* Full-width responsive iframe styling */
    .iframe-container {
        position: relative;
        width: 100%;
        height: 85vh;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-top: 10px;
        background-color: #ffffff;
    }

    .iframe-container iframe {
        width: 100%;
        height: 100%;
        border: none;
    }

    /* Custom sidebar styling */
    .sidebar-header {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

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
    st.title("⚙️ Dashboard Controls")
    st.markdown("Use this portal to access all embedded tools in one place.")
    
    st.divider()
    
    # Adjustable iframe height control
    iframe_height = st.slider("Adjust Viewer Height (px)", min_value=500, max_value=1200, value=850, step=50)
    
    # Reload button helper
    st.markdown("### 🔄 Quick Actions")
    if st.button("Reload Current View", use_container_width=True):
        st.rerun()

    st.divider()
    
    # External direct links section
    st.markdown("<p class='sidebar-header'>🔗 Direct Links</p>", unsafe_allow_html=True)
    for app in APPS:
        st.markdown(f"• [{app['icon']} {app['title']}]({app['url']})")

    st.caption("Built with Streamlit • Responsive Embedding Portal")

st.markdown("## 🌐 Unified Application Hub")

tab_labels = [f"{app['icon']} {app['title']}" for app in APPS]
tabs = st.tabs(tab_labels)

for i, tab in enumerate(tabs):
    app = APPS[i]
    with tab:
        # Display app sub-header and link
        col1, col2 = st.columns([4, 1])
        with col1:
            st.caption(f"**Description:** {app['description']}")
        with col2:
            st.markdown(f"<p style='text-align: right;'><a href='{app['url']}' target='_blank'>↗ Open in new tab</a></p>", unsafe_allow_html=True)

        # Responsive HTML iframe container
        iframe_html = f"""
        <div class="iframe-container" style="height: {iframe_height}px;">
            <iframe 
                src="{app['url']}" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                allowfullscreen>
            </iframe>
        </div>
        """
        st.components.v1.html(iframe_html, height=iframe_height + 20, scrolling=False)
