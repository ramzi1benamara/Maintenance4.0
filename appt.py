import dash
import pandas as pd

import plotly.express as px
import plotly.graph_objs as go
from scipy.signal import find_peaks

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets = ['https://codepen.io/anon/pen/mardKv.css']
theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df1 = pd.read_csv('testhive.csv', delimiter=',')
df1['sourcetimestamp'] = pd.to_datetime(df1['sourcetimestamp'], format="%Y-%m-%d %H:%M:%S.%f")
df1.sort_values(by=['sourcetimestamp'], inplace=True)
#df1out = df1[df1['sourcetimestamp'] >= "2020-02-26 21:26:08.750"]
#df1 = df1out[df1out['sourcetimestamp'] <= "2020-02-26 23:00:00.000"]
df1 = df1[df1['sourcetimestamp'] >= "2020-02-26 23:17:00.750"]
available_Production_Range = df1[df1['variablename'] == 'RangeNumber']['datavalue'].unique()

##FILTER SUR LES GAMMES FINAL
dfrangehoro = pd.DataFrame(columns=['rangenumber', 'horodaterangemin', 'horodaterangemax'])
drange = df1[df1['variablename'] == 'RangeNumber']
drangegroup = drange.groupby(['datavalue']).agg(['min', 'max'])
dfrangehoro['rangenumber'] = drangegroup.index
dfrangehoro['horodaterangemin'] = drangegroup['sourcetimestamp']['min'].values
dfrangehoro.sort_values(by=['horodaterangemin'], inplace=True)
dfrangehoro['horodaterangemax'] = dfrangehoro['horodaterangemin'].shift(-1)
# dfrangehoro['horodaterangemax'].iloc[-1]=df1['sourcetimestamp'].max()

horodatemin = dfrangehoro[dfrangehoro['rangenumber'] == '33']['horodaterangemin']
horodatemax = dfrangehoro[dfrangehoro['rangenumber'] == '33']['horodaterangemax']
# df1 = df1[df1['sourcetimestamp'] >= horodatemin.iloc[0]]
# df1 = df1[df1['sourcetimestamp'] <= horodatemax.iloc[0]]
# df1 = df1.reset_index(drop=True)
available_indicators = ['Point_1_ActFrontLeftForce', 'Point_2_ActRearLeftForce',
                        'Point_3_ActRearRightForce', 'Point_4_ActFrontRightForce']
##calcul de l'effort total % limite machine
dftotalefforts = df1[df1['variablename'] == 'TotalForce']['datavalue']
dftotaleffortsmax = (dftotalefforts.astype('int').max())
##detection des peaks sur les efforts
time_series1 = df1[df1['variablename'] == 'Point_1_ActFrontLeftForce']['datavalue'].to_numpy()
indices1 = find_peaks(time_series1, threshold=20)[0]
dfpeaks = pd.DataFrame(columns=['xindice', 'ytimeserie'])
dfpeaks['xindice'] = indices1
dfpeaks['ytimeserie'] = [time_series1[j] for j in indices1]
time_series2 = df1[df1['variablename'] == 'Point_2_ActRearLeftForce']['datavalue'].to_numpy()
indices2 = find_peaks(time_series2, threshold=20)[0]
dfpeaks2 = pd.DataFrame(columns=['xindice2', 'ytimeserie2'])
dfpeaks2['xindice2'] = indices2
dfpeaks2['ytimeserie2'] = [time_series2[j] for j in indices2]
time_series3 = df1[df1['variablename'] == 'Point_3_ActRearRightForce']['datavalue'].to_numpy()
indices3 = find_peaks(time_series3, threshold=20)[0]
dfpeaks3 = pd.DataFrame(columns=['xindice3', 'ytimeserie3'])
dfpeaks3['xindice3'] = indices3
dfpeaks3['ytimeserie3'] = [time_series3[j] for j in indices3]
time_series4 = df1[df1['variablename'] == 'Point_4_ActFrontRightForce']['datavalue'].to_numpy()
indices4 = find_peaks(time_series4, threshold=20)[0]
dfpeaks4 = pd.DataFrame(columns=['xindice4', 'ytimeserie4'])
dfpeaks4['xindice4'] = indices4
dfpeaks4['ytimeserie4'] = [time_series4[j] for j in indices4]
##déséquilibre des pieds de bielles
# P1_P2
P1 = df1[df1['variablename'] == 'Point_1_ActFrontLeftForce']['datavalue']
P1max = (P1.astype('int').max())
P2 = df1[df1['variablename'] == 'Point_2_ActRearLeftForce']['datavalue']
P2max = (P2.astype('int').max())
P3 = df1[df1['variablename'] == 'Point_3_ActRearRightForce']['datavalue']
P3max = (P3.astype('int').max())
P4 = df1[df1['variablename'] == 'Point_4_ActFrontRightForce']['datavalue']
P4max = (P4.astype('int').max())

