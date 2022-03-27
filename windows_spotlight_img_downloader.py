import os
from getpass import getuser
from shutil import copyfile
user = getuser()
src='C:/Users/'+user+'/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
dist = 'C:/Users/'+user+'/Desktop/SpotLight Wallpaper'
if not os.path.exists(dist):
    os.mkdir(dist)
    
curr_img_list = []
file_list = os.listdir(src)

for file in file_list:
    if os.path.getsize(src+'/'+file) > 204800:
	    curr_img_list.append(file)
 
i = 1
for img in curr_img_list:
    old_dir = src+'/'+img
    new_dir = dist+'/img_'+str(i)+'.jpg'
    copyfile(old_dir, new_dir)
    i+=1
