import functions
import cv2
import os

image_folder="E:/datasetCopy/"# Give the name of the directory containing dataset

myHashMap = {} # to identify duplicate images
myShapeMap = {} # store reference image path for each image shape

prevImShape, i = None, 0

image_files = os.listdir(image_folder)

for images in image_files:
        image_path = os.path.join(image_folder, images)
        try:

                curr_image=cv2.imread(image_path)
                # if the previous image shape and current image shape are equal, we use the same reference image. if not we check in our dictionary if we have another reference image
                #with that shape. if the dictionary has the reference image of that shape we use that image. if not we store the current image and use that as the reference image.
                if prevImShape !=curr_image.shape:
                        if curr_image.shape in myShapeMap:
                                ref_image_path=myShapeMap[curr_image.shape][0]
                        else:
                                myShapeMap[curr_image.shape]=[image_path]
                                ref_image_path=image_path
                        ref_image=cv2.imread(ref_image_path)
                        ref_image_gray=functions.preprocess_image_change_detection(ref_image,[3, 5, 9])

                image_gray=functions.preprocess_image_change_detection(curr_image,[3, 5, 9])
                score,cnts,thresh=functions.compare_frames_change_detection(ref_image_gray,image_gray,2150)
                print(image_path,"Score",score,"cnts",len(cnts))
                #cv2.imshow(image_path,thresh)
                #we round the score value to nearest multiple of 3000
                rounded_score = round(score / 3000) * 3000
                prevImShape = curr_image.shape
                mykey= f"{rounded_score} {len(cnts)} {curr_image.shape}"
                #the hashmap called myHashMap is used to check duplicate/ almost similar images . The key is a string containing score, number of contours and shape of the image.
                #so an identical image would have same key and we remove tha image using os.remove.
                if mykey in myHashMap:
                        i+=1
                        myHashMap[mykey].append(images)
                        os.remove(image_path)
                        print("removed",images)
                else:
                        myHashMap[mykey] = [images]
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
        cv2.waitKey(0)  # Wait until any key is pressed
        cv2.destroyAllWindows()  # Close all OpenCV windows

print("removed "+str(i)+" images out of "+ str(len(image_files)))
print(myHashMap.keys())


cv2.waitKey(0)  # Wait until any key is pressed
cv2.destroyAllWindows()  # Close all OpenCV windows

