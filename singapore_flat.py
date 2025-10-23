import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import numpy as np

# =========================
# 1️⃣ Load the trained model
# =========================
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# =========================
# 🌿 Set background colors and label styles
# =========================
st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background-color: #50CEA2;  /* light green */
    }

    /* Sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #2ECC71 !important;  /* green */
    }

    /* Sidebar text color and size */
    [data-testid="stSidebar"] * {
        color: white !important;
        font-size: 18px !important;
        font-weight: 600 !important;
    }

    /* Label text size */
    label {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #1B2631 !important;
    }

    /* Input box size */
    input, select, textarea {
        font-size: 18px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 2️⃣ App title
# =========================
st.markdown('<h1 style="color: black;">Singapore Flat Resale Price Predictor</h1>', unsafe_allow_html=True)

# =========================
# 3️⃣ Sidebar navigation
# =========================
st.sidebar.title('Navigation')
selection = st.sidebar.radio('Go to', ['Home', 'Predict'])

# =========================
# 🏠 Home Page
# =========================
if selection == 'Home':
    image = Image.open("C:/Users/anbarasi/OneDrive/Pictures/singapore_image.jpg")
    st.image(image, caption="Singapore Flat", use_container_width=True)

    st.markdown(
        """
        <div style='
            background-color: #C8E6C9;
            padding: 20px;
            border-radius: 10px;
            font-size: 20px;
            color: darkgreen;
        '>
            <h3>Welcome to the <b>Singapore Flat Resale Price Predictor!</b> </h3>
            <p>
            Singapore's public housing market is one of the most well-regulated and dynamic in the world. 
            With factors such as location, flat type, floor area, and remaining lease period influencing resale values, 
            understanding market trends can be challenging.
            </p>
            <p>
            This tool helps you explore and predict <b>HDB flat resale prices</b> based on real data. 
            By entering key details like the town, flat type, and lease information, 
            you can get an estimated resale price instantly — helping buyers, sellers, 
            and analysts make informed decisions.
            </p>
            <p>
            Whether you're a homeowner, real estate enthusiast, or data analyst, 
            this interactive dashboard offers insights into Singapore’s housing landscape 
            and supports smarter decision-making.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# 🔮 Prediction Page
# =========================
if selection == "Predict":
    st.subheader("Enter Flat Details for Prediction")

    # ✅ Floor area input
    floor_area_sqm = st.number_input("Floor Area (sqm)", min_value=40, max_value=200, value=90)

    # ✅ Lease Commence Year dropdown (sorted ascending)
    years = sorted([
        1986, 1981, 1980, 1979, 1978, 1985, 1976, 1977, 2002, 1993, 1996,
        2006, 2003, 1982, 1974, 2010, 1987, 1984, 2000, 1989, 1995, 1992,
        1988, 1998, 1990, 1983, 2004, 1997, 2005, 1969, 1970, 1971, 1973,
        2009, 1999, 2001, 2008, 2007, 1975, 2011, 1968, 1967, 1972, 1991,
        2012, 1994, 1966, 2013
    ])
    lease_commence_date = st.selectbox("Lease Commence Year", years, index=len(years) - 1)

    # ✅ Remaining Lease dropdown (sorted descending)
    remaining_lease_values = sorted([
        70., 65., 64., 63., 62., 69., 60., 61., 86., 77., 80., 90., 87.,
        66., 58., 94., 71., 68., 84., 73., 79., 76., 72., 82., 74., 67.,
        88., 81., 89., 53., 54., 55., 57., 93., 83., 85., 92., 91., 59.,
        95., 52., 51., 56., 75., 96., 78., 50., 97., 49., 48.
    ], reverse=True)
    remaining_lease = st.selectbox("Remaining Lease", remaining_lease_values)

    # ✅ Flat Type encoding
    flat_type_encoded = {
        "1 ROOM": 0, "2 ROOM": 1, "3 ROOM": 2,
        "4 ROOM": 3, "EXECUTIVE": 4, "MULTI-GENERATION": 5
    }
    flat_type_selected = st.selectbox("Flat Type", list(flat_type_encoded.keys()))
    flat_type_value = flat_type_encoded[flat_type_selected]

    # ✅ Storey Range Encoded (numeric, sorted ascending)
    storey_range_encoded = sorted([2, 0, 4, 3, 1, 6, 5, 7, 8, 9, 11, 15, 10, 12, 14, 13, 16])
    storey_selected = st.selectbox("Storey Range", storey_range_encoded)
    storey_encoded_value = storey_selected

    # ✅ Towns (one-hot encoding)
    towns = [
        'ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
        'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
        'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
        'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
        'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
        'TOA PAYOH', 'WOODLANDS', 'YISHUN'
    ]
    town_selected = st.selectbox("Town", towns)
    town_encoded = {f"town_{t}": 1 if t == town_selected else 0 for t in towns}

    # ✅ Prepare input DataFrame
    input_data = {
        'floor_area_sqm': [floor_area_sqm],
        'lease_commence_date': [lease_commence_date],
        'remaining_lease': [remaining_lease],
        'flat_type_encoded': [flat_type_value],
        'storey_range_encoded': [storey_encoded_value]
    }
    input_data.update({col: [val] for col, val in town_encoded.items()})
    input_df = pd.DataFrame(input_data)

    # 🧮 Predict resale price
    if st.button("Predict Resale Price"):
        try:
            # 🔹 Align input columns with model training features
            if hasattr(model, 'feature_names_in_'):
                model_features = list(model.feature_names_in_)
                for col in model_features:
                    if col not in input_df.columns:
                        input_df[col] = 0
                input_df = input_df[model_features]

            # 🔹 Predict (log-transformed output)
            log_pred = model.predict(input_df)[0]

            # 🔹 Inverse transform back to rupees
            price = np.expm1(log_pred)

            # 💚 Display bigger, styled output
            st.markdown(
                f"""
                <div style='
                    background-color: #C8E6C9;
                    padding: 20px;
                    border-radius: 12px;
                    text-align: center;
                '>
                    <h3 style='color: darkgreen; font-size:28px;'>💰 Estimated Resale Price</h3>
                    <h2 style='color:#1B5E20; font-size:38px;'>₹{price:,.0f}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Error during prediction: {e}")
