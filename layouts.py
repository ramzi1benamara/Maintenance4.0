import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import plotly.graph_objs as go
import appt
from datetime import datetime as dt

params = ['Cylinder_1_Cylinder_2', 'Cylinder_2_Cylinder_3',
          'Cylinder_3_Cylinder_4', 'Cylinder_4_Cylinder_1', 'Cylinder_1_Cylinder_3', 'Cylinder_2_Cylinder_4']
max_length = len(appt.available_indicators_Cushion_POS)

suffix_row = "_row"
suffix_button_id = "_button"
suffix_sparkline_graph = "_sparkline_graph"
suffix_count = "_count"
suffix_ooc_n = "_OOC_number"
suffix_ooc_g = "_OOC_graph"
suffix_indicator = "_indicator"
df1 = appt.df1
dftemperaturemax1 = appt.dftemperaturemax1
dftotaleffortsmax = appt.dftotaleffortsmax
dfpressure = appt.dfpressure
b = int(appt.P1_P2)
if b <= 20:
    a = "green"
elif b <= 30:
    a = "orange"
else:
    a = "red"
b1 = int(appt.P3_P2)
if b1 <= 20:
    a1 = "green"
elif b1 <= 30:
    a1 = "orange"
else:
    a1 = "red"
b2 = int(appt.P3_P1)
if b2 <= 20:
    a2 = "green"
elif b2 <= 30:
    a2 = "orange"
else:
    a2 = "red"
b3 = int(appt.P1_P4)
if b3 <= 20:
    a3 = "green"
elif b3 <= 30:
    a3 = "orange"
else:
    a3 = "red"

b4 = int(appt.P4_P2)
if b4 <= 20:
    a4 = "green"
elif b4 <= 30:
    a4 = "orange"
else:
    a4 = "red"

b5 = int(appt.P3_P4)
if b5 <= 20:
    a5 = "green"
elif b5 <= 30:
    a5 = "orange"
else:
    a5 = "red"

Pulse1 = appt.dfpulse1min
if Pulse1 < 67:
    PC1 = "red"
else:
    PC1 = "green"

Pulse2 = appt.dfpulse2min
if Pulse2 < 67:
    PC2 = "red"
else:
    PC2 = "green"

Pulse3 = appt.dfpulse3min
if Pulse3 < 67:
    PC3 = "red"
else:
    PC3 = "green"

Pulse4 = appt.dfpulse4min
if Pulse4 < 67:
    PC4 = "red"
else:
    PC4 = "green"

Pulse5 = appt.dfpulse5min
if Pulse5 < 67:
    PC5 = "red"
else:
    PC5 = "green"

PulseSlide = appt.dfpulseSlidemin
if PulseSlide < 64:
    PSlideC = "red"
else:
    PSlideC = "green"

PulseBalancing = appt.dfpulseCounterBalancingmin
if PulseBalancing < 64:
    PBalancingC = "red"


else:
    PBalancingC = "green"
layout_index = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('Monitoring Presse 50 Tanger'),
                                  html.Br(),
                                  html.H3('Gamme de production à suivre'),
                                  dcc.Dropdown(
                                      id='page-2-dropdown',
                                      options=[{'label': i, 'value': i} for i in appt.available_Production_Range],

                                  ),
                                  html.Div(id='page-2-dropdownOUT'),
                                  html.Div(id='dataframeout'),

                                  html.Div([
                                      dcc.Link('Navigate to "/Suivi des efforts de bielles"', href='/page-1'),
                                      html.Br(),
                                      dcc.Link('Navigate to "/Suivi des températures"', href='/page-2'),
                                      html.Br(),
                                      dcc.Link('Navigate to "/Suivi de pression d équilibrage "', href='/page-3'),
                                      html.Br(),
                                      dcc.Link('Navigate to "/Suivi désynchronisation des axes coussin"',
                                               href='/page-4a'),
                                      html.Br(),
                                      dcc.Link('Navigate to "/Suivi efforts coussin "', href='/page-4'),
                                      html.Br(),
                                      dcc.Link('Navigate to "/Suivi des impulsions de graissages "', href='/page-5'),
                                      html.Br(),
                                      dcc.Link('Navigate to "/Suivi des pressions de surcharge"', href='/page-6'),
                                  ]),
                                  html.Br(),
                                  html.Br(),
                                  html.Br(),


                                  dcc.Link('Compare to "/Rafales"', href='/page-7)'),
                                    html.Br(),
                                  dcc.Link('Compare to "/Gammes"', href='/page-8'),

                              ]
                              ),

                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.Div([
                                      html.Img(src='/assets/Image3.png',
                                               style={'height': '100%',
                                                      'width': '70%',
                                                      'text-align': 'center'
                                                      })
                                  ], style={'text-align': 'center'})
                              ]),

                 ])
    ]

)

