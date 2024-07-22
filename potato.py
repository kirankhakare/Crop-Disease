import streamlit as st
from PIL import Image

# Function to classify potato diseases and provide treatment recommendations
def classify_and_detect_potato_disease(image):
    # Placeholder function for potato disease classification and detection
    # Replace this with your actual classification and detection code
    # For demonstration purposes, let's assume we have a dictionary mapping potato diseases to treatment recommendations
    potato_diseases = {
        "Early Blight": {
            "keywords": ["potato01", "potato02", "potato03", "potato04", "potato05"],
            "recommendations": [
                "To treat potato early blight, consider using fungicides containing active ingredients like chlorothalonil, mancozeb, or azoxystrobin. These fungicides effectively suppress the development and spread of early blight on potato plants, helping to protect the foliage and tubers. Adhere to the proper composition of the ingredients, rates, and timings for optimal control of early blight and to safeguard the yield of potato crops."
            ]
        },
        "Late Blight": {
            "keywords": ["potato06", "potato07", "potato08", "potato09", "potato10"],
            "recommendations": [
                "For treating potato late blight, utilize fungicides containing active ingredients such as chlorothalonil, mancozeb, or metalaxyl. These fungicides are effective in managing late blight by controlling the spread of the fungal pathogen responsible for the disease. Follow the proper composition of the ingredients, rates, and timings to mitigate the impact of late blight and safeguard potato yields."
            ]
        },
    }

    # Placeholder for classification model
    # In a real-world scenario, you would use a trained deep learning model for classification
    # Here, we'll just assume we can determine the potato plant from the image filename
    filename = image.name.lower()
    if "potato" in filename:
        plant_species = "Potato"
    else:
        plant_species = "Unknown"

    # Get potential diseases for the detected potato plant
    diseases = []  # Placeholder for detected diseases
    if plant_species == "Potato":
        # In a real-world scenario, you would implement your disease detection logic here
        # For demonstration, let's assume we detected the disease based on some conditions
        for disease, data in potato_diseases.items():
            for keyword in data["keywords"]:
                if keyword in filename:
                    diseases.append(disease)

    recommendations = []  # Placeholder for treatment recommendations
    for disease in diseases:
        recommendations.extend(potato_diseases[disease]["recommendations"])

    # Check for healthy state
    healthy = len(diseases) == 0

    return plant_species, diseases, recommendations, healthy

def app():
    st.title("Potato Disease Classification and Treatment Recommendation")

    st.write("Please upload your potato plant image")
    uploaded_file = st.file_uploader("Upload Potato Plant Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Classify disease and provide treatment recommendations
        plant_species, diseases, recommendations, healthy = classify_and_detect_potato_disease(uploaded_file)

        # Display results
        st.write(f"Potato Plant Species: {plant_species}")
        if healthy:
            st.write("The Potato plant appears to be healthy.")
        else:
            st.write("Detected Diseases:")
            for disease in diseases:
                st.write(f"- {disease}")
            st.write("Treatment Recommendations:")
            for recommendation in recommendations:
                st.write(f"- {recommendation}")


if __name__ == "__main__":
    app()
