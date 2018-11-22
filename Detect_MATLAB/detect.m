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