layout1 = html.Div([
    html.H2('Monitoring Efforts'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'Gamme 33 tunnel J92 FK67 B52'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),

    dcc.Link('Go to App 2', href='/apps/app2'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),
    html.Br(),
    html.Br(),
    html.H3('Indicateurs Déséquilibre/Limite Machine'),
    html.Div(
        id='dark-theme-component-demo_tank1',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Tank(showCurrentValue=True, width=70, color=a, units="%", min=0, max=80,
                                  value=int(appt.P1_P2),
                                  label='Déséquilibre P1_P2 ',
                                  scale={'interval': 5, 'labelInterval': ((10)), 'custom': {'20': 'Alarm 20%'}})
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),
    html.Div(
        id='dark-theme-component-demo_tank2',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Tank(showCurrentValue=True, width=70, color=a1, units="%", min=0, max=80,
                                  value=int(appt.P3_P2),
                                  label='Déséquilibre P3_P2 ',
                                  scale={'interval': 5, 'labelInterval': ((10)), 'custom': {'20': 'Alarm 20%'}})
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),

    html.Div(
        id='dark-theme-component-demo_tank3',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Tank(showCurrentValue=True, width=70, color=a2, units="%", min=0, max=80,
                                  value=int(appt.P3_P1),
                                  label='Déséquilibre P3_P1 ',
                                  scale={'interval': 5, 'labelInterval': ((10)), 'custom': {'20': 'Alarm 20%'}})
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),
    html.Div(
        id='dark-theme-component-demo_tank4',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Gauge(showCurrentValue=True, units="TON",
                                   color={"gradient": True, "ranges": {"green": [0, 1800], "orange": [1800, 2100],
                                                                       "red": [2100, 2400]}},
                                   value=dftotaleffortsmax, label='Total Efforts -> Limite machine ', max=2400, min=0))
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),

    html.Div(
        id='dark-theme-component-demo_tank5',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Tank(showCurrentValue=True, width=70, color=a3, units="%", min=0, max=80,
                                  value=int(appt.P1_P4),
                                  label='Déséquilibre P1_P4 ',
                                  scale={'interval': 5, 'labelInterval': ((10)), 'custom': {'20': 'Alarm 20%'}})
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),
    html.Div(
        id='dark-theme-component-demo_tank6',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Tank(showCurrentValue=True, width=70, color=a4, units="%", min=0, max=80,
                                  value=int(appt.P4_P2),
                                  label='Déséquilibre P4_P2 ',
                                  scale={'interval': 5, 'labelInterval': ((10)), 'custom': {'20': 'Alarm 20%'}})
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),

    html.Div(
        id='dark-theme-component-demo_tank7',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Tank(showCurrentValue=True, width=70, color=a5, units="%", min=0, max=80,
                                  value=int(appt.P3_P4),
                                  label='Déséquilibre P3_P4 ',
                                  scale={'interval': 5, 'labelInterval': ((10)), 'custom': {'20': 'Alarm 20%'}})
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),

    html.Br(),
    html.Br(),
    html.H3('Suivi des Efforts de Bielles'),
    dcc.Graph(
        id='Monitoring Press Efforts',
        figure={

            'data': [

                dict(
                    x=df1[df1['variablename'] == i]['sourcetimestamp'],
                    y=df1[df1['variablename'] == i]['datavalue'],
                    text=df1[df1['variablename'] == i]['variablename'],
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size': 5,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in appt.available_indicators
            ],

            'layout': {'plot_bgcolor': '#1E1E1E', 'paper_bgcolor': '#1E1E1E', 'font': {
                'color': '#FFF'}}
        }
    ),

    html.Br(),

    html.H3('Graphe de Tendance Max efforts /cycle'),

    dcc.Graph(figure=appt.fig4),
    html.Br(),
    html.H3('Distribution des efforts bielles'),
    dcc.Graph(figure=appt.fig2),
    html.Div([

        dcc.Link('Navigate to "/"', href='/'),
    ])
])

