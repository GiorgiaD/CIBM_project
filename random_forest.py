# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:15:38 2018

@author: Giorgia
"""

# Required Python Packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score
from data_and_targets import *
from compute_features import *
 
import pdb
 
# File Paths
INPUT_PATH = "../Data_Txt"
OUTPUT_PATH = "../Figures"

def list_data_and_labels(which_dataset,balance):
    data_tono, data_anat, data_dupl, data_names, targets = define_data_and_labels(which_dataset,balance)
    return data_tono, data_anat, data_dupl, data_names, targets

def build_dataset(data_tono, data_anat, data_dupl, data_names, targets, which_dataset, which_fit = 'comb_tono_anat'):
    #features, targets, tot_test_size = compute_features(data_tono, data_anat, data_dupl, data_names, targets, which_dataset, which_fit = 'comb_tono_anat')
    features, targets = compute_features(data_tono, data_anat, data_dupl, data_names, targets, which_dataset, which_fit = 'anat_only')
    #return features, targets, tot_test_size
    return features, targets

def split_dataset(features, targets, train_percentage):
    """
    Split the dataset with train_percentage
    :param features:
    :param targets:
    :param train_percentage:
    
    :return: train_x, test_x, train_y, test_y
    """
 
    # Split dataset into train and test dataset
    print('shape of features',np.shape(features))
    print('len of targets',len(targets))
    
    train_x, test_x, train_y, test_y = train_test_split(features, targets, train_size=train_percentage)
    return train_x, test_x, train_y, test_y
 
 
def random_forest_classifier(features, target):
    """
    To train the random forest classifier with features and target data
    :param features:
    :param target:
    :return: trained random forest classifier
    """
    clf = RandomForestClassifier(n_estimators = 100, oob_score=True, class_weight = 'balanced')
    clf.fit(features, target)
    return clf
 
 
def dataset_statistics(dataset):
    """
    Basic statistics of the dataset
    :param dataset: Pandas dataframe
    :return: None, print the basic statistics of the dataset
    """
    print(dataset.describe())
 
 
def main(which_dataset = 'big_dataset',balance = True):
    """
    Main function
    :return:
    """
    # define the dataset type
    data_tono, data_anat, data_dupl, data_names, targets = list_data_and_labels(which_dataset,balance)
    
    print('target before',len(targets))
    
    
    # build the feature matrix
    #features, targets, tot_test_size = build_dataset(data_tono, data_anat, data_dupl, data_names, targets, which_dataset, which_fit = 'tono_only')
    features, targets = build_dataset(data_tono, data_anat, data_dupl, data_names, targets, which_dataset, which_fit = 'anat_only')
   
    print('features after',len(features))
    print('target after',len(targets))
    #print('total test size is', tot_test_size)
    
    # split the dataset
    train_x, test_x, train_y, test_y = split_dataset(features, targets, 0.8) # this is the previous version
    #test_x = features[0:tot_test_size,:]
    #train_x = features[tot_test_size+1:len(features),:]
    #test_y = targets[0:tot_test_size]
    #train_y = targets[tot_test_size+1:len(features)]
    
    # Train and Test dataset size details
    print("Train_x Shape :: ", train_x.shape)
    print("Train_y Shape :: ", len(train_y))
    print("Test_x Shape :: ", test_x.shape)
    print("Test_y Shape :: ", len(test_y))
 
    # Create random forest classifier instance
    trained_model = random_forest_classifier(train_x, train_y)
    print("Trained model :: ", trained_model)
    predictions = trained_model.predict(test_x)
    pred_prob = trained_model.predict_proba(test_x)
 
    for i in range(0, len(test_x)):
    #for i in range(0, 5):    
        print("Actual outcome :: {} and Predicted outcome :: {} with prob :: {}".format(list(test_y)[i], predictions[i], pred_prob[i]))
 
    #print("Train Accuracy :: ", accuracy_score(train_y, trained_model.predict(train_x)))
    print("Test Accuracy  :: ", accuracy_score(test_y, predictions))
    print(" Confusion matrix ", confusion_matrix(test_y, predictions)) 
    print("OOB score :: ", trained_model.oob_score_)
    # confusion matrix is a table layout that allows visualization of the performance of an algorithm 
    # each row represents the actual instance, while each column the predicted instance
    
    fpr, tpr, _ = roc_curve(test_y, pred_prob[:,1])


    plt.figure()
    plt.plot(fpr, tpr)
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.title('ROC curve')
    plt.show()
    

 
 
if __name__ == "__main__":
    main()