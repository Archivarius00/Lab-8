import cv2


my_image = cv2.imread('images/variant-6.png')
b, g, r = cv2.split(my_image)

res = (cv2.resize(my_image, (2*my_image.shape[0], 2*my_image.shape[1]))) #Растягиваем в 2 раза по ширине и высоте
res1 = (cv2.resize(my_image, (2*my_image.shape[0], my_image.shape[1]))) #Растягиваем в 2 раза по ширине
res2 = (cv2.resize(my_image, (my_image.shape[0], 2*my_image.shape[1]))) #Растягиваем в 2 раза по высоте
cv2.imshow('Original image', my_image)
cv2.imshow('2 раза в ширину и высоту', res)
cv2.imshow('2 раза в ширину', res1)
cv2.imshow('2 раза в высоту', res2)


cv2.waitKey(0)
cv2.destroyAllWindows()