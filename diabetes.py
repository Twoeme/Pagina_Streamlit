from turtle import width
from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

#icono de página
icono = Image.open("Icono_diabetes.png")

##Configurar nombre de pagina
st.set_page_config(page_title="Mi APP_Diabetes", page_icon=icono, layout="wide")

##Agregar titulo y descripcion
st.sidebar.header("Información general")
st.markdown("<h1 style='color:blue;'>Predicción de la Diabetes</h1>", unsafe_allow_html=True)
st.write("La diabetes es una condición crónica que afecta la forma en que el cuerpo utiliza la glucosa, su principal fuente de energía. Existen diferentes tipos de diabetes, y cada uno requiere cuidados especiales para mantener una buena calidad de vida. El objetivo de esta página es brindar información básica, fomentar la conciencia sobre la importancia de la prevención y promover hábitos saludables que ayuden a controlar la enfermedad.")

## Separador visual
###
st.header("Objetivos")

st.write("""- Analizar factores de riesgo asociados a la diabetes.
- Identificar patrones en variables como edad, glucosa y BMI.
- Visualizar tendencias y distribución de los datos.
""")
##Seccion de genero de los pacientes

def main():
        st.sidebar.header("Genero de los pacientes")
    
    #cargar dataset
df = pd.read_csv('diabetes_risk_dataset.csv')
st.dataframe(df)

df_cuenta = df.groupby('gender').count().reset_index()
fig = px.pie(df_cuenta, names='gender', values='Patient_ID', title='Distribución de Género de los Pacientes')
st.plotly_chart(fig, width=800)


df_avg = df.groupby('diabetes_risk_category')['age'].mean().reset_index()
fig = px.bar(df_avg, x='diabetes_risk_category', y='age', title='Edad Promedio por Categoría de Riesgo de Diabetes')
st.plotly_chart(fig, width=800)


 ### Grafico de sidebar
##st.sidebar.plotly_chart(fig, width=800)



diabetes = pd.read_csv("diabetes_risk_dataset.csv")

edad_promedio = df.groupby('diabetes_risk_category')['age'].mean()

plt.figure(figsize=(10,5))
plt.bar(edad_promedio.index, edad_promedio.values)

plt.title("Edad promedio según categoría de riesgo de diabetes")
plt.xlabel("Categoría de riesgo")
plt.ylabel("Edad promedio")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

diabetes.columns = diabetes.columns.str.strip()
diabetes.rename(columns={'age': 'Año', 'gender': 'Genero', 'bmi': 'IMC', 'blood_pressure': 'Presión Arterial', 'fasting_glucose_level': 'Glucosa en ayunas', 'insulin_level': 'Nivel de insulina', 'HbA1c_level': 'Nivel de insulina Glicosilada', 'cholesterol_level': 'Nivel de colesterol', 'triglycerides_level': 'Nivel de trigliceridos', 'physical_activity_level': 'Nivel de actividad fisica', 'daily_calorie_intake': 'Ingesta diaria de caloria', 'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia', 'sleep_hours': 'Horas de sueño', 'stress_level':'Nivel de estres', 'family_history_diabetes': 'Historial Familiar', 'waist_circumference_cm': 'Circunferencia de cintura cm', 'diabetes_risk_score': 'Puntuacion de riesgo', 'diabetes_risk_category': 'Categoria de riesgo'}, inplace=True)
print(diabetes.columns)

diabetes.info()

columns = ['Año', 'Genero', 'IMC', 'Presión Arterial', 'Glucosa en ayunas', 'Nivel de insulina Glicosilada', 'Nivel de insulina', 'Nivel de colesterol', 'Nivel de trigliceridos', 'Ingesta diaria de caloria', 'Ingesta de azucar g/dia', 'Horas de sueño', 'Nivel de estres', 'Circunferencia de cintura cm', 'Historial Familiar', 'Puntuacion de riesgo']
print("---Reporte de valores en cero ---")
for column in columns:
   print(column, "valores en 0: ", (diabetes[column] == 0).sum())



## Placeholder for prediction result
st.success("Prediction result will be displayed here.")
if __name__ == "__main__":
 main()


## insertar imagen
img = Image.open("pexels-diabetes.jpg")
st.image(img, width=800)
### st.image("https://picsun.photos/800")


with open("ReflexivoDiabetes.mp4", "rb") as video_file:
    st.video(video_file.read(), start_time=0)


    # Input fields for user data
st.write("Para predecir su diabetes, seleccione las siguintes preguntas.")

embarazos = st.number_input("Numero de embarazos", min_value=0, max_value=20, value=0)
glucosa = st.number_input("Nivel de glucosa", min_value=0, max_value=200, value=0)
presion_arterial = st.number_input("Presión arterial", min_value=0, max_value=150, value=0)
skin_thickness = st.number_input("Grosor de la piel", min_value=0, max_value=100, value=0)
insulina = st.number_input("Nivel de insulina", min_value=0, max_value=900, value=0)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=0.0)
diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.0)
edad = st.number_input("Edad", min_value=1, max_value=120, value=1)

    # Button to trigger prediction
if st.button("Predict"):
        # Here you would typically load your trained model and make a prediction
        # For demonstration purposes, we'll just display the input values
        st.write(f"Pregnancies: {embarazos}")
        st.write(f"Glucose Level: {glucosa}")
        st.write(f"Blood Pressure: {presion_arterial}")
        st.write(f"Skin Thickness: {skin_thickness}")
        st.write(f"Insulin Level: {insulina}")
        st.write(f"BMI: {bmi}")
        st.write(f"Diabetes Pedigree Function: {diabetes_pedigree_function}")
        st.write(f"Edad: {edad}")
 # Placeholder for prediction result

edad = st.slider("Seleccina tu edad", min_value=1, max_value=120, value=1,step=1)
st.write(f"Tu edad es: {edad}")

