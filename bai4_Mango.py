import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

folder_sour = 'Program/python/bai4/sour'
folder_sweet = 'Program/python/bai4/sweet'

images_sour = os.listdir(folder_sour)
images_sweet = os.listdir(folder_sweet)

# Tạo mảng lưu các giá trị chỉ số của các hình
RGB_sour = np.zeros(len(images_sour))
RGB_sweet = np.zeros(len(images_sweet))

# Hàm tính chỉ số
def calc_RGB(I):
    R = np.sum(I[:,:,0])
    G = np.sum(I[:,:,1])
    B = np.sum(I[:,:,2])
    return R / (R + G + B)

# Tính chỉ số của tất cả các hình trong thư mục
for i, img in enumerate(images_sour):
    I = np.array(Image.open(os.path.join(folder_sour, img)))
    RGB_sour[i] = calc_RGB(I)

for i, img in enumerate(images_sweet):
    I = np.array(Image.open(os.path.join(folder_sweet, img)))
    RGB_sweet[i] = calc_RGB(I)

# Vẽ đồ thị
plt.figure()
plt.stem(RGB_sour, np.zeros(len(images_sour)), 'g', markerfmt='og', label='sour mango')
plt.stem(RGB_sweet, np.zeros(len(images_sweet)), 'r', markerfmt='or', label='sweet mango')
plt.legend()
plt.title('feature of sweet and sour mango')
plt.xlabel('R/(R+G+B)')
plt.show()

# Chọn ngưỡng chua ngọt theo công thức
threshold = (np.max(RGB_sweet) + np.min(RGB_sour)) / 2

# Test theo công thức
I_test = np.array(Image.open("Program/python/bai4/sweet/5.png"))
testRGB = calc_RGB(I_test)

if testRGB > threshold:
    print("Test images is sweet mango")
else:
    print("Test images is sour mango")