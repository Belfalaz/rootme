from PIL import Image
import os, pytesseract, re, cv2, argparse

# Construct Argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to input iamge")
ap.add_argument("-p", "--pre", type=str, default="thresh", help="Type of preprocessing")
args = vars(ap.parse_args())

# Load Image and Convert into grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Check Preprocessing
if args["pre"] == "thresh":
	gray = cv2.threshold(gray, 0 , 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

if args["pre"] == "blur":
	gray = cv2.medianBlur(gray, 3)

# Write grayscale image to disk as temp file (wait for OCR)
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# Load Image as PIL/Pillow and Apply OCR then Delete Temp File
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

#r = requests.get
# Show output Image
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)
