import streamlit as st

# Configuración
st.set_page_config(page_title="Sugerencia de Sanciones - Colegio Manquemávida", page_icon="⚖️")
st.title("⚖️ Colegio Manquemávida Sistema de Sugerencia de Sanciones")
st.markdown("Este sistema ayuda a identificar la gravedad de una falta cometida por un estudiante y sugiere una sanción proporcional a partir de IA basada en el **Reglamento Interno del Colegio Manquemávida**.")

# Reglamento: lista de (palabra clave, falta, sanción, nivel)
reglamento = [
    # FALTAS LEVES
    ("atraso", "Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Art. 282. Numeral 1 y 2 : Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("Atraso", "Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Art. 282. Numeral 1 y 2 : Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("atrasado", "Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Art. 282. Numeral 1 y 2 : Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("Atrasado", "Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Art. 282. Numeral 1 y 2 : Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("se queda", "Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Art. 282. Numeral 1 y 2 : Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("uniforme", "Presentarse sin uniforme completo o materiales solicitados", "Art. 282. Numeral 3: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("firmado", "No presentar firmadas por el apoderado las circulares o documentos que lo requieran.", "Art. 282. Numeral 4: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("tarea", "No cumplir con deberes, tareas o compromisos", "Art. 282. Numeral 5: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("trabaja", "No trabajar en clases", "Art. 282. Numeral 6: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("trabajar", "No trabajar en clases", "Art. 282. Numeral 6: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("deambula", "Deambular por el establecimiento sin justificación", "Art. 282. Numeral 7: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("deambular", "Deambular por el establecimiento sin justificación", "Art. 282. Numeral 7: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("garabatos", "Uso inadecuado del vocabulario trivial (groserías e insolencias). ", "Art. 282. Numeral 8: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("garabato", "Uso inadecuado del vocabulario trivial (groserías e insolencias). ", "Art. 282. Numeral 8: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("insolente", "Uso inadecuado del vocabulario trivial (groserías e insolencias). ", "Art. 282. Numeral 8: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("insolencia", "Uso inadecuado del vocabulario trivial (groserías e insolencias). ", "Art. 282. Numeral 8: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("insolencias", "Uso inadecuado del vocabulario trivial (groserías e insolencias). ", "Art. 282. Numeral 8: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("inasistencia", "No justificar oportunamente por parte del apoderado su inasistencia a clases u otras actividades programadas por el Colegio. . ", "Art. 282. Numeral 9: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("inasistencias", "No justificar oportunamente por parte del apoderado su inasistencia a clases u otras actividades programadas por el Colegio. . ", "Art. 282. Numeral 9: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("justifica inasistencia", "No justificar oportunamente por parte del apoderado su inasistencia a clases u otras actividades programadas por el Colegio. . ", "Art. 282. Numeral 9: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("aseo personal", "Despreocupación, manifiesta en el aseo, en la presentación personal o en otros elementos de trabajo. ", "Art. 282. Numeral 10: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("presentación personal", "Despreocupación, manifiesta en el aseo, en la presentación personal o en otros elementos de trabajo. ", "Art. 282. Numeral 10: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("vender", "Comercializar o vender algún producto al interior del establecimiento. ", "Art. 282. Numeral 11: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("vendiendo", "Comercializar o vender algún producto al interior del establecimiento. ", "Art. 282. Numeral 11: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("celular", "Usar celular sin autorización", "Amonestación escrita", "Grave"),
    ("copiar", "Copiar en una evaluación", "Suspensión", "Gravísima"),
    ("copiaando", "Copiar en una evaluación", "Suspensión", "Gravísima"),
    ("agresión", "Agresión física, verbal o psicológica", "Suspensión o expulsión", "Gravísima"),
    ("agrede", "Agresión física, verbal o psicológica", "Suspensión o expulsión", "Gravísima"),
    ("agredió", "Agresión física, verbal o psicológica", "Suspensión o expulsión", "Gravísima"),
    ("cimarra", "Hacer cimarra (salir de casa y no ir al colegio)", "Suspensión", "Gravísima"),
    ("plagio", "Presentar trabajos plagiados o usando IA para engañar", "Suspensión", "Gravísima"),
    ("insulto", "Insultos, garabatos o amenazas", "Suspensión o expulsión", "Gravísima"),
    ("daño", "Dañar infraestructura o materiales", "Amonestación escrita o suspensión", "Grave"),
    ("reiteración", "Reiteración de faltas", "Agravante: leve → grave, grave → gravísima", "Variable"),
    ("fumar", "Fumar en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("fumando", "Fumar en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("alcohol", "Beber en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("bebiendo", "Beber en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("tomando", "Beber en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("fumar", "Fumar en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("desobedecer", "Desobedecer órdenes de autoridad", "Amonestación escrita", "Grave"),
    ("hurto", "Hurto de bienes", "Suspensión o expulsión", "Gravísima"),
    ("robo", "robo de bienes", "Suspensión o expulsión", "Gravísima"),
    ("discriminación", "Discriminar a un integrante de la comunidad", "Suspensión o expulsión", "Gravísima"),
]

# Entrada del usuario
st.subheader("Describe la falta cometida:")
falta_usuario = st.text_input("Ejemplo: 'Alumno copia en una prueba y usa IA para hacer una tarea'")

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
