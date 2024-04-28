import cv2
import numpy as np


#================================================ center_frame ==================================================
def center_frame(filename, param):
    print(f"Now reading {filename}")

    # Read image
    img = cv2.imread(filename)
    if img is None:
        print("File not found!!!(%s)\n" % filename)
        return -1, 0

    # Convert to grayscale if necessary
    if len(img.shape) > 2:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    # Thresholding
    _, bw = cv2.threshold(gray, param.threshold*255, 255, cv2.THRESH_BINARY)

    # Remove small objects
    bw2 = cv2.morphologyEx(bw, cv2.MORPH_OPEN, np.ones((param.filterRadius,param.filterRadius),np.uint8))

    # Find contours
    contours, _ = cv2.findContours(bw2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if Sun is detected
    if len(contours) == 0:
        print("Can not detect Sun")
        return -1, 0

    # Get the largest contour (assuming it's the Sun)
    cnt = max(contours, key=cv2.contourArea)

    # Minimum enclosing circle
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)

    # Crop and resize
    x_min, y_min = max(0, center[0] - param.crop//2), max(0, center[1] - param.crop//2)
    x_max, y_max = min(img.shape[1], center[0] + param.crop//2), min(img.shape[0], center[1] + param.crop//2)
    cropped = img[y_min:y_max, x_min:x_max]
    if param.resize != param.crop:
        resized = cv2.resize(cropped, (param.resize, param.resize))

    # return the image
    return 0, resized