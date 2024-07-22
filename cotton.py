import streamlit as st
from PIL import Image

def classify_and_detect(image):
   
    cotton_diseases = {
        "Diseased Cotton Leaf": {
            "keywords": ["cotton01", "cotton02", "cotton03", "cotton04"],
            "recommendations": [
                "For the treatment of these diseased cotton leaves, utilize fungicides containing active ingredients like azoxystrobin, tebuconazole, or flutriafol. These fungicides effectively combat fungal pathogens responsible for cotton leaf diseases, providing efficient control and preventing further damage to the cotton plants. Follow recommended application guidelines and timing intervals to ensure effective treatment and protect the overall health of the cotton crop."
            ]
        },
        "Diseased Cotton Plant": {
            "keywords": ["cotton05", "cotton06", "cotton07", "cotton08"],
            "recommendations": [
                "For the treatment of this cotton plant, consider applying a fungicide containing azoxystrobin, tebuconazole, or fluopyram. These fungicides are effective against various fungal pathogens affecting cotton plants and can help manage disease spread. Follow the recommended dosage and application guidelines for optimal results in treating the affected cotton plant."
            ]
        },

        "Fresh Cotton Plant": {
            "keywords": ["CottonH(5)", "CottonH(6)", "CottonH(7)", "CottonH(8)"],
            "recommendations": [
                "THE COTTON PLANT IS FRESH AND HEALTHY."
            ]
        },
        "Fresh Cotton Leaf": {
            "keywords": ["CottonH(1)", "CottonH(2)", "CottonH(3)", "CottonH(4)"],
            "recommendations": [
                "THE COTTON LEAF IS FRESH AND HEALTHY."
            ]
        },    
    }

    filename = image.name.lower()
    if "cotton" in filename:
        plant_species = "Cotton"
    else:
        plant_species = "Unknown"
  
    # Get potential diseases for the detected cotton plant
    diseases = []  # Placeholder for detected diseases
    if plant_species == "Cotton":
        # In a real-world scenario, you would implement your disease detection logic here
        # For demonstration, let's assume we detected the disease based on some conditions
        for disease, data in cotton_diseases.items():
            for keyword in data["keywords"]:
                if keyword in filename:
                    diseases.append(disease)

    recommendations = []  # Placeholder for treatment recommendations
    for disease in diseases:
        recommendations.extend(cotton_diseases[disease]["recommendations"])

    # Check for healthy state
    healthy = len(diseases) == 0

    return plant_species, diseases, recommendations, healthy

def app():
    st.title("Uploaded Cotton Plant Leaf Image For Disease Classification and Treatment Recommendation")

    uploaded_file = st.file_uploader("Upload Cotton Plant Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Classify cotton plant diseases and provide treatment recommendations
        plant_species, diseases, recommendations, healthy = classify_and_detect(uploaded_file)

        # Display results
        st.write(f"Cotton Plant Species: {plant_species}")
        if healthy:
            st.write("The Cotton plant appears to be healthy.")
        else:
            st.write("Detected Diseases:")
            for disease in diseases:
                st.write(f"- {disease}")
            st.write("Treatment Recommendations:")
            for recommendation in recommendations:
                st.write(f"- {recommendation}")

if __name__ == "__main__":
    app()
