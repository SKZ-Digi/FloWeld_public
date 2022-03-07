import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Create plots
fig1, ax1 = plt.subplots(dpi = 500)
fig2, ax2 = plt.subplots(dpi = 500)
fig3, ax3 = plt.subplots(dpi = 500)

def measurment_plotter(option1, offset_group):
    
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
    WS_S0_y=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_WS0[µV]'].values
    W_max_x=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_WS_max[µV]'].values
    #W__x=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_WS_delta_t_max[s]'].values
    WS_angl_y=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_WS_angl[µV]'].values
    WS_angl_x=t_angl+delta_t_angl
    WS_anw_y=df_features.loc[df_features['META_ExperimentalPoint'] == option1]['FEAT_WS_anw[µV]'].values
    WS_anw_x=t_angl+t_anw+delta_t_angl+delta_t_anw

    
    i=0
    for element in timeline_pressure_set:

        #ax1.plot(Delta_t_angl_x, Delta_t_angl_y,  alpha=0.5, label='\u0394$t_{angl}$')
        #ax1.plot(t_angl_x, t_angl_y,  alpha=0.5, label='$t_{angl}$')
        #ax1.plot(Delta_t_anw_x, Delta_t_anw_y,  alpha=0.5, label='\u0394$t_{anw}$')
        #ax1.plot(t_anw_x, t_anw_y,  alpha=0.5 ,label='$t_{anw}$')
        #ax1.plot(F_angl_x, F_angl_y, color="black")
        #ax1.plot(F_anw_x, F_anw_y, color="black")
        #ax1.text(F_angl_x[5], F_angl_y[0],'$F_{angl}$')
        #ax1.text(F_anw_x[5], F_anw_y[0],'$F_{anw}$')

        #Plot Force-Time
        ax1.plot(timeline_time_set[i], np.array(element)+i*offset_Force_time+offset_group)
        ax1.set_ylabel('Kraft in [N]')
        ax1.set_xlabel('Zeit in [s]')
        ax1.title.set_text(str(option1)+' Force-Time with offset')
        
        #Plot Way-Time
        ax2.plot(timeline_time_set[i], np.array(timeline_way_set[i])+i*offset_Way_time+offset_group)
        ax2.set_ylabel('Weg in [mm]')
        ax2.set_xlabel('Zeit in [s]')
        ax2.title.set_text(str(option1)+' Way-Time with offset')

        #Plot Force-Time
        #Depending on the checkboxes
        if WS_0_flag == True:
            ax3.scatter(0,WS_S0_y[i]+i*offset_Waermestrom_time+15*offset_group, marker="x", s=100, color="forestgreen")
            ax3.text(0, WS_S0_y[i]+i*offset_Waermestrom_time+15*offset_group,'$WS_{0}$')
        #if WS_0_flag == True:
        #    ax3.scatter(W_Smax_x,W_Smax_y, marker="x", s=100, color="peru")
        #    ax3.text(W_Smax_x, W_Smax_y,'$WS_{max}$')
        if WS_angl_flag == True:
            ax3.scatter(WS_angl_x[i],WS_angl_y[i]+i*offset_Waermestrom_time+15*offset_group, marker="x", s=100, color="blue")
            ax3.text(WS_angl_x[i], WS_angl_y[i]+i*offset_Waermestrom_time+15*offset_group,'$WS_{angl}$')
        if WS_anw_flag == True:
            ax3.scatter(WS_anw_x[i],WS_anw_y[i]+i*offset_Waermestrom_time+15*offset_group, marker="x", s=100, color="aqua")
            ax3.text(WS_anw_x[i], WS_anw_y[i]+i*offset_Waermestrom_time+15*offset_group,'$WS_{anw}$')
        #Plot the timeline
        ax3.plot(timeline_time_set[i], np.array(timeline_waermestrom_set[i])+i*offset_Waermestrom_time+15*offset_group)
        ax3.set_ylabel('Waermestrom in [µV]')
        ax3.set_xlabel('Zeit in [s]')
        ax3.title.set_text(str(option1)+' Waermestrom-Time with offset')
        i=i+1


