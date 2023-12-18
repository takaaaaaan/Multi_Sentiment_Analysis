# 多感情分析
[English](../README.md) | [韓国語](./README.ko-kr.md)
## 韓国語感情分類器 - TensorFlowを使用した多重分類

韓国語感情分類器は、韓国語の会話テキストにおける基本感情を分類するPythonプログラムです。このプロジェクトでは、ディープラーニングモデルをトレーニングするためにTensorFlowを使用しています。

## 特徴

- 6つの基本感情（怒り、喜び、不安、恥ずかしさ、悲しみ、傷つき）を分類
- LSTM（Long Short-Term Memory）を使用したシーケンスモデリング
- カスタムトークナイザーによるテキスト処理

## 依存関係

- Python 3.10.3
- TensorFlow 2.x
- NumPy
- pandas

## 使用方法

### 1. データセットの準備

`training.csv`ファイルには、`감정_대분류`（感情大分類）と`사람문장1`（人間の文章1）の列が含まれている必要があります。

### 2. モデルのトレーニング

```bash
python Multiple_classification.py
```

### 3. モデルのテスト
```bush
python emotion_test.py
```
## コード説明
[`Multiple_classification.py`](Multiple_classification.py)

このファイルはモデルのトレーニングに使用されます。トークナイザーとモデルはそれぞれ`tokenizer.json`と`model_name.h5`として保存されます。

[`emotion_test.py`](emotion_test.py)

このファイルは保存されたモデルを読み込み、新しいテキストデータに対して感情分析を実行します。

## ライセンス
MIT

## 作者
上野嵩弘