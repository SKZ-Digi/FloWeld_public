from matplotlib import markers
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(layout="wide")
layout = go.Layout(
  margin=go.layout.Margin(
        l=0, #left margin
        r=0, #right margin
        b=0, #bottom margin
        t=40, #top margin
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


#Create plots
fig1 = go.Figure(layout=layout)
fig3 = go.Figure(layout=layout)




def measurment_plotter(option1, offset_group, offset_Force_time, offset_Waermestrom_time):

#Obtain the timelines for the diagrams
    timeline_pressure_set=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['TIMESERIES_Kraft_rechts[N]'].values
    timeline_way_set=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['TIMESERIES_Weg_rechts[mm]'].values
    timeline_waermestrom_set=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['TIMESERIES_Waermestromsensor[µV]'].values
    timeline_time_set=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['TIMESERIES_Timestamp[s]'].values

    #Obtain the Features for the plots
    t_angl=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_t_angl[s]'].values
    t_anw=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_t_anw[s]'].values
    delta_t_angl=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_Delta_t_angl[s]'].values
    delta_t_anw=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_Delta_t_anw[s]'].values

    #Obtain the Features for the plots, see Feature Design for definiton
    delta_t_angl_x=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_Delta_t_angl[s]'].values
    t_angl_x=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_t_angl[s]'].values+delta_t_angl_x
    delta_t_anw_x=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_Delta_t_anw[s]'].values+t_angl_x
    t_anw_x=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_t_anw[s]'].values+delta_t_anw_x

    F_angl_y=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_F_angl[N]'].values
    F_anw_y=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_F_anw[N]'].values

    WS_S0_y=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_WS0[µV]'].values

    WS_max_y=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_WS_max[µV]'].values
    WS_max_x=[]
    i=0
    for element in WS_max_y:
        WS_max_index = np.where(timeline_waermestrom_set[i]==element)
        WS_max_x.append(timeline_time_set[i][WS_max_index])
        i=i+1


    WS_angl_y=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_WS_angl[µV]'].values
    WS_angl_x=t_angl+delta_t_angl
    WS_anw_y=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_WS_anw[µV]'].values
    WS_anw_x=t_angl+t_anw+delta_t_angl+delta_t_anw

    ID_list=df_features.loc[df_features['META_ExperimentalPoint'] == option1].index #df_features.iloc[:, 0]
    #ID_list=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['META_ID'].values

    delta_t_angl_off_y=[]
    t_angl_off_y=[]
    delta_t_anw_off_y=[]
    t_anw_off_y=[]
    F_angl_off_y=[]
    F_anw_off_y=[]
    WS_0_off_x=[]
    WS_0_off_y=[]
    WS_angl_off_y=[]
    WS_anw_off_y=[]
    WS_max_off_y=[]

    colorlist = []
    if offset_group==0:
        colorlist_force=['rgb(245,245,220)','rgb(255,228,220)','rgb(245,245,196)','rgb(255,235,205)','rgb(245,222,179)',
                        'rgb(255,248,220)','rgb(255,250,205)','rgb(250,250,210)','rgb(255,255,224)']
        colorlist_time=['rgb(128,0,128)','rgb(186,85,211)','rgb(153,50,204)','rgb(148,0,211)','rgb(139,0,139)',
                        'rgb(216,191,216)','rgb(221,160,221)','rgb(238,130,238)','rgb(255,0,255)']
    else:
        colorlist_force=['rgb(139,69,19)','rgb(160,82,45)','rgb(210,105,30)','rgb(205,133,63)','rgb(244,164,96)',
                        'rgb(222,184,135)','rgb(210,180,140)','rgb(188,143,143)','rgb(210,184,135)']
        colorlist_time=['rgb(0,206,209)','rgb(64,224,208)','rgb(72,209,204)','rgb(175,238,238)','rgb(127,255,212)',
                        'rgb(176,224,230)','rgb(95,158,160)','rgb(0,255,255)','rgb(0,139,139)']
    i=0
    for element in timeline_pressure_set:
        
        if offset_group==0:
            base1=255
            base2=0
            base3=0
            colorlist.append('rgb('+str(base1-i*13)+','+str(base2+i*20)+','+str(base3+i*40)+')')

        
            i=i+1
        else:
            base1=0
            base2=0
            base3=255
            colorlist.append('rgb('+str(base1+i*25)+','+str(base2+i*20)+','+str(base3-i*30)+')')

            i=i+1
    i=0
    for element in timeline_pressure_set:
        delta_t_angl_off_y.append(1)
        t_angl_off_y.append(1)
        delta_t_anw_off_y.append(1)
        t_anw_off_y.append(1)
        #F_angl_off_y.append(F_angl_y[i]+i*offset_Force_time+offset_group,F_angl_y[i]+i*offset_Force_time+offset_group)
        #F_anw_off_y.append(F_anw_y[i]+i*offset_Force_time+offset_group,F_anw_y[i]+i*offset_Force_time+offset_group)
        WS_0_off_x.append(0)
        WS_0_off_y.append(WS_S0_y[i]+i*offset_Waermestrom_time+15*offset_group)
        WS_angl_off_y.append(WS_angl_y[i]+i*offset_Waermestrom_time+15*offset_group)
        WS_anw_off_y.append(WS_anw_y[i]+i*offset_Waermestrom_time+15*offset_group)
        WS_max_off_y.append(WS_max_y[i]+i*offset_Waermestrom_time+15*offset_group)

        #Plot Force-Time
        fig1.add_trace(go.Scatter(x=timeline_time_set[i], y=np.array(element)+i*offset_Force_time+offset_group,
                    mode='lines',
                    name=ID_list[i],
                    line=dict(color=colorlist[i])))
        if Time_all == True:
            fig1.add_trace(go.Scatter(x=[delta_t_angl_x[i],delta_t_angl_x[i]], y=[delta_t_angl_off_y[i],250],
                    mode='lines',
                    name='\u0394t<sub>angl</sub>',
                    showlegend=False,
                    line=dict(color=colorlist_time[i])
                    ))
        
            fig1.add_trace(go.Scatter(x=[t_angl_x[i],t_angl_x[i]], y=[t_angl_off_y[i],250],
                    mode='lines',
                    name='t<sub>angl</sub>',
                    showlegend=False,
                    line=dict(color=colorlist_time[i])
                    ))
        
            fig1.add_trace(go.Scatter(x=[delta_t_anw_x[i],delta_t_anw_x[i]], y=[delta_t_anw_off_y[i],250],
                    mode='lines',
                    name='\u0394t<sub>anw</sub>',
                    showlegend=False,
                    line=dict(color=colorlist_time[i])
                    ))
       
            fig1.add_trace(go.Scatter(x=[t_anw_x[i],t_anw_x[i]], y=[t_anw_off_y[i],250],
                    mode='lines',

                    name='t<sub>anw</sub>',
                    showlegend=False,
                    line=dict(color=colorlist_time[i])
                    ))
        if Force_all == True:
            fig1.add_trace(go.Scatter(x=[delta_t_angl_x[i],t_angl_x[i]], y=[F_angl_y[i]+i*offset_Force_time+offset_group,F_angl_y[i]+i*offset_Force_time+offset_group],
                    mode='lines+markers',
                    marker_symbol='x',
                    showlegend=False,
                    line=dict(color=colorlist_force[i])))
                    
        
            fig1.add_trace(go.Scatter(x=[delta_t_anw_x[i],t_anw_x[i]], y=[F_anw_y[i]+i*offset_Force_time+offset_group,F_anw_y[i]+i*offset_Force_time+offset_group],
                    mode='lines+markers',
                    marker_symbol='x',
                    showlegend=False,
                    line=dict(color=colorlist_force[i])))
                    

        

        #Plot WS-Time
        #Depending on the checkboxes
        
            
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
        i=i+1

    i=i-1
    fig1.add_trace(go.Scatter(x=timeline_time_set[i], y=np.array(element)+i*offset_Force_time+offset_group,
                mode='lines',
                name=ID_list[i],
                line=dict(color=colorlist[i])))
    if Time_all == True:
        fig1.add_trace(go.Scatter(x=[delta_t_angl_x[i],delta_t_angl_x[i]], y=[delta_t_angl_off_y[i],250],
                mode='lines+text',
                name='\u0394t<sub>angl</sub>',
                showlegend=False,
                text=["","\u0394t<sub>angl</sub>"],
                textposition="top center",
                line=dict(color=colorlist_time[i])
                ))
        
        fig1.add_trace(go.Scatter(x=[t_angl_x[i],t_angl_x[i]], y=[t_angl_off_y[i],250],
                mode='lines+text',
                name='t<sub>angl</sub>',
                showlegend=False,
                text=["","t<sub>angl</sub>"],
                textposition="top center",
                line=dict(color=colorlist_time[i])
                ))
        
        fig1.add_trace(go.Scatter(x=[delta_t_anw_x[i],delta_t_anw_x[i]], y=[delta_t_anw_off_y[i],250],
                mode='lines+text',
                name='\u0394t<sub>anw</sub>',
                showlegend=False,
                text=["","\u0394t<sub>anw</sub>"],
                textposition="top center",
                line=dict(color=colorlist_time[i])
                ))
       
        fig1.add_trace(go.Scatter(x=[t_anw_x[i],t_anw_x[i]], y=[t_anw_off_y[i],250],
                mode='lines+text',

                name='t<sub>anw</sub>',
                showlegend=False,
                text=["","t<sub>anw</sub>"],
                textposition="top center",
                line=dict(color=colorlist_time[i])
                ))
    if (Force_all == True) and (offset_group==0):
        fig1.add_trace(go.Scatter(x=[delta_t_angl_x[i],(delta_t_angl_x[i]+t_angl_x[i])/2,t_angl_x[i]], y=[F_angl_y[i]+i*offset_Force_time+offset_group,F_angl_y[i]+i*offset_Force_time+offset_group,F_angl_y[i]+i*offset_Force_time+offset_group],
                mode='lines+text',
                #marker_symbol='x',
                showlegend=False,
                name='F<sub>angl</sub>',
                text=["","F<sub>angl</sub>",""],
                textposition="top center",
                line=dict(color=colorlist_force[i])))
                    
        
        fig1.add_trace(go.Scatter(x=[delta_t_anw_x[i],(delta_t_anw_x[i]+t_anw_x[i])/2, t_anw_x[i]], y=[F_anw_y[i]+i*offset_Force_time+offset_group,F_anw_y[i]+i*offset_Force_time+offset_group,F_anw_y[i]+i*offset_Force_time+offset_group],
                mode='lines+text',
                #marker_symbol='x',
                showlegend=False,
                name='F<sub>anw</sub>',
                text=["","F<sub>anw</sub>",""],
                textposition="top center",
                line=dict(color=colorlist_force[i])))
                    

        

        #Plot WS-Time
        #Depending on the checkboxes
        
            
    fig3.add_trace(go.Scatter(x=timeline_time_set[i], y=np.array(timeline_waermestrom_set[i])+i*offset_Waermestrom_time+15*offset_group,
                mode='lines',
                name=ID_list[i],
                line=dict(color=colorlist[i])))
    if (WS_all == True) and (offset_group==0):
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
    
    fig1.update_xaxes(range=[0, timeline_time_set[0][-1]*1.1])
    fig3.update_xaxes(range=[0, timeline_time_set[0][-1]*1.1])

st.sidebar.write("download the data [here](www.google.de)")
option0 = st.sidebar.selectbox(
     'Select page',
     ['Measurements and features', 'Results'])
st.sidebar.markdown('***')


if option0=='Measurements and features':
    #Header
    st.title('Daten des FloWeld-Projekts')

    #Loading the dataframe
    df_features = pd.read_parquet('data_processed')
    #df_features.to_excel("data_processed.xlsx") 
    #df_features.to_excel('data_processed.xlsx')


    #Obtain a list of all measurement variations
    df_experimental_points=df_features['META_ExperimentalPoint'].values
    #Remove duplicates
    list_experimental_points=list(dict.fromkeys(df_experimental_points))
    list_experimental_points_2=list(dict.fromkeys(df_experimental_points))
    list_experimental_points_2.insert(0, '-')
    #Ask which to display
    option_measurment = st.sidebar.selectbox(
        'Choose the experimental point',
        list_experimental_points)

    
    option_compare = st.sidebar.selectbox(
        'Compare with different experimental point?',
        list_experimental_points_2)
    if option_compare != '-':
        offset_group_slider = 45 #st.sidebar.slider('Offset between experimental points', min_value=1,max_value= 200, value=40)

    st.sidebar.markdown('***')
    #Sidebar elements for Force-Time diagram
    st.sidebar.write('Choose the features for Force-Time plot:')
    offset_Force_time = 20 #st.sidebar.slider('offset_Force_time', max_value= 120, value=20)
    #explanation_force=st.sidebar.expander(label="What does this mean?")
    #explanation_force.write("explanation of the features")
    
    Time_all = st.sidebar.checkbox('Show all time Features ')
    Force_all = st.sidebar.checkbox('Show all force Features')
    #F_angl_flag = st.sidebar.checkbox('F_{angl}')
    #F_anw_flag = st.sidebar.checkbox('F_{anw}')
    #t_angl_flag = st.sidebar.checkbox('t_{angl}')
    #t_anw_flag = st.sidebar.checkbox('t_{anw}')
    st.sidebar.markdown('***')

    #Sidebar elements for Way-Time diagram
    #st.sidebar.write('Choose the features for Way-Time plot:')
    #offset_Way_time = st.sidebar.slider('offset_Way_time', max_value= 120, value=20)
    #s_0_flag = st.sidebar.checkbox('s_{0}')
    #s_angl_flag = st.sidebar.checkbox('s_{angl}')
    #s#_tot_flag = st.sidebar.checkbox('s_{tot}')

    #Sidebar elements for Waermestrom-Time diagram
    st.sidebar.write('Choose the features for Waermestrom-Time plot:')
    offset_Waermestrom_time = 300 #st.sidebar.slider('offset_Waermestrom_time', max_value= 3000, value=300)
    WS_all = st.sidebar.checkbox('all Waermestrom Features')
    ##WS_0_flag = st.sidebar.checkbox('WS_{0}', True)
    #WS_angl_flag = st.sidebar.checkbox('WS_{angl}', True)
    #WS_anw_flag = st.sidebar.checkbox('WS_{anw}', True)

    measurment_plotter(option_measurment, 0, offset_Force_time, offset_Waermestrom_time)
    if option_compare != '-':
        measurment_plotter(option_compare, offset_group_slider, offset_Force_time, offset_Waermestrom_time)
    
    #st.write('You selected:', option1)
    
    #Display plots
    expander_table = st.expander(label="View data")
    expander_table.write(option_measurment)
    expander_table.dataframe(df_features.loc[df_features['META_ExperimentalPoint'] == option_measurment])

    if option_compare != '-':
        expander_table.write(option_compare)
        expander_table.dataframe(df_features.loc[df_features['META_ExperimentalPoint'] == option_compare])
    #expander_table.write("test")
    #clicked = expander_table.button("View data")
    col1, col3 = st.columns((2,2))

    fig1.update_layout(
    title="Force-Time Plot",
    xaxis_title="Time in [s]",
    yaxis_title="Force in [N]",)
    fig3.update_layout(
    title="Waermestrom-Time Plot",
    xaxis_title="Time in [s]",
    yaxis_title="Voltage signal of the Waermestrom sensor in [µV]",)


    col1.plotly_chart(fig1, use_container_width=True)
    
    col3.plotly_chart(fig3, use_container_width=True)

elif option0=='Results':
    st.title('Ergebnisse')
    df_features = pd.read_parquet('data_processed')

    list_experimental_points=[]
    list_experimental_points.insert(0, 'PVC-U')
    list_experimental_points.insert(0, 'PP-H')
    checkbox_list = []
    all_PP = st.sidebar.checkbox('PP-H', True)
    all_PVC= st.sidebar.checkbox('PVC-U', True )
 

    if all_PP == True:
        selected_data=df_features.loc[df_features['FEAT_Material_PP'] == 1]
        fig1.add_trace(go.Scatter(x=selected_data['META_ExperimentalPoint'].values, y=selected_data['LABEL_weld_factor'].values, 
                    mode='markers',
                    marker=dict(color='firebrick'),
                    name='PP-H',
                    marker_symbol='x',))

    if all_PVC ==True:
        selected_data=df_features.loc[df_features['FEAT_Material_PVC'] == 1]
        fig1.add_trace(go.Scatter(x=selected_data['META_ExperimentalPoint'].values, y=selected_data['LABEL_weld_factor'].values, 
                    mode='markers',
                    marker=dict(color='slateblue'),
                    name='PVC-U',
                    marker_symbol='x',))
    

    #fig1 = go.Figure()
    fig1.update_layout(
    title="Weld Factor for different experimental points",
    xaxis_title="Experimental Point",
    yaxis_title="Weld Factor",)
    
    st.plotly_chart(fig1, use_container_width=True)
