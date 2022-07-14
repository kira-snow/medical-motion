import sys
import glob
import h5py
import cv2
import os
import numpy as np

# origin_width = 740-110
# origin_height = 760-280
# width = 180
# height = origin_height * width // origin_width

height = 120
width = 157

if __name__ == '__main__':
    # print(str(0).zfill(3))
    h5_dataset_number = 10
    total_dataset_number = 240
    dataset_folder_number = total_dataset_number // h5_dataset_number
    dataset_image_number = 50
    root_dir = './png_crop'
    global_dataset_id = 1
    for folder_id in range(0, dataset_folder_number):
        print('prepare folder {}'.format(folder_id))

        folder = os.path.join('dataset', 'fold{}'.format(folder_id))
        if not os.path.exists(folder):
            os.makedirs(folder)
        h5filepath = os.path.join(folder, 'images.h5')

        with h5py.File(h5filepath, 'w') as h5f:
            for dataset_name in range(0, h5_dataset_number):
                print('prepare dataset {}'.format(dataset_name))
                dataset_id = str(global_dataset_id).zfill(3)
                dataset_path = os.path.join(root_dir, 'Bmode_' + dataset_id)
                img_ds = h5f.create_dataset("obs{}".format(dataset_name),
                                            shape=(height, width, dataset_image_number),
                                            dtype=np.uint8)

                for image_id in range(dataset_image_number):
                    image_path = os.path.join(dataset_path, 'Bmode_{}.png'.format(str(image_id + 1).zfill(2)))
                    print(image_path)
                    img = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_4)
                    img_ds[:, :, image_id] = img

                global_dataset_id += 1
