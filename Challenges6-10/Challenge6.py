#First download the zip file from url 'channel.zip' and extract it.
import  re, zipfile

#base_path = os.getcwd() + "\\Challenge6files\\" #For windows devices only
z = zipfile.ZipFile("channel.zip")

#z.extractall(path = str(base_path) + "extraction")

file_number = 90052  #Initial file number
comments = []
for i in range(910):
    file_reader = z.open(str(file_number) + ".txt" )
    contents = file_reader.readline().decode('utf-8')
    comments.append(z.getinfo(str(file_number) + ".txt").comment.decode('utf-8'))
    file_reader.close()
    search = re.search(r'[0-9]{2,5}', contents)
    #print(contents)
    try:
        file_number = search.group()
    except AttributeError:
        break

print("".join(comments))