layout2 = html.Div([
    html.H2('Monitoring Temperature'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'range - {}'.format(i), 'value': i} for i in [
                'Gamme 33 tunnel J92 FK67 B52'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1'),
    html.Br(),
    html.H3('Indicateurs Températures'),
    html.Br(),
    html.Div(
        id='dark-theme-component-dem_temp1',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Thermometer(
                    label='Temperature Main Shaft Front Left',
                    min=10,
                    max=100,
                    value=appt.dftemperaturemax1,
                    height=150,
                    width=5,
                    color='green',
                    showCurrentValue=True,
                    units="°C",
                    id='darktheme-daq-thermometer',
                    className='dark-theme-control'
                )
            )
        ],
        style={'width': '33%', 'display': 'inline-block'}
    ),
    html.Div(
        id='dark-theme-component-demo_temp2',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Thermometer(
                    label='Temperature Main Shaft Rear Right',
                    min=10,
                    max=100,
                    value=appt.dftemperaturemax2,
                    height=150,
                    width=5,
                    color='green',
                    showCurrentValue=True,
                    units="°C",
                    id='darktheme-daq-thermometer',
                    className='dark-theme-control'
                )
            )
        ],
        style={'width': '33%', 'display': 'inline-block'}
    ),
    html.Div(
        id='dark-theme-component-demo_temp3',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Thermometer(
                    label='Temperature Gear Front Right',
                    min=10,
                    max=100,
                    value=appt.dftemperaturemax3,
                    height=150,
                    width=5,
                    color='green',
                    showCurrentValue=True,

                    units="°C"
                )
            )
        ],
        style={'width': '33%', 'display': 'inline-block'}
    ),

    html.Br(),

    html.H3('Graphe de tendances Températures'),
    html.Br(),
    dcc.Graph(
        id='Monitoring-temperature',
        figure={'data': [
            dict(
                x=df1[df1['variablename'] == i]['sourcetimestamp'],
                y=df1[df1['variablename'] == i]['datavalue'].astype(int) / 10,

                text=df1[df1['variablename'] == i]['variablename'],
                mode='lines',
                opacity=0.7,
                marker={
                    'size': 5,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ) for i in appt.available_temperature
        ], 'layout': {'plot_bgcolor': '#1E1E1E', 'paper_bgcolor': '#1E1E1E', 'font': {
            'color': '#FFF'
        }}}
    ),
    html.Br(),

])

layout3 = html.Div([
    html.H2("Suivi Pression d'équilibrage"),

    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    html.H3("Actual Pressure"),
    dcc.Graph(
        id='Monitoring Pressure',
        figure={
            'data': [

                {'y': (dfpressure).astype(float), 'mode': 'lines',
                 'name': 'Actual Pressure'},

            ],
            'layout': {'plot_bgcolor': '#1E1E1E', 'paper_bgcolor': '#1E1E1E', 'font': {
                'color': '#FFF'
            }}
        }
    )
])


