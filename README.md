# zisyupuro-memo
memo folder for zisyupuro

操り人形ヒューマノイドを作る。


各フォルダのメモ  
・arduino　モータなどを動かすためのarduinoのスケッチ。  
・euslisp　lispで作った棒人間。これを人の姿勢情報と連動させたい。  
・kinect　kinectを使うファイル。演習のをもとにしていて、人の姿勢情報を取ってくる。  
・openpose　open poseのライブラリ。  
・tf-pose-estimation　tf-openposeのライブラリ。こっちをメインで使うかも。ROSにも対応している？  

最終的にはcatkinのワークスペースとROSのパッケージを作って、その中で完結させたい。


## 自分用のメモ

[Scrapboxのページ](https://scrapbox.io/zisyupuro/)

### Coral TPU
Coral TPUを使ってカメラから人の姿勢検知を行う。
/edgetpu_human_pose_estimator/output/poses
のトピックに関節の情報が送られる。

もとのgithub:https://github.com/knorth55/coral_usb_ros

実行の手順は  
まず、usbカメラのノードを立てる。
```
rosrun usb_cam usb_cam_node
```
次に人の姿勢検知を行うノードを立てる。
```
source ~/coral_ws/devel/setup.bash
roslaunch coral_usb edgetpu_human_pose_estimator.launch INPUT_IMAGE:=/usb_cam/image_raw
```
以下の用にしてimageの結果を表示する事も出来る。
```
rosrun image_view image_view image:=/edgetpu_human_pose_estimator/output/image /edgetpu_human_detector/output/image
```

### rosbag
[これ](https://qiita.com/srs/items/f6e2c36996e34bcc4d73)を参考にした。  

以下の用にして保存をする。-Oで保存するファイルを指定出来る。
```
rosbag record -a -O robot_bag #全てのトピックを保存
rosbag record -e /tf.* #マッチしたものだけ保存
rosbag record /topic1 /topic2 #指定したトピックだけを保存
```
以下のようにファイル名を指定して再生をする。
```
rosbag play coral_test1_2019-12-09-13-57-34.bag
```
### ROSシリアル
ROSシリアルを使ってPCからArduinoにシリアル通信をしてモータを制御する。[ROSwiki](http://wiki.ros.org/rosserial_arduino/Tutorials)を参考にした。
ArduinoにROS用のスケッチを書き込んで、以下を実行する。ポートはArduinoが接続しているものに変更する。これでArduinoとシリアル通信をするROSのノードを作ることが出来る。
```
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```


### 関節角度計算
pythonで関節の位置から関節角度を計算して/2d_human_jointにpublishするコードを書いた。
以下で実行をする（lanchファイルを作りたい。）
```
python coral2dpose.py
```
