
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
# CSVからデータを読み込む
df = pd.read_csv('training.csv')
print(df)
# '감정_대분류'と'사람문장1'のみを抽出
df = df[['감정_대분류', '사람문장1']]
df.columns = ['emotion', 'text']

# 감정을 숫자にマッピング
emotion_mapping = {'분노': 0, '기쁨': 1, '불안': 2, '당황': 3, '슬픔': 4, '상처': 5}
df['emotion'] = df['emotion'].map(emotion_mapping)

# Tokenizer 객체 생성
tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')

# データにあるテキストを基に語彙辞書を作成
tokenizer.fit_on_texts(df['text'])
sequences = tokenizer.texts_to_sequences(df['text'])

# Tokenizerを保存
tokenizer_json = tokenizer.to_json()
with open('tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(tokenizer.to_json())


padded = pad_sequences(sequences, maxlen=10, padding='post', truncating='post')

# Sequential 모델 생성
model = Sequential([
    Embedding(10000, 16, input_length=10),
    LSTM(32),
    Dense(24, activation='relu'),
    Dropout(0.5),
    Dense(6, activation='softmax')
])


model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

# 모델 학습
model.fit(padded, df['emotion'], epochs=100)

model.save("model_name.h5")
