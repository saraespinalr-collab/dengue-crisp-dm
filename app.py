import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Predicción de Hospitalización por Dengue", page_icon="🦟")

modelo = joblib.load("modelo_dengue.pkl")

st.title("🦟 Apoyo analítico: riesgo de hospitalización por dengue")
st.markdown(
    "Esta aplicación es una **herramienta de apoyo analítico** basada en un modelo de "
    "Machine Learning entrenado con datos históricos de SIVIGILA. **No reemplaza el "
    "criterio médico** ni constituye un diagnóstico."
)

st.header("Datos del caso")
col1, col2 = st.columns(2)
with col1:
    edad_anios = st.number_input("Edad (años)", min_value=0, max_value=110, value=30)
    dias_sintomas = st.number_input("Días desde inicio de síntomas hasta la consulta", min_value=0, max_value=30, value=3)
    semana = st.number_input("Semana epidemiológica", min_value=1, max_value=53, value=25)
    sexo = st.selectbox("Sexo", ["M", "F"])
    tipo_ss = st.selectbox("Tipo de seguridad social", ["C", "S", "N", "E", "P", "I"])
    comuna = st.text_input("Comuna de residencia", "Belen")
    desplazamiento = st.selectbox("¿En situación de desplazamiento?", ["No", "Sí"])

with col2:
    st.markdown("**Síntomas y signos presentes**")
    fiebre = st.checkbox("Fiebre", value=True)
    cefalea = st.checkbox("Cefalea")
    dolor_retroocular = st.checkbox("Dolor retroocular")
    mialgias = st.checkbox("Mialgias")
    artralgia = st.checkbox("Artralgia")
    erupcion = st.checkbox("Erupción")
    dolor_abdominal = st.checkbox("Dolor abdominal")
    vomito = st.checkbox("Vómito")
    somnolencia = st.checkbox("Somnolencia / decaimiento")
    hipotension = st.checkbox("Hipotensión")
    hepatomegalia = st.checkbox("Hepatomegalia")
    hemorragia_mucosa = st.checkbox("Sangrado de mucosas")
    hipotermia = st.checkbox("Hipotermia")
    aumento_hematocrito = st.checkbox("Aumento del hematocrito")
    caida_plaquetas = st.checkbox("Caída de plaquetas")
    acumulacion_liquidos = st.checkbox("Acumulación de líquidos")

if st.button("Calcular riesgo de hospitalización"):
    entrada = pd.DataFrame([{
        "edad_anios": edad_anios,
        "dias_sintomas": dias_sintomas,
        "semana": semana,
        "fiebre": int(fiebre), "cefalea": int(cefalea), "dolrretroo": int(dolor_retroocular),
        "malgias": int(mialgias), "artralgia": int(artralgia), "erupcionr": int(erupcion),
        "dolor_abdo": int(dolor_abdominal), "vomito": int(vomito), "somnolenci": int(somnolencia),
        "hipotensio": int(hipotension), "hepatomeg": int(hepatomegalia), "hem_mucosa": int(hemorragia_mucosa),
        "hipotermia": int(hipotermia), "aum_hemato": int(aumento_hematocrito),
        "caida_plaq": int(caida_plaquetas), "acum_liquievento": int(acumulacion_liquidos),
        "desplazami": 1 if desplazamiento == "Sí" else 0,
        "sexo_": sexo, "tipo_ss_": tipo_ss, "comuna": comuna,
    }])

    prediccion = modelo.predict(entrada)[0]
    probabilidad = modelo.predict_proba(entrada)[0, 1]

    if prediccion == 1:
        st.error(f"**Predicción del modelo: mayor probabilidad de hospitalización** "
                 f"(probabilidad estimada: {probabilidad:.1%})")
    else:
        st.success(f"**Predicción del modelo: menor probabilidad de hospitalización** "
                   f"(probabilidad estimada: {probabilidad:.1%})")

    st.caption(
        "Esta salida es una predicción estadística de apoyo analítico y epidemiológico, "
        "no un diagnóstico médico. Toda decisión clínica debe ser tomada por personal de salud calificado."
    )
