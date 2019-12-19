from pathlib import Path
import cv2
import numpy as np


def read_transparent_png(filename):
    image_4channel = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    alpha_channel = image_4channel[:, :, 3]
    rgb_channels = image_4channel[:, :, :3]

    # black Background Image
    black_background_image = np.zeros_like(rgb_channels, dtype=np.uint8) * 255

    # Alpha factor
    alpha_factor = alpha_channel[:, :, np.newaxis].astype(np.float32) / 255.0
    alpha_factor = np.concatenate((alpha_factor, alpha_factor, alpha_factor), axis=2)

    # Transparent Image Rendered on White Background
    base = rgb_channels.astype(np.float32) * alpha_factor
    white = black_background_image.astype(np.float32) * (1 - alpha_factor)
    final_image = base + white
    return final_image.astype(np.uint8)


if __name__ == '__main__':
    # directory for pngs
    images_dir = Path('images_nearmap/annotations')
    # directory to save binary images
    mask_save_dir = Path(f'{images_dir}/annotations/binary')
    mask_save_dir.mkdir(exist_ok=True, parents=True)

    image_paths = images_dir.glob('*.png')
    for image_path in list(image_paths):
        image_name = f'{image_path.stem}.png'
        print(image_name)
        image = read_transparent_png(str(image_path))
        cv2.imwrite(f'{mask_save_dir}/{image_name}', image)