P1_P2 = P1max - P2max
P1_P2 = P1_P2 / P1max
P1_P2 = abs(P1_P2 * 100)
# P2_P3
P3_P2 = P3max - P2max
P3_P2 = P3_P2 / P3max
P3_P2 = abs(P3_P2 * 100)
# P3_P1
P3_P1 = P3max - P1max
P3_P1 = P3_P1 / P3max
P3_P1 = abs(P3_P1 * 100)
# P1_P4
P1_P4 = P1max - P4max
P1_P4 = P1_P4 / P1max
P1_P4 = abs(P1_P4 * 100)
# P2_P4
P4_P2 = P4max - P2max
P4_P2 = P4_P2 / P4max
P4_P2 = abs(P4_P2 * 100)
# P3_P4
P3_P4 = P3max - P4max
P3_P4 = P3_P4 / P3max
P3_P4 = abs(P3_P4 * 100)
# calcul des temperatures
available_temperature = ['ActTemperatureMainShaftFrontLeft', 'ActTemperatureMainShaftRearRight',
                         'ActTemperatureGearFrontRight']
dftemperatureint1 = df1[df1['variablename'] == 'ActTemperatureMainShaftFrontLeft']['datavalue']
dftemperaturemax1 = (dftemperatureint1.astype('int').max())
dftemperaturemax1 = (dftemperaturemax1) / 10

dftemperatureint2 = df1[df1['variablename'] == 'ActTemperatureMainShaftRearRight']['datavalue']
dftemperaturemax2 = (dftemperatureint2.astype('int').max())
dftemperaturemax2 = (dftemperaturemax2) / 10

dftemperatureint3 = df1[df1['variablename'] == 'ActTemperatureGearFrontRight']['datavalue']
dftemperaturemax3 = (dftemperatureint3.astype('int').max())
dftemperaturemax3 = (dftemperaturemax3) / 10

##calcul des pressions dequilibrage
dfpressure = df1[df1['variablename'] == 'ActPressure']['datavalue']

##CALCUL DES IMPULSIONS DE GRAISSAGES
available_Pulse = ['Doser_1_ActCounter', 'Doser_2_ActCounter', 'Doser_3_ActCounter', 'Doser_4_ActCounter',
                   'Doser_5_ActCounter']
##detection des peaks sur les IMPUSLSIONS DE GRAISSAGES
time_seriespulse1 = df1[df1['variablename'] == 'Doser_1_ActCounter']['datavalue'].to_numpy()
indicespulse1 = find_peaks(time_seriespulse1)[0]
time_seriespulse2 = df1[df1['variablename'] == 'Doser_2_ActCounter']['datavalue'].to_numpy()
indicespulse2 = find_peaks(time_seriespulse2)[0]
time_seriespulse3 = df1[df1['variablename'] == 'Doser_3_ActCounter']['datavalue'].to_numpy()
indicespulse3 = find_peaks(time_seriespulse3)[0]
time_seriespulse4 = df1[df1['variablename'] == 'Doser_4_ActCounter']['datavalue'].to_numpy()
indicespulse4 = find_peaks(time_seriespulse4)[0]
time_seriespulse5 = df1[df1['variablename'] == 'Doser_5_ActCounter']['datavalue'].to_numpy()
indicespulse5 = find_peaks(time_seriespulse5)[0]
time_seriespulseSlide1 = (df1[df1['variablename'] == 'SlideActCounter']['datavalue'].astype(int)) / 10
time_seriespulseSlide = time_seriespulseSlide1.to_numpy()
indicespulseSlide = find_peaks(time_seriespulseSlide)[0]

