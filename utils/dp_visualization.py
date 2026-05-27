import streamlit as st
import streamlit.components.v1 as components

def render_dp_table(dp, loads, target, closest):

    html = f"""
    <div style="
        background:#0a0a0a;
        border:1px solid rgba(251,191,36,0.15);
        border-radius:20px;
        padding:25px;
        margin-top:25px;
        overflow-x:auto;
    ">

    <h2 style="
        color:white;
        margin-bottom:10px;
    ">
        DP Table — Subset Sum
    </h2>

    <p style="color:#9ca3af;">
        dp[i][j] =
        <span style="color:#fbbf24;font-weight:bold;">
            true
        </span>
        if sum j is achievable using first i loads.
        Target:
        <span style="color:#fbbf24;font-weight:bold;">
            {target}
        </span>
    </p>

    <table style="
        width:100%;
        border-collapse:collapse;
        text-align:center;
        color:white;
        margin-top:20px;
    ">
    """

    max_sum = len(dp[0])    

    html += """
    <tr>
        <th style="
            padding:10px;
            color:#9ca3af;
            border-bottom:1px solid #222;
        ">
            Load\\Sum
        </th>
    """

    for j in range(max_sum):

        color = "#fbbf24" if j == closest else "#94a3b8"

        html += f"""
        <th style="
            color:{color};
            padding:10px;
            border-bottom:1px solid #222;
        ">
            {j}
        </th>
        """

    html += "</tr>"

    labels = ["∅"] + [f"+{x}" for x in loads]

    for i in range(len(dp)):

        html += "<tr>"

        html += f"""
        <td style="
            color:#9ca3af;
            text-align:left;
            padding:10px;
            border-bottom:1px solid #111;
        ">
            {labels[i]}
        </td>
        """

        for j in range(max_sum):

            if dp[i][j]:

                if i == len(dp)-1 and j == closest:

                    html += """
                    <td style="
                        background:#fbbf24;
                        color:black;
                        font-weight:bold;
                        border-radius:8px;
                    ">
                        T
                    </td>
                    """

                else:

                    html += """
                    <td style="
                        color:#fbbf24;
                    ">
                        T
                    </td>
                    """

            else:

                html += """
                <td style="
                    color:#374151;
                ">
                    .
                </td>
                """

        html += "</tr>"

    html += "</table>"

    html += f"""
    <hr style="
        border-color:#222;
        margin-top:20px;
    ">

    <div style="
        color:#9ca3af;
        margin-top:10px;
    ">

        <span style="
            color:#fbbf24;
            font-weight:bold;
        ">
            T
        </span>
        = achievable

        &nbsp;&nbsp;&nbsp;&nbsp;

        .
        = not achievable

        &nbsp;&nbsp;&nbsp;&nbsp;

        Closest:
        <span style="
            color:#fbbf24;
            font-weight:bold;
        ">
            {closest}
        </span>

        &nbsp;&nbsp;&nbsp;&nbsp;

        Δ =
        <span style="
            color:white;
            font-weight:bold;
        ">
            {abs(target-closest)} MW
        </span>

    </div>

    </div>
    """

    st.components.v1.html(
        html,
        height=550,
        scrolling=True
    )