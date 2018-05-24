# WebCam Motion Detector
This python program will allow you to detect motion, store the time interval of the motion and create a timeplot of the motion.
Videos can be treated as stack of pictures called frames. Here I am comparing different frames(pictures) to the first static (no movement initially) frame. We compare two images by comparing the intensity value of each pixels. 

# Requirements
Python3 installation, Python libraries - OpenCV (opencv-python), Pandas, datetime.

# Folder Description 
1. motion_detector.py - code to detect the motion.
2. plotting.py - code to plot the timeplot of the motion detected 
3. Time.csv - CSV file that will store the start and end times of the detected motion. This file will be generated after the first run.

# Execution
  1. Clone the repo from github using command line
        * Open command line 
        * git clone git@github.com:jasniyas/Webcam_Motion_Detector.git
        * Repo would be cloned
  2. Run plotting.py in the command line or in any IDE. 
  3. Keep the first frame static when the webcam activates.
  4. Try different motions at different time intervals.
  5. Press "q" to quit the webcam.
  6. Browser will open automatically with the interactive timeplot graph drawn using Bokeh.
  7. Close browser.

# Analysis of all windows
After running the code, 4 new window will appear on screen.
1. Gray Frame: The image is a bit blur and in grayscale. There is only one intensity value whereas in RGB(Red, Green and Blue) image thre are three intensity values. So it would be easy to calculate the intensity difference in grayscale.
2. Difference Frame (delta frame): Shows the difference of intensities of first frame to the current frame.
3. Threshold Frame: If the intensity difference for a particular pixel is more than 30(in my case) then that pixel will be white and if the difference is less than 30 that pixel will be black.
4. Color Frame: In this frame you can see the color images in color frame along with green contour rectangle around the moving objects.
