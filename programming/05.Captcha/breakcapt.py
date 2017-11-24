from PIL import Image
import pytesseract, sys, argparse, re, os

# Construct Argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to input iamge")
args = vars(ap.parse_args())

# Convert to RGBA if possible
image = Image.open(args["image"])
size = image.size
image.thumbnail(size, Image.ANTIALIAS) # Generate the thumbnail

offset_x = max((size[0] - image.size[0]) / 2, 0)
offset_y = max((size[1] - image.size[1]) / 2, 0)
offset_tuple = (offset_x, offset_y)

final_thumb = Image.new(mode='RGBA', size=size, color=(255,255,255,255)) #Create the image object to be the final product
final_thumb.paste(image, offset_tuple) # paste the thumbnail into image
final_thumb.save('test.png') # Save

#canvas = Image.new('RGBA', image.size, (255,255,255,255)) # Empty canvas color (r,g,b,a)
#canvas.paste(image, mask=image) # Paste the image onto the canvas
#canvas.thumbnail([resolution.width, resolution.height], Image.ANTIALIAS)
#canvas.save('test', format="PNG")
