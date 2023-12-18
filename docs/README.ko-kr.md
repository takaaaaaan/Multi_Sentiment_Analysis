# 다중 감정 분석
[English](../README.md) | [일본어](./README.ja-jp.md)
## 한국어 감정 분류기 - TensorFlow를 이용한 다중 분류

한국어 감정 분류기는 한국어 대화 텍스트에서 기본 감정을 분류하는 Python 프로그램입니다. 이 프로젝트는 딥러닝 모델을 훈련하기 위해 TensorFlow를 사용합니다.

## 특징

- 6가지 기본 감정(분노, 기쁨, 불안, 당황, 슬픔, 상처) 분류
- LSTM(Long Short-Term Memory)을 사용한 시퀀스 모델링
- 맞춤형 토크나이저를 이용한 텍스트 처리

## 의존성

- Python 3.10.3
- TensorFlow 2.0
- NumPy
- pandas

## 사용 방법

### 1. 데이터셋 준비

`training.csv` 파일에는 `감정_대분류`와 `사람문장1` 열이 포함되어 있어야 합니다.

### 2. 모델 훈련

```bash
python Multiple_classification.py
```

### 3. 모델 테스트
```bash
python emotion_test.py
```
## 코드 설명

[`Multiple_classification.py`](Multiple_classification.py)
이 파일은 모델을 훈련하는 데 사용됩니다. 토크나이저와 모델은 각각 `tokenizer.json`과`model_name.h5`로 저장됩니다.

[`emotion_test.py`](emotion_test.py)
이 파일은 저장된 모델을 불러와 새로운 텍스트 데이터에 대한 감정 분석을 수행합니다.

## 라이선스
MIT

## 저자
우에노 고홍