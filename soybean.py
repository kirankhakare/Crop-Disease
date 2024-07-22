import streamlit as st
from PIL import Image

# Function to classify soybean diseases and provide treatment recommendations
def classify_and_detect_soybean_disease(image):
    # Placeholder function for soybean disease classification and detection
    # For demonstration purposes, let's assume we have a dictionary mapping soybean diseases to treatment recommendations
    soybean_diseases = {
        "Healthy": {
            "recommendations": [
                "Practice good crop management practices.",
                "Implement crop rotation with non-host crops."
            ]
        }
    }

    # Placeholder for disease detection logic
    # For demonstration, let's assume we have a model that predicts soybean disease based on the image
    predicted_disease = "Healthy"  # Placeholder for the predicted disease

    # Get treatment recommendations for the detected disease
    recommendations = soybean_diseases.get(predicted_disease, {}).get("recommendations", [])

    return predicted_disease, recommendations

def app():
    st.title("Soybean Disease Classification and Treatment Recommendation")

    uploaded_file = st.file_uploader("Upload Soybean Plant Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Check if the filename contains "soybean"
        filename = uploaded_file.name.lower()
        if "soybean" in filename:
            predicted_disease = "Healthy"

            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Provide treatment recommendations based on predicted disease
            _, recommendations = classify_and_detect_soybean_disease(image)

            # Display treatment recommendations
            st.write("Treatment Recommendations:")
            for recommendation in recommendations:
                st.write(f"- {recommendation}")
        
if __name__ == "__main__":
    app()
