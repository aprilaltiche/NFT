import random
import os
from itertools import product
from PIL import Image
import json

project = 'NFT'
folder = './layers'
thisdir = os.listdir(folder)
count = '100'
layers_names = ["background", "face", "shirt", "accessory"]

c=0
metadata={}



def mkdir():
   if not os.path.isdir('metadata'):
      os.mkdir('metadata')
   if not os.path.isdir('images'):
      os.mkdir('images')
   
def create():
    # list of png combinations
    mkdir() 
    combinations = list(product(*[os.listdir(f'{folder}/{x}') for x in os.listdir(folder) ]))
    random.shuffle(combinations)
       

    for combination in combinations:
        
        # if c != count:
                
            # if len(combination)>2:
            # opens the file on the specified path and combinations
                im1 = Image.open(f'{folder}/1/{combination[0]}').convert('RGBA')
                im2 = Image.open(f'{folder}/2/{combination[1]}').convert('RGBA')
                
                comp = Image.alpha_composite(im1, im2)
                # comp.show()
                
                #Convert to RGB
                rgb_im = comp.convert('RGB')
                file_name = str(combinations.index(combination)) + ".png"
                rgb_im.save("./images/" + file_name)
                
                
                for item in combination:
                    metadata['image']=f'./images/{file_name}'
                    metadata['tokenId']=str(combinations.index(combination))
                    metadata['name']= project+' '+str(combinations.index(combination))
                    metadata['attributes']=[]
                        
                    
                    for item in layers_names:
                        
                        print({item})
                        
                        metadata['attributes'].append({item:combination})
                        
                    with open(f"./metadata/{str(combinations.index(combination))}.json", "w") as outfile:
                        json.dump(metadata, outfile, indent=4)
                    # c+=1
    print(metadata)                               
    # else:
        # break    
        
if __name__ == "__main__":
   create()        