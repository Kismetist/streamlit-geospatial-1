import ast
import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


@st.cache
def get_layers(url):
    options = leafmap.get_wms_layers(url)
    return options


def app():
    st.title("网络地图服务(WMS)")
    st.markdown(
        """
这个应用程序是一个加载网络地图服务（WMS）图层的演示。只需在下面的文本框中输入WMS服务的URL，然后按回车键即可检索图层。如果需要的话，请到https://apps.nationalmap.gov/services，下载一些WMS的URL。
    """
    )

    row1_col1, row1_col2 = st.columns([3, 1.3])
    width = 800
    height = 600
    layers = None

    with row1_col2:

        esa_landcover = "https://services.terrascope.be/wms/v2"
        url = st.text_input(
            "Enter a WMS URL:", value="https://services.terrascope.be/wms/v2"
        )
        empty = st.empty()

        if url:
            options = get_layers(url)

            default = None
            if url == esa_landcover:
                default = "WORLDCOVER_2020_MAP"
            layers = empty.multiselect(
                "Select WMS layers to add to the map:", options, default=default
            )
            add_legend = st.checkbox("Add a legend to the map", value=True)
            if default == "WORLDCOVER_2020_MAP":
                legend = str(leafmap.builtin_legends["ESA_WorldCover"])
            else:
                legend = ""
            if add_legend:
                legend_text = st.text_area(
                    "Enter a legend as a dictionary {label: color}",
                    value=legend,
                    height=200,
                )

        with row1_col1:
            m = leafmap.Map(center=(36.3, 0), zoom=2)

            if layers is not None:
                for layer in layers:
                    m.add_wms_layer(
                        url, layers=layer, name=layer, attribution=" ", transparent=True
                    )
            if add_legend and legend_text:
                legend_dict = ast.literal_eval(legend_text)
                m.add_legend(legend_dict=legend_dict)

            m.to_streamlit(height=height)


app()
