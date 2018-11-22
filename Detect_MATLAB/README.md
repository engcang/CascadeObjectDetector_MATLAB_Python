# Detect object using _**CascadeObjectDetector**_ in MATLAB
+ Using trained result _**.xml**_ file from [_here_](https://github.com/engcang/CascadeObjectDetector_MATLAB_Python/tree/master/Train_Detector_MATLAB)
</br></br>

## Detector code running
+ MATLAB<br><br>
  ~~~MATLAB
  detector = vision.CascadeObjectDetector('name.xml');
  %rosinit('192.168.2.15')
  %sub_img = rossubscriber('/zed/rgb/image_rect_color/compressed');
  %while 1
  %img_temp = receive(sub_img);
  %img = readImage(img_temp);
  bbox = step(detector,img);
  detectedImg = insertObjectAnnotation(img,'rectangle',bbox,'Detected');
  figure(2);
  imshow(detectedImg);
  %end
  ~~~
<br>

1.For me, used commented block to get and detect consequtive images via ROS <br><br>

2.make detector handler using _**'vision.CascadeObjectDetector('name.xml')'**_ <br><br>

3.and detect image using _**'step(detector,img)'**_ it yields _**'bbox'**_ which is in rectangle form (x_start_point,y_start_point,width,height) <br><br><br>

  <p align="center">
  <img src="https://github.com/engcang/image-files/blob/master/opencv/Detected.gif" width="600" hspace="0"/>
  </p></br>
