from cmath import e

import streamlit as st
import plotly.express as px
import time

from utils.dp_visualization import render_dp_table
from ui.styles import apply_styles
from algorithms.brute_force import brute_force_partition
from algorithms.dynamic_programming import dp_partition
from automata import build_automata, graph_to_plotly
from utils.benchmark import *
import plotly.express as px


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

    subset_dp, steps_dp, dp_table = dp_partition(loads)

    runtime_dp = round((time.time() - start) * 1000, 3)

    plantA_dp = subset_dp
    plantB_dp = loads.copy()

    for x in subset_dp:
        if x in plantB_dp:
            plantB_dp.remove(x)

    loadA_dp = sum(plantA_dp)
    loadB_dp = sum(plantB_dp)

    # ------------------------------------------------
    # CAPACITY CHECK
    # ------------------------------------------------

    capacity_ok = (
    loadA_dp <= capacity and
    loadB_dp <= capacity
    )

    # ----------------------------
    # IMBALANCE
    # ----------------------------

    imbalance_bf = abs(loadA_bf - loadB_bf)
    imbalance_dp = abs(loadA_dp - loadB_dp)


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

        st.plotly_chart(
            fig_bf,
            use_container_width=True
        )

        st.metric("Plant A Load", f"{loadA_bf} MW")
        st.metric("Plant B Load", f"{loadB_bf} MW")

        st.write("Plant A Zones:", plantA_bf)
        st.write("Plant B Zones:", plantB_bf)

        st.metric("Imbalance", f"{imbalance_bf} MW")
        st.metric("Steps", steps_bf)
        st.metric("Time", f"{runtime_bf} ms")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:

        st.markdown('<div class="algo-card">', unsafe_allow_html=True)

        st.subheader("Dynamic Programming")

        st.plotly_chart(
            fig_dp,
            use_container_width=True
        )

        st.metric("Plant A Load", f"{loadA_dp} MW")
        st.metric("Plant B Load", f"{loadB_dp} MW")

        st.write("Plant A Zones:", plantA_dp)
        st.write("Plant B Zones:", plantB_dp)

        st.metric("Imbalance", f"{imbalance_dp} MW")
        st.metric("Steps", steps_dp)
        st.metric("Time", f"{runtime_dp} ms")

        st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------------------------------
    # CAPACITY STATUS
    # ------------------------------------------------

    if capacity_ok:

        st.success(
            f"✅ Capacity Constraint Satisfied "
            f"(Max Capacity = {capacity} MW)"
        )

    else:

        st.error(
            f"⚠ Capacity Constraint Violated "
            f"(Max Capacity = {capacity} MW)"
        )

    # ------------------------------------------------
    # WINNER CARD
    # ------------------------------------------------

    if runtime_dp < runtime_bf:

        st.success(
            "🏆 Dynamic Programming is Faster"
        )

    else:

        st.success(
            "🏆 Brute Force is Faster"
        )

        # ------------------------------------------------
        # COMPARISON TABLE
        # ------------------------------------------------

        st.markdown('<div class="card-box">', unsafe_allow_html=True)

        st.subheader("Algorithm Comparison")

        comparison = {
            "Metric": [
                "Time Complexity",
                "Space Complexity",
                "Steps Executed",
                "Execution Time",
                "Imbalance"
            ],

            "Brute Force": [
                f"O(2^{len(loads)})",
                "O(1)",
                steps_bf,
                f"{runtime_bf} ms",
                f"{imbalance_bf} MW"
            ],

            "Dynamic Programming": [
            f"O(n * Sum) = O({len(loads)} * {total_load})",
                f"O(Sum) = O({total_load})",
                steps_dp,
                f"{runtime_dp} ms",
                f"{imbalance_dp} MW"
            ]
        }

        st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

        st.markdown('</div>', unsafe_allow_html=True)

        # ==========================================
        # FINITE AUTOMATA VISUALIZATION
        # ==========================================

        st.markdown('<div class="card-box">', unsafe_allow_html=True)

        st.markdown("""
        <div style="padding-bottom:15px;">
            <h2 style="color:white;">
                ⚡ Finite Automaton — Load Selection
            </h2>
        </div>
        """, unsafe_allow_html=True)

        G = build_automata(
            loads, 
            max_depth=4
        )

        fig_automata = graph_to_plotly(G)

        st.plotly_chart(
            fig_automata,
            use_container_width=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

        # -------------------------------------
        # DP TABLE VISUALIZATION
        # -------------------------------------

        target = total_load // 2

        closest = 0

        for s in range(target, -1, -1):

            if dp_table[-1][s]:

                closest = s
                break

        render_dp_table(
            dp_table,
            loads,
            target,
            closest
        )

        # ------------------------------------------------
        # PERFORMANCE BENCHMARK
        # ------------------------------------------------

        st.markdown('<div class="card-box">', unsafe_allow_html=True)

        st.markdown("""
        <div style="padding-bottom:15px;">
            <h2 style="color:white;">
                📈 Performance Benchmark
            </h2>
        </div>
        """, unsafe_allow_html=True)

        df_time, df_ops = generate_benchmark()

        bench_col1, bench_col2 = st.columns(2)

        with bench_col1:

            st.subheader("Execution Time (ms)")

            fig_time = create_time_chart(df_time)

            st.plotly_chart(
                fig_time,
                use_container_width=True
            ) 

        with bench_col2:

            st.subheader("Theoretical Operations")

            fig_ops = create_ops_chart(df_ops)

            st.plotly_chart(
                fig_ops,
                use_container_width=True
            )

        st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------------------------------
    # COMPLEXITY EXPLANATION
    # ------------------------------------------------

    st.info(
    """
    Brute Force explores every possible subset,
    resulting in exponential growth O(2ⁿ).

    Dynamic Programming stores intermediate
    results and avoids repeated computation.

    Time Complexity:
    • Brute Force → O(2ⁿ)

    • Dynamic Programming → O(n × Sum)

    Space Complexity:
    • Brute Force → O(1)

    • Dynamic Programming → O(Sum)
    """
    )

    # ------------------------------------------------
    # DOWNLOAD REPORT
    # ------------------------------------------------

    report = f"""
    POWER GRID LOAD BALANCING REPORT

    Loads:
    {loads}

    BRUTE FORCE

    Plant A:
    {plantA_bf}

    Plant B:
    {plantB_bf}

    Imbalance:
    {imbalance_bf}

    DYNAMIC PROGRAMMING

    Plant A:
    {plantA_dp}

    Plant B:
    {plantB_dp}

    Imbalance:
    {imbalance_dp}

    Execution Time

    Brute Force:
    {runtime_bf} ms

    Dynamic Programming:
    {runtime_dp} ms
    """

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="load_balancing_report.txt",
        mime="text/plain"
    )
