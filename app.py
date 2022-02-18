import random
import os
from itertools import product
from PIL import Image
import json

project = 'NFT'
folder = './layers'
count = '100'
folder1 = './images'
layers_names = ["avatar", "face", "shirt", "accessory"]

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
    # random.shuffle(combinations)
        
    for combination in combinations:
        
        # if c != count:
            # print(len(combination))    
            # if len(combination)>2:
            # opens the file on the specified path and combinations
                im1 = Image.open(f'{folder}/1/{combination[0]}').convert('RGBA')
                im2 = Image.open(f'{folder}/2/{combination[1]}').convert('RGBA')
                
                comp = Image.alpha_composite(im1, im2)
                # comp.show()
                n=3
                for item in combination[2:]:
                    
                    if combination.index(item)!=-1:
                        comp = Image.alpha_composite(comp,
                                            Image.open(f'{folder}/{n}/{item}').convert('RGBA'))
                        n+=1
                    #Convert to RGB
                    rgb_im = comp.convert('RGB')
                    file_name = str(combinations.index(combination)) + ".png"
                    rgb_im.save("./images/" + file_name)
                
                    metadata['image']=f'./images/{file_name}'
                    metadata['tokenId']=str(combinations.index(combination))
                    metadata['name']= project+' '+str(combinations.index(combination))
                    metadata['attributes']=[]
                        
                    
                    for item in layers_names:
                        print(item)
                        metadata['attributes'].append({item:combination[layers_names.index(item)][:-4]})
                        
                    with open(f"./metadata/{str(combinations.index(combination))}.json", "w") as outfile:
                        json.dump(metadata, outfile, indent=4)
                    # c+=1
            # else:
            #     break 
                                   
               
        
if __name__ == "__main__":
   create()       