1st file: Data_augmentation.ipynb
---------------------------------
In this file we create two augmented datasets, one with 20 random rotations/image (augmented_data_20) and the other with 
100 random rotations/image (augmented_data_100) and then we split these datasets in training and testing sets each. We use the 
augmented_data_20 set for grid hyperparameter search to be quicker and finally we train the best model on the augmented_data_100 dataset.


2nd file: UNET.ipynb
--------------------
In this file there is the implementation of our UNET. We have modified the decision/output function to predict 3 classes with softmax
activation and reshape our output to [sample size, 256*256, 3]. We use sparse categorical cross entropy as loss function.

*********************** HERE YOU CAN CHANGE THE FILTER AND DEPTH PARAMETERS BEFORE COMPILING (In[3]) ***********************


3rd file: Train_Evaluate_Unet.ipynb
-----------------------------------
In this file we load the train and test sets and the UNET we want to use. 
We compute the weights for each class based on the train set.
We normalize the input images to have values between 0 and 1.
We convert the training labels to categorical vectors.
We train the UNET.
We evaluate the UNET on the test set and compute overall precision, per-class precision, IoU and the Confusion Matrix.




