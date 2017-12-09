from PIL import Image

inputpath = "48x42pixlar"
outputpath = "output"
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(inputpath) if isfile(join(inputpath, f))]

#print onlyfiles

for f in xrange(len(onlyfiles)):
	#generates array from pixel-values
	im = Image.open(inputpath + '/' + onlyfiles[f], 'r')
	width, height = im.size
	pixel_values = list(im.getdata())
	#print pixel_values

	#remove dimension in pixel_values array
	pixellistan = []
	for i in range(len(pixel_values)):
		dim_length = len(pixel_values[i]) #find out the dimension of the array due to both rgb and greyscale images...
		dim_length = dim_length - 1 #decrease by one
		#print dim_length
		#print pixel_values[i][1]
		pixellistan.append(pixel_values[i][dim_length])


#	creates an empty file to add data into 
	filnamn = onlyfiles[f]
	filen = filnamn[0:-8] # removes .svg.png from filename
	print filen
	open(outputpath + '/' + filen, 'a').close() #creates an empty file
	str_listan = str(pixellistan) # converts array to string
	output = open(outputpath + '/' + filen, 'a').write(str_listan) #writes the string to the file
