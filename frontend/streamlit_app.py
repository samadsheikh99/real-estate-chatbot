import streamlit as st
import requests

st.title("🏡 AI Real Estate Valuator & Description Generator")

property_type = st.selectbox("Property Type", ["Flat", "House", "Villa"])
location = st.text_input("Location", "E-11")
city = st.selectbox("City", ["Islamabad", "Lahore", "Karachi"])
bedrooms = st.number_input("Bedrooms", 1, 10, 2)
baths = st.number_input("Bathrooms", 1, 10, 2)
purpose = st.selectbox("Purpose", ["For Sale", "For Rent"])
area_type = st.selectbox("Area Type", ["Marla", "Kanal", "Sqft"])
area_size = st.number_input("Area Size", 1.0, 10000.0, 6.0)

if st.button("Generate Valuation & Description"):
    data = {
        "property_type": property_type,
        "location": location,
        "city": city,
        "baths": baths,
        "purpose": purpose,
        "bedrooms": bedrooms,
        "area_type": area_type,
        "area_size": area_size
    }

    res = requests.post("http://localhost:8000/predict/", json=data)

    if res.status_code == 200:
        result = res.json()
        st.subheader("💰 Predicted Price")
        st.success(f"{result['predicted_price']:,} PKR")

        st.subheader("📝 Auto-generated Description")
        st.write(result["description"])
    else:
        st.error("Error: Could not fetch prediction.")
