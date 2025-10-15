from __future__ import annotations

from dash import Dash
from dash import html

from divine_simplicity.constants import APP_TITLE
from divine_simplicity.plotting import triangle_graph


def main() -> int:

    app = Dash()

    app.layout = [
        html.Div(
            className='shiny_wrapper',
            children=html.Div(
                className='userContent vr',
                children=[
                    APP_TITLE,
                    triangle_graph(),
                ],
            ),
        ),
    ]

    app.run(debug=True)

    return 0


if __name__ == '__main__':

    raise SystemExit(main())
