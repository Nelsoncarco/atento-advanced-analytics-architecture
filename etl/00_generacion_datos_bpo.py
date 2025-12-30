import pandas as pd
import numpy as np
import os

# -----------------------------
# Configuración general
# -----------------------------
np.random.seed(42)

N_INTERACCIONES = 1000   # Escalable a volumen real BPO
N_CLIENTES = 200
N_AGENTES = 50

# Crear carpetas si no existen
os.makedirs('data/raw', exist_ok=True)

# -----------------------------
# Interacciones BPO
# -----------------------------
interacciones = pd.DataFrame({
    'interaccion_id': range(1, N_INTERACCIONES + 1),
    'fecha': pd.date_range(
        start='2024-01-01',
        periods=N_INTERACCIONES,
        freq='h'
    ),
    'canal': np.random.choice(
        ['Llamada', 'Chat', 'Email'],
        N_INTERACCIONES,
        p=[0.6, 0.25, 0.15]  # Canales típicos BPO
    ),
    'duracion_seg': np.random.randint(60, 900, N_INTERACCIONES),
    'cliente_id': np.random.randint(1, N_CLIENTES + 1, N_INTERACCIONES),
    'sentimiento': np.random.choice(
        ['Positivo', 'Neutro', 'Negativo'],
        N_INTERACCIONES,
        p=[0.4, 0.4, 0.2]
    )
})

# -----------------------------
# Clientes
# -----------------------------
clientes = pd.DataFrame({
    'cliente_id': range(1, N_CLIENTES + 1),
    'segmento': np.random.choice(
        ['Premium', 'Standard'],
        N_CLIENTES,
        p=[0.3, 0.7]
    ),
    'antiguedad_meses': np.random.randint(1, 60, N_CLIENTES),
    'churn': np.random.choice(
        [0, 1],
        N_CLIENTES,
        p=[0.8, 0.2]
    )
})

# -----------------------------
# Agentes
# -----------------------------
agentes = pd.DataFrame({
    'agente_id': range(1, N_AGENTES + 1),
    'skill': np.random.choice(['Soporte', 'Ventas'], N_AGENTES),
    'turno': np.random.choice(['Mañana', 'Tarde'], N_AGENTES),
    'antiguedad_meses': np.random.randint(1, 48, N_AGENTES)
})

# -----------------------------
# Guardado de datos
# -----------------------------
interacciones.to_csv('data/raw/interacciones.csv', index=False)
clientes.to_csv('data/raw/clientes.csv', index=False)
agentes.to_csv('data/raw/agentes.csv', index=False)

print("✅ Datos BPO simulados generados correctamente en data/raw/")

