import streamlit as st
import difflib

# Configuración de la página
st.set_page_config(page_title="Sugerencia de Sanciones - Colegio Manquemávida", page_icon="⚖️")

# Título
st.title("⚖️ Sistema de Sugerencia de Sanciones")
st.markdown("""
Este sistema ayuda a identificar la gravedad de una falta cometida por un estudiante 
y sugiere una sanción proporcional según el **Reglamento Interno del Colegio Manquemávida**.
""")

# Reglamento estructurado: (descripción, sanción sugerida, nivel)
reglamento = [
    # FALTAS LEVES (Art. 282)
    ("Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("Quedarse fuera de la sala después del timbre", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("Presentarse sin uniforme completo o materiales solicitados", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("No presentar circulares firmadas por el apoderado", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("No cumplir con deberes, tareas o compromisos", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("No trabajar en clases", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("Deambular por el establecimiento sin justificación", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("Uso inadecuado de vocabulario (groserías, insolencias)", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("No justificar inasistencia", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("Despreocupación en aseo o presentación personal", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("Comercializar o vender productos en el colegio", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("No portar agenda escolar o materiales requeridos", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("Recurrir a excusas para no enfrentar responsabilidades", "Medidas de apoyo pedagógico o psicosocial", "Leve"),

    # FALTAS GRAVES (Art. 287)
    ("Reiteración de una falta leve (al menos 3 veces)", "Amonestación escrita o advertencia de condicionalidad", "Grave"),
    ("Incumplir carta de compromiso", "Amonestación escrita", "Grave"),
    ("Cimarra interna (esconderse en el colegio)", "Amonestación escrita", "Grave"),
    ("Conducta irrespetuosa o insolente con profesores o compañeros", "Amonestación escrita", "Grave"),
    ("Presentar trabajo ajeno como propio", "Amonestación escrita", "Grave"),
    ("Fumar en el colegio o con uniforme institucional", "Amonestación escrita", "Grave"),
    ("Desobedecer órdenes de autoridad", "Amonestación escrita", "Grave"),
    ("Dañar infraestructura o materiales", "Amonestación escrita", "Grave"),
    ("Provocar peleas o desórdenes", "Amonestación escrita", "Grave"),
    ("Usar celular
