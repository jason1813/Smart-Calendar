# grab all picture file names in images folder
# files_grabbed = array of image file names
import glob, os
types = ('*.jpg', '*.png', '*.gif')
files_grabbed = []
for files in types:
    files_grabbed.extend(glob.glob(files))

# get all text in the Ads.html file and put in a string 
# called htmlString
os.chdir("..")
with open('Ads.html', 'r') as myfile:
    htmlString=myfile.read()

# split the string in between the '<!--images-->'
picString = htmlString.split("<!--images-->")

# what goes before and after file names in Ads.html
preFName = '<img class="mySlides" src="./images/'
postFName = '" style="width:96%">'

# go through and chang newText to have the new files
newText = ''
for x in range(0, len(files_grabbed)):
    newText += '\n\t\t\t' + preFName + files_grabbed[x] + postFName
newText += '\n\t\t'

# replace the old text with the new for the new images
htmlString = htmlString.replace(picString[1], newText)

# write the htmlString into the Ads.html file
writeFile = open("Ads.html", "w")
writeFile.write(htmlString)