## Transformers to classify the IMDB dataset

from transformers import pipeline
from transformers.pipelines.pt_utils import KeyDataset
import datasets
from sklearn.metrics import confusion_matrix
from tqdm.auto import tqdm
from sklearn.metrics import classification_report

## loads the dataset 25k samples from the test split
dataset = datasets.load_dataset("imdb", name="plain_text", split="test")

## use the model tuned to imdb - device 0 means the GPU
pipe = pipeline(model="textattack/bert-base-uncased-imdb",  device=0)

i =0 
y_pred =[]
y = []

for out in pipe(KeyDataset(dataset, "text"), batch_size=32,truncation="only_first"):
    y.append(dataset['label'][i])
    if (out['label'] == 'LABEL_0' ):
        y_pred.append(0)
    else:
        y_pred.append(1)

    i = i+1
    if (i%100==0):
        print(i)

print(confusion_matrix(y, y_pred))
print(classification_report(y, y_pred))

