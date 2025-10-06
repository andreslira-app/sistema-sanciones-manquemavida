import streamlit as st

# Configuración
st.set_page_config(page_title="Sugerencia de Sanciones - Colegio Manquemávida", page_icon="⚖️")
st.title("⚖️ Colegio Manquemávida Sistema de Sugerencia de Sanciones")
st.markdown("Este sistema ayuda a identificar la gravedad de una falta cometida por un estudiante y sugiere una sanción proporcional a partir de IA basada en el **Reglamento Interno del Colegio Manquemávida**.")

# Reglamento: lista de (palabra clave, falta, sanción, nivel)
reglamento = [
    # FALTAS LEVES
    ("atras", "Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Art. 282. Numeral 1 y 2 : Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("se queda", "Atrasos en la entrada a clases, entrega de trabajos o pruebas sin justificación", "Art. 282. Numeral 1 y 2 : Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("uniforme", "Presentarse sin uniforme completo o materiales solicitados", "Art. 282. Numeral 3: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("firmado", "No presentar firmadas por el apoderado las circulares o documentos que lo requieran.", "Art. 282. Numeral 4: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("tarea", "No cumplir con deberes, tareas o compromisos", "Art. 282. Numeral 5: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("trabaj", "No trabajar en clases", "Art. 282. Numeral 6: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("deambul", "Deambular por el establecimiento sin justificación", "Art. 282. Numeral 7: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("garabat", "Uso inadecuado del vocabulario trivial (groserías e insolencias). ", "Art. 282. Numeral 8: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("insolen", "Uso inadecuado del vocabulario trivial (groserías e insolencias). ", "Art. 282. Numeral 8: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("inasistenc", "No justificar oportunamente por parte del apoderado su inasistencia a clases u otras actividades programadas por el Colegio. . ", "Art. 282. Numeral 9: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("justific", "No justificar oportunamente por parte del apoderado su inasistencia a clases u otras actividades programadas por el Colegio. . ", "Art. 282. Numeral 9: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("aseo personal", "Despreocupación, manifiesta en el aseo, en la presentación personal o en otros elementos de trabajo. ", "Art. 282. Numeral 10: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("presentación personal", "Despreocupación, manifiesta en el aseo, en la presentación personal o en otros elementos de trabajo. ", "Art. 282. Numeral 10: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("vend", "Comercializar o vender algún producto al interior del establecimiento. ", "Art. 282. Numeral 11: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("materiales", "No portar la agenda escolar institucional o cuaderno de comunicaciones, cuadernos, libros o materiales requeridos para las clases. ", "Art. 282. Numeral 12: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("excusa", "Recurrir a excusas para no enfrentar sus responsabilidades y desafíos", "Art. 282. Numeral 13: Medidas de apoyo pedagógico o psicosocial", "Leve"),
    ("celular", "Usar celular sin autorización", "Amonestación escrita", "Grave"),
    ("telefono", "Usar celular sin autorización", "Amonestación escrita", "Grave"),
    ("no entra", "No ingresar a clases, ocultándose en algún espacio del colegio. (Cimarra interna) ", "Art. 287 Numeral 3: Amonestación escrita", "Grave"),
    ("no ingres", "No ingresar a clases, ocultándose en algún espacio del colegio. (Cimarra interna) ", "Art. 287 Numeral 3: Amonestación escrita", "Grave"),
    ("irrespetuos", "Mostrar una conducta irrespetuosa o insolente con algún Profesor, Inspector, otro funcionario o compañero.", "Art. 287 Numeral 4: Amonestación escrita", "Grave"),
    ("insolente", "Mostrar una conducta irrespetuosa o insolente con algún Profesor, Inspector, otro funcionario o compañero.", "Art. 287 Numeral 4: Amonestación escrita", "Grave"),
    ("engañ", "Tratar de engañar al Profesor mostrando algún trabajo o prueba ajena como propia. ", "Art. 287 Numeral 5: Amonestación escrita", "Grave"),
    ("fuma", "Fumar en el colegio o con uniforme", "Art. 287 Numeral 6: Amonestación escrita", "Grave"),
    ("odedec", "Desobedecer a instrucciones u órdenes dadas por el Profesor, Inspector, Director u otra autoridad del Colegio. ", "Art. 287 Numeral 7: Amonestación escrita", "Grave"),
    ("ensuci", "Ensuciar, rayar, causar daños menores en infraestructura, materiales, muebles u otro elemento del Colegio, Profesores o Estudiantes. ", "Art. 287 Numeral 8: Amonestación escrita", "Grave"),
    ("ray", "Ensuciar, rayar, causar daños menores en infraestructura, materiales, muebles u otro elemento del Colegio, Profesores o Estudiantes. ", "Art. 287 Numeral 8: Amonestación escrita", "Grave"),
    ("dañ", "Ensuciar, rayar, causar daños menores en infraestructura, materiales, muebles u otro elemento del Colegio, Profesores o Estudiantes. ", "Art. 287 Numeral 8: Amonestación escrita", "Grave"),
    ("pelea", "Ensuciar, rayar, causar daños menores en infraestructura, materiales, muebles u otro elemento del Colegio, Profesores o Estudiantes. ", "Art. 287 Numeral 8: Amonestación escrita", "Grave"),
    ("dispositivo", "Utilizar dispositivos electrónicos al interior de la sala de clases sin autorización del docente y/o funcionario a cargo.", "Art. 287 Numeral 10: Amonestación escrita", "Grave"),
    ("celular", "Usar el celular en todo espacio interno del colegio. ", "Art. 287 Numeral 12: Amonestación escrita", "Grave"),
    ("agre", "Toda agresión física, verbal o sicológica, o de connotación sexual que vulnere a algún miembro de la comunidad educativa. ", "Art. 292 Numeral 2: Suspensión o expulsión", "Gravísima"),
    ("insult", "Proferir insultos o garabatos, hacer gestos groseros o amenazantes u ofender reiteradamente a cualquier miembro de la comunidad educativa. ", "Art. 292 Numeral 3: Suspensión o expulsión", "Gravísima"),
    ("garabat", "Proferir insultos o garabatos, hacer gestos groseros o amenazantes u ofender reiteradamente a cualquier miembro de la comunidad educativa. ", "Art. 292 Numeral 3: Suspensión o expulsión", "Gravísima"),
    ("groser", "Proferir insultos o garabatos, hacer gestos groseros o amenazantes u ofender reiteradamente a cualquier miembro de la comunidad educativa. ", "Art. 292 Numeral 3: Suspensión o expulsión", "Gravísima"),
    ("amenaz", "Proferir insultos o garabatos, hacer gestos groseros o amenazantes u ofender reiteradamente a cualquier miembro de la comunidad educativa. ", "Art. 292 Numeral 3: Suspensión o expulsión", "Gravísima"),
    ("ofen", "Proferir insultos o garabatos, hacer gestos groseros o amenazantes u ofender reiteradamente a cualquier miembro de la comunidad educativa. ", "Art. 292 Numeral 3: Suspensión o expulsión", "Gravísima"),

    ("copi", "Copiar en una evaluación", "Suspensión", "Gravísima"),
    

    
    ("cimarra", "Hacer cimarra (salir de casa y no ir al colegio)", "Suspensión", "Gravísima"),
    ("plagio", "Presentar trabajos plagiados o usando IA para engañar", "Suspensión", "Gravísima"),
    
    ("daño", "Dañar infraestructura o materiales", "Amonestación escrita o suspensión", "Grave"),
    ("reiteración", "Reiteración de faltas", "Agravante: leve → grave, grave → gravísima", "Variable"),
    ("alcohol", "Beber en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("beb", "Beber en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("toma", "Beber en el colegio o con uniforme", "Amonestación escrita", "Grave"),
    ("desobed", "Desobedecer órdenes de autoridad", "Amonestación escrita", "Grave"),
    ("hurt", "Hurto de bienes", "Suspensión o expulsión", "Gravísima"),
    ("rob", "robo de bienes", "Suspensión o expulsión", "Gravísima"),
    ("discrimin", "Discriminar a un integrante de la comunidad", "Suspensión o expulsión", "Gravísima"),
]

# Entrada del usuario
st.subheader("Describe la falta cometida:")
falta_usuario = st.text_input("Ejemplo: usa minúsculas 'alumno copia en una prueba y usa IA para hacer una tarea'")

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
