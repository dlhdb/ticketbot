from PIL import Image
from PIL import ImageFilter
import numpy as np

im = Image.open('screenshot_crop.png')
im = im.convert('RGBA')

blurred_im = im.filter(ImageFilter.SHARPEN)
blurred_im.save('screenshot_crop_filter.png')

data = np.array(im)
# just use the rgb values for comparison
rgb = data[:,:,:3]

# create mask
mask = np.zeros((rgb.shape[0],rgb.shape[1]),dtype='bool')
for row in range(0,rgb.shape[0]):
    for col in range(0,rgb.shape[1]):
        if rgb[row][col][0] > 213 and rgb[row][col][0] < 219 \
        and rgb[row][col][1] > 230 and rgb[row][col][1] < 235 \
        and rgb[row][col][2] > 218 and rgb[row][col][2] < 223:
            mask[row][col] = True
    
#color = [216, 232, 221]   # Original value
#mask = np.all(rgb == color, axis=-1)

# change all pixels that match color to white
white = [255,255,255,255]
data[mask] = white


new_im = Image.fromarray(data)
new_im.save('screenshot_crop_bgrm.png')