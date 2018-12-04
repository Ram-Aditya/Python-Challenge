#http://www.pythonchallenge.com/pc/def/oxygen.html
import PIL.Image

image = PIL.Image.open("oxygen.png")

pix = image.load()

middle_row = []
print(image.size)

for i in range(image.size[0]):
    middle_row.append(pix[i, image.size[1] // 2])

#Values seem to repeat 7 times. Duplicate values can be deleted

middle_row = middle_row[::7]
#Last 3 values in the tuple seem  to be garbage values

middle_row = middle_row[:-3]

for i in range(len(middle_row)):
    print(chr(middle_row[i][0]), end = "")
print()


#We get a list of array values which must be converted back to characters

result = [105, 110, 116, 101, 103, 114, 105, 116, 121]

for i in range(len(result)):
    print(chr(result[i]), end = "")