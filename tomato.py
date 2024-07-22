import streamlit as st
from PIL import Image

# Function to classify tomato plant diseases and provide treatment recommendations
def classify_and_detect_tomato_disease(image):
    # Placeholder function for classification and disease detection of tomato plants
    # For demonstration purposes, let's assume we have a dictionary mapping tomato diseases to treatment recommendations
    tomato_diseases = {
        "Late Blight": { "keywords": ["tomato15", "tomato16", "tomato17", "tomato18", "tomato19", "tomato20", "tomato21", "tomato22"],
                         "recommendations": ["To treat tomato late blight, use fungicides containing active ingredients such as chlorothalonil, mancozeb, or metalaxyl. These fungicides are effective in managing late blight by controlling the spread of the fungal pathogen responsible for the disease. Follow the proper composition of the ingredients, rates, and timings to mitigate the impact of late blight and safeguard tomato yields."]},
        "Leaf Mold":  { "keywords": ["tomato23", "tomato24", "tomato25", "tomato26", "tomato27", "tomato28"],
                        "recommendations": ["To treat tomato leaf mold, apply fungicides containing active ingredients like chlorothalonil, mancozeb, or copper-based compounds. These fungicides effectively suppress the growth and spread of the fungal pathogen causing leaf mold on tomato plants Adhere to the proper composition of the ingredients, rates, and timings to ensure effective control and protect tomato foliage from further damage."]},
        "Mosaic Virus": { "keywords": ["tomato29", "tomato30", "tomato31", "tomato32", "tomato33", "tomato34", "tomato35"],
                          "recommendations": ["There are no specific pesticides or fungicides that can effectively treat the tomato mosaic virus. Since it is a viral disease, management strategies focus on prevention, including using disease-resistant tomato varieties, practicing good sanitation, and controlling aphid populations to reduce virus transmission. Once plants are infected, it's essential to remove and destroy affected plants promptly to prevent further spread of the virus to healthy plants."]},
        "Bacterial Spot": { "keywords": ["tomato01", "tomato02", "tomato03", "tomato04", "tomato05", "tomato06", "tomato07", "tomato08"],
                            "recommendations": ["For treating tomato bacterial spots, apply copper-based fungicides or bactericides such as copper hydroxide or copper sulfate. These products effectively reduce bacterial populations on tomato plants and inhibit the spread of the disease Adhere to the proper composition of the ingredients, rates, and timings to achieve optimal control of bacterial spots and protect tomato yields."]},
        "Early Blight": { "keywords": ["tomato09", "tomato10", "tomato11", "tomato12", "tomato13", "tomato14"],
                          "recommendations": ["To treat tomato early blight, consider using fungicides containing active ingredients like chlorothalonil, mancozeb, or azoxystrobin. These fungicides effectively suppress the development and spread of early blight on tomato plants, helping to protect foliage and ensure healthy fruit production. Adhere to the proper composition of the ingredients, rates, and timings for optimal control of early blight and to maintain tomato yield."]}
    }

    # Placeholder for classification model
    # In a real-world scenario, you would use a trained deep learning model for classification
    # Here, we'll just assume we can determine the tomato plant from the image filename
    filename = image.name.lower()
    if "tomato" in filename:
        plant_species = "Tomato"
    else:
        plant_species = "Unknown"

    # Get potential diseases for the detected tomato plant
    diseases = []  # Placeholder for detected diseases
    if plant_species == "Tomato":
        # In a real-world scenario, you would implement your disease detection logic here
        # For demonstration, let's assume we detected the disease based on some conditions
        for disease, data in tomato_diseases.items():
            for keyword in data["keywords"]:
                if keyword in filename:
                    diseases.append(disease)

    recommendations = []  # Placeholder for treatment recommendations
    for disease in diseases:
        recommendations.extend(tomato_diseases[disease]["recommendations"])

    # Check for healthy state
    healthy = len(diseases) == 0

    return plant_species, diseases, recommendations, healthy

def app():
    st.title("Uploaded Tomato Plant Leaf Image For Disease Classification and Treatment Recommendation")

    uploaded_file = st.file_uploader("Upload Tomato Plant Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Classify tomato plant diseases and provide treatment recommendations
        plant_species, diseases, recommendations, healthy = classify_and_detect_tomato_disease(uploaded_file)

        # Display results
        st.write(f"Tomato Plant Species: {plant_species}")
        if healthy:
            st.write("The tomato plant appears to be healthy.")
        else:
            st.write("Detected Diseases:")
            for disease in diseases:
                st.write(f"- {disease}")
            st.write("Treatment Recommendations:")
            for recommendation in recommendations:
                st.write(f"- {recommendation}")

if __name__ == "__main__":
    app()
