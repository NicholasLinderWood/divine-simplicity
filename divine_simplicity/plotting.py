from __future__ import annotations

from dash import dcc
from plotly import graph_objects

from divine_simplicity.constants import EQUILATERAL_TRIANGLE
from divine_simplicity.geometry import centroid
from divine_simplicity.geometry import get_coordinates


def init_triangle_figure() -> graph_objects.Figure:

    x, y = get_coordinates(EQUILATERAL_TRIANGLE)
    (c_x,),  (c_y,) = get_coordinates(
        centroid(EQUILATERAL_TRIANGLE),
    )

    fig = graph_objects.Figure(
        data=[
            graph_objects.Scatter(
                x=x,
                y=y,
                mode='lines',
                line={
                    'color': 'black',
                    'width': 5,
                },
            ),
        ],
        layout=graph_objects.Layout(
            xaxis={
                'range': [c_x - 1, c_x + 1],
                'showticklabels': False,
                'fixedrange': True,
            },
            yaxis={
                'range': [c_y - 1, c_y + 1],
                'showticklabels': False,
                'fixedrange': True,
            },
        ),
    )
    fig.add_trace(
        graph_objects.Scatter(
            x=x[0:-1],
            y=y[0:-1],
            mode='markers',
            name='Points',
            marker={
                'color': 'black',
            },
            hoverinfo='none',
        ),
    )
    fig.update_layout(
        yaxis={
            'scaleanchor': 'x',
            'scaleratio': 1,
        },
        width=600,
        height=600,
        showlegend=False,
    )

    return fig


def triangle_graph() -> dcc.Graph:

    return dcc.Graph(
        id='triangle-graph',
        figure=init_triangle_figure(),
    )
