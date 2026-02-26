import sys
import os
from PIL import Image
#Fix code saftey
if len(sys.argv) < 2:
    print("Usage: python script.py <input_folder> <output_folder>")
    sys.exit(1)

#Grab the arguments from the terminal
folder_needed = sys.argv[1]
folder_output = sys.argv[2]

#check if the folder exists and if not , we create it. 
if not os.path.exists(folder_output):
    os.makedirs(folder_output)
#loop through the folder , take images and convert them into png format. 

for filename in os.listdir(folder_needed):
    img = Image.open(f'{folder_needed}\\{filename}')
    clean_name = os.path.splitext(filename)[0] #splitting to only remain with the filename and remove the extension. 
    img.save(f'{folder_output}\\{clean_name}.png' , 'png')
print('Done ✅')
