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
    # FALTAS GRAVES ARTICULO 287
    ("no entra", "No ingresar a clases, ocultándose en algún espacio del colegio. (Cimarra interna) ", "Art. 287 Numeral 3: Amonestación escrita", "Grave"),
    ("no ingres", "No ingresar a clases, ocultándose en algún espacio del colegio. (Cimarra interna) ", "Art. 287 Numeral 3: Amonestación escrita", "Grave"),
    ("irrespetuos", "Mostrar una conducta irrespetuosa o insolente con algún Profesor, Inspector, otro funcionario o compañero.", "Art. 287 Numeral 4: Amonestación escrita", "Grave"),
    ("insolente", "Mostrar una conducta irrespetuosa o insolente con algún Profesor, Inspector, otro funcionario o compañero.", "Art. 287 Numeral 4: Amonestación escrita", "Grave"),
    ("engañ", "Tratar de engañar al Profesor mostrando algún trabajo o prueba ajena como propia. ", "Art. 287 Numeral 5: Amonestación escrita", "Grave"),
    ("fuma", "Fumar en el colegio o con uniforme", "Art. 287 Numeral 6: Amonestación escrita", "Grave"),
    ("desobedec", "Desobedecer a instrucciones u órdenes dadas por el Profesor, Inspector, Director u otra autoridad del Colegio. ", "Art. 287 Numeral 7: Amonestación escrita", "Grave"),
    ("ensuci", "Ensuciar, rayar, causar daños menores en infraestructura, materiales, muebles u otro elemento del Colegio, Profesores o Estudiantes. ", "Art. 287 Numeral 8: Amonestación escrita", "Grave"),
    ("ray", "Ensuciar, rayar, causar daños menores en infraestructura, materiales, muebles u otro elemento del Colegio, Profesores o Estudiantes. ", "Art. 287 Numeral 8: Amonestación escrita", "Grave"),
    ("dañ", "Ensuciar, rayar, causar daños menores en infraestructura, materiales, muebles u otro elemento del Colegio, Profesores o Estudiantes. ", "Art. 287 Numeral 8: Amonestación escrita", "Grave"),
    ("daño", "Causar daño material o destrucción de algún bien del establecimiento, del Profesor o de algún compañero. ). ", "Art. 287 Numeral 9: Amonestación escrita", "Grave"),
    ("pelea", "Provocar desórdenes, peleas entre compañeros o con otros niños estando en representación del Colegio. ", "Art. 287 Numeral 10: Amonestación escrita", "Grave"),
    ("dispositivo", "Utilizar dispositivos electrónicos al interior de la sala de clases sin autorización del docente y/o funcionario a cargo.", "Art. 287 Numeral 11: Amonestación escrita", "Grave"),
    ("celular", "Usar el celular en todo espacio interno del colegio. ", "Art. 287 Numeral 12: Amonestación escrita", "Grave"),
    ("indebida", "Usar indebidamente fondos o recursos del Colegio o de su curso.. ", "Art. 287 Numeral 13: Amonestación escrita", "Grave"),
    ("amoros", "Manifestaciones de relaciones amorosas dentro del establecimiento realizando acciones tales como: abrazos, besos y otras que contravengan las normas disciplinarias que deben observarse al interior del Colegio. ", "Art. 287 Numeral 14: Amonestación escrita", "Grave"),
    ("bes", "Manifestaciones de relaciones amorosas dentro del establecimiento realizando acciones tales como: abrazos, besos y otras que contravengan las normas disciplinarias que deben observarse al interior del Colegio. ", "Art. 287 Numeral 14: Amonestación escrita", "Grave"),
    ("clima", "Alterar o interrumpir la clase.", "Art. 287 Numeral 15: Amonestación escrita", "Grave"),
    ("interrump", "Alterar o interrumpir la clase.", "Art. 287 Numeral 16: Amonestación escrita", "Grave"),
    ("engañ", "Engañar o mentir.", "Art. 287 Numeral 17: Amonestación escrita", "Grave"),
    ("ment", "Engañar o mentir.", "Art. 287 Numeral 17: Amonestación escrita", "Grave"),
    ("mient", "Engañar o mentir.", "Art. 287 Numeral 17: Amonestación escrita", "Grave"),
    ("burl", "Burlarse faltar el respeto a cualquier miembro de la comunidad educativa. ", "Art. 287 Numeral 18: Amonestación escrita", "Grave"),
    ("lenguaje", "Utilizar un lenguaje escrito u oral inadecuado al contexto escolar. ). ", "Art. 287 Numeral 19: Amonestación Escrita", "Grave"),
    ("energ", "Portar, comercializar o consumir bebidas energéticas. ", "Art. 287 Numeral 20: Amonestación Escrita", "Grave"),
  
    # FALTAS GRAVISIMAS ARTICULO 292
    ("agre", "Toda agresión física, verbal o sicológica, o de connotación sexual que vulnere a algún miembro de la comunidad educativa. ", "Art. 292 Numeral 2: Suspensión o expulsión", "Gravísima"),
    ("insult", "Proferir insultos o garabatos, hacer gestos groseros o amenazantes u ofender reiteradamente a cualquier miembro de la comunidad educativa. ", "Art. 292 Numeral 3: Suspensión o expulsión", "Gravísima"),
    ("garabat", "Proferir insultos o garabatos, hacer gestos groseros o amenazantes u ofender reiteradamente a cualquier miembro de la comunidad educativa. ", "Art. 292 Numeral 3: Suspensión o expulsión", "Gravísima"),
    ("groser", "Proferir insultos o garabatos, hacer gestos groseros o amenazantes u ofender reiteradamente a cualquier miembro de la comunidad educativa. ", "Art. 292 Numeral 3: Suspensión o expulsión", "Gravísima"),
    ("amenaz", "Proferir insultos o garabatos, hacer gestos groseros o amenazantes u ofender reiteradamente a cualquier miembro de la comunidad educativa. ", "Art. 292 Numeral 3: Suspensión o expulsión", "Gravísima"),
    ("ofen", "Proferir insultos o garabatos, hacer gestos groseros o amenazantes u ofender reiteradamente a cualquier miembro de la comunidad educativa. ", "Art. 292 Numeral 3: Suspensión o expulsión", "Gravísima"),
    ("amedrent", "Amedrentar, amenazar, chantajear, intimidar, hostigar, acosar, difamar o burlarse de un estudiante u otro miembro de la comunidad educativa (por ejemplo, utilizar sobrenombres hirientes, mofarse de características físicas, etc.).  ", "Art. 292 Numeral 4: Suspensión o expulsión", "Gravísima"),
    ("amenaz", "Amedrentar, amenazar, chantajear, intimidar, hostigar, acosar, difamar o burlarse de un estudiante u otro miembro de la comunidad educativa (por ejemplo, utilizar sobrenombres hirientes, mofarse de características físicas, etc.).  ", "Art. 292 Numeral 4: Suspensión o expulsión", "Gravísima"),
    ("chantaj", "Amedrentar, amenazar, chantajear, intimidar, hostigar, acosar, difamar o burlarse de un estudiante u otro miembro de la comunidad educativa (por ejemplo, utilizar sobrenombres hirientes, mofarse de características físicas, etc.).  ", "Art. 292 Numeral 4: Suspensión o expulsión", "Gravísima"),
    ("intimid", "Amedrentar, amenazar, chantajear, intimidar, hostigar, acosar, difamar o burlarse de un estudiante u otro miembro de la comunidad educativa (por ejemplo, utilizar sobrenombres hirientes, mofarse de características físicas, etc.).  ", "Art. 292 Numeral 4: Suspensión o expulsión", "Gravísima"),
    ("hostig", "Amedrentar, amenazar, chantajear, intimidar, hostigar, acosar, difamar o burlarse de un estudiante u otro miembro de la comunidad educativa (por ejemplo, utilizar sobrenombres hirientes, mofarse de características físicas, etc.).  ", "Art. 292 Numeral 4: Suspensión o expulsión", "Gravísima"),    
    ("acos", "Amedrentar, amenazar, chantajear, intimidar, hostigar, acosar, difamar o burlarse de un estudiante u otro miembro de la comunidad educativa (por ejemplo, utilizar sobrenombres hirientes, mofarse de características físicas, etc.).  ", "Art. 292 Numeral 4: Suspensión o expulsión", "Gravísima"),
    ("difam", "Amedrentar, amenazar, chantajear, intimidar, hostigar, acosar, difamar o burlarse de un estudiante u otro miembro de la comunidad educativa (por ejemplo, utilizar sobrenombres hirientes, mofarse de características físicas, etc.).  ", "Art. 292 Numeral 4: Suspensión o expulsión", "Gravísima"),
    ("burl", "Amedrentar, amenazar, chantajear, intimidar, hostigar, acosar, difamar o burlarse de un estudiante u otro miembro de la comunidad educativa (por ejemplo, utilizar sobrenombres hirientes, mofarse de características físicas, etc.).  ", "Art. 292 Numeral 4: Suspensión o expulsión", "Gravísima"),    
    ("discrimin", "Discriminar a un integrante de la comunidad educativa, ya sea por su condición social, situación económica, religión, pensamiento político o filosófico, ascendencia étnica, nombre, nacionalidad, orientación sexual, discapacidad, aspecto físico o cualquier otra circunstancia. ", "Art. 292 Numeral 5: Suspensión o expulsión", "Gravísima"),    
    ("hurt", "Hurtar algún bien o valor del Colegio o de algún compañero o funcionario del Colegio.", "Art. 292 Numeral 6: Suspensión o expulsión", "Gravísima"),    
    ("falta a clases", "Faltar a clases habiendo salido de su casa con destino al Colegio (Hacer Cimarra) ", "Art. 292 Numeral 7: Suspensión o expulsión", "Gravísima"),  
    ("cimarra", "Faltar a clases habiendo salido de su casa con destino al Colegio (Hacer Cimarra) ", "Art. 292 Numeral 7: Suspensión o expulsión", "Gravísima"),  
    ("adulter", "Adulterar o falsificar cualquier documento, nota, firma o timbre del establecimiento. ", "Art. 292 Numeral 8: Suspensión o expulsión", "Gravísima"),  
    ("falsific", "Adulterar o falsificar cualquier documento, nota, firma o timbre del establecimiento. ", "Art. 292 Numeral 8: Suspensión o expulsión", "Gravísima"),  
    ("sopla", "Ser sorprendido diciendo o mostrando las respuestas de una evaluación a un compañero(a)", "Art. 292 Numeral 9: Suspensión o expulsión", "Gravísima"),
    ("mostrando respuesta", "Ser sorprendido diciendo o mostrando las respuestas de una evaluación a un compañero(a)", "Art. 292 Numeral 9: Suspensión o expulsión", "Gravísima"),
    ("muestra respuesta", "Ser sorprendido diciendo o mostrando las respuestas de una evaluación a un compañero(a)", "Art. 292 Numeral 9: Suspensión o expulsión", "Gravísima"),
    ("copi", "Ser sorprendido copiando durante una evaluación", "Art. 292 Numeral 10: Suspensión o expulsión", "Gravísima"),
    ("plagi", "Presentar trabajos plagiados, no inéditos o utilizando inteligencia artificial, con el propósito de engañar.", "Art. 292 Numeral 11: Suspensión o expulsión", "Gravísima"),
    ("inteligencia", "Presentar trabajos plagiados, no inéditos o utilizando inteligencia artificial, con el propósito de engañar.", "Art. 292 Numeral 11: Suspensión o expulsión", "Gravísima"),
    ("ia", "Presentar trabajos plagiados, no inéditos o utilizando inteligencia artificial, con el propósito de engañar.", "Art. 292 Numeral 11: Suspensión o expulsión", "Gravísima"),
    ("IA", "Presentar trabajos plagiados, no inéditos o utilizando inteligencia artificial, con el propósito de engañar.", "Art. 292 Numeral 11: Suspensión o expulsión", "Gravísima"),
    ("destru", "Destruir en forma intencional cualquier bien del Colegio. ", "Art. 292 Numeral 12: Suspensión o expulsión", "Gravísima"),
    ("arma", "Portar algún tipo de arma", "Art. 292 Numeral 13: Suspensión o expulsión", "Gravísima"),
    

    
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

st.caption("Sistema basado en el Reglamento Interno del Colegio Manquemávida. Uso exclusivo para apoyo en la toma de decisiones.")
