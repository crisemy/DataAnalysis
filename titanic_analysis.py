import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carga de datos
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
try:
    df = pd.read_csv(url)
    print("Dataset cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar el dataset: {e}")
    exit()

print(df.head(10))

# 2. Limpieza de datos
# Manejar valores faltantes
df['Age'] = df['Age'].fillna(df['Age'].median())
df = df.dropna(subset=['Embarked'])
df = df.drop(columns=['Cabin', 'Ticket'], errors='ignore')  # Ignorar si columnas no existen
df['Sex'] = df['Sex'].str.lower()
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# 3. Exploratory Data Analysis
print("\nEstadísticas descriptivas:")
print(df.describe())

# Seleccionar solo columnas numéricas para correlaciones
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
print("\nCorrelaciones (solo columnas numéricas):")
print(df[numeric_cols].corr())

# 4. Visualizaciones
# Supervivencia por género
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex_male', hue='Survived', data=df)
plt.title('Supervivencia por Género')
plt.savefig('survival_by_gender.png')
plt.close()

# Distribución de edad
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Distribución de Edad')
plt.savefig('age_distribution.png')
plt.close()

# Tarifas por clase
plt.figure(figsize=(8, 6))
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title('Tarifas por Clase')
plt.savefig('fare_by_class.png')
plt.close()

# 5. Guardar dataset limpio
try:
    df.to_csv('titanic_cleaned.csv', index=False)
    print("Dataset limpio guardado como 'titanic_cleaned.csv'")
except Exception as e:
    print(f"Error al guardar el dataset: {e}")