import streamlit as st
import folium
from streamlit_folium import st_folium

location_coords = {
    "台北": (25.0330, 121.5654),
    "新北": (25.0169, 121.4628),
    "桃園": (24.9931, 121.3000),
    "台中": (24.1477, 120.6736),
    "台南": (22.9999, 120.2269),
    "高雄": (22.6273, 120.3014),
}

aqi_ranges = [
    (0, 11, "良好", "green"),
    (12, 23, "普通", "yellow"),
    (24, 35, "對敏感族群不健康", "orange"),
    (36, 41, "對所有族群不健康", "red"),
    (42, 47, "非常不健康", "purple"),
    (48, 100, "危害", "maroon")
]

def get_aqi_level(pm25):
    for low, high, label, color in aqi_ranges:
        if low <= pm25 <= high:
            return label, color
    return "超出範圍", "gray"

# Streamlit 介面
st.title("台灣 PM2.5 地圖視覺化")

location = st.selectbox("選擇地區：", list(location_coords.keys()))
pm25 = st.number_input("輸入 PM2.5 數值（μg/m³）：", 0.0, 100.0, 25.0)

if st.button("顯示地圖"):
    aqi_level, color = get_aqi_level(pm25)
    lat, lon = location_coords[location]

    m = folium.Map(location=[23.7, 121], zoom_start=7)
    folium.CircleMarker(
        location=[lat, lon],
        radius=15,
        color=color,
        fill=True,
        fill_opacity=0.8,
        popup=f"{location} PM2.5: {pm25} μg/m³\n等級：{aqi_level}"
    ).add_to(m)

    st.write(f"目前地區：{location}，PM2.5 為 {pm25} μg/m³，空氣品質等級：**{aqi_level}**")
    st_folium(m, width=700)
