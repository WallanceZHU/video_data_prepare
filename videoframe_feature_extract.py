import os 
import os.path as osp
import numpy as np
import commands  
from collections import OrderedDict
root_dir = "/disk2/data/lsvc/trainval"
  
#INTERPRETER = "python"
processor = "python ./tools/video_compute_bottleneck.py"

#input_file_name = "/tmp/cat.jpg"  

#output_dict = {}
#out_file_name = "try.out"
#pargs = processor +" "+ input_file_name

path_walk = os.walk(root_dir)
print('path_walk: {} \n'.format(path_walk))
def main():
    for root,dirs,files in path_walk:
        print('--->enter dir: ' + str(root))
        #output_dict = {}
        if root!=root_dir and not root.startswith('.'):
        #if not root.startswith('.'):
           output_dict = {}
           save_name = root.split('/')
           save_numpy_name = save_name[-1]
           print('--->Processing dir: ' + str(root))
           for f in files:
               print f
               (filename,filetype) = osp.splitext(f)
               frame_num = int(filename.split('-')[1])
               cmd = processor +" "+osp.join(root,f)
               output = commands.getoutput(cmd).split('\n')
               output_dict[frame_num] = output[-1]
               print frame_num,output[-1]
           output_ordered = OrderedDict(sorted(output_dict.items(), key=lambda t: t[0]))
           output_list = list(output_ordered.values())
           print output_list
           save_path = osp.join('/disk2/data/lsvc/extracted_feature_data','{0}.npy'.format(save_numpy_name))
           np.save(save_path,output_list)
           c = np.load(save_path)
           print "displaying results"
           print c
if __name__ == '__main__':
   main()
#cmd = ''.join(pargs)
#print pargs
#pargs.extend(["--input=inputMd5s"]) 
#output = commands.getoutput(pargs).split(')')

#print output[len(output)-1]
    
