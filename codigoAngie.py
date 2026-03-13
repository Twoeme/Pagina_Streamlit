import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = "diabetes_risk_dataset.csv"
diabetes = pd.read_csv(url)
print(diabetes.head())


diabetes.columns = diabetes.columns.str.strip()
diabetes.rename(columns={'age': 'Año', 'gender': 'Genero', 'bmi': 'IMC', 'blood_pressure': 'Presión Arterial', 'fasting_glucose_level': 'Glucosa en ayunas', 'insulin_level': 'Nivel de insulina', 'HbA1c_level': 'Nivel de insulina Glicosilada', 'cholesterol_level': 'Nivel de colesterol', 'triglycerides_level': 'Nivel de trigliceridos', 'physical_activity_level': 'Nivel de actividad fisica', 'daily_calorie_intake': 'Ingesta diaria de caloria', 'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia', 'sleep_hours': 'Horas de sueño', 'stress_level':'Nivel de estres', 'family_history_diabetes': 'Historial Familiar', 'waist_circumference_cm': 'Circunferencia de cintura cm', 'diabetes_risk_score': 'Puntuacion de riesgo', 'diabetes_risk_category': 'Categoria de riesgo'}, inplace=True)
print(diabetes.columns)

diabetes.info()

diabetes.dropna()

diabetes.describe()

columns = ['Año', 'Genero', 'IMC', 'Presión Arterial', 'Glucosa en ayunas', 'Nivel de insulina Glicosilada', 'Nivel de insulina', 'Nivel de colesterol', 'Nivel de trigliceridos', 'Ingesta diaria de caloria', 'Ingesta de azucar g/dia', 'Horas de sueño', 'Nivel de estres', 'Circunferencia de cintura cm', 'Historial Familiar', 'Puntuacion de riesgo']
print("---Reporte de valores en cero ---")
for column in columns:
    print(column, "valores en 0: ", (diabetes[column] == 0).sum())

diabetes[column] = diabetes[column].replace(0, np.nan)

correlacion = diabetes.corr(numeric_only=True)
print(correlacion["Puntuacion de riesgo"].sort_values(ascending=False))

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))

sns.regplot(data=diabetes, 
            x="IMC", 
            y="Puntuacion de riesgo", 
            scatter_kws={'alpha':0.5}, 
            line_kws={'color':'red'})

plt.title("Relación Médica: IMC vs Puntuación de Riesgo", fontsize=14)
plt.show()



diabetes.isnull().sum()



plt.figure(figsize=(12, 8))

sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Mapa de Calor: Factores de Riesgo de Diabetes", fontsize=15)
plt.show()

