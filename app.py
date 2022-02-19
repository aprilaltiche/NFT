import random
import os
from itertools import product
from PIL import Image
import json
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
project = 'NFT'
folder = './layers'
count = '100'
layers_names = ["avatar", "accessories"]

c=0
metadata={}

def mkdir():
   if not os.path.isdir('metadata'):
      os.mkdir('metadata')
   if not os.path.isdir('images'):
      os.mkdir('images')
   if not os.path.isdir('layers'):
      os.mkdir('layers')
      
def create():
    # list of png combinations
    mkdir() 
    
    combinations = list(product(*[os.listdir(f'{folder}/{x}') for x in os.listdir(folder) ]))
    # random.shuffle(combinations)
    
    for combination in combinations:
        
        # if c != count:
            # print(len(combination))    
            # if len(combination)>2:
            # opens the file on the specified path and combinations
                im1 = Image.open(f'{folder}/1/{combination[0]}').convert('RGBA')
                im2 = Image.open(f'{folder}/2/{combination[1]}').convert('RGBA')
                # print(im1)
                # exit()
                comp = Image.alpha_composite(im1, im2)
                # comp.show()
                saveComposite(comp,combination,combinations)
                
                
                # for item in layers_names:
                #     metadata['attributes'].append({item:combination[layers_names.index(item):len(os.listdir(folder))][:len(os.listdir(f'{folder}/2'))]})
                    
                # with open(f"./metadata/{str(combinations.index(combination))}.json", "w") as outfile:
                #     json.dump(metadata, outfile, indent=4)
                if len(os.listdir())>2:
                    n=3
                    for item in combination[2:]:
                        
                        if combination.index(item)!=-1:
                            comp = Image.alpha_composite(comp,
                                                Image.open(f'{folder}/{n}/{item}').convert('RGBA'))
                            n+=1
                        #Convert to RGB
                        saveComposite(comp,combination,combinations)
                    
                # c+=1
    
                                   
def saveComposite(comp,combination,combinations):
    rgb_im = comp.convert('RGB')
    file_name = str(combinations.index(combination)) + ".png"
    rgb_im.save("./images/" + file_name)

    metadata['image']=f'./images/{file_name}'
    metadata['tokenId']=str(combinations.index(combination))
    metadata['name']= project+' '+str(combinations.index(combination))
    metadata['attributes']=[]
    upTo=-(len(os.listdir('layers/2')))
    print(upTo)
    for item in layers_names:
        metadata['attributes'].append({item:combination[layers_names.index(item)][:upTo]})
        
    with open(f"./metadata/{str(combinations.index(combination))}.json", "w") as outfile:
        json.dump(metadata, outfile, indent=4)    

if not os.listdir(folder):
    filedialog.askopenfilename()
    

createFile = tk.Button(root,text="Create NFT", command=create , pady="5", fg="white", bg="#263D42")
createFile.pack()


root.title ("NFT Generator")
# icon = PhotoImage(file="logo.png")
root.eval('tk::PlaceWindow . center')
root.mainloop()

# if __name__ == "__main__":
#    checkFiles()       