option0 = st.sidebar.selectbox(
     'select page',
     ['Measurements and features', 'Results'])


if option0=='Measurements and features':
    #Header
    st.title('Messungen und Features')

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
        'Choose the measurement set',
        list_experimental_points)

    
    option_compare = st.sidebar.selectbox(
        'Compare with different dataset?',
        list_experimental_points_2)
    if option_compare != '-':
        offset_group_slider = st.sidebar.slider('Offset between comparisons', max_value= 200, value=40)

    #Sidebar elements for Force-Time diagram
    st.sidebar.write('Choose the features for Force-Time plot:')
    offset_Force_time = st.sidebar.slider('offset_Force_time', max_value= 120, value=20)
    delta_t_angl_flag = st.sidebar.checkbox('\u0394t_{angl}', True)
    delta_t_anw_flag = st.sidebar.checkbox('\u0394t_{anw}')
    F_angl_flag = st.sidebar.checkbox('F_{angl}')
    F_anw_flag = st.sidebar.checkbox('F_{anw}')
    t_angl_flag = st.sidebar.checkbox('t_{angl}')
    t_anw_flag = st.sidebar.checkbox('t_{anw}')

    #Sidebar elements for Way-Time diagram
    st.sidebar.write('Choose the features for Way-Time plot:')
    offset_Way_time = st.sidebar.slider('offset_Way_time', max_value= 120, value=20)
    s_0_flag = st.sidebar.checkbox('s_{0}')
    s_angl_flag = st.sidebar.checkbox('s_{angl}')
    s_tot_flag = st.sidebar.checkbox('s_{tot}')

    #Sidebar elements for Waermestrom-Time diagram
    st.sidebar.write('Choose the features for Waermestrom-Time plot:')
    offset_Waermestrom_time = st.sidebar.slider('offset_Waermestrom_time', max_value= 3000, value=300)
    WS_max_flag = st.sidebar.checkbox('WS_{max}')
    WS_0_flag = st.sidebar.checkbox('WS_{0}', True)
    WS_angl_flag = st.sidebar.checkbox('WS_{angl}', True)
    WS_anw_flag = st.sidebar.checkbox('WS_{anw}', True)

    measurment_plotter(option_measurment, 0)
    if option_compare != '-':
        measurment_plotter(option_compare, offset_group_slider)
    #st.write('You selected:', option1)


    #Display plots
    st.pyplot(fig1)
    st.pyplot(fig2)
    st.pyplot(fig3)
elif option0=='Results':
    st.title('Ergebnisse')
    df_features = pd.read_parquet('data_processed')
    #df_features.to_excel("data_processed.xlsx") 
    #df_features.to_excel('data_processed.xlsx')


    #Obtain a list of all measurement variations
    df_experimental_points=df_features['META_ExperimentalPoint'].values
    #Remove duplicates
    list_experimental_points=list(dict.fromkeys(df_experimental_points))
    list_experimental_points.insert(0, 'all PVC')
    list_experimental_points.insert(0, 'all PP')
    checkbox_list = []
    
    i=850
    for element in list_experimental_points:
        checkbox_list.append(st.sidebar.checkbox(element, key = i))
        i=i+1

    if checkbox_list[0] == True:
        selected_data=df_features.loc[df_features['FEAT_Material_PVC'] == 1]
       

    elif checkbox_list[1] == True:
        selected_data=df_features.loc[df_features['FEAT_Material_PP'] == 1]

    else:
        del checkbox_list[0]
        del checkbox_list[0]
        del list_experimental_points[0]
        del list_experimental_points[0]
        i=0
        selected_data = pd.DataFrame()
        for element in checkbox_list:
            if element ==True:
                new_dataframe=df_features.loc[df_features['META_ExperimentalPoint'] == list_experimental_points[i]]
                selected_data = pd.concat([selected_data, new_dataframe])
            i=i+1
        st.write(selected_data)
