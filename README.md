# Machine Learning for Healthcare - Homework 3
## Overview
The third homework of the course [Machine Learning for Healthcare](https://bmi.inf.ethz.ch/teaching/261-5120-00l-machine-learning-for-health-care-spring-2020/) deals with a medical image segmentation problem. We were tasked to do so with a [U-Net](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/) and as an additional hurdle to overcome, the different images could be rotated.

## Explanation of files
This explanation and all the other files are alternatively available on [GitHub](https://github.com/rostro36/ML4HC-HW3). The files should be used according to the appearence in this list.
- [report.pdf](https://github.com/rostro36/ML4HC-HW3/blob/master/report.pdf) has all the information and discussion to the project.
- [environment.yml](https://github.com/rostro36/ML4HC-HW3/blob/master/environment.yml) is the conda environment to run all the other files.
- [project3\_data/data/](https://github.com/rostro36/ML4HC-HW3/tree/master/project3_data/data) is the data folder we were given in the task description.
- [Data_augmentation.ipynb](https://github.com/rostro36/ML4HC-HW3/blob/master/Data_augmentation.ipynb) gives some visualizations on the data and adds rotations to augment the data. 
- [CV\_rotation.ipynb](https://github.com/rostro36/ML4HC-HW3/blob/master/CV_rotation.ipynb) is for the rotation attempt with computer vision techniques.
- [corrected/](https://github.com/rostro36/ML4HC-HW3/tree/master/corrected) is the folder containing the resulting images of the computer vision attempt.
- [UNET.ipynb](https://github.com/rostro36/ML4HC-HW3/blob/master/UNET.ipynb) generates the U-Nets. In the last cell you can give the hyperparameters to generate the U-Nets. The current values are for the grid and in comments are the hypervariables for the big model.
- [models/](https://github.com/rostro36/ML4HC-HW3/tree/master/models) is where the generated models are saved.
- [diagrams/](https://github.com/rostro36/ML4HC-HW3/tree/master/diagrams) holds schematics of the generated models.
- [Train_Evaluate_Unet_Iter_X_XX.ipynb](https://github.com/rostro36/ML4HC-HW3/blob/master/Train_Evaluate_Unet_Iter_1_nw.ipynb) are used to train and evaluate on the validation data. Each file is used for a different U-Net, the code given only differs in the "string", that encapsulates all the parameters and is also at the back of all other files, which are model specific.
- [Evaluate_Unet_Org_Testdata.ipynb](https://github.com/rostro36/ML4HC-HW3/blob/master/Evaluate_Unet_Org_Testdata.ipynb) finally tests the model on the test data.
