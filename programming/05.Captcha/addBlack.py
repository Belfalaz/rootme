from PIL import Image
import pytesseract, sys, argparse, re, os, cv2

# Construct Argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to input iamge")
args = vars(ap.parse_args())

# Convert to RGBA if possible
image = Image.open(args["image"])
image = image.convert("RGBA")
datas = image.getdata()

newData = []
for item in datas:
	if item[0] == 0 and item[1] == 0 and item[2] == 0:
		newData.append((255,255,255,255))
	else:
		newData.append(item)

image.putdata(newData)
image.save("test.png", "PNG")

newImg = cv2.imread("/home/tester/rootme-programming/05.Captcha/test.png")
gray = cv2.cvtColor(newImg, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0 , 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# Load Image as PIL/Pillow and Apply OCR then Delete Temp File
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
