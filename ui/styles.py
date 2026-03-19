import streamlit as st

def apply_styles():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* GRID BACKGROUND */

    .stApp{
        background-color:#0a0500;
        background-image:
        linear-gradient(rgba(255,200,0,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,200,0,0.05) 1px, transparent 1px);
        background-size:40px 40px;
    }

    /* HERO SECTION */

    .hero-wrapper{
        text-align:center;
        margin-top:120px;
        margin-bottom:90px;
    }

    .hero-badge{
        display:inline-block;
        padding:8px 20px;
        border-radius:20px;
        background:#1a1205;
        color:#facc15;
        font-size:14px;
        margin-bottom:30px;
    }

    .hero-title-top{
        font-size:90px;
        font-weight:300;
        color:#e5e5e5;
        letter-spacing:-2px;
        margin-bottom:0px;
    }

    .hero-title-bottom{
        font-size:110px;
        font-weight:800;
        letter-spacing:-3px;
        background:linear-gradient(90deg,#facc15,#f59e0b);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        text-shadow:0px 0px 30px rgba(255,180,0,0.4);
        margin-top:-20px;
    }

    .hero-subtitle{
        font-size:18px;
        color:#d4d4d4;
        margin-top:40px;
    }

    .hero-features{
        margin-top:30px;
        color:#d4d4d4;
        font-size:15px;
    }

    /* INPUT CARD */

    .card-box{
        background:#120a02;
        border-radius:18px;
        padding:30px;
        border:1px solid rgba(255,200,0,0.2);
        box-shadow:0 0 30px rgba(255,200,0,0.15);
        margin-top:40px;
    }

    .section-title{
        font-size:24px;
        font-weight:700;
        margin-bottom:20px;
    }

    /* ALGORITHM CARDS */

    .algo-card{
        background:#120a02;
        padding:25px;
        border-radius:16px;
        border:1px solid rgba(255,200,0,0.15);
        box-shadow:0 0 25px rgba(255,200,0,0.12);
        margin-top:30px;
    }

    /* RUN BUTTON */

    div.stButton > button{
        background:linear-gradient(90deg,#facc15,#f59e0b);
        color:black;
        font-weight:600;
        border-radius:10px;
        padding:12px 26px;
        border:none;
        box-shadow:0 0 20px rgba(250,204,21,0.4);
    }

    div.stButton > button:hover{
        transform:scale(1.05);
        box-shadow:0 0 35px rgba(250,204,21,0.7);
    }

    </style>
    """, unsafe_allow_html=True)