time_seriespulseCounterBalancing = df1[df1['variablename'] == 'CounterBalancingActCounter']['datavalue'].to_numpy()
indicespulseCounterBalancing = find_peaks(time_seriespulseCounterBalancing)[0]
time_seriespulseCushionActCounter = df1[df1['variablename'] == 'CushionActCounter']['datavalue'].to_numpy()
indicespulseCushionActCounter = find_peaks(time_seriespulseCushionActCounter)[0]
dfpulse1min = int(min(([time_seriespulse1[j] for j in indicespulse1])))
dfpulse2min = int(min(([time_seriespulse2[j] for j in indicespulse2])))
dfpulse3min = int(min(([time_seriespulse3[j] for j in indicespulse3])))
dfpulse4min = int(min(([time_seriespulse4[j] for j in indicespulse4])))
dfpulse5min = int(min(([time_seriespulse5[j] for j in indicespulse5])))
dfpulseSlidemin = int(min(([time_seriespulseSlide[j] for j in indicespulseSlide])))
dfpulseCounterBalancingmin = int(min(([time_seriespulseCounterBalancing[j] for j in indicespulseCounterBalancing])))
# dfpulseCushionActCountermin = int(min(([time_seriespulseCushionActCounter[j] for j in indicespulseCushionActCounter])))
df2 = df1[df1.variablename.isin(available_indicators)]

fig2 = go.Figure()

for variablename in available_indicators:
    fig2.add_trace(go.Violin(x=df2['variablename'][df2['variablename'] == variablename],
                             y=df2['datavalue'][df2['variablename'] == variablename],
                             name=variablename,
                             box_visible=True,
                             meanline_visible=True))
fig2.update_traces(meanline_visible=True,
                   points='all',  # show all points
                   jitter=0.05,  # add some jitter on points for better visibility
                   scalemode='count')  # scale violin plot area with total count
fig2.update_layout(plot_bgcolor='#1E1E1E', paper_bgcolor='#1E1E1E', font={'color': '#FFF'})
fig4 = go.Figure()
fig4.add_trace(go.Scatter(
    y=time_series1,
    mode='lines+markers',
    name='Original Point_1_ActFrontLeftForce',
    visible='legendonly'
))

fig4.add_trace(go.Scatter(
    x=indices1,
    y=[time_series1[j] for j in indices1],
    mode='markers',
    marker=dict(
        size=8,
        color='red',
        symbol='cross'

    ),
    name='Detected Peaks Point_1_ActFrontLeftForce'
))
fig44 = px.scatter(dfpeaks, x=dfpeaks['xindice'].astype(float), y=dfpeaks['ytimeserie'].astype(float),
                   trendline='lowess')
trendline = fig44.data[1]
fig4.add_trace(trendline)

fig4.add_trace(go.Scatter(
    y=time_series2,
    mode='lines+markers',
    name='Original Point_2_ActRearLeftForce',
    visible='legendonly'
))

fig4.add_trace(go.Scatter(
    x=indices2,
    y=[time_series2[j] for j in indices2],
    mode='markers',
    marker=dict(
        size=8,
        color='green',
        symbol='cross'
    ),
    name='Detected Peaks Point_2_ActRearLeftForce'
))
fig45 = px.scatter(dfpeaks2, x=dfpeaks2['xindice2'].astype(float), y=dfpeaks2['ytimeserie2'].astype(float),
                   trendline='lowess')
trendline2 = fig45.data[1]
fig4.add_trace(trendline2)

fig4.add_trace(go.Scatter(
    y=time_series3,
    mode='lines+markers',
    name='Original Point_3_ActRearRightForce',
    visible='legendonly'
))

fig4.add_trace(go.Scatter(
    x=indices3,
    y=[time_series3[j] for j in indices3],
    mode='markers',
    marker=dict(
        size=8,
        color='blue',
        symbol='cross'
    ),
    name='Detected Peaks Point_3_ActRearRightForce'
))
fig46 = px.scatter(dfpeaks3, x=dfpeaks3['xindice3'].astype(float), y=dfpeaks3['ytimeserie3'].astype(float),
                   trendline='lowess')
trendline3 = fig46.data[1]
fig4.add_trace(trendline3)
fig4.add_trace(go.Scatter(
    y=time_series4,
    mode='lines+markers',
    name='Original Point_4_ActFrontRightForce',
    visible='legendonly'
))

fig4.add_trace(go.Scatter(
    x=indices4,
    y=[time_series4[j] for j in indices4],
    mode='markers',
    marker=dict(
        size=8,
        color='orange',
        symbol='cross'
    ),
    name='Detected Peaks Point_4_ActFrontRightForce'
))
fig47 = px.scatter(dfpeaks4, x=dfpeaks4['xindice4'].astype(float), y=dfpeaks4['ytimeserie4'].astype(float),
                   trendline='lowess')
