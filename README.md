# Kopernikus_Automotive_Programming_Task
## What did you learn after looking on our dataset?

The dataset has different images of parking areas with vehicles and without them. Dataset has images of different lighting conditions.

## How does you program work?

Every images are compared with same reference image.

Two hashmaps are created. 

myShapeMap: A dictionary used to store reference images based on their shapes. since there are images of different shapes, we store an image as reference for each shapes.

myHashMap: A dictionary that will store the images based on their characteristics (score, count, and shape). The key would be a string with ”score, count, and shape” the score is rounded to nearest hundred.

We initialize a variable called prevImShape to zero.  Each time , when the image is loaded, we check if the shape is equal to that of the reference image used for previous image - prevImShape. If they are different, then we selected current image as the reference image and pass same image  as previous image and next image. As expected the output score, number of contours would be zero. But this doesn’t remove the image. Because. Now we add this image to the myHashMap dictionary with key as (score, count, and shape) and value as the image name.
For the next image, if the shape is same as the previous image we consider the same previous reference image used. And the output of the ‘compare_frames_change_detection’ function is stored to myHashMap. 
Each time we check if the key is already present in the myHashMap. If the key is already present, this means that a similar image with the same values were stored. So we can understand that it is the duplicate image and we remove them. This solves the duplication problem. 
This solution only iterate along all the image once.
## What values did you decide to use for input parameters and how did you find these values?
The input parameter that were used are gaussian_blur_radius_list = [15, 17, 25]. It was obtained by trial and error method. At this configuration, better detection of duplicate images are obtained.
The min_contour_area is selected as 2150 so that unwanted noises and high exposure lights are removed.
## What you would suggest to implement to improve data collection of unique cases in future?
•	Diverse Data Sources: Collect data from diverse sources to ensure a broad representation of scenarios. This could include different cameras, angles, lighting conditions, environments, and demographics.
•	Data Augmentation: Use data augmentation techniques to generate new samples from existing data. Techniques such as rotation, flipping, scaling, and color adjustments can help increase dataset size and diversity.
•	 Annotated Data: Collect annotated data to create a ground truth for training machine learning models. Annotation can include object bounding boxes, semantic segmentation masks, or key point annotations.
•	User Feedback: Encourage users to provide feedback on the dataset. Implement mechanisms for users to flag mislabelled data or suggest additional data categories.
•	Benchmarking: Regularly benchmark and evaluate the dataset's performance in real-world applications. This helps identify areas for improvement and guides future data collection efforts. 
•	Collaboration: Collaborate with other institutions or researchers to combine datasets and leverage collective knowledge for more comprehensive data collection.

