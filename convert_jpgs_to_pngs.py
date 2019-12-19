import os
from pathlib import Path
from PIL.Image import Image

images_dir = Path(Add directory which contains your jpgs)
image_paths = images_dir.glob('*.jpg')
for image_path in list(image_paths):
    image_name = f'{image_path.stem}.png'
    print(image_path)
    im = Image.open(f'{image_path}')
    rgb_im =  im.convert('RGB')
    rgb_im.save(f'{images_dir}/{image_name}')
    # Remove JPGs
    os.remove(image_path)