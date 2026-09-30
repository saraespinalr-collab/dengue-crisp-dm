# Predicción de Hospitalización por Dengue (Proyecto Integrador CRISP-DM)

Aplicación de apoyo analítico que estima la probabilidad de que un caso de dengue
requiera hospitalización, entrenada con datos de SIVIGILA siguiendo la metodología CRISP-DM.

## Contenido del repositorio
- `app.py`: aplicación Streamlit.
- `modelo_dengue.pkl`: pipeline completo serializado (preprocesamiento + modelo).
- `requirements.txt`: dependencias.
- Notebook de Google Colab con las 6 fases de CRISP-DM: [Completar con enlace de Colab]
- `reporte_profiling_dengue.html`: reporte exploratorio (ydata-profiling).

## Cómo ejecutar localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Despliegue en Streamlit.io
1. Subir este repositorio a GitHub (público).
2. Ingresar a https://streamlit.io/cloud y conectar el repositorio.
3. Seleccionar `app.py` como archivo principal.
4. Publicar y copiar la URL pública. [Completar con URL de Streamlit.io]

## Advertencia ética
Este modelo es una herramienta de apoyo analítico y epidemiológico. No sustituye
el criterio médico ni debe usarse como única base para decisiones clínicas.
Cualquier uso en un entorno real requiere anonimización de datos, validación
clínica y aprobación institucional.
