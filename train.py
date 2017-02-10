__author__ = "Laura Martinez Sanchez, Margherita Di Leo"
__license__ = "GPL 3"
__version__ = "2.0"
__email__ = "lmartisa@gmail.com, dileomargherita@gmail.com"



from mlh import *
from serialize import *

#from multiprocessing import Pool

# the pickle of the model is different from the clipshape
# here you can put None to create a new pickle, or the name of an existing pickle
picklemodel= "modelKNN"
pickleclip="clipfeat-4"
layer=4
Classifier = ImageClassifier(modeltype = 2, Threads = 4, picklemodel = picklemodel, model = None)
Mylist = read("pickle"+os.sep+"clip"+os.sep+pickleclip)
feat = Mylist[0]
nPixels = Mylist[1]
# if picklemodel == None:
#     MyName = pickleclip + "model"
# else:
#     MyName = picklemodel
Classifier.Train(feat,nPixels,layer,picklemodel)
