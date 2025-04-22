# 📰 Fake News Detector with Machine Learning

Este projeto tem como objetivo desenvolver um modelo de Machine Learning capaz de identificar notícias falsas com base em seu conteúdo textual. Ele utiliza técnicas de **Processamento de Linguagem Natural (NLP)** aplicadas em um conjunto de dados real com notícias verdadeiras e falsas.

---

## 🔍 Sobre o Projeto

- 🔎 **Problema:** A disseminação de fake news é um problema crescente nas redes sociais e mídias digitais.
- 🎯 **Objetivo:** Criar um classificador que consiga distinguir notícias reais de falsas a partir do texto da notícia.
- 🧠 **Técnica:** Machine Learning com pré-processamento de texto (NLP) e vetorização com TF-IDF.

---

## 🗂 Dataset

O dataset utilizado está disponível publicamente no Kaggle:

- Fonte: [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- Contém:
  - `Fake.csv`: Notícias falsas
  - `True.csv`: Notícias reais

---

## 🛠️ Tecnologias e Bibliotecas

- Python
- Pandas, NumPy
- scikit-learn
- NLTK
- Matplotlib, Seaborn
- Jupyter Notebook

---

## 📊 Etapas do Projeto

1. **Exploração dos Dados (EDA):**
   - Análise de distribuição, tamanhos de texto, classes
   - Limpeza básica

2. **Pré-processamento de Texto (NLP):**
   - Tokenização, remoção de stopwords, lematização

3. **Vetorização:**
   - Conversão de texto em vetores com TF-IDF

4. **Modelagem:**
   - Treinamento com Logistic Regression
   - Avaliação com métricas de classificação

5. **Deploy:**
   - Interface interativa para testar o modelo com novas notícias

---

## ✅ Resultados

- Modelo: **Logistic Regression**
- Acurácia: **99%**  
- Boas métricas de precisão e recall para ambas as classes

---

## 🚀 Como Rodar o Projeto

1. Clone este repositório:
```bash
git clone https://github.com/XxRuanOliveiraxX/fake-news-detector-ml.git
cd fake-news-detector-ml