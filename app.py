import streamlit as st
import plotly.express as px
import time

from ui.styles import apply_styles
from algorithms.brute_force import brute_force_partition
from algorithms.dynamic_programming import dp_partition


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Power Grid Load Balancing",
    layout="wide"
)

apply_styles()


# ------------------------------------------------
# HERO SECTION
# ------------------------------------------------

st.markdown("""
<div class="hero-wrapper">

<div class="hero-badge">
⚡ Design & Analysis of Algorithms
</div>

<div class="hero-title-top">
Power Grid
</div>

<div class="hero-title-bottom">
Load Balancing
</div>

<div class="hero-subtitle">
Partition electrical loads between two power plants with minimum imbalance using 
<b style="color:#facc15;">Brute Force O(2ⁿ)</b> and 
<b style="color:#f59e0b;">Dynamic Programming O(n × Sum)</b>
</div>

<div class="hero-features">
⚙ Real-time Benchmarks &nbsp;&nbsp;&nbsp;&nbsp; ⚡ Live Visualization
</div>

</div>
""", unsafe_allow_html=True)



# ------------------------------------------------
# INPUT CARD
# ------------------------------------------------

st.markdown('<div class="card-box">', unsafe_allow_html=True)

st.markdown(
'<div class="section-title">⚡ City Zone Loads (MW)</div>',
unsafe_allow_html=True
)

loads_input = st.text_input(
"Enter loads separated by commas",
placeholder="Example: 10,20,15,25,30"
)

capacity = st.number_input(
"Maximum capacity per power plant (MW)",
min_value=1,
value=60
)

run_algo = st.button("Run Algorithms")

st.markdown('</div>', unsafe_allow_html=True)



# ------------------------------------------------
# SHOW TOTAL LOAD
# ------------------------------------------------

if loads_input:
    loads_preview = list(map(int, loads_input.split(",")))
    st.caption(f"Total Load: {sum(loads_preview)} MW | Zones: {len(loads_preview)}")



# ------------------------------------------------
# RUN ALGORITHMS
# ------------------------------------------------

if run_algo and loads_input:

    loads = list(map(int, loads_input.split(",")))
    total_load = sum(loads)

    # ----------------------------
    # BRUTE FORCE
    # ----------------------------

    start = time.time()

    subset_bf = brute_force_partition(loads)
    steps_bf = 2 ** len(loads)

    runtime_bf = round((time.time() - start) * 1000, 3)

    plantA_bf = subset_bf
    plantB_bf = loads.copy()

    for x in subset_bf:
        if x in plantB_bf:
            plantB_bf.remove(x)

    loadA_bf = sum(plantA_bf)
    loadB_bf = sum(plantB_bf)


    # ----------------------------
    # DYNAMIC PROGRAMMING
    # ----------------------------

    start = time.time()

    subset_dp, steps_dp = dp_partition(loads)

    runtime_dp = round((time.time() - start) * 1000, 3)

    plantA_dp = subset_dp
    plantB_dp = loads.copy()

    for x in subset_dp:
        if x in plantB_dp:
            plantB_dp.remove(x)

    loadA_dp = sum(plantA_dp)
    loadB_dp = sum(plantB_dp)


    # ----------------------------
    # IMBALANCE
    # ----------------------------

    imbalance = abs(loadA_bf - loadB_bf)


    # ------------------------------------------------
    # BAR CHARTS
    # ------------------------------------------------

    fig_bf = px.bar(
        x=["Plant A","Plant B"],
        y=[loadA_bf, loadB_bf],
        color=["Plant A","Plant B"],
        color_discrete_sequence=["#2dd4bf","#0d9488"]
    )

    fig_dp = px.bar(
        x=["Plant A","Plant B"],
        y=[loadA_dp, loadB_dp],
        color=["Plant A","Plant B"],
        color_discrete_sequence=["#facc15","#d97706"]
    )


    # ------------------------------------------------
    # RESULT CARDS
    # ------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown('<div class="algo-card">', unsafe_allow_html=True)

        st.subheader("Brute Force")

        st.plotly_chart(fig_bf, use_container_width=True)

        st.metric("Plant A Load", f"{loadA_bf} MW")
        st.metric("Plant B Load", f"{loadB_bf} MW")

        st.write("Plant A Zones:", plantA_bf)
        st.write("Plant B Zones:", plantB_bf)

        st.metric("Imbalance", f"{imbalance} MW")
        st.metric("Steps", steps_bf)
        st.metric("Time", f"{runtime_bf} ms")

        st.markdown('</div>', unsafe_allow_html=True)



    with col2:

        st.markdown('<div class="algo-card">', unsafe_allow_html=True)

        st.subheader("Dynamic Programming")

        st.plotly_chart(fig_dp, use_container_width=True)

        st.metric("Plant A Load", f"{loadA_dp} MW")
        st.metric("Plant B Load", f"{loadB_dp} MW")

        st.write("Plant A Zones:", plantA_dp)
        st.write("Plant B Zones:", plantB_dp)

        st.metric("Imbalance", f"{imbalance} MW")
        st.metric("Steps", steps_dp)
        st.metric("Time", f"{runtime_dp} ms")

        st.markdown('</div>', unsafe_allow_html=True)



    # ------------------------------------------------
    # COMPARISON TABLE
    # ------------------------------------------------

    st.markdown('<div class="card-box">', unsafe_allow_html=True)

    st.subheader("Algorithm Comparison")

    comparison = {
        "Metric":[
            "Time Complexity",
            "Space Complexity",
            "Steps Executed",
            "Execution Time",
            "Imbalance"
        ],

        "Brute Force":[
            f"O(2^{len(loads)})",
            "O(1)",
            steps_bf,
            f"{runtime_bf} ms",
            f"{imbalance} MW"
        ],

        "Dynamic Programming":[
            f"O(n × Sum) = O({len(loads)} × {total_load})",
            f"O(Sum) = O({total_load})",
            steps_dp,
            f"{runtime_dp} ms",
            f"{imbalance} MW"
        ]
    }

    st.table(comparison)

    st.markdown('</div>', unsafe_allow_html=True)