import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

day_df = pd.read_csv("https://raw.githubusercontent.com/saniapradnya/sania-dicoding/refs/heads/main/data/hour.csv")
hour_df = pd.read_csv("https://github.com/saniapradnya/sania-dicoding/blob/4b777a4b6a27ba3d32bf730aad420f600d681077/data/hour.csv")


st.header('Bike Sharing Dataset Analysis')

st.sidebar.title("Bike Sharing Dataset Analysis")
st.sidebar.write("Based on")
side = st.sidebar.selectbox(
    label="Select data", options=("Season", "Working Day"))

if side == "Season":
    st.subheader("Which season has the highest number of bike rental?")
    
    spring_count = 471348
    summer_count = 918589
    fall_count = 1061129
    winter_count = 841613

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Spring: ", spring_count)
    with col2:
        st.metric("Summer: ", summer_count)
    with col3:
        st.metric("Fall: ", fall_count, "User")
    with col4:
        st.metric("Winter: ", winter_count)


    season_count = day_df.groupby(by="season").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum",
    "workingday": lambda x: x.value_counts().idxmax()
    }).reset_index()

    
    season_count['season'] = season_count['season'].replace({
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
    })

    visualization_season_df = pd.DataFrame({
    "Season": season_count["season"],
    "Casual Users": season_count["casual"],
    "Registered Users": season_count["registered"],
    "Total Users": season_count["cnt"]
    })
    
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x="Season", y="Total Users", data=visualization_season_df, palette="viridis") 
    plt.title("Total Users Based on Season", fontsize=16)
    plt.xlabel("Season", fontsize=14)
    plt.ylabel("Total Users", fontsize=14)
    plt.xticks(rotation=0)
    ax.set_ylim()
    ax.ticklabel_format(style='plain', axis='y')
    plt.show()

    st.pyplot(plt)

elif side == "Working Day":
    st.subheader("How working day affect the total users of bike rental?")

    count_workingday = 2292410
    count_holiday = 1000269

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Working Day: ", count_workingday, "User")
    with col2:
        st.metric("Holiday: ", count_holiday)


    workingday_hour = day_df.groupby(by="workingday").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum",
    "season": lambda x: x.value_counts().idxmax()
    }).reset_index()


    workingday_hour['workingday_label'] = workingday_hour['workingday'].replace({0: "Holiday", 1: "Working Day"})

    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='workingday_label', y='cnt', data=workingday_hour, palette='viridis')

    plt.title("Total Bike Rentals Based on Working Day", fontsize=16)
    plt.xlabel("Day Type", fontsize=14)
    plt.ylabel("Total Rentals (cnt)", fontsize=14)
    plt.xticks(rotation=0)
    ax.set_ylim() 
    ax.ticklabel_format(style='plain', axis='y') 
    plt.show()
    
    st.pyplot(plt)
