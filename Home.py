import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("可视化")
st.sidebar.info(
    """
    Web App URL: <https://kismetist-streamlit-geospatial-1-home-076n41.streamlit.app/>
    """
)

st.sidebar.title("小组成员")
st.sidebar.info(
    """
   赵瑞坤、方鹏贺、杨安恺、张泽宇
    """
)


st.title("可视化大作业")


st.info("点击←侧来进行可视化展示")

st.subheader("请欣赏")

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

with row1_col2:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