def generate_metric_row(id, style, col1, col2, col3, col4, col5, col6):
    if style is None:
        style = {"height": "8rem", "width": "100%"}

    return html.Div(
        id=id,
        className="row metric-row",
        style=style,
        children=[
            html.Div(
                id=col1["id"],
                className="one column",
                style={"margin-right": "2.5rem", "minWidth": "50px"},
                children=col1["children"],
            ),
            html.Div(
                id=col2["id"],
                style={"textAlign": "center"},
                className="one column",
                children=col2["children"],
            ),
            html.Div(
                id=col3["id"],
                style={"height": "100%"},
                className="four columns",
                children=col3["children"],
            ),
            html.Div(
                id=col4["id"],
                style={},
                className="one column",
                children=col4["children"],
            ),
            html.Div(
                id=col5["id"],
                style={"height": "100%", "margin-top": "5rem"},
                className="three columns",
                children=col5["children"],
            ),
            html.Div(
                id=col6["id"],
                style={"display": "flex", "justifyContent": "center"},
                className="one column",
                children=col6["children"],
            ),
        ],
    )


def generate_metric_list_header():
    return generate_metric_row(
        "metric_header",
        {"height": "3rem", "margin": "1rem 0", "textAlign": "center"},
        {"id": "m_header_1", "children": html.Div("Parameter")},
        {"id": "m_header_2", "children": html.Div("Count_Depassement")},
        {"id": "m_header_3", "children": html.Div("Diff en mm")},
        {"id": "m_header_4", "children": html.Div("Max_Value")},
        {"id": "m_header_5", "children": html.Div("%Limite diff (mm)")},
        {"id": "m_header_6", "children": "OK/NOK"},
    )


def generate_metric_row_helper(index):
    item = params[index]

    div_id = item + suffix_row
    button_id = item + suffix_button_id
    sparkline_graph_id = item + suffix_sparkline_graph
    count_id = item + suffix_count
    ooc_percentage_id = item + suffix_ooc_n
    ooc_graph_id = item + suffix_ooc_g
    indicator_id = item + suffix_indicator

    return generate_metric_row(
        div_id,
        None,
        {
            "id": item,
            "className": "metric-row-button-text",
            "children": html.Button(
                id=button_id,
                className="metric-row-button",
                children=item,

                n_clicks=0,
            ),
        },
        {"id": count_id, "children": 0},
        {
            "id": item + "_sparkline",
            "children": dcc.Graph(
                id=sparkline_graph_id,
                style={"width": "100%", "height": "95%"},
                config={
                    "staticPlot": False,
                    "editable": False,
                    "displayModeBar": False,
                },

                figure=go.Figure(
                    {
                        "data": [
                            {
                                'x': appt.dfposition_Cylinder_1_Cylinder_2['sourcetimestamp'],

                                'y': abs(appt.dfCoussinpos[item]),
                                "mode": "lines+markers",
                                "name": item,
                                "line": {"color": "#f4d44d"},
                            }
                        ],
                        "layout": {
                            "uirevision": True,
                            "margin": dict(l=0, r=0, t=4, b=4, pad=0),
                            "xaxis": dict(
                                showline=False,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=False,
                            ),
                            "yaxis": dict(
                                showline=False,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=False,
                            ),
                            "paper_bgcolor": "rgba(0,0,0,0)",
                            "plot_bgcolor": "rgba(0,0,0,0)",
                        },
                    }
                ),
            ),
        },
        {"id": ooc_percentage_id, "children": round(max(abs(appt.dfCoussinpos[item])), 2)},
        {
            "id": ooc_graph_id + "_container",
            "children": daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.GraduatedBar(
                    id=ooc_graph_id,
                    color={"gradient": True, "ranges": {"green": [0, 1.5], "orange": [1.5, 3],
                                                        "red": [3, 5]}},
                    showCurrentValue=True,
                    max=5,
                    value=round(max(abs(appt.dfCoussinpos[item])), 2),
                ), )
        },

        {
            "id": item + "_pf",
            "children": daq.Indicator(
                id=indicator_id, value=True, color="green", size=12
            ),
        },
    )


