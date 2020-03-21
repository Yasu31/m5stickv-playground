# Train with raccoon dataset
based on [this article](https://raspberrypi.mongonta.com/howto-make-kmodel-on-ubuntu/)
## create Docker image
```bash
docker build -t raccoon .
docker run -it -v $(PWD):/root/data raccoon /bin/bash
```
## train NN
```bash
conda activate yolo
cd Yolo-digit-detector/
python train.py -c /root/data/raccoon.json
cp model.* /root/data/gen/
```
## convert to use on K210
```bash
cd Maix_Toolbox
cp ../data/gen/model.tflite .
cp ../raccoon_dataset/images/* images/
./tflite2kmodel.sh model.tflite
cp model.kmodel /root/data/gen/
```
## run on M5stickV
copy *model.kmodel* and *boot.py* to microSD and turn on device

# resources
* ﾗｽﾞﾊﾟｲｽﾞｷﾉﾆｯｷ [M5StickVやUnitVで使えるkmodelファイルをローカル環境で作成する。](https://raspberrypi.mongonta.com/howto-make-kmodel-on-ubuntu/)
  * ここのDockerfileなどは基本的にこれに基づいている。
* GitHub [AIWintermuteAI/Yolo-digit-detector](https://github.com/AIWintermuteAI/Yolo-digit-detector)
  * 上の記事の大元
  * [raccoon dataset](https://github.com/datitran/raccoon_dataset)
  * 具体的な手順は[Instructables](https://www.instructables.com/id/Object-Detection-With-Sipeed-MaiX-BoardsKendryte-K/)
* Qiita [MobileNet(v1,v2,v3)を簡単に解説してみた](https://qiita.com/omiita/items/77dadd5a7b16a104df83)
  * MobileNetでどういう工夫がなされているかの解説
* Qiita [【物体検出手法の歴史 : YOLOの紹介】](https://qiita.com/mdo4nt6n/items/68dcda71e90321574a2b)
  * YOLOの概要
* arxiv [You Only Look Once:Unified, Real-Time Object Detection](https://arxiv.org/pdf/1506.02640.pdf)
  * original paper for YOLO
* [CS231n Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/convolutional-networks/)
  * Convolutional NNs
  * class notes for a Stanford CS class
* Hackernoon [Understanding YOLO](https://hackernoon.com/understanding-yolo-f5a74bbc7967)
  * nice overview of YOLO
* Gentle guide on how YOLO Object Localization works with Keras [part 1](https://hackernoon.com/gentle-guide-on-how-yolo-object-localization-works-with-keras-part-1-aec99277f56f) [part 2](https://heartbeat.fritz.ai/gentle-guide-on-how-yolo-object-localization-works-with-keras-part-2-65fe59ac12d)
* Medium [Real-time Object Detection with YOLO, YOLOv2 and now YOLOv3](https://medium.com/@jonathan_hui/real-time-object-detection-with-yolo-yolov2-28b1b93e2088)
* Home Made Garbage [オリジナル金魚認識モデルの生成 ーエッジAI活用への道 3ー](https://homemadegarbage.com/ai03)
  * how to make your own model
* EETimes Japan [RISC-V活用が浸透し始めた中国](https://eetimes.jp/ee/articles/1907/08/news006.html)

As I infer... YOLO specifies how the outputs and loss functions should be formatted, and the architecture (MobileNet etc) specifies the structure of the neural network itself??