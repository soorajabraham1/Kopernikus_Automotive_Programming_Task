# Kopernikus_Automotive_Programming_Task
## What did you learn after looking on our dataset?

The dataset has different images of parking areas with vehicles and without them. Dataset has images of different lighting conditions.

## How does you program work?

*	The code begins by initializing two dictionaries, myHashMap and myShapeMap, which will be used to store image information and reference images, respectively.
*	myHashMap: This dictionary is used to identify duplicate or almost similar images based on their characteristics, including a rounded score, count of contours, and shape. The key is a string in the format "score, count, and shape," where the score is rounded to the nearest multiple of 3000. Images with identical characteristics will have the same key, allowing for efficient duplicate detection.
*	myShapeMap: This dictionary is employed to store reference images for each unique image shape. If the shape of the current image differs from the shape of the previously processed image, a new reference image is chosen and stored in this dictionary. This ensures that images with different shapes have their respective reference images.
*	The code then proceeds to process each image in the image_files list, which is obtained using os.listdir() on the specified image_folder.
*	
For each image, the following steps are performed:
1.	The image is loaded using cv2.imread() and stored in the variable curr_image.
2.	The code checks if the shape of the current image (curr_image.shape) is different from that of the previously processed image (prevImShape). If they are different, a check is made in myShapeMap to see if a reference image with the current shape already exists. If such an image exists, it is used as the reference image (ref_image). If not, the current image is stored as the reference image for its shape.
3.	Both the current image and the reference image are preprocessed using the preprocess_image_change_detection() function with specific kernel sizes [3, 5, 9]. The result is stored in image_gray and ref_image_gray, respectively.
4.	The frames of the reference and current images are compared using the compare_frames_change_detection() function, which returns a score, a list of contours (cnts), and a thresholded frame (thresh).
5.	The score is rounded to the nearest multiple of 3000 to create the key for the myHashMap dictionary, along with the count of contours and the shape of the current image.
6.	The key is checked in myHashMap. If it already exists, this indicates that a similar image has been processed before, making the current image a duplicate. The duplicate image is removed using os.remove(). Otherwise, the image is added to myHashMap with the key and the image name.
Any exceptions that occur during image processing are caught, and relevant error messages are printed.
At the end of the code, the number of removed images (i) is printed, along with the unique keys present in the myHashMap dictionary, which represent the characteristics of the images used for duplicate detection.s through the input array once and performs constant-time operations for each element. The space complexity is O(n) as well, considering the worst case where all elements are unique and stored in the numSet.


## What values did you decide to use for input parameters and how did you find these values?

The input parameter that was used is gaussian_blur_radius_list = [15, 17, 25]. It was obtained by trial and error method. At this configuration, better detection of duplicate images is obtained.
The min_contour_area is selected as 2150 so that unwanted noises and high-exposure lights are removed.

## What you would suggest to implement to improve data collection of unique cases in the future?

•	Diverse Data Sources: Collect data from diverse sources to ensure a broad representation of scenarios. This could include different cameras, angles, lighting conditions, environments, and demographics.
•	Data Augmentation: Use data augmentation techniques to generate new samples from existing data. Techniques such as rotation, flipping, scaling, and color adjustments can help increase dataset size and diversity.
•	 Annotated Data: Collect annotated data to create a ground truth for training machine learning models. Annotation can include object bounding boxes, semantic segmentation masks, or key point annotations.
•	User Feedback: Encourage users to provide feedback on the dataset. Implement mechanisms for users to flag mislabelled data or suggest additional data categories.
•	Benchmarking: Regularly benchmark and evaluate the dataset's performance in real-world applications. This helps identify areas for improvement and guides future data collection efforts. 
•	Collaboration: Collaborate with other institutions or researchers to combine datasets and leverage collective knowledge for more comprehensive data collection.

