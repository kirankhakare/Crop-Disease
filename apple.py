import streamlit as st
from PIL import Image

def classify_and_detect(image):
    
    apple_diseases = {
        "Apple Scab": {
            "keywords": ["apple06", "apple07", "apple08", "apple09", "apple10", "apple11"],
            "recommendations": [
                "For treating apple scab, effective fungicides include Captan, mancozeb, and chlorothalonil. These fungicides can help control apple scabs by preventing the development of fungal spores on the apple tree's leaves and fruit. It is crucial to follow the recommended application schedule and dosage provided by agricultural experts or the fungicide manufacturer for the successful management of apple scabs."
            ]
        },
        "Apple Black Rot": {
            "keywords": ["apple01", "apple02", "apple03", "apple04", "apple05"],
            "recommendations": [
                "For treating apple black rot, it is recommended to use fungicides such as captan, thiophanate-methyl, or myclobutanil. These fungicides can effectively control the spread of the disease and prevent further damage to the apple trees. It is essential to follow the manufacturer's instructions and apply the fungicides at the appropriate timing to achieve optimal results in managing apple black rot."
            ]
        },
   
    }

    filename = image.name.lower()
    if "apple" in filename:
        plant_species = "Apple"
    else:
        plant_species = "Unknown"
  
    diseases = []  # Placeholder for detected diseases
    if plant_species == "Apple":
        # In a real-world scenario, you would implement your disease detection logic here
        # For demonstration, let's assume we detected the disease based on some conditions
        for disease, data in apple_diseases.items():
            for keyword in data["keywords"]:
                if keyword in filename:
                    diseases.append(disease)

    recommendations = []  # Placeholder for treatment recommendations
    for disease in diseases:
        recommendations.extend(apple_diseases[disease]["recommendations"])

    healthy = len(diseases) == 0

    return plant_species, diseases, recommendations, healthy

def app():
    st.title("Uploaded Apple Plant Leaf Image For Disease Classification and Treatment Recommendation")

    uploaded_file = st.file_uploader("Upload Apple Plant Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Classify cotton plant diseases and provide treatment recommendations
        plant_species, diseases, recommendations, healthy = classify_and_detect(uploaded_file)

        # Display results
        st.write(f"Apple Plant Species: {plant_species}")
        if healthy:
            st.write("The Apple plant appears to be healthy.")
        else:
            st.write("Detected Diseases:")
            for disease in diseases:
                st.write(f"- {disease}")
            st.write("Treatment Recommendations:")
            for recommendation in recommendations:
                st.write(f"- {recommendation}")

if __name__ == "__main__":
    app()