# Análise de Sentimentos na Base IMDB

## Modelos Hugging Face
* HuggingFace.py

  - Modelo já treinado para a tarefa de classificação de sentimentos IMDB (Positivo/Negativo)

|            | Previsto Positivo | Previsto Negativo |
|------------|-------------------|-------------------|
| Real Positivo | 11.801               | 699                 |
| Real Negativo | 1.044               | 11.456               |


| Classe | Precisão | Recall | F1-Score | Suporte |
|--------|----------|--------|----------|---------|
| 0 (Negativo) | 0.92     | 0.94   | 0.93     | 12.500  |
| 1 (Positivo) | 0.94     | 0.92   | 0.93     | 12.500  |


| Métrica           | Valor |
|-------------------|-------|
| Acurácia          | 0.93  |

## BERT
* bert.py
  - Script usa um modelo previamente treinado para extrair os embeddings
  - De posso dos embedding, qualquer classificador pode ser treinando para
    classificar os comentários (positivo/negativo)
  - o script rf.py treina um Random Forest para essa tarefa

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

* O script Sentiment.sh seleciona aleatoriamente 10 comentarios da base de dados e realiza a classificação usando o prompt.

## Erros de Rotulação
* A base IMDB contem alguns erros de rotulação, veja esse por exemplo:

Random number: 30475
30473,train,"Time travel is a fun concept, and this film gives it a different slant. I got a kick out of Captain Billingham, one of the more down-to-earth characters, who was just not having a good day. Ordinarily, I don't choose to watch horror films, but this is an exception. Good story, excellent acting.",neg,3677_3.txt
Running 

Esse comentário foi classificado como positivo tanto pelo Llama3.2 (Meta) quanto pelo nemotron-mini (NVidia)
