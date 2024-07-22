import streamlit as st
from PIL import Image

# Function to classify corn plant diseases and provide treatment recommendations
def classify_and_detect_corn_disease(image):
    # Placeholder function for classification and disease detection of corn plants
    # For demonstration purposes, let's assume we have a dictionary mapping corn diseases to treatment recommendations
    corn_diseases = {
        "Common Rust": {
            "keywords": ["corn01", "corn02", "corn03", "corn04", "corn05"],
            "recommendations": [
                "For treating common rust in corn, consider using fungicides such as azoxystrobin, propiconazole, or pyraclostrobin. These fungicides are effective in controlling common rust by inhibiting the growth and spread of fungal spores on corn leaves. Adhere to recommended application rates and timings for optimal results in managing common rust in corn crops."
            ]
        },
        "Northern Corn Leaf Blight": {
            "keywords": ["corn11", "corn12", "corn13", "corn14", "corn15"],
            "recommendations": [
                "For treating northern leaf blight in corn, consider using fungicides containing active ingredients such as azoxystrobin, propiconazole, or pyraclostrobin. These fungicides are effective in managing northern leaf blight by suppressing the growth and spread of the fungal pathogen responsible for the disease. Adhere to recommended application rates and timings for optimal control of northern leaf blight in corn crops."
            ]
        },
        "Leaf Spot Grey Leaf Spot": {
            "keywords": ["corn06", "corn07", "corn08", "corn09", "corn10"],
            "recommendations": [
                "For treating grey leaf spot in corn, fungicides containing active ingredients like azoxystrobin, pyraclostrobin, or trifloxystrobin are recommended. These fungicides effectively suppress grey leaf spot by targeting the fungal pathogen responsible for the disease. Follow the recommended application rates and timing intervals specified by agricultural experts or the fungicide manufacturer to mitigate the impact of grey leaf spot on corn crops."
            ]
        },    
    }

    filename = image.name.lower()
    if "corn" in filename:
        plant_species = "Corn"
    else:
        plant_species = "Unknown"
  
    # Get potential diseases for the detected corn plant
    diseases = []  # Placeholder for detected diseases
    if plant_species == "Corn":
        # In a real-world scenario, you would implement your disease detection logic here
        # For demonstration, let's assume we detected the disease based on some conditions
        for disease, data in corn_diseases.items():
            for keyword in data["keywords"]:
                if keyword in filename:
                    diseases.append(disease)

    recommendations = []  # Placeholder for treatment recommendations
    for disease in diseases:
        recommendations.extend(corn_diseases[disease]["recommendations"])

    # Check for healthy state
    healthy = len(diseases) == 0

    return plant_species, diseases, recommendations, healthy

def app():
    st.title("Uploaded Corn Plant Leaf Image For Disease Classification and Treatment Recommendation")

    uploaded_file = st.file_uploader("Upload Corn Plant Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Classify corn plant diseases and provide treatment recommendations
        plant_species, diseases, recommendations, healthy = classify_and_detect_corn_disease(uploaded_file)

        # Display results
        st.write(f"Corn Plant Species: {plant_species}")
        if healthy:
            st.write("The Corn plant appears to be healthy.")
        else:
            st.write("Detected Diseases:")
            for disease in diseases:
                st.write(f"- {disease}")
            st.write("Treatment Recommendations:")
            for recommendation in recommendations:
                st.write(f"- {recommendation}")

if __name__ == "__main__":
    app()