trendline4 = fig47.data[1]
fig4.add_trace(trendline4)
fig4.update_layout(xaxis=dict(
                                showline=True,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=True,
                            ),
                            yaxis=dict(
                                showline=True,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=True,
                            ),

                   paper_bgcolor='#1E1E1E',
                   plot_bgcolor='#1E1E1E',
                   font={'color': '#FFF'}
                   )
available_indicators_Cushion = ['Cylinder_3_ActServoValveFrontLeftForce', 'Cylinder_4_ActServoValveRearLeftForce',
                                'Cylinder_2_ActServoValveRearRightForce', 'Cylinder_1_ActServoValveFrontRightForce']
available_indicators_Cushion_POS = ['Cylinder_3_ActCushionFrontLeftPosition', 'Cylinder_4_ActCushionRearLeftPosition',
                                    'Cylinder_2_ActCushionRearRightPosition', 'Cylinder_1_ActCushionFrontRightPosition']
available_indicators_Cushion_angle = ['Cylinder_3_ActServoValveFrontLeftForce', 'Cylinder_4_ActServoValveRearLeftForce',
                                      'Cylinder_2_ActServoValveRearRightForce',
                                      'Cylinder_1_ActServoValveFrontRightForce', 'ActAngularPressEncoder']
df3 = df1[df1.variablename.isin(available_indicators_Cushion)]
# df3['consigne']='100'
df4 = df1[df1.variablename.isin(available_indicators_Cushion_angle)]
dfConsigne = pd.DataFrame(
    columns=['sourcetimestamp', 'variablename', 'datavalue', 'consigne1', 'consigne2', 'consigne3', 'consigne4'])
dfConsigne['sourcetimestamp'] = df4['sourcetimestamp']
dfConsigne['variablename'] = df4['variablename']
dfConsigne['datavalue'] = df4['datavalue']
dfConsigne['consigne1'] = 100
dfConsigne['consigne2'] = 100
dfConsigne['consigne3'] = 100
dfConsigne['consigne4'] = 100
dfConsigne1 = dfConsigne[dfConsigne['variablename'] == 'Cylinder_1_ActServoValveFrontRightForce']
dfConsigne1 = dfConsigne1[(dfConsigne1['datavalue'].astype(float)) > 80000]
dfConsigne2 = dfConsigne[dfConsigne['variablename'] == 'Cylinder_2_ActServoValveRearRightForce']
dfConsigne2 = dfConsigne2[(dfConsigne2['datavalue'].astype(float)) > 80000]
dfConsigne3 = dfConsigne[dfConsigne['variablename'] == 'Cylinder_3_ActServoValveFrontLeftForce']
dfConsigne3 = dfConsigne3[(dfConsigne3['datavalue'].astype(float)) > 80000]
dfConsigne4 = dfConsigne[dfConsigne['variablename'] == 'Cylinder_4_ActServoValveRearLeftForce']
dfConsigne4 = dfConsigne4[(dfConsigne4['datavalue'].astype(float)) > 80000]

fig5 = go.Figure()

for variablename in available_indicators_Cushion:
    fig5.add_trace(go.Violin(x=df3['variablename'][df3['variablename'] == variablename],
                             y=(df3['datavalue'][(df3['datavalue'].astype(float)) > 80000][
                                 df3['variablename'] == variablename]).astype(
                                 int).div(1000),
                             name=variablename,
                             box_visible=True,
                             meanline_visible=True)),

fig5.update_traces(meanline_visible=True,
                   points='all',  # show all points
                   jitter=0.05,  # add some jitter on points for better visibility
                   scalemode='count')  # scale violin plot area with total count
fig5.update_layout(plot_bgcolor='#1E1E1E', paper_bgcolor='#1E1E1E', font={'color': '#FFF'})

dfposc2 = df1[df1['variablename'] == 'Cylinder_2_ActCushionRearRightPosition']

dfposc1 = df1[df1['variablename'] == 'Cylinder_1_ActCushionFrontRightPosition']
dfposc3 = df1[df1['variablename'] == 'Cylinder_3_ActCushionFrontLeftPosition']

dfposc4 = df1[df1['variablename'] == 'Cylinder_4_ActCushionRearLeftPosition']
params = ['Cylinder_1_Cylinder_2', 'Cylinder_2_Cylinder_3',
          'Cylinder_3_Cylinder_4', 'Cylinder_4_Cylinder_1', 'Cylinder_1_Cylinder_3', 'Cylinder_2_Cylinder_4']
