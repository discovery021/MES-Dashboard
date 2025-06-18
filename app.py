
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulate machine data
np.random.seed(42)
machine_data = {
    'Machine': ['Machine 1', 'Machine 2', 'Machine 3', 'Machine 4'],
    'Status': np.random.choice(['OK', 'Warning', 'Störung'], 4),
    'Taktzeit': np.random.uniform(5, 15, 4),
    'Temperatur': np.random.uniform(60, 100, 4),
    'Stillstand': np.random.uniform(0, 5, 4)
}

df = pd.DataFrame(machine_data)

# Streamlit app
st.title("MES Dashboard")

# Display machine status
st.header("Maschinenstatus")
status_colors = {'OK': 'green', 'Warning': 'yellow', 'Störung': 'red'}
for index, row in df.iterrows():
    st.markdown(f"**{row['Machine']}**: <span style='color:{status_colors[row['Status']]}'>{row['Status']}</span>", unsafe_allow_html=True)

# Display live data
st.header("Live-Daten")
st.dataframe(df)

# Plot Taktzeit
st.subheader("Taktzeit")
fig, ax = plt.subplots()
df.plot(kind='bar', x='Machine', y='Taktzeit', ax=ax, color='blue')
st.pyplot(fig)

# Plot Temperatur
st.subheader("Temperatur")
fig, ax = plt.subplots()
df.plot(kind='bar', x='Machine', y='Temperatur', ax=ax, color='orange')
st.pyplot(fig)

# Plot Stillstand
st.subheader("Stillstand")
fig, ax = plt.subplots()
df.plot(kind='bar', x='Machine', y='Stillstand', ax=ax, color='purple')
st.pyplot(fig)
        