import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Tokenizerをロード
with open("tokenizer.json", "r", encoding="utf-8") as f:
    json_data = f.read()
    loaded_tokenizer = tokenizer_from_json(json_data)

# モデルをロード
model = load_model("model_name.h5")

# テストするテキスト
test_texts = ["키우던 강아지가 죽었어", "오늘은 날씨가 좋아", "시발"]  # これを適当なテキストで置き換えてください

# テキストをシーケンスに変換
test_sequences = loaded_tokenizer.texts_to_sequences(test_texts)

# パディング
test_padded = pad_sequences(
    test_sequences, maxlen=10, padding="post", truncating="post"
)

# 予測
predictions = model.predict(test_padded)

# 予測結果を解釈
emotion_mapping_reverse = {0: "분노", 1: "기쁨", 2: "불안", 3: "당황", 4: "슬픔", 5: "상처"}
predicted_labels = np.argmax(predictions, axis=1)
predicted_emotions = [emotion_mapping_reverse[label] for label in predicted_labels]

# 結果を表示
for text, emotion in zip(test_texts, predicted_emotions):
    print(f"テキスト: {text}, 予測された感情: {emotion}")
