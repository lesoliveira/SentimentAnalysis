# Análise de Sentimentos na Base IMDB

## Modelos Hugging Face
* HuggingFace.py
  - Modelo já treinado para a tarefa de classificação de sentimentos IMDB (Positivo/Negativo)

[[11801   699]
 [ 1044 11456]]
              precision    recall  f1-score   support

           0       0.92      0.94      0.93     12500
           1       0.94      0.92      0.93     12500

    accuracy                           0.93     25000
   macro avg       0.93      0.93      0.93     25000
weighted avg       0.93      0.93      0.93     25000


## BERT
* bert.py
  - Script usa um modelo previamente treinado para extrair os embeddings
  - De posso dos embedding, qualquer classificador pode ser treinando para
    classificar os comentários (positivo/negativo)

## LLM (Prompt)
* Instale o ollama:
    curl -fsSL https://ollama.com/install.sh | sh
    ollama serve
    service ollama start

    - baixe o modelo 
    ollama pull gemma2

    prompt interativo
    - ollama run gemma2

    https://ollama.com/library

    // salvar o resultado 
    ollama run gemma2 "why the sky is blue" >> out.md

    ollama run gemma2 "$(cat comments.txt)" classify these comments into positive or negative

* O script Sentiment.sh seleciona aleatoriamente 10 comentarios da base de dados e realiza a classificação usando o prompt