dfposition_Cylinder_1_Cylinder_2 = pd.merge(dfposc2, dfposc1, how='left', on='sourcetimestamp')
dfposition_Cylinder_1_Cylinder_2[['datavalue_x', 'datavalue_y']] = dfposition_Cylinder_1_Cylinder_2[['datavalue_x', 'datavalue_y']].astype(float) / 1000
dfposition_Cylinder_1_Cylinder_2['diffpos'] = dfposition_Cylinder_1_Cylinder_2['datavalue_x'] - dfposition_Cylinder_1_Cylinder_2['datavalue_y']


dfposition_Cylinder_2_Cylinder_3 = pd.merge(dfposc2, dfposc3, how='left', on='sourcetimestamp')
dfposition_Cylinder_2_Cylinder_3[['datavalue_x', 'datavalue_y']] = dfposition_Cylinder_2_Cylinder_3[['datavalue_x', 'datavalue_y']].astype(float) / 1000
dfposition_Cylinder_2_Cylinder_3['diffpos'] = dfposition_Cylinder_2_Cylinder_3['datavalue_x'] - dfposition_Cylinder_2_Cylinder_3['datavalue_y']


dfposition_Cylinder_3_Cylinder_4 = pd.merge(dfposc3, dfposc4, how='left', on='sourcetimestamp')
dfposition_Cylinder_3_Cylinder_4[['datavalue_x', 'datavalue_y']] = dfposition_Cylinder_3_Cylinder_4[['datavalue_x', 'datavalue_y']].astype(float) / 1000
dfposition_Cylinder_3_Cylinder_4['diffpos'] = dfposition_Cylinder_3_Cylinder_4['datavalue_x'] - dfposition_Cylinder_3_Cylinder_4['datavalue_y']

dfposition_Cylinder_4_Cylinder_1 = pd.merge(dfposc4, dfposc1, how='left', on='sourcetimestamp')
dfposition_Cylinder_4_Cylinder_1[['datavalue_x', 'datavalue_y']] = dfposition_Cylinder_4_Cylinder_1[['datavalue_x', 'datavalue_y']].astype(float) / 1000
dfposition_Cylinder_4_Cylinder_1['diffpos'] = dfposition_Cylinder_4_Cylinder_1['datavalue_x'] - dfposition_Cylinder_4_Cylinder_1['datavalue_y']

dfposition_Cylinder_1_Cylinder_3 = pd.merge(dfposc1, dfposc3, how='left', on='sourcetimestamp')
dfposition_Cylinder_1_Cylinder_3[['datavalue_x', 'datavalue_y']] = dfposition_Cylinder_1_Cylinder_3[['datavalue_x', 'datavalue_y']].astype(float) / 1000
dfposition_Cylinder_1_Cylinder_3['diffpos'] = dfposition_Cylinder_1_Cylinder_3['datavalue_x'] - dfposition_Cylinder_1_Cylinder_3['datavalue_y']

dfposition_Cylinder_2_Cylinder_4 = pd.merge(dfposc2, dfposc4, how='left', on='sourcetimestamp')
dfposition_Cylinder_2_Cylinder_4[['datavalue_x', 'datavalue_y']] = dfposition_Cylinder_2_Cylinder_4[['datavalue_x', 'datavalue_y']].astype(float) / 1000
dfposition_Cylinder_2_Cylinder_4['diffpos'] = dfposition_Cylinder_2_Cylinder_4['datavalue_x'] - dfposition_Cylinder_2_Cylinder_4['datavalue_y']

dfCoussinpos = pd.DataFrame(
    columns=['Cylinder_1_Cylinder_2', 'Cylinder_2_Cylinder_3', 'Cylinder_3_Cylinder_4', 'Cylinder_4_Cylinder_1', 'Cylinder_1_Cylinder_3', 'Cylinder_2_Cylinder_4'])
dfCoussinpos['Cylinder_1_Cylinder_2']=dfposition_Cylinder_1_Cylinder_2['diffpos']
dfCoussinpos['Cylinder_2_Cylinder_3']=dfposition_Cylinder_2_Cylinder_3['diffpos']
dfCoussinpos['Cylinder_3_Cylinder_4']=dfposition_Cylinder_3_Cylinder_4['diffpos']
dfCoussinpos['Cylinder_4_Cylinder_1']=dfposition_Cylinder_4_Cylinder_1['diffpos']
dfCoussinpos['Cylinder_1_Cylinder_3']=dfposition_Cylinder_1_Cylinder_3['diffpos']
dfCoussinpos['Cylinder_2_Cylinder_4']=dfposition_Cylinder_2_Cylinder_4['diffpos']
server = app.server
app.config.suppress_callback_exceptions = True
