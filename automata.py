import networkx as nx
import plotly.graph_objects as go


def build_automata(loads, max_depth=4):
    """
    Builds a subset-selection automata tree.
    States = partial sums
    Edges = take / skip decisions
    """

    loads = loads[:max_depth]

    G = nx.DiGraph()

    node_counter = 0

    def create_node(level, current_sum):
        nonlocal node_counter

        node = f"q{node_counter}"
        node_counter += 1

        G.add_node(
            node,
            level=level,
            sum=current_sum
        )

        return node

    root = create_node(0, 0)

    def dfs(parent, index, current_sum):

        if index >= len(loads):
            return

        load = loads[index]

        # skip transition
        skip_node = create_node(
            index + 1,
            current_sum
        )

        G.add_edge(
            parent,
            skip_node,
            label=f"skip {load}",
            action="skip"
        )

        dfs(
            skip_node,
            index + 1,
            current_sum
        )

        # take transition
        take_node = create_node(
            index + 1,
            current_sum + load
        )

        G.add_edge(
            parent,
            take_node,
            label=f"+{load}",
            action="take"
        )

        dfs(
            take_node,
            index + 1,
            current_sum + load
        )

    dfs(root, 0, 0)

    return G


def hierarchy_layout(G):
    
    pos = {}

    levels = {}

    for node, data in G.nodes(data=True):

        level = data["level"]

        if level not in levels:
            levels[level] = []

        levels[level].append(node)

    max_level = max(levels.keys())

    for level in levels:

        nodes = levels[level]

        total = len(nodes)

        for i, node in enumerate(nodes):

            x = level

            y = -(i - total / 2)

            pos[node] = (x, y)

    return pos


def graph_to_plotly(G):
    
    pos = hierarchy_layout(G)

    edge_x = []
    edge_y = []

    edge_label_x = []
    edge_label_y = []
    edge_texts = []

    for u, v, data in G.edges(data=True):

        x0, y0 = pos[u]
        x1, y1 = pos[v]

        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

        edge_label_x.append((x0 + x1) / 2)
        edge_label_y.append((y0 + y1) / 2)

        edge_texts.append(data["label"])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        line=dict(
            width=2,
            color="#facc15"
        ),
        hoverinfo="none"
    )

    edge_labels = go.Scatter(
    x=edge_label_x,
    y=edge_label_y,
    mode="markers",
    marker=dict(
        size=1,
        color="rgba(0,0,0,0)"
    ),
    text=edge_texts,
    hovertemplate="%{text}<extra></extra>"
)

    node_x = []
    node_y = []
    node_text = []
    hover_text = []

    for node, data in G.nodes(data=True):

        x, y = pos[node]

        node_x.append(x)
        node_y.append(y)

        node_text.append(node)

        hover_text.append(
            f"{node}<br>Σ = {data['sum']}"
        )

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=node_text,
        textposition="middle center",
        hovertext=hover_text,
        hoverinfo="text",
        marker=dict(
            size=42,
            color="#0f172a",
            line=dict(
                width=2,
                color="#374151"
            )
        ),
        textfont=dict(
            color="white",
            size=12
        )
    )

    fig = go.Figure(
        data=[
            edge_trace,
            edge_labels,
            node_trace
        ]
    )

    fig.update_layout(
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        font_color="white",
        height=700,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        showlegend=False,
        xaxis=dict(
            visible=False
        ),
        yaxis=dict(
            visible=False
        )
    )

    return fig


