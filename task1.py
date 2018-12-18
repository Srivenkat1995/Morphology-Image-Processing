import cv2 

import numpy as np

import copy

def imagePadding(image):

    rows,columns = image.shape
    new_image = [[0 for x in range(columns + 2)] for y in range(rows + 2 )]
    for i in range(rows+1):
        for j in range(columns+1):
            if i == 0 or i == rows+1:
                new_image[i][j] = 0
            elif j == 0 or j == columns+1:
                new_image[i][j] = 0
            else:
                new_image[i][j] = image[i-1][j-1]

    return new_image



def dilation(image):

    rows,columns = image.shape
    print(rows,columns)
    for i in range(rows-2):
        for j in range(columns-2):
            #print(i,j)
            if image[i][j] == 255 or image[i][j+1] == 255 or image[i][j+2] == 255 or image[i+1][j] == 255 or image[i+1][j+1] == 255 or  image[i+1][j+2] == 255 or image[i+2][j] == 255 or image[i+2][j+1] == 255 or image[i+2][j+2] == 255:

                image[i][j] = 255

            else:

                continue    


    return image

def erosion(image):

    rows,columns = image.shape
    print(rows,columns)
    for i in range(rows-2):
        for j in range(columns-2):
            #print(i,j)
            if image[i][j] == 255 and image[i][j+1] == 255 and image[i][j+2] == 255 and image[i+1][j] == 255 and image[i+1][j+1] == 255 and  image[i+1][j+2] == 255 and image[i+2][j] == 255 and image[i+2][j+1] == 255 and image[i+2][j+2] == 255:

                image[i][j] = 255

            else:
                image[i][j] = 0   
                continue    


    return image

def opening(image):

    erosion_image = erosion(copy.deepcopy(image))
    dilation_image = dilation(copy.deepcopy(erosion_image))
    resultant_image = copy.deepcopy(dilation_image)

    return resultant_image

def closing(image):

    dilation_image = dilation(copy.deepcopy(image))
    erosion_image = erosion(copy.deepcopy(dilation_image))
    resultant_image = copy.deepcopy(erosion_image)

    return resultant_image

def boundary(image,name_of_image):

    erosion_image = erosion(copy.deepcopy(image))

    resultant_image = image - erosion_image
    
    cv2.imwrite(name_of_image,resultant_image)



if __name__ == "__main__":

    image = cv2.imread('noise.jpg',0)
    image = np.asarray(image)

   
    padded_image = imagePadding(image)
    padded_image = np.asarray(padded_image)
   
    resultant_image_1_opening = opening(copy.deepcopy(padded_image))
    resultant_image_1 = closing(copy.deepcopy(resultant_image_1_opening))

    resultant_image_2_closing = closing(copy.deepcopy(padded_image))
    resultant_image_2 = opening(copy.deepcopy(resultant_image_2_closing))

    cv2.imwrite('res_noise1.jpg',copy.deepcopy(resultant_image_1))
    cv2.imwrite('res_noise2.jpg',copy.deepcopy(resultant_image_2))

    

    boundary(copy.deepcopy(resultant_image_1),'res_bound1.jpg')
    boundary(copy.deepcopy(resultant_image_2), 'res_bound2.jpg')
 
   
    
