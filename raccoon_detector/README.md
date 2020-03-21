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