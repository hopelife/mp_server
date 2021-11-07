import flask
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html

## NOTE: https://community.plotly.com/t/dash-exceptions-nolayoutexception-the-layout-was-none-at-the-time-that-run-server/34798/3

server = flask.Flask(__name__)
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True


# App Layout

app.layout = html.Div([
    # header
    html.Div([
        html.Div(
            html.Img(src='logo',height="100%")
            ,style={"float":"right","width":"170px","height":"100px","margin-top":"-14px"})
        ],
        className="row header"
        ),

    # tabs
    html.Div([
        dcc.Tabs(
            id="tabs",
            style={"height":"60","verticalAlign":"middle"},
            children=[
                 dcc.Tab(label="Market", value="market_tab"),
                 dcc.Tab(label="Portfolio", value="portfolio_tab"),
                 dcc.Tab(label="Reporting", value="reporting_tab"),
            ],
            value="market_tab",
        )
        ],

        className="row tabs_div"
        ),
        # Tab content
        html.Div(id="tab_content", style={"margin": "2% 3%"})
])


@app.callback(Output("tab_content", "children"),
              [
                  Input("tabs", "value")
              ]
             )

def render_content(tab):
    """
    For user selections, return the relevant tab
    """
    if tab == "portfolio_tab":
        return portfolio.layout
    if tab == "reporting_tab":
        return reporting.layout
    elif tab == "market_tab":
        return market.layout
    else:
        return market.layout


if __name__ == '__main__':
    app.run_server(debug=True)

## NOTE: https://kibua20.tistory.com/216
# application = flask.Flask(__name__)
# dash_app1 = Dash(__name__, server = application, url_base_pathname='/dashapp1/')
# dash_app2 = Dash(__name__, server = application, url_base_pathname='/dashapp2/')
# dash_app3 = Dash(__name__, server = application, url_base_pathname='/dashapp3/')
# dash_app4 = Dash(__name__, server = application, url_base_pathname='/dashapp4/')
# dash_app5 = Dash(__name__, server = application, url_base_pathname='/dashapp5/')
 
# # flask app
# @application.route('/')
# def index():
#     print ('flask index()')
#     return 'index'
 
# # run the app.
# if __name__ == "__main__":
#     application.debug=True
#     application.run(host='127.0.0.1', port=6868)
#     # app.run(debug=True, host='127.0.0.1', port=6868)
