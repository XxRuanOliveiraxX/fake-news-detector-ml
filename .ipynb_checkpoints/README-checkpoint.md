# 📰 Detector de Fake News com Machine Learning

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

## 🔍 Resultados dos Modelos

### Logistic Regression

- **Acurácia**: 98.72%
- **Precisão / Revocação / F1**: veja mais no notebook `02_model.ipynb`

### Random Forest

- **Acurácia**: 99.73%
- **Precisão / Revocação / F1**: veja mais no notebook `02_model.ipynb`

---

### 📈 Comparação entre os Modelos

| Modelo              | Acurácia   |
|---------------------|------------|
| Logistic Regression | 98.72%     |
| Random Forest       | 99.73%     |

---

## 🚀 Como Rodar o Projeto

1. Clone este repositório:
```bash
git clone https://github.com/XxRuanOliveiraxX/fake-news-detector-ml.git
cd fake-news-detector-ml
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rodando o app (você pode rodar o app Streamlit de duas maneiras):

✅ Opção 1: Terminal normal<br/>Abra o terminal, navegue até a raiz do projeto e rode:
```bash
streamlit run app/app.py
```

✅ Opção 2: Terminal embutido do JupyterLab<br/>Se você está utilizando o JupyterLab, também pode rodar o app diretamente pelo terminal embutido:

1. No JupyterLab, clique em:
```bash
File > New > Terminal
```
2. No terminal aberto, navegue até a pasta do projeto:
```bash
cd fake-news-detector-ml
```
3. Execute o comando:
```bash
streamlit run app/app.py
```
4. Copie e cole o link http://localhost:8501 no seu navegador!