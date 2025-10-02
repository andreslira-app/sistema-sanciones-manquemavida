import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np

# Descargar recursos de NLTK (solo una vez)
@st.cache_resource
def download_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)

download_nltk()

# Título
st.set_page_config(page_title="Sugerencia de Sanciones - Colegio Manquemávida", page_icon="⚖️")
st.title("⚖️ Sistema de Sugerencia de Sanciones")
st.markdown("""
Este sistema ayuda a identificar la gravedad de una falta cometida por un estudiante 
y sugiere una sanción proporcional según el **Reglamento Interno del Colegio Manquemávida**.
""")

# Reglamento (mismo que antes)
reglamento = [
    # FALTAS LEVES
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

    # FALTAS GRAVES
    ("Reiteración de una falta leve (al menos 3 veces)", "Amonestación escrita o advertencia de condicionalidad", "Grave"),
    ("Incumplir carta de compromiso", "Amonestación escrita", "Grave"),
    ("Cimarra interna (esconderse en el colegio)", "Amonestación escrita", "Grave"),
    ("Conducta irrespetuosa o insolente con profesores o compañeros", "Amonestación escrita", "Grave"),
    ("Presentar trabajo ajeno como propio", "Amonestación escrita", "Grave"),
    ("Fumar en el colegio o con uniforme institucional", "Amonestación escrita", "Grave"),
    ("Desobedecer órdenes de autoridad", "Amonestación escrita", "Grave"),
    ("Dañar infraestructura o materiales", "Amonestación escrita", "Grave"),
    ("Provocar peleas o desórdenes", "Amonestación escrita", "Grave"),
    ("Usar celular sin autorización o en espacios internos", "Amonestación escrita", "Grave"),
    ("Manifestaciones de afecto inapropiadas", "Amonestación escrita", "Grave"),
    ("Alterar el clima escolar o interrumpir la clase", "Amonestación escrita", "Grave"),
    ("Engañar, mentir, burlarse o faltar el respeto", "Amonestación escrita", "Grave"),
    ("Usar lenguaje inadecuado", "Amonestación escrita", "Grave"),
    ("Portar/consumir bebidas energéticas", "Amonestación escrita", "Grave"),

    # FALTAS GRAVÍSIMAS
    ("Reiteración de faltas graves", "Advertencia de condicionalidad, condicionalidad de matrícula o expulsión", "Gravísima"),
    ("Agresión física, verbal, psicológica o sexual", "Suspensión, condicionalidad o expulsión", "Gravísima"),
    ("Insultos, garabatos, amenazas, hostigamiento, acoso", "Suspensión o expulsión", "Gravísima"),
    ("Discriminación por cualquier motivo", "Suspensión o expulsión", "Gravísima"),
    ("Hurto de bienes", "Suspensión o expulsión", "Gravísima"),
    ("Hacer cimarra (salir de casa y no ir al colegio)", "Suspensión", "Gravísima"),
    ("Adulterar documentos, firmas o notas", "Suspensión o expulsión", "Gravísima"),
    ("Copiar en evaluaciones o mostrar respuestas", "Suspensión", "Gravísima"),
    ("Plagio o uso de IA para engañar", "Suspensión", "Gravísima"),
    ("Destruir bienes intencionalmente", "Suspensión o expulsión", "Gravísima"),
    ("Portar armas o objetos cortantes no autorizados", "Expulsión inmediata", "Gravísima"),
    ("Presentarse bajo efecto de alcohol o drogas", "Suspensión o expulsión", "Gravísima"),
    ("Difamar, calumniar o exhibir situaciones que afecten la honra", "Suspensión o expulsión", "Gravísima"),
    ("Acoso cibernético o presencial", "Suspensión o expulsión", "Gravísima"),
    ("Falsificar firma del apoderado", "Suspensión", "Gravísima"),
    ("Retirarse sin autorización", "Suspensión", "Gravísima"),
    ("No entregar una prueba", "Suspensión", "Gravísima"),
]

faltas = [item[0] for item in reglamento]
sanciones = [item[1] for item in reglamento]
niveles = [item[2] for item in reglamento]

# Entrada del usuario
st.subheader("Describe la falta cometida:")
falta_usuario = st.text_area("Ejemplo: 'Copió en una prueba y usó IA para hacer una tarea'", height=100)

if st.button("🔍 Sugerir sanción"):
    if not falta_usuario.strip():
        st.warning("Por favor, describe la falta.")
    else:
        with st.spinner("Analizando la falta según el reglamento..."):
            # Combinar la falta del usuario con las faltas del reglamento
            textos = [falta_usuario] + faltas

            # Vectorizar con TF-IDF
            vectorizer = TfidfVectorizer(stop_words='spanish')
            tfidf_matrix = vectorizer.fit_transform(textos)

            # Calcular similitud coseno entre la falta del usuario y cada falta del reglamento
            similitudes = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
            idx_mejor = np.argmax(similitudes)

            falta_detectada = faltas[idx_mejor]
            sancion_sugerida = sanciones[idx_mejor]
            nivel = niveles[idx_mejor]

        # Mostrar resultado
        st.success(f"✅ **Falta más parecida detectada**: {falta_detectada}")
        
        if nivel == "Leve":
            st.info(f"🔹 **Nivel**: {nivel}")
            st.info(f"⚖️ **Sanción sugerida**: {sancion_sugerida}")
        elif nivel == "Grave":
            st.warning(f"🔸 **Nivel**: {nivel}")
            st.warning(f"⚖️ **Sanción sugerida**: {sancion_sugerida}")
        else:
            st.error(f"🔴 **Nivel**: {nivel}")
            st.error(f"⚖️ **Sanción sugerida**: {sancion_sugerida}")

        st.markdown("""
        ---
        ℹ️ **Nota**: Esta sugerencia se basa en el **principio de proporcionalidad** del reglamento. 
        Siempre debe aplicarse en conjunto con el análisis de **atenuantes y agravantes**.
        """)

st.caption("Sistema basado en el Reglamento Interno del Colegio Manquemávida. Uso exclusivo para apoyo formativo.")
