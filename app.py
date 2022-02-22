import random
import os
import shutil
from itertools import product
import itertools
import json
import tkinter as tk
from tkinter import  *
from tkinter import filedialog
from unicodedata import category
from PIL import Image
import ctypes

root = tk.Tk()
project = 'NFT'
folder = './layers1'
output = './images/'
layers_names = ["avatar", "face","neck"]
metadata={}

def mkdir():
   if not os.path.isdir(f'./metadata'):
      os.mkdir(f'./metadata')
   if not os.path.isdir(f'{output}'):
      os.mkdir(f'{output}')
   if not os.path.isdir(f'{output}/Design1'):
      os.mkdir(f'{output}/Design1')
   if not os.path.isdir('images/Design2'):
      os.mkdir(f'{output}/Design2')
   if not os.path.isdir('metadata/Design1'):
      os.mkdir(f'./metadata/Design1')
   if not os.path.isdir(f'./metadata/Design2'):
      os.mkdir(f'./metadata/Design2')      
   if not os.path.isdir(f'{folder}'):
      os.mkdir(f'{folder}')
      
def create():
    # list of png combinations
    mkdir() 
    
    combinations = list(product(*[os.listdir(f'{folder}/{x}') for x in os.listdir(folder) ]))
    # random.shuffle(combinations)
    set_img=Entry1.get()
    attribute_category=Entry2.get()
    folder_number=Entry3.get()
    category = attribute_category.lower()
    if category in layers_names:
       print(layers_names)
    else:
        layers_names.append(category)
        
    for combination in combinations:
        
        # if c != count:
            # print(len(combination))    
            # if len(combination)>2:
            # opens the file on the specified path and combinations
                
                path1 =f'{folder}/{folder_number}'
                im1 = Image.open(f'{folder}/1/{combination[0]}').convert('RGBA')
                im2 = Image.open(f'{folder}/2/{combination[1]}').convert('RGBA')
                
                comp = Image.alpha_composite(im1, im2)
                
                save_to='./images/Design1/'
                metadata='Design1/'
                saveComposite(comp,combination,combinations,save_to,metadata)
                if len(os.listdir())>2:
                    n=3
                    for item in combination[2:]:
                        
                        if combination.index(item)!=-1:
                            comp = Image.alpha_composite(comp,
                                                Image.open(f'{folder}/{n}/{item}').convert('RGBA'))
                            n+=1
                        #Convert to RGB
                        
                        saveComposite(comp,combination,combinations,save_to,metadata)
            
                if combination[1] == set_img and set_img in os.listdir(path1):
                   comp1 = Image.alpha_composite(im1, im2)
                
                   attributes = list(*[os.listdir(f'./layers2/{x}') for x in os.listdir(f'./layers2')])
                
                   length = len(attributes)
                   
                   folder_num=1
                   index=0
                   metadata={}                                  
                   
                   while index!=length:                      
                       comp2 = Image.alpha_composite(comp1,Image.open(f'./layers2/{folder_num}/{attributes[index]}').convert('RGBA'))
                    #    comp2.show()
                       save2='./images/Design2/'
                       meta='Design2/'
                       rgb_im = comp2.convert('RGB')
                       file_name = str(index) + ".png"
                       rgb_im.save(save2 + file_name)
                       
                       metadata['image']=f'{save2}{file_name}'
                       metadata['tokenId']=str(file_name)
                       metadata['name']= project+' '+str(file_name)
                       metadata['attributes']=[]
                       upTo=-(len(os.listdir(f'layers2/{folder_num}')))
                    
                       for item in layers_names:
                           
                           metadata['attributes'].append({item:combination[layers_names.index(item)][:upTo]})
                       with open(f"./metadata/{meta}{str(file_name)}.json", "w") as outfile:
                           json.dump(metadata, outfile, indent=4) 
                       index+=1
                # else:
                #     Mbox('Warning', 'Image name does not exist', 0)
                # c+=1
    
    # shutil.rmtree('./metadata/')  
    # shutil.rmtree(output)  
    Mbox('Information', 'Images has been created!', 0)                                  
def saveComposite(comp,combination,combinations,save_to,folder):
    rgb_im = comp.convert('RGB')
    file_name = str(combinations.index(combination)) + ".png"
    rgb_im.save(save_to + file_name)

    metadata['image']=f'{save_to}{file_name}'
    metadata['tokenId']=str(combinations.index(combination))
    metadata['name']= project+' '+str(combinations.index(combination))
    metadata['attributes']=[]
    upTo=-(len(os.listdir('layers1/2')))
    
    for item in layers_names:
        metadata['attributes'].append({item:combination[layers_names.index(item)][:upTo]})
        
    with open(f"./metadata/{folder}{str(combinations.index(combination))}.json", "w") as outfile:
        json.dump(metadata, outfile, indent=4)    

if not os.listdir(folder):
    filedialog.askopenfilename()
    
canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.pack()
label1 = Label(canvas,bg="white", text= "Enter Image name that will have different attributes "+'\n')
label1.pack()
Entry1 = Entry(canvas)
Entry1.insert(END, 'octagon-glass.png')
Entry1.pack()
Entry1.focus_set() 

label3 = Label(canvas,bg="white", text= "Enter the folder where you put this Image "+'\n')
label3.pack()
Entry3 = Entry(canvas)
Entry3.insert(END, '2')
Entry3.pack()
Entry3.focus_set() 


label2 = Label(canvas,bg="white", text= "Enter Name of Attributes "+'\n')
label2.pack()
Entry2 = Entry(canvas)
Entry2.insert(END, 'Neck')
Entry2.pack()
Entry2.focus_set() 


createFile = tk.Button(root,text="Create NFT", command=create , pady="5", fg="white", bg="#263D42")
createFile.pack()

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


# rare = tk.Button(root,text="Add Rare Items", command=addRareItems , pady="5", fg="white", bg="#263D42")
# rare.pack()

root.title ("NFT Generator")
# icon = PhotoImage(file="logo.png")
root.eval('tk::PlaceWindow . center')
root.mainloop()

# if __name__ == "__main__":
#    checkFiles()       