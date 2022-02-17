import pandas as pd
import altair as alt
import streamlit as st


df = pd.read_parquet('DO_data.parquet')
my_headers = ['STATION_NAME', 'PARAMETER', 'FDR_RESULT', 'UNS_NAME',
              'SAMPLE_DATE', 'SAMPLE_DEPTH', 'SAMPLE_DEPTH_UNITS', 'Month', 'COUNTY_NAME']

base = alt.Chart(df).properties(width=1000, height=700)

selection = alt.selection_multi(fields=['STATION_NAME'], bind='legend')

my_bounds = (5, 13)
dots = base.mark_point(size=30, clip=True).encode(
    x=alt.X('Month', title='Month'),
    y=alt.Y('FDR_RESULT', title='Dissolved Oxygen (mg/L)',
            # axis=alt.Axis(ticks=True, tickCount=my_bounds[1] - my_bounds[0])
            ),
    shape=alt.Shape('COUNTY_NAME', title='County'),
    color=alt.Color('STATION_NAME', title='Station Name'),
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
    size=alt.condition(selection, alt.value(50), alt.value(5)),
    tooltip=my_headers
    # tooltip=alt.condition(selection, my_headers, ['STATION_NAME'])
).add_selection(selection)
# ).add_selection(selection).interactive()
# dots
# st.write(dots)
st.altair_chart(dots, use_container_width=True)
