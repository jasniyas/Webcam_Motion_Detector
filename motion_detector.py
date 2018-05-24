#  Importing all relevant libraries.
import cv2, pandas
from datetime import datetime

# Assigning the first static frame to none.
first_frame=None

# create a list of when any moving object appears.
status_list=[None, None]

# Time of movement.
times= []

# Initializing dataframe with start and end time of movement.
df=pandas.DataFrame(columns=["Start", "End"])

# Capture the video.
video = cv2.VideoCapture(0)

# Infinite while loop to treat stack of image as video.
while True:
    # Read frame from video.
    check, frame = video.read()

    #initialise motion status to 0 which indicates no motion.
    status=0

    # Convert color image to gray scale and GaussianBlur images.
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray= cv2.GaussianBlur(gray, (21, 21), 0)

    # In the first iteration we assign the value of first_frame to gray
    if first_frame is None:
        first_frame= gray
        continue

    # Difference between first frame and current frame (which is Gaussianblur).
    delta_frame= cv2.absdiff(first_frame, gray)

    # If change in between first_frame and current frame is greater than 30
    # it will show white color(255)
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame= cv2.dilate(thresh_frame, None, iterations=2)

    # Find contours of moving object.
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1

        # green rectanle around the object.
        (x, y, w, h)= cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    # Appending status of motion to the list
    status_list.append(status)

    status_list= status_list[-2:]

    # Appending start and end time of motion.
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())


    # Display the different frames.
    cv2.imshow("Gray_frame", gray)
    cv2.imshow("Delta_frame", delta_frame)
    cv2.imshow("Threshold frame", thresh_frame)
    cv2.imshow("Color_frame", frame)

    key = cv2.waitKey(1)

    if key== ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

# Appending time of motion in dataframe.
for i in range(0, len(times), 2):
    df=df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

# Creating a csv file that stores the start and end time.
df.to_csv("Times.csv")
video.release()

# Destroy all the windows.
cv2.destroyAllWindows()
