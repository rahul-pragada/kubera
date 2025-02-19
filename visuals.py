# https://medium.com/@suhacapital/visualizing-financial-data-using-pythons-plotly-45d55cc5e405
import streamlit as st
import pandas as pd
import numpy as np

from scraputils.sector_company_list import fetch_sector_list


sectors=["Aerospace & Defence","Agro Chemicals","Air Transport Service","Alcoholic Beverages","Auto Ancillaries","Automobile",
"Banks","Bearings","Cables","Capital Goods - Electrical Equipment","Capital Goods-Non Electrical Equipment",
"Castings, Forgings & Fastners","Cement","Cement - Products","Ceramic Products","Chemicals","Computer Education","Construction","Consumer Durables",
"Credit Rating Agencies","Crude Oil & Natural Gas","Diamond, Gems and Jewellery","Diversified","Dry cells","E-Commerce/App based Aggregator",
"Edible Oil","Education","Electronics","Engineering","Entertainment","ETF","Ferro Alloys","Fertilizers","Finance",
"Financial Services","FMCG","Gas Distribution","Glass & Glass Products","Healthcare","Hotels & Restaurants","Infrastructure Developers & Operators","Infrastructure Investment Trusts","Insurance","IT - Hardware","IT - Software","Leather","Logistics","Marine Port & Services","Media - Print/Television/Radio",
"Mining & Mineral products","Miscellaneous","Non Ferrous Metals","Oil Drill/Allied","Online Media","Packaging","Paints/Varnish",
"Paper","Petrochemicals","Pharmaceuticals","Plantation & Plantation Products","Plastic products","Plywood Boards/Laminates","Power Generation & Distribution",
"Power Infrastructure","Printing & Stationery","Quick Service Restaurant","Railways","Readymade Garments/ Apparells","Real Estate Investment Trusts",
"Realty","Refineries","Refractories","Retail","Sanitaryware","Ship Building","Shipping","Steel","Stock/ Commodity Brokers","Sugar","Telecom-Handsets/Mobile",
"Telecomm Equipment & Infra Services","Telecomm-Service","Textiles","Tobacco Products","Trading","Tyres"]



# Create two columns (20% width for left, 80% for right)
left_col, right_col = st.columns([1, 4])

# Left panel - Menu
with left_col:
    st.markdown('<div class="left-pane">', unsafe_allow_html=True)
    st.write("## Menu")
    menu_option = st.radio("Choose an option:", sectors)
    st.markdown("</div>", unsafe_allow_html=True)

# Right panel - Content
with right_col:
    st.markdown('<div class="right-pane">', unsafe_allow_html=True)
    for i in sectors:
        if menu_option == i:
            st.dataframe(fetch_sector_list())
    st.markdown("</div>", unsafe_allow_html=True)
