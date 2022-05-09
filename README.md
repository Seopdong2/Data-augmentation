# Data-augmentation
## overfitting
![img1](https://user-images.githubusercontent.com/97939479/167332770-dcaf7f35-aa56-4422-92e9-f051e3732e27.jpg)
Overfitting은 학습 데이터(Training Set)에 대해 과하게 학습된 상황입니다. 따라서 학습 데이터 이외의 데이터에 대해선 모델이 잘 동작하지 못합니다. 학습 데이터가 부족하거나, 데이터의 특성에 비해 모델이 너무 복잡한 경우 발생합니다. Training Set에 대한 loss는 계속 떨어지는데, Test Set에 대한 loss는 감소하다가 다시 증가합니다.


## Data augmentation 종류
![img2](https://user-images.githubusercontent.com/97939479/167333135-d1a63d82-2c83-4263-b345-cc6676a3f65e.jpg)
이미지에서 임의의 사각형 부분을 떼어내고 그 빈자리에 임의의 noise, 평균값 or 0으로 대체하는 방식
![3](https://user-images.githubusercontent.com/97939479/167333254-7d152438-531a-4764-b30e-1845a93b0eb7.jpg)
![4](https://user-images.githubusercontent.com/97939479/167333289-7bf45aeb-7b91-46e4-8004-09c7359fcc99.jpg)
cuotout + mixup



이미지 예시
![5](https://user-images.githubusercontent.com/97939479/167333759-ea7098ae-e5c1-49f1-9917-eb07e0acf0fe.jpg)
