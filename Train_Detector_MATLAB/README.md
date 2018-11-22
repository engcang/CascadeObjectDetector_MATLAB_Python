# Train Detector using MATLAB Computer Vision System Toolbox
+ Trained by stages which are ensembles of weak learners. 
+ Each stage is trained using a technique called boosting.
</br></br>

### Nessecary :
+ [< Computer Vision System Toolbox> ](https://kr.mathworks.com/help/vision/index.html)
+ Image files
+ [gTruth](#before-running-code) of ROI
<br><br>

## Before running code
+ Make gTruth data using _**imageLabeler**_ from Computer Vision System Toolbox in MATLAB </br>
  Run imageLabeler
  ~~~MATLAB
  >>imageLabeler
  ~~~
  </br></br>
  Using **"Load"**, load images including object you want to detect</br>
and define **"ROI"** with Rectangle form
  <p align="left">
  <img src="https://github.com/engcang/image-files/blob/master/opencv/labeler.png" width="600" hspace="100"/>
  </p></br>
  
  Drag the ROI on images and then **"Export Labels" "To workspace"** (for later, save the session is recommended)
  <p align="left">
  <img src="https://github.com/engcang/image-files/blob/master/opencv/roi.png" width="600" hspace="100"/>
  </p>
  Now you have gTruth!<br><br>

## Code running, breakdown
+ Run the code in [_**train.m**_](https://github.com/engcang/CascadeObjectDetector_MATLAB_Python/blob/master/Train_Detector_MATLAB/train.m)
  ~~~MATLAB
  %% training the turtlebot detector
  trainingData = objectDetectorTrainingData(gTruth,'ImageFormat','jpg'); % image labeler Result exported into workspace as 'gTruth'

  positiveInstances = trainingData(:,1:2);
  imDir = fullfile('./imagefolder');
  addpath(imDir);

  negativeFolder = fullfile('./negativeimagefolder');
  negativeImages = imageDatastore(negativeFolder);
  trainCascadeObjectDetector('name.xml',positiveInstances, negativeFolder,'FalseAlarmRate',0.1,'NumCascadeStages',5,'FeatureType','Haar');
  % featuretype important, 'HOG' type cannot be used in python from OpenCV 3.x version
  ~~~
  Code train image detector with Positive Images and Negative Images into _**.xml**_ result file </br>
  'FeatureType' can differ the result and 'HOG'(default) type cannot be used in python from OpenCV 3.X version<br><br>

## Result
+ Detection code is available [here]()
  <p align="center">
  <img src="https://github.com/engcang/image-files/blob/master/opencv/Detected.gif" width="600" hspace="0"/>
  </p></br>
