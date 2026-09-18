import streamlit as st
import requests
import folium

from streamlit_folium import st_folium


st.set_page_config(
    page_title="Cybercrime Risk Prediction",
    page_icon="🛡️",
    layout="wide"
)


st.title("🛡️ Cybercrime Cash Withdrawal Risk Prediction")

st.write(
    "AI-based prototype for identifying potential high-risk "
    "cash withdrawal locations."
)


col1, col2 = st.columns(2)


with col1:

    st.subheader("Transaction Information")

    amount = st.number_input(
        "Withdrawal Amount",
        min_value=0.0,
        value=10000.0
    )

    previous_incidents = st.number_input(
        "Previous Suspicious Incidents",
        min_value=0,
        value=2
    )

    withdrawal_count = st.number_input(
        "Withdrawal Count",
        min_value=0,
        value=5
    )

    hour = st.slider(
        "Withdrawal Hour",
        min_value=0,
        max_value=23,
        value=20
    )


with col2:

    st.subheader("Location")

    latitude = st.number_input(
        "Latitude",
        value=22.5726
    )

    longitude = st.number_input(
        "Longitude",
        value=88.3639
    )


if st.button("🔍 Predict Risk"):

    payload = {
        "amount": amount,
        "previous_incidents": previous_incidents,
        "withdrawal_count": withdrawal_count,
        "hour": hour,
        "latitude": latitude,
        "longitude": longitude
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        risk = result["risk"]
        score = result["risk_score"]

        st.subheader("Prediction Result")

        if risk == "High":
            st.error(f"🔴 HIGH RISK — {score}/100")

        elif risk == "Medium":
            st.warning(f"🟡 MEDIUM RISK — {score}/100")

        else:
            st.success(f"🟢 LOW RISK — {score}/100")


        # Map

        st.subheader("📍 Risk Location")

        m = folium.Map(
            location=[latitude, longitude],
            zoom_start=13
        )

        folium.Marker(
            [latitude, longitude],
            popup=f"Risk: {risk} | Score: {score}",
            tooltip=f"{risk} Risk"
        ).add_to(m)

        st_folium(
            m,
            width=900,
            height=500
        )

    except Exception as e:

        st.error(
            "Backend API is not running. "
            "Start FastAPI first."
        )