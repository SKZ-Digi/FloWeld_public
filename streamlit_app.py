from matplotlib import markers
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# Config, damit der Inhalt die Seite füllt
st.set_page_config(layout="wide",page_title='SKZ Data Hub', page_icon='Gandalf_Icon2.PNG') #SKZ-Logo transparent 128x64.png
layout = go.Layout(
    margin=go.layout.Margin(
        l=0,  # left margin
        r=0,  # right margin
        b=0,  # bottom margin
        t=40,  # top margin
    )
)
st.markdown("""
        <style>
                
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
               .css-1d391kg {
                    padding-top: 0rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)


# Create plots
fig1 = go.Figure(layout=layout)
fig3 = go.Figure(layout=layout)


def measurment_plotter(option1, offset_group, offset_Force_time, offset_Waermestrom_time):

    # Obtain the timelines for the diagrams
    timeline_pressure_set = df_features.loc[df_features['META_ExperimentalPoint']
                                            == option1]['TIMESERIES_Kraft_rechts[N]'].values
    timeline_way_set = df_features.loc[df_features['META_ExperimentalPoint']
                                       == option1]['TIMESERIES_Weg_rechts[mm]'].values
    timeline_waermestrom_set = df_features.loc[df_features['META_ExperimentalPoint']
                                               == option1]['TIMESERIES_Waermestromsensor[µV]'].values
    timeline_time_set = df_features.loc[df_features['META_ExperimentalPoint']
                                        == option1]['TIMESERIES_Timestamp[s]'].values

    # Obtain the Features for the plots
    t_angl = df_features.loc[df_features['META_ExperimentalPoint']
                             == option1]['FEAT_t_angl[s]'].values
    t_anw = df_features.loc[df_features['META_ExperimentalPoint']
                            == option1]['FEAT_t_anw[s]'].values
    delta_t_angl = df_features.loc[df_features['META_ExperimentalPoint']
                                   == option1]['FEAT_Delta_t_angl[s]'].values
    delta_t_anw = df_features.loc[df_features['META_ExperimentalPoint']
                                  == option1]['FEAT_Delta_t_anw[s]'].values

    # Obtain the Features for the plots, see Feature Design for definiton
    delta_t_angl_x = df_features.loc[df_features['META_ExperimentalPoint']
                                     == option1]['FEAT_Delta_t_angl[s]'].values
    t_angl_x = df_features.loc[df_features['META_ExperimentalPoint']
                               == option1]['FEAT_t_angl[s]'].values+delta_t_angl_x
    delta_t_anw_x = df_features.loc[df_features['META_ExperimentalPoint']
                                    == option1]['FEAT_Delta_t_anw[s]'].values+t_angl_x
    t_anw_x = df_features.loc[df_features['META_ExperimentalPoint']
                              == option1]['FEAT_t_anw[s]'].values+delta_t_anw_x

    F_angl_y = df_features.loc[df_features['META_ExperimentalPoint']
                               == option1]['FEAT_F_angl[N]'].values
    F_anw_y = df_features.loc[df_features['META_ExperimentalPoint']
                              == option1]['FEAT_F_anw[N]'].values

    WS_S0_y = df_features.loc[df_features['META_ExperimentalPoint']
                              == option1]['FEAT_WS0[µV]'].values

    WS_max_y = df_features.loc[df_features['META_ExperimentalPoint']
                               == option1]['FEAT_WS_max[µV]'].values
    WS_max_x = []
    i = 0
    for element in WS_max_y:
        WS_max_index = np.where(timeline_waermestrom_set[i] == element)
        WS_max_x.append(timeline_time_set[i][WS_max_index])
        i = i+1

    WS_angl_y = df_features.loc[df_features['META_ExperimentalPoint']
                                == option1]['FEAT_WS_angl[µV]'].values
    WS_angl_x = t_angl+delta_t_angl
    WS_anw_y = df_features.loc[df_features['META_ExperimentalPoint']
                               == option1]['FEAT_WS_anw[µV]'].values
    WS_anw_x = t_angl+t_anw+delta_t_angl+delta_t_anw

    # df_features.iloc[:, 0]
    ID_list = df_features.loc[df_features['META_ExperimentalPoint']
                              == option1].index
    #ID_list=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['META_ID'].values

    delta_t_angl_off_y = []
    t_angl_off_y = []
    delta_t_anw_off_y = []
    t_anw_off_y = []
    F_angl_off_y = []
    F_anw_off_y = []
    WS_0_off_x = []
    WS_0_off_y = []
    WS_angl_off_y = []
    WS_anw_off_y = []
    WS_max_off_y = []

    # Farben, welche für die Plots verwendet werden
    colorlist = []
    if offset_group == 0:
        colorlist_force = ['rgb(245,245,220)', 'rgb(255,228,220)', 'rgb(245,245,196)', 'rgb(255,235,205)', 'rgb(245,222,179)',
                           'rgb(255,248,220)', 'rgb(255,250,205)', 'rgb(250,250,210)', 'rgb(255,255,224)']
        colorlist_time = ['rgb(128,0,128)', 'rgb(186,85,211)', 'rgb(153,50,204)', 'rgb(148,0,211)', 'rgb(139,0,139)',
                          'rgb(216,191,216)', 'rgb(221,160,221)', 'rgb(238,130,238)', 'rgb(255,0,255)']
    else:
        colorlist_force = ['rgb(139,69,19)', 'rgb(160,82,45)', 'rgb(210,105,30)', 'rgb(205,133,63)', 'rgb(244,164,96)',
                           'rgb(222,184,135)', 'rgb(210,180,140)', 'rgb(188,143,143)', 'rgb(210,184,135)']
        colorlist_time = ['rgb(0,206,209)', 'rgb(64,224,208)', 'rgb(72,209,204)', 'rgb(175,238,238)', 'rgb(127,255,212)',
                          'rgb(176,224,230)', 'rgb(95,158,160)', 'rgb(0,255,255)', 'rgb(0,139,139)']
    i = 0
    for element in timeline_pressure_set:

        if offset_group == 0:
            base1 = 255
            base2 = 0
            base3 = 0
            colorlist.append('rgb('+str(base1-i*13)+',' +
                             str(base2+i*20)+','+str(base3+i*40)+')')

            i = i+1
        else:
            base1 = 0
            base2 = 0
            base3 = 255
            colorlist.append('rgb('+str(base1+i*25)+',' +
                             str(base2+i*20)+','+str(base3-i*30)+')')

            i = i+1

    # draw each plot and Feature
    i = 0
    for element in timeline_pressure_set:
        delta_t_angl_off_y.append(1)
        t_angl_off_y.append(1)
        delta_t_anw_off_y.append(1)
        t_anw_off_y.append(1)
        # F_angl_off_y.append(F_angl_y[i]+i*offset_Force_time+offset_group,F_angl_y[i]+i*offset_Force_time+offset_group)
        # F_anw_off_y.append(F_anw_y[i]+i*offset_Force_time+offset_group,F_anw_y[i]+i*offset_Force_time+offset_group)
        WS_0_off_x.append(0)
        WS_0_off_y.append(WS_S0_y[i]+i*offset_Waermestrom_time+15*offset_group)
        WS_angl_off_y.append(
            WS_angl_y[i]+i*offset_Waermestrom_time+15*offset_group)
        WS_anw_off_y.append(
            WS_anw_y[i]+i*offset_Waermestrom_time+15*offset_group)
        WS_max_off_y.append(
            WS_max_y[i]+i*offset_Waermestrom_time+15*offset_group)

        # Plot Force-Time
        fig1.add_trace(go.Scatter(x=timeline_time_set[i], y=np.array(element)+i*offset_Force_time+offset_group,
                                  mode='lines',
                                  name=ID_list[i],
                                  line=dict(color=colorlist[i])))
        if Time_all == True:
            fig1.add_trace(go.Scatter(x=[delta_t_angl_x[i], delta_t_angl_x[i]], y=[delta_t_angl_off_y[i], 250],
                                      mode='lines',
                                      name='\u0394t<sub>angl</sub>',
                                      showlegend=False,
                                      line=dict(color=colorlist_time[i])
                                      ))

            fig1.add_trace(go.Scatter(x=[t_angl_x[i], t_angl_x[i]], y=[t_angl_off_y[i], 250],
                                      mode='lines',
                                      name='t<sub>angl</sub>',
                                      showlegend=False,
                                      line=dict(color=colorlist_time[i])
                                      ))

            fig1.add_trace(go.Scatter(x=[delta_t_anw_x[i], delta_t_anw_x[i]], y=[delta_t_anw_off_y[i], 250],
                                      mode='lines',
                                      name='\u0394t<sub>anw</sub>',
                                      showlegend=False,
                                      line=dict(color=colorlist_time[i])
                                      ))

            fig1.add_trace(go.Scatter(x=[t_anw_x[i], t_anw_x[i]], y=[t_anw_off_y[i], 250],
                                      mode='lines',

                                      name='t<sub>anw</sub>',
                                      showlegend=False,
                                      line=dict(color=colorlist_time[i])
                                      ))

        # Plot WS-Time
        # Depending on the checkboxes

        fig3.add_trace(go.Scatter(x=timeline_time_set[i], y=np.array(timeline_waermestrom_set[i])+i*offset_Waermestrom_time+15*offset_group,
                                  mode='lines',
                                  name=ID_list[i],
                                  line=dict(color=colorlist[i])))
        if WS_all == True:
            fig3.add_trace(go.Scatter(x=[WS_max_x[i]], y=[WS_max_off_y[i]],
                                      mode='markers',
                                      marker_symbol='x',
                                      marker=dict(color=colorlist_time[i]),
                                      showlegend=False,
                                      name='WS<sub>max</sub>'
                                      ))

            fig3.add_trace(go.Scatter(x=[WS_0_off_x[i]], y=[WS_0_off_y[i]],
                                      mode='markers',
                                      marker_symbol='x',
                                      marker=dict(color=colorlist_time[i]),
                                      showlegend=False,
                                      name='WS<sub>0</sub>'
                                      ))

            fig3.add_trace(go.Scatter(x=[WS_angl_x[i]], y=[WS_angl_off_y[i]],
                                      mode='markers',
                                      marker_symbol='x',
                                      marker=dict(color=colorlist_force[i]),
                                      showlegend=False,
                                      name='WS<sub>angl</sub>'
                                      ))

            fig3.add_trace(go.Scatter(x=[WS_anw_x[i]], y=[WS_anw_off_y[i]],
                                      mode='markers',
                                      marker_symbol='x',
                                      marker=dict(color=colorlist_force[i]),
                                      showlegend=False,
                                      name='WS<sub>anw</sub>'
                                      ))
        i = i+1

    # Draw the last elements again and add annotations, so we only have 1 annotation per element
    i = i-1
    fig1.add_trace(go.Scatter(x=timeline_time_set[i], y=np.array(element)+i*offset_Force_time+offset_group,
                              mode='lines',
                              name=ID_list[i],
                              line=dict(color=colorlist[i])))
    if Time_all == True:
        fig1.add_trace(go.Scatter(x=[delta_t_angl_x[i], delta_t_angl_x[i]], y=[delta_t_angl_off_y[i], 250],
                                  mode='lines+text',
                                  name='\u0394t<sub>angl</sub>',
                                  showlegend=False,
                                  text=["", "\u0394t<sub>angl</sub>"],
                                  textposition="top center",
                                  line=dict(color=colorlist_time[i])
                                  ))

        fig1.add_trace(go.Scatter(x=[t_angl_x[i], t_angl_x[i]], y=[t_angl_off_y[i], 250],
                                  mode='lines+text',
                                  name='t<sub>angl</sub>',
                                  showlegend=False,
                                  text=["", "t<sub>angl</sub>"],
                                  textposition="top center",
                                  line=dict(color=colorlist_time[i])
                                  ))

        fig1.add_trace(go.Scatter(x=[delta_t_anw_x[i], delta_t_anw_x[i]], y=[delta_t_anw_off_y[i], 250],
                                  mode='lines+text',
                                  name='\u0394t<sub>anw</sub>',
                                  showlegend=False,
                                  text=["", "\u0394t<sub>anw</sub>"],
                                  textposition="top center",
                                  line=dict(color=colorlist_time[i])
                                  ))

        fig1.add_trace(go.Scatter(x=[t_anw_x[i], t_anw_x[i]], y=[t_anw_off_y[i], 250],
                                  mode='lines+text',

                                  name='t<sub>anw</sub>',
                                  showlegend=False,
                                  text=["", "t<sub>anw</sub>"],
                                  textposition="top center",
                                  line=dict(color=colorlist_time[i])
                                  ))
    if (Force_all == True) and (offset_group == 0):
        fig1.add_annotation(x=(delta_t_angl_x[i]+t_angl_x[i])/2, y=F_angl_y[i]+i*offset_Force_time+offset_group,
                            # mode='markers+text',
                            # marker_symbol='x',
                            # showlegend=False,
                            # name='F<sub>angl</sub>',
                            showarrow=False,
                            text="F<sub>angl</sub>",
                            yshift=10
                            #textposition="top center",
                            # line=dict(color=colorlist_force[i])
                            )

        fig1.add_annotation(x=(delta_t_anw_x[i]+t_anw_x[i])/2, y=F_anw_y[i]+i*offset_Force_time+offset_group,
                            # mode='lines+text',
                            # marker_symbol='x',
                            # showlegend=False,
                            # name='F<sub>anw</sub>',
                            text="F<sub>anw</sub>",
                            showarrow=False,
                            yshift=10
                            #textposition="top center",
                            # line=dict(color=colorlist_force[i])
                            )

        # Plot WS-Time
        # Depending on the checkboxes

    fig3.add_trace(go.Scatter(x=timeline_time_set[i], y=np.array(timeline_waermestrom_set[i])+i*offset_Waermestrom_time+15*offset_group,
                              mode='lines',
                              name=ID_list[i],
                              line=dict(color=colorlist[i])))
    if (WS_all == True) and (offset_group == 0):
        fig3.add_trace(go.Scatter(x=[WS_max_x[i]], y=[WS_max_off_y[i]],
                                  mode='markers+text',
                                  marker_symbol='x',
                                  marker=dict(color=colorlist_time[i]),
                                  showlegend=False,
                                  text=["WS<sub>0</sub>"],
                                  textposition="top center",
                                  name='WS<sub>max</sub>'
                                  ))
        fig3.add_trace(go.Scatter(x=[WS_0_off_x[i]], y=[WS_0_off_y[i]],
                                  mode='markers+text',
                                  marker_symbol='x',
                                  marker=dict(color=colorlist_time[i]),
                                  showlegend=False,
                                  text=["WS<sub>0</sub>"],
                                  textposition="top center",
                                  name='WS<sub>0</sub>'
                                  ))

        fig3.add_trace(go.Scatter(x=[WS_angl_x[i]], y=[WS_angl_off_y[i]],
                                  mode='markers+text',
                                  marker_symbol='x',
                                  marker=dict(color=colorlist_force[i]),
                                  showlegend=False,
                                  text=["WS<sub>angl</sub>"],
                                  textposition="top center",
                                  name='WS<sub>angl</sub>'
                                  ))

        fig3.add_trace(go.Scatter(x=[WS_anw_x[i]], y=[WS_anw_off_y[i]],
                                  mode='markers+text',
                                  marker_symbol='x',
                                  marker=dict(color=colorlist_force[i]),
                                  showlegend=False,
                                  text=["WS<sub>anw</sub>"],
                                  textposition="top center",
                                  name='WS<sub>anw</sub>'
                                  ))
    # Set axis
    fig1.update_xaxes(range=[0, timeline_time_set[0][-1]*1.1])
    fig3.update_xaxes(range=[0, timeline_time_set[0][-1]*1.1])


# # Top element of the Page
# sb1, sb3 = st.sidebar.columns((2, 2))
# sb1.image("SKZ-LogoSlogan_Int_4C.jpg")   #SKZ-Logo.jpg
# sb3.image("bmwi_de_2021.png")
# st.sidebar.write(
#     "[Download data and description here](https://b2share.eudat.eu/records/657bb2383ce946dcb4cab9419e1645d3)")
# option0 = st.sidebar.selectbox(
#     'Select page',
#     ['Plot Experiments', 'Overview'])
# st.sidebar.markdown('***')

# Top element of the Page

st.sidebar.image("SKZ-LogoSlogan_Int_web.png")  # SKZ-Logo.jpg

st.sidebar.write(
    "[Download data and description here](https://b2share.eudat.eu/records/657bb2383ce946dcb4cab9419e1645d3)")
option0 = st.sidebar.selectbox(
    'Select page',
    ['Plot Experiments', 'Overview'])
st.sidebar.markdown('***')


# Page 1
if option0 == 'Plot Experiments':
    # Header
    st.title('FloWeld-Project Data')

    # Loading the dataframe
    df_features = pd.read_parquet('data_processed')
    # df_features.to_excel("data_processed.xlsx")
    # df_features.to_excel('data_processed.xlsx')

    # Obtain a list of all measurement variations
    df_experimental_points = df_features['META_ExperimentalPoint'].values
    # Remove duplicates
    list_experimental_points = list(dict.fromkeys(df_experimental_points))
    list_experimental_points_2 = list(dict.fromkeys(df_experimental_points))
    list_experimental_points_2.insert(0, '-')
    # Ask which to display
    option_measurment = st.sidebar.selectbox(
        'Choose the experimental point',
        list_experimental_points)

    # Compare function
    option_compare = st.sidebar.selectbox(
        'Compare with different experimental point?',
        list_experimental_points_2)
    if option_compare != '-':
        # st.sidebar.slider('Offset between experimental points', min_value=1,max_value= 200, value=40)
        offset_group_slider = 80

    st.sidebar.markdown('***')

    # st.sidebar.slider('offset_Force_time', max_value= 120, value=20)
    offset_Force_time = 20

    # st.sidebar.slider('offset_Waermestrom_time', max_value= 3000, value=300)
    offset_Waermestrom_time = 300

    # Show Features
    WS_all = st.sidebar.checkbox('show all Features')
    if WS_all == True:
        Time_all = True
        Force_all = True
    else:
        Time_all = False
        Force_all = False

    # Plot the data by using the function above
    measurment_plotter(option_measurment, 0,
                       offset_Force_time, offset_Waermestrom_time)
    if option_compare != '-':
        measurment_plotter(option_compare, offset_group_slider,
                           offset_Force_time, offset_Waermestrom_time)

    # Display data
    expander_table = st.expander(label="View data")
    expander_table.write(option_measurment)
    expander_table.dataframe(
        df_features.loc[df_features['META_ExperimentalPoint'] == option_measurment])
    if option_compare != '-':
        expander_table.write(option_compare)
        expander_table.dataframe(
            df_features.loc[df_features['META_ExperimentalPoint'] == option_compare])

    st.write("#")   # Empty space
    
    # Display plots
    col1, col3 = st.columns((2, 2))

    fig1.update_layout(
        title=dict(text="Force over time", 
                    font=dict(size=25)),
        xaxis_title="Time in [s]",
        yaxis_title="Force in [N]",)
    fig3.update_layout(
        title=dict(text="Heatflux over time", 
                    font=dict(size=25)),
        xaxis_title="Time in [s]",
        yaxis_title="Voltage signal of the Heatflux sensor in [µV]",)

    col1.plotly_chart(fig1, use_container_width=True)

    col3.plotly_chart(fig3, use_container_width=True)


# Page 2
elif option0 == 'Overview':
    st.title('Overview')
    df_features = pd.read_parquet('data_processed')

    list_experimental_points = []
    list_experimental_points.insert(0, 'PVC-U')
    list_experimental_points.insert(0, 'PP-H')
    checkbox_list = []
    all_PP = st.sidebar.checkbox('PP-H', True)
    all_PVC = st.sidebar.checkbox('PVC-U', True)

    # Select the data
    if all_PP == True:
        selected_data = df_features.loc[df_features['FEAT_Material_PP'] == 1]
        fig1.add_trace(go.Scatter(x=selected_data['META_ExperimentalPoint'].values, y=selected_data['LABEL_weld_factor'].values,
                                  mode='markers',
                                  marker=dict(color='firebrick'),
                                  name='PP-H',
                                  marker_symbol='x',))

    if all_PVC == True:
        selected_data = df_features.loc[df_features['FEAT_Material_PVC'] == 1]
        fig1.add_trace(go.Scatter(x=selected_data['META_ExperimentalPoint'].values, y=selected_data['LABEL_weld_factor'].values,
                                  mode='markers',
                                  marker=dict(color='slateblue'),
                                  name='PVC-U',
                                  marker_symbol='x',))

    # Show data
    st.markdown("**Data Description:**  \n The dataset was acquired during the research project FloWeld, which researches the usage of heatflux sensors in the process of plastics-welding. It consists of 68 weldings with the material PP-H (Polypropylen Homopolymer) and 69 weldings of PVC-U (Polyvinylchlorid unplasticized). The dataset contains timeseries data recorded during the welding process itself as well as features extracted from those timeseries based on domain knowledge. The duration and the temperature of the weldings was varied on purpose throughout the experiment, therefore weldings with different flexural strengths were created with five weldings per experimental point.")
    st.markdown("The Weld Factor is defined as: ")
    st.latex(r'''Weld~Factor = \frac{Flexural~strength~of~welding}{Flexural~strength~of~raw~material}''')
    st.write("#")   # Empty space
    st.write("#")
    
    fig1.update_layout(
        #title="Weld Factor for different experimental points",
        title=dict(text="Weld Factor for different experimental points", 
                    font=dict(size=25)),
        xaxis_title="Experimental Point",
        yaxis_title="Weld Factor",)

    st.plotly_chart(fig1, use_container_width=True)
    

st.sidebar.image("bmwi_de_2021.png", width=200)
