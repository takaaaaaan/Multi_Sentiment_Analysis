# Multi-Sentiment Analysis
[日本語](./docs/README.ja-jp.md) | [한국어](./docs/README.ko-kr.md)
## Korean Emotion Classifier - Multiple Classification with TensorFlow

The Korean Emotion Classifier is a Python program that classifies basic emotions in Korean conversational text. This project uses TensorFlow to train a deep learning model.

## Features

- Classifies 6 basic emotions (Anger, Joy, Anxiety, Embarrassment, Sadness, Hurt)
- Sequence modeling using LSTM (Long Short-Term Memory)
- Text processing with a custom tokenizer

## Dependencies

- Python 3.10.3
- TensorFlow 2.x
- NumPy
- pandas

## Usage

### 1. Preparing the Dataset

The `training.csv` file should contain columns `감정_대분류` and `사람문장1`.

### 2. Training the Model

```bash
python Multiple_classification.py
```

### 3. Testing the Model
```bash
python emotion_test.py
```
## Code Description
[`Multiple_classification.py`](Multiple_classification.py)

This file is used for training the model. The tokenizer and model are saved as `tokenizer.json`and`model_name.h5`, respectively.

[`emotion_test.py`](emotion_test.py)


This file loads the saved model and performs emotion analysis on new text data.

## License

MIT

## Author

Ueno Takahiro