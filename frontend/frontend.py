import streamlit as st
import requests
import os

def check_pico_placa(plate_number, date, time):
    url = "http://127.0.0.1:8000/predictor/check"
    formatted_date = date.strftime("%Y-%m-%d")  # Format date to YYYY-MM-DD
    formatted_time = time.strftime("%H:%M")     # Format time to HH:MM
    
    try:
        response = requests.post(url, json={
            "plate_number": plate_number,
            "date": formatted_date,
            "time": formatted_time
        })
        data = response.json()
        if "message" in data:
            return data["message"]
        elif "detail" in data:
            return data["detail"]
        else:
            return f"Unexpected response: {data}"
    except requests.exceptions.RequestException as e:
        return f"Error connecting to API: {e}"


st.title("Pico y Placa Predictor")
image_path = os.path.join(os.getcwd(), 'frontend', 'assets', 'pico_EC50025_MG60828.jpg')
st.image(image_path, use_container_width=True)
plate_number = st.text_input("Enter your license plate (e.g., ABC-1234 or ABC-123):")
date = st.date_input("Select a date:")
time = st.time_input("Select or enter a time:", value=None)

if st.button("Check"):
    if plate_number and date and time:
        result = check_pico_placa(plate_number, date, time)  # Pass objects, not strings
        # st.write(result)
        if "Invalid plate format" in result:
            st.error(result)  # Display the error message using Streamlit's error style
        else:
            st.markdown(
                f"""
                <div style="background-color: #ffe0C7; padding: 10px; border-radius: 5px;">
                    <p style="color: #333; font-size: 16px;">{result}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.error("Please fill in all fields.")