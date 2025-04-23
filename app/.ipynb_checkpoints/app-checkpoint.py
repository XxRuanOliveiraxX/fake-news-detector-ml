import streamlit as st
import joblib

# Carregar modelos
rf_model = joblib.load('models/random_forest_model.pkl')
log_model = joblib.load('models/logistic_regression_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Título do app
st.title("Detector de Fake News 🕵️‍♂️📰")

# Opção para escolher modelo
model_option = st.selectbox("Escolha o modelo de classificação:", 
                            ("Random Forest", "Logistic Regression"))

# Caixa de texto para entrada do usuário
user_input = st.text_area("Digite a notícia que você quer verificar:")

# Botão de verificação
if st.button("Verificar"):
    if user_input.strip() == "":
        st.warning("Por favor, digite uma notícia.")
    else:
        # Vetorizar entrada
        input_vector = vectorizer.transform([user_input])

        # Previsão com o modelo escolhido
        if model_option == "Random Forest":
            prediction = rf_model.predict(input_vector)[0]
        else:
            prediction = log_model.predict(input_vector)[0]

        # Exibir resultado
        if prediction == 0:
            st.success("✅ Esta notícia é VERDADEIRA!")
        else:
            st.error("🚨 Esta notícia é FALSA!")
