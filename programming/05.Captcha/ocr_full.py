from PIL import Image
import os, pytesseract, re, requests, cv2

# GET URL and Image
r = requests.get("http://challenge01.root-me.org/programmation/ch8/")
if re.search('img src="data:image/png;base64', r.text):
	matches = re.search(r'data:image([^"]+)', r.text)
	if matches:
		arr = matches.group()
		fh = open("sample.png", "wb")
		fh.write(str(arr.split(",")[1].decode('base64')))
		fh.close()
	else:
		sys.exit()

# Convert to RGBA
img = Image.open("/home/tester/rootme-programming/05.Captcha/sample.png")
img = img.convert("RGBA")
data = img.getdata()

# Loop turning Black pixel to White pixel
newData = []
for item in data:
	if item[0] == 0 and item[1] == 0 and item[2] == 0:
		newData.append((255,255,255,255))
	else:
		newData.append(item)

#Put new data to Image
img.putdata(newData)
img.save("new.png", "PNG")

#Make letter bolder

#img = Image.open("/home/tester/rootme-programming/05.Captcha/new.png")
#img = img.convert("RGBA")
#pixdata = img.load()

#for y in xrange(img.size[1]):
#	for x in xrange(img.size[0]):
#		if pixdata[x, y][0] < 90:
#			pixdata[x, y] = (0, 0, 0, 255)

#for y in xrange(img.size[1]):
#        for x in xrange(img.size[0]):
#                if pixdata[x, y][1] < 136:
#                        pixdata[x, y] = (0, 0, 0, 255)

#for y in xrange(img.size[1]):
#        for x in xrange(img.size[0]):
#                if pixdata[x, y][2] > 0:
#                        pixdata[x, y] = (255, 255, 255, 255)

#img.save("new.png", "PNG")

# Make image bigger
origin = Image.open("/home/tester/rootme-programming/05.Captcha/new.png")
origin = origin.resize((1250,250), Image.NEAREST)
origin.save("big.png","PNG")

# Load Image and Convert into grayscale
image = cv2.imread("/home/tester/rootme-programming/05.Captcha/big.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0 , 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# Load Image as PIL/Pillow and Apply OCR then Delete Temp File
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

r = requests.post("http://challenge01.root-me.org/programmation/ch8/", data = {'cametu': text})
print(r.text)

#
# Show output Image
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)
