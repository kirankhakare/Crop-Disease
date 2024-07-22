import streamlit as st
from PIL import Image

# Function to classify pepper plant diseases and provide treatment recommendations
def classify_and_detect_pepper_disease(image):
    # Placeholder function for classification and disease detection of pepper plants
    # For demonstration purposes, let's assume we have a dictionary mapping pepper diseases to treatment recommendations
    pepper_diseases = {
        "Bacterial Spot": {
            "keywords": ["pepper01", "pepper02", "pepper03", "pepper04", "pepper05"],
            "recommendations": [
                "For treating pepper bacterial spot, consider using copper-based fungicides or bactericides such as copper hydroxide or copper sulfate. These products are effective in managing bacterial spot by reducing bacterial populations on pepper plants and preventing the spread of the disease. Apply the recommended dosage and timing as per agricultural guidelines to achieve optimal control of pepper bacterial spot."
            ]
        }
    }

    # Placeholder for classification model
    # In a real-world scenario, you would use a trained deep learning model for classification
    # Here, we'll just assume we can determine the pepper plant from the image filename
    filename = image.name.lower()
    if "pepper" in filename:
        plant_species = "Pepper"
    else:
        plant_species = "Unknown"

    # Get potential diseases for the detected pepper plant
    diseases = []  # Placeholder for detected diseases
    if plant_species == "Pepper":
        # In a real-world scenario, you would implement your disease detection logic here
        # For demonstration, let's assume we detected the disease based on some conditions
        for disease, data in pepper_diseases.items():
            for keyword in data["keywords"]:
                if keyword in filename:
                    diseases.append(disease)

    recommendations = []  # Placeholder for treatment recommendations
    for disease in diseases:
        recommendations.extend(pepper_diseases[disease]["recommendations"])

    # Check for healthy state
    healthy = len(diseases) == 0

    return plant_species, diseases, recommendations, healthy

def app():
    st.title("Uploaded Pepper Plant Leaf Image For Disease Classification and Treatment Recommendation")

    uploaded_file = st.file_uploader("Upload Pepper Plant Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Classify pepper plant diseases and provide treatment recommendations
        plant_species, diseases, recommendations, healthy = classify_and_detect_pepper_disease(uploaded_file)

        # Display results
        st.write(f"Pepper Plant Species: {plant_species}")
        if healthy:
            st.write("The pepper plant appears to be healthy.")
        elif len(diseases) > 0:
            st.write("Detected Diseases:")
            for disease in diseases:
                st.write(f"- {disease}")
            st.write("Treatment Recommendations:")
            for recommendation in recommendations:
                st.write(f"- {recommendation}")
        else:
            st.write("No diseases detected.")

if __name__ == "__main__":
    app()
