%% training the turtlebot detector
trainingData = objectDetectorTrainingData(gTruth,'ImageFormat','jpg'); % image labeler Result exported into workspace as 'gTruth'

positiveInstances = trainingData(:,1:2);
imDir = fullfile('./tunnel');
addpath(imDir);

negativeFolder = fullfile('./OTHERS');
negativeImages = imageDatastore(negativeFolder);
trainCascadeObjectDetector('name.xml',positiveInstances, negativeFolder,'FalseAlarmRate',0.1,'NumCascadeStages',5,'FeatureType','Haar');
% featuretype important, 'HOG' type cannot be used in python from OpenCV 3.x version
