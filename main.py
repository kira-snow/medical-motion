import torchio as tio
import cv2
from pathlib import Path
from glob import glob
import os


def transform(path, out_path):
    transform_0 = tio.transforms.RandomGhosting(num_ghosts = (4, 10), axes= (0, 1, 2), intensity = (0.5, 1), restore = 0.02)  # tio.transforms.RandomMotion(degrees=0, translation=10, num_transforms=2, image_interpolation='linear')
    # tio.transforms.RandomAffine(scales=(0.9, 1.2),degrees=15,)  #
    transforms = [transform_0]
    final_transform = tio.Compose(transforms)

    subject = tio.Subject(t1=tio.ScalarImage(path))
    subject = final_transform.apply_transform(subject)

    img = subject.get_images()[0]
    img.save(out_path)


transform('crop1.png', 'crop1_motion.png')
transform('crop2.png', 'crop2_motion.png')
transform('crop3.png', 'crop3_motion.png')
transform('crop4.png', 'crop4_motion.png')
transform('crop5.png', 'crop5_motion.png')