layout4a = html.Div([
    html.H2("Suivi Désynchronisation coussin"),

    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    html.H3("Position des vérins"),
    dcc.Graph(
        id='Monitoring-vérins-coussin',
        figure={'data': [
            dict(
                x=df1[df1['variablename'] == i]['sourcetimestamp'],
                y=df1[df1['variablename'] == i]['datavalue'].astype(float) / 1000,

                text=df1[df1['variablename'] == i]['variablename'],
                mode='lines',
                opacity=0.7,
                marker={
                    'size': 5,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ) for i in appt.available_indicators_Cushion_POS
        ], 'layout': {'plot_bgcolor': '#1E1E1E', 'paper_bgcolor': '#1E1E1E', 'font': {
            'color': '#FFF'
        }}}
    ),
    html.Br(),
    html.H3("Désynchronisation vérin 1,2"),
    dcc.Graph(id='Monitoring desynchro',
              figure={
                  'data': [
                      {'x': appt.dfposition_Cylinder_1_Cylinder_2['sourcetimestamp'],
                       'y': abs(appt.dfposition_Cylinder_1_Cylinder_2['diffpos']), 'mode': 'LINES',
                       'name': 'diffpos'},
                      {'x': appt.dfposition_Cylinder_1_Cylinder_2['sourcetimestamp'],
                       'y': appt.dfposition_Cylinder_1_Cylinder_2['datavalue_x'], 'mode': 'LINES',
                       'name': 'Position1'},
                      {'x': appt.dfposition_Cylinder_1_Cylinder_2['sourcetimestamp'],
                       'y': appt.dfposition_Cylinder_1_Cylinder_2['datavalue_y'], 'mode': 'LINES',
                       'name': 'Position2'},

                  ],
                  'layout': {'plot_bgcolor': '#1E1E1E', 'paper_bgcolor': '#1E1E1E', 'font': {
                      'color': '#FFF'
                  }}
              }),
    html.Div(
        id="top-section-container",
        className="row",
        children=[
            # Metrics summary
            html.Div(
                id="metric-summary-session",
                className="eight columns",
                children=[
                    html.H3("Cushion diff Position Summary"),
                    html.Div(
                        id="metric-div",
                        children=[
                            generate_metric_list_header(),
                            html.Div(
                                id="metric-rows",
                                children=[
                                    generate_metric_row_helper(0),
                                    generate_metric_row_helper(1),
                                    generate_metric_row_helper(2),
                                    generate_metric_row_helper(3),
                                    generate_metric_row_helper(4),
                                    generate_metric_row_helper(5),

                                ],
                            ),
                        ],
                    ),
                ],
            ),

        ],
    )
])

layout4 = html.Div([
    html.H2("Suivi Efforts coussin"),
    html.Div(
        id="control-chart-container",
        className="twelve columns",
        children=[
            html.H3("Distribution C3 coussin% consigne"),
            dcc.Graph(
                id="control-chart-live",
                figure=go.Figure(
                    {'data': [
                        {
                            "x": appt.dfConsigne3['sourcetimestamp'],
                            "y": (appt.dfConsigne3['datavalue'].astype(int)).div(1000),
                            "mode": "lines+markers",
                            "name": 'Cylinder_3_',
                        },
                        {

                            "y": (appt.dfConsigne3['datavalue'].astype(int)).div(1000),
                            "type": "histogram",
                            "orientation": "h",
                            "name": "Distribution",
                            "xaxis": "x2",
                            "yaxis": "y",
                            "marker": {"color": "#f4d44d"},
                        },
                        {
                            "x": appt.dfConsigne3['sourcetimestamp'],
                            "y": (appt.dfConsigne3['consigne3']),
                            "mode": "lines+markers",
                            "name": 'Consigne Cylinder_3_',
                            "marker": {"color": "#c90e0e"},
                        },

                    ], "layout": dict(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", xaxis=dict(
                        showline=False, showgrid=False, zeroline=False
                    ), yaxis=dict(
                        showgrid=False, showline=False, zeroline=False
                    ), autosize=True),

                    }
                ),
            ),
        ],
    ),
    html.Div(
        id="control-chart-container1",
        className="twelve columns",
        children=[
            html.H3("Distribution C4 coussin% consigne"),
            dcc.Graph(
                id="control-chart-live1",
                figure=go.Figure(
                    {
                        "data": [
                            {
                                "x": appt.dfConsigne4['sourcetimestamp'],
                                "y": (appt.dfConsigne4['datavalue'].astype(int)).div(1000),
                                "mode": "lines+markers",
                                "name": 'Cylinder_4_',
                            },
                            {

                                "y": (appt.dfConsigne4['datavalue'].astype(int)).div(1000),
                                "type": "histogram",
                                "orientation": "h",
                                "name": "Distribution",
                                "xaxis": "x2",
                                "yaxis": "y",
                                "marker": {"color": "#f4d44d"},
                            },
                            {
                                "x": appt.dfConsigne4['sourcetimestamp'],
                                "y": (appt.dfConsigne4['consigne4']),
                                "mode": "lines+markers",
                                "name": 'Consigne Cylinder_3_',
                                "marker": {"color": "#c90e0e"},
                            },

                        ],
                        "layout": {
                            "paper_bgcolor": "rgba(0,0,0,0)",
                            "plot_bgcolor": "rgba(0,0,0,0)",
                            "xaxis": dict(
                                showline=False, showgrid=False, zeroline=False
                            ),
                            "yaxis": dict(
                                showgrid=False, showline=False, zeroline=False
                            ),
                            "autosize": True,
                        },
                    }
                ),
            ),
        ],
    ),
    html.Div(
        id="control-chart-container2",
        className="twelve columns",
        children=[
            html.H3("Distribution C2 coussin% consigne"),
            dcc.Graph(
                id="control-chart-live2",
                figure=go.Figure(
                    {
                        "data": [
                            {
                                "x": appt.dfConsigne2['sourcetimestamp'],
                                "y": (appt.dfConsigne2['datavalue'].astype(
                                    int)).div(1000),
                                "mode": "lines+markers",
                                "name": 'Cylinder_2_',
                            },
                            {

                                "y": (appt.dfConsigne2['datavalue'].astype(int)).div(1000),
                                "type": "histogram",
                                "orientation": "h",
                                "name": "Distribution",
                                "xaxis": "x2",
                                "yaxis": "y",
                                "marker": {"color": "#f4d44d"},
                            },
                            {
                                "x": appt.dfConsigne2['sourcetimestamp'],
                                "y": (appt.dfConsigne2['consigne2']),
                                "mode": "lines+markers",
                                "name": 'Consigne Cylinder_3_',
                                "marker": {"color": "#c90e0e"},
                            },

                        ],
                        "layout": {
                            "paper_bgcolor": "rgba(0,0,0,0)",
                            "plot_bgcolor": "rgba(0,0,0,0)",
                            "xaxis": dict(
                                showline=False, showgrid=False, zeroline=False
                            ),
                            "yaxis": dict(
                                showgrid=False, showline=False, zeroline=False
                            ),
                            "autosize": True,
                        },
                    }
                ),
            ),
        ],
    ),
    html.Div(
        id="control-chart-container3",
        className="twelve columns",
        children=[
            html.H3("Distribution C1 coussin% consigne"),
            dcc.Graph(
                id="control-chart-live3",
                figure=go.Figure(
                    {
                        "data": [
                            {
                                "x": appt.dfConsigne1['sourcetimestamp'],
                                "y": (appt.dfConsigne1['datavalue'].astype(int)).div(1000),
                                "mode": "lines+markers",
                                "name": 'Cylinder_1_',
                            },
                            {

                                "y": (appt.dfConsigne1['datavalue'].astype(int)).div(1000),
                                "type": "histogram",
                                "orientation": "h",
                                "name": "Distribution",
                                "xaxis": "x2",
                                "yaxis": "y",
                                "marker": {"color": "#f4d44d"},
                            },
                            {
                                "x": appt.dfConsigne1['sourcetimestamp'],
                                "y": appt.dfConsigne1['consigne1'],
                                "mode": "lines+markers",
                                "name": 'Consigne Cylinder_3_',
                                "marker": {"color": "#c90e0e"},
                            },

                        ],
                        "layout": {
                            "paper_bgcolor": "rgba(0,0,0,0)",
                            "plot_bgcolor": "rgba(0,0,0,0)",
                            "xaxis": dict(
                                showline=False, showgrid=False, zeroline=False
                            ),
                            "yaxis": dict(
                                showgrid=False, showline=False, zeroline=False
                            ),
                            "autosize": True,
                        },
                    }
                ),
            ),
        ],
    ),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),

    dcc.Graph(figure=appt.fig5)
])
layout5 = html.Div([
    html.H2("Suivi Impulsions de graissage"),

    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    html.Div(
        id='dark-theme-component-demo_PULSE1',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Indicator(
                    label="Pulse 1",
                    color=PC1,
                    value=True
                )
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),
    html.Div(
        id='dark-theme-component-demo_PULSE2',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Indicator(
                    label="Pulse 2",
                    color=PC2,
                    value=True
                )
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),
    html.Div(
        id='dark-theme-component-demo_PULSE3',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Indicator(
                    label="Pulse 3",
                    color=PC3,
                    value=True
                )
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),
    html.Div(
        id='dark-theme-component-demo_PULSE4',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Indicator(
                    label="Pulse 4",
                    color=PC4,
                    value=True
                )
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(
        id='dark-theme-component-demo_PULSE5',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Indicator(
                    label="Pulse 5",
                    color=PC5,
                    value=True
                )
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),
    html.Div(
        id='dark-theme-component-demo_PULSESlide',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Indicator(
                    label="Pulse Slide",
                    color=PSlideC,
                    value=True
                )
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),

    html.Div(
        id='dark-theme-component-demo_PULSECOUNTERBALANCING',
        children=[
            daq.DarkThemeProvider(
                theme={'dark': True, 'detail': '#007439', 'primary': '#00EA64', 'secondary': '#6E6E6E'},
                children=daq.Indicator(
                    label="Pulse C.Balancing",
                    color=PBalancingC,
                    value=True
                )
            )
        ],
        style={'width': '25%', 'display': 'inline-block'}
    ),

    dcc.Graph(
        id='Monitoring Pulses',
        figure={
            'data': [

                {'x': appt.indicespulse1, 'y': [appt.time_seriespulse1[j] for j in appt.indicespulse1], 'mode': 'LINES',
                 'name': 'Peaks Pulse 1'},
                {'x': appt.indicespulse2, 'y': [appt.time_seriespulse2[k] for k in appt.indicespulse2], 'mode': 'LINES',
                 'name': 'Peaks Pulse 2'},
                {'x': appt.indicespulse3, 'y': [appt.time_seriespulse3[l] for l in appt.indicespulse3], 'mode': 'LINES',
                 'name': 'Peaks Pulse 3'},
                {'x': appt.indicespulse4, 'y': [appt.time_seriespulse4[m] for m in appt.indicespulse4], 'mode': 'LINES',
                 'name': 'Peaks Pulse 4'},
                {'x': appt.indicespulse5, 'y': [appt.time_seriespulse5[o] for o in appt.indicespulse5], 'mode': 'LINES',
                 'name': 'Peaks Pulse 5'},
                {'x': appt.indicespulseSlide, 'y': [appt.time_seriespulseSlide[p] for p in appt.indicespulseSlide],
                 'mode': 'LINES',
                 'name': 'Peaks Pulse Slide'},
                {'x': appt.indicespulseCounterBalancing,
                 'y': [appt.time_seriespulseCounterBalancing[q] for q in appt.indicespulseCounterBalancing],
                 'mode': 'LINES',
                 'name': 'Peaks Pulse CounterBalancing'},

            ],
            'layout': {'title': 'Actual Pulse', 'plot_bgcolor': '#1E1E1E', 'paper_bgcolor': '#1E1E1E', 'font': {
                'color': '#FFF'
            }}

        }
    ),

])
