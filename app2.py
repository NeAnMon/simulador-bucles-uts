import streamlit as st
import time

st.title("🔁 La Fábrica de Bucles - UTS")
st.markdown("Identifica el patrón y observa cómo la computadora repite tareas por ti.")

# Selección del tipo de ciclo
tipo_ciclo = st.sidebar.selectbox("Selecciona el tipo de Ciclo:", ["Ciclo FOR", "Ciclo WHILE"])

if tipo_ciclo == "Ciclo FOR":
    st.subheader("Configurando un Ciclo FOR")
    vueltas = st.slider("¿Cuántas iteraciones quieres realizar?", 1, 10, 5)
    
    if st.button("¡Ejecutar Bucle!"):
        acumulador = 0
        progreso = st.progress(0)
        
        for i in range(vueltas):
            iteracion = i + 1
            acumulador += 10 # Supongamos que sumamos puntos
            st.write(f"🔄 Vuelta {iteracion}: El acumulador ahora vale {acumulador}")
            progreso.progress(iteracion / vueltas)
            time.sleep(0.5) # Para que vean el proceso
        st.success(f"¡Ciclo completado! El valor final es {acumulador}")

else:
    st.subheader("Simulador de Ciclo WHILE")
    st.write("Este ciclo se ejecutará mientras el número sea menor a 100.")
    inicio = st.number_input("Valor inicial:", 0, 90, 50)
    incremento = st.slider("¿Cuánto sumar en cada vuelta?", 1, 20, 10)
    
    if st.button("Iniciar Proceso"):
        actual = inicio
        pasos = 0
        while actual < 100:
            st.write(f"⚡ Valor actual: {actual} (Es menor a 100, seguimos...)")
            actual += incremento
            pasos += 1
            time.sleep(0.5)
        st.error(f"🛑 ¡STOP! El valor es {actual}. La condición 'menor a 100' ya no se cumple.")
        st.info(f"Se realizaron {pasos} iteraciones.")