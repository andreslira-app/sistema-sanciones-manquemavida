import streamlit as st

# Configuración
st.set_page_config(page_title="Sugerencia de Sanciones - Colegio Manquemávida", page_icon="⚖️")
st.title("⚖️ Sistema de Sugerencia de Sanciones")
st.markdown("Este sistema ayuda a identificar la gravedad de una falta cometida por un estudiante y sugiere una sanción proporcional según el **Reglamento Interno del Colegio Manquemávida**.")

# Reglamento: lista de (palabra clave, falta, sanción, nivel)
reglamento = [
    # FALTAS LEVES
    ("atraso", "Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("atrasado", "Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("Retraso", "Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("uniforme", "Presentarse sin uniforme completo o materiales solicitados", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("tarea", "No cumplir con deberes, tareas o compromisos", "Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("celular", "Usar celular sin autorización", "Amonestación escrita", "Grave"),
    ("copiar", "Copiar en una evaluación", "Suspensión", "Gravísima"),
    ("copiaando", "Copiar en una evaluación", "Suspensión", "Gravísima"),
    ("agresión", "Agresión física, verbal o psicológica", "Suspensión o expulsión", "Gravísima"),
    ("agrede", "Agresión física, verbal o psicológica", "Suspensión o expulsión", "Gravísima"),
    ("agredio", "Agresión física, verbal o psicológica", "Suspensión o expulsión", "Gravísima"),
    ("cimarra", "Hacer cimarra (salir de casa y no ir al colegio)", "Suspensión", "Gravísima"),
    ("plagio", "Presentar trabajos plagiados o usando IA para engañar", "Suspensión", "Gravísima"),
    ("insulto", "Insultos, garabatos o amenazas", "Suspensión o expulsión", "Gravísima"),
    ("daño", "Dañar infraestructura o materiales", "Amonestación escrita o suspensión", "Grave"),
    ("reiteración", "Reiteración de faltas", "Agravante: leve → grave, grave → gravísima", "Variable"),
    ("fumar", "Fumar en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("fumando", "Fumar en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("Alcohol", "Beber en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("fumar", "Fumar en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("desobedecer", "Desobedecer órdenes de autoridad", "Amonestación escrita", "Grave"),
    ("hurto", "Hurto de bienes", "Suspensión o expulsión", "Gravísima"),
    ("discriminación", "Discriminar a un integrante de la comunidad", "Suspensión o expulsión", "Gravísima"),
]

# Entrada del usuario
st.subheader("Describe la falta cometida:")
falta_usuario = st.text_input("Ejemplo: 'Copió en una prueba y usó IA para hacer una tarea'")

if st.button("🔍 Sugerir sanción"):
    if not falta_usuario.strip():
        st.warning("Por favor, describe la falta.")
    else:
        falta_usuario_lower = falta_usuario.lower()
        coincidencias = []

        for palabra, desc, sancion, nivel in reglamento:
            if palabra in falta_usuario_lower:
                coincidencias.append((desc, sancion, nivel))

        if coincidencias:
            st.success("✅ **Faltas detectadas:**")
            for desc, sancion, nivel in coincidencias:
                if nivel == "Leve":
                    st.info(f"🔹 **{desc}** → **{sancion}** (Nivel: {nivel})")
                elif nivel == "Grave":
                    st.warning(f"🔸 **{desc}** → **{sancion}** (Nivel: {nivel})")
                else:
                    st.error(f"🔴 **{desc}** → **{sancion}** (Nivel: {nivel})")
        else:
            st.info("ℹ️ No se encontraron coincidencias claras. Se sugiere revisar el reglamento manualmente o usar palabras como: *copiar, atraso, celular, agresión, cimarra, plagio*, etc.")

st.caption("Sistema basado en el Reglamento Interno del Colegio Manquemávida. Uso exclusivo para apoyo formativo.")
