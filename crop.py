import torchio as tio
import cv2
from pathlib import Path
from glob import glob
import os


def crop(path, out_path):
    img = cv2.imread(path)
    crop_img = img[280:760, 110:740]
    cv2.imwrite(out_path, crop_img)


if __name__ == '__main__':
    root_path = './png'
    pattern = '**/*.png'
    image_paths = [Path(x) for x in glob(root_path + "/" + pattern, recursive=True)]

    output_paths = []
    for i in range(0, len(image_paths)):
        parts = image_paths[i].parts
        output_path = parts[0] + '_crop'
        for j in range(1, len(parts)):
            output_path = os.path.join(output_path, parts[j])
        output_paths.append(Path(output_path))

    for i in range(0, len(image_paths)):
        parent_dir = output_paths[i].parent.absolute()

        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        crop(str(image_paths[i]), str(output_paths[i]))


