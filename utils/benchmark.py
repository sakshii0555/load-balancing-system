import pandas as pd
import plotly.express as px


def generate_benchmark():

    sizes = [4, 6, 8, 10, 12, 14, 16, 18, 20]

    brute_ops = []
    dp_ops = []

    brute_time = []
    dp_time = []

    for n in sizes:

        brute = 2 ** n
        dp = n * 100

        brute_ops.append(brute)
        dp_ops.append(dp)

        brute_time.append(brute / 15000)
        dp_time.append(dp / 50000)

    df_time = pd.DataFrame({
        "Input Size": sizes,
        "Brute Force": brute_time,
        "Dynamic Programming": dp_time
    })

    df_ops = pd.DataFrame({
        "Input Size": sizes,
        "Brute Force": brute_ops,
        "Dynamic Programming": dp_ops
    })

    return df_time, df_ops


# ---------------------------------------------------
# EXECUTION TIME CHART
# ---------------------------------------------------

def create_time_chart(df):
    
    fig = px.line(
        df,
        x="Input Size",
        y=["Brute Force", "Dynamic Programming"],
        markers=True
    )

    # Brute Force = Cyan
    fig.data[0].line.color = "#2dd4bf"
    fig.data[0].marker.color = "#2dd4bf"
    fig.data[0].line.width = 4

    # DP = Gold
    fig.data[1].line.color = "#fbbf24"
    fig.data[1].marker.color = "#fbbf24"
    fig.data[1].line.width = 4

    fig.update_layout(
        paper_bgcolor="#070b1a",
        plot_bgcolor="#0b1020",
        font_color="white",
        height=350,

        margin=dict(l=20, r=20, t=20, b=20),

        legend=dict(
            orientation="h",
            y=-0.2,
            x=0.25,
            font=dict(color="white")
        ),

        xaxis=dict(
            title="Input Size (n)",
            gridcolor="rgba(251,191,36,0.08)",
            zeroline=False
        ),

        yaxis=dict(
            title="Execution Time (ms)",
            gridcolor="rgba(251,191,36,0.08)",
            zeroline=False
        )
    )

    return fig


# ---------------------------------------------------
# OPERATIONS CHART
# ---------------------------------------------------

def create_ops_chart(df):
    
    fig = px.line(
        df,
        x="Input Size",
        y=["Brute Force", "Dynamic Programming"],
        markers=True
    )

    # Brute Force = Cyan
    fig.data[0].line.color = "#2dd4bf"
    fig.data[0].marker.color = "#2dd4bf"
    fig.data[0].line.width = 4

    # DP = Gold
    fig.data[1].line.color = "#fbbf24"
    fig.data[1].marker.color = "#fbbf24"
    fig.data[1].line.width = 4

    fig.update_layout(
        paper_bgcolor="#070b1a",
        plot_bgcolor="#0b1020",
        font_color="white",
        height=350,

        margin=dict(l=20, r=20, t=20, b=20),

        legend=dict(
            orientation="h",
            y=-0.2,
            x=0.25,
            font=dict(color="white")
        ),

        xaxis=dict(
            title="Input Size (n)",
            gridcolor="rgba(251,191,36,0.08)",
            zeroline=False
        ),

        yaxis=dict(
            title="Operations",
            gridcolor="rgba(251,191,36,0.08)",
            zeroline=False
        )
    )

    return fig