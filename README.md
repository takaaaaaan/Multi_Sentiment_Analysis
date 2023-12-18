# Multi_Sentiment_Analysis


# 감정 분석기 - Multiple Classification with TensorFlow

Korean Emotion Classifierは、한국어로된 대화 텍스트에서 기본적인 감정을 분류하는 Pythonプログラムです。このプロジェクトはTensorFlowを使用して深層学習モデルを訓練しています。

## 特徴

- 6種類の基本感情（분노, 기쁨, 불안, 당황, 슬픔, 상처）に分類
- LSTM (Long Short-Term Memory) を使用したシーケンスモデリング
- カスタムトークナイザーによるテキスト処理

## 依存関係

- Python 3.10.3
- TensorFlow 2.x
- NumPy
- pandas

## 使い方

### 1. データセットの用意

`training.csv`ファイルには、`감정_대분류`と`사람문장1`のカラムが含まれている必要があります。

### 2. モデルの訓練

```bash
python Multiple_classification.py
```

### 3. モデルのテスト

```bash
python emotion_test.py
```

## コード説明

### Multiple_classification.py

このファイルはモデルの訓練に使用されます。トークナイザーとモデルはそれぞれ`tokenizer.json`と`model_name.h5`として保存されます。

[コードを見る](Multiple_classification.py)

### emotion_test.py

このファイルは保存されたモデルをロードし、新しいテキストデータに対して感情分析を行います。

[コードを見る](emotion_test.py)

## ライセンス

MIT

## 作成者

Ueno Takahiro

```

