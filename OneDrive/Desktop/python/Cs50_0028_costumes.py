# Hare krsna

import sys

from plistlib import Image

images = []

for arg in sys.argv:
    image = Image.open(arg)
    images.append(image)
    
    
images[0].save(
    
)