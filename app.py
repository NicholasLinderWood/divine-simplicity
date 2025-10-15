from __future__ import annotations

from dash import Dash
from dash import html

APP_TITLE = html.H1(
    html.Strong(
        className='hdg hdg_h1 mix-hdg_bold vr',
        children='Divine Simplicity',
    ),
)


def main() -> int:

    app = Dash()

    app.layout = [
        html.Div(
            className='shiny_wrapper',
            children=html.Div(
                className='userContent vr',
                children=[
                    APP_TITLE,
                ],
            ),
        ),
    ]

    app.run(debug=True)

    return 0


if __name__ == '__main__':

    raise SystemExit(main())
