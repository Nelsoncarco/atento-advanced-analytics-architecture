import pandas as pd
import os

# ----------------------------------
# Configuración
# ----------------------------------
os.makedirs('data/processed', exist_ok=True)

# ----------------------------------
# Cargar datos crudos
# ----------------------------------
interacciones = pd.read_csv('data/raw/interacciones.csv')
clientes = pd.read_csv('data/raw/clientes.csv')
agentes = pd.read_csv('data/raw/agentes.csv')

# ----------------------------------
# Limpieza y validación de interacciones
# ----------------------------------
# Fechas
interacciones['fecha'] = pd.to_datetime(interacciones['fecha'], errors='coerce')

# Duración
interacciones = interacciones[(interacciones['duracion_seg'] > 0) & (interacciones['duracion_seg'] <= 3600)]

# Sentimiento válido
interacciones = interacciones[interacciones['sentimiento'].isin(['Positivo', 'Neutro', 'Negativo'])]

# IDs válidos
interacciones = interacciones[interacciones['cliente_id'].isin(clientes['cliente_id'])]

# Métricas de calidad
print("Interacciones - nulos:\n", interacciones.isnull().sum())

# ----------------------------------
# Limpieza y validación de clientes
# ----------------------------------
clientes['antiguedad_meses'] = clientes['antiguedad_meses'].clip(lower=0)
clientes['churn'] = clientes['churn'].astype(int)
clientes = clientes[clientes['segmento'].isin(['Premium', 'Standard'])]
print("Clientes - nulos:\n", clientes.isnull().sum())

# ----------------------------------
# Limpieza y validación de agentes
# ----------------------------------
agentes['antiguedad_meses'] = agentes['antiguedad_meses'].clip(lower=0)
agentes = agentes[agentes['skill'].isin(['Soporte', 'Ventas'])]
agentes = agentes[agentes['turno'].isin(['Mañana', 'Tarde'])]
print("Agentes - nulos:\n", agentes.isnull().sum())

# ----------------------------------
# Guardar datos limpios
# ----------------------------------
interacciones.to_csv('data/processed/interacciones_clean.csv', index=False)
clientes.to_csv('data/processed/clientes_clean.csv', index=False)
agentes.to_csv('data/processed/agentes_clean.csv', index=False)

print("Datos limpios guardados en data/processed/")
