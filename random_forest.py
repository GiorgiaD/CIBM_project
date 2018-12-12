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
from data_and_targets import *
from compute_features import *
 
import pdb
 
# File Paths
INPUT_PATH = "../Data_Txt"
OUTPUT_PATH = "../Figures"

def list_data_and_labels(which_dataset):
    data_tono, data_anat, data_dupl, data_names, targets = define_data_and_labels(which_dataset)
    return data_tono, data_anat, data_dupl, data_names, targets

def build_dataset(data_tono, data_anat, data_dupl, data_names, which_dataset, which_fit = 'comb_tono_anat'):
    features = compute_features(data_tono, data_anat, data_dupl, data_names, which_dataset, which_fit = 'comb_tono_anat')
    return features

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
    clf = RandomForestClassifier(n_estimators = 50)
    clf.fit(features, target)
    return clf
 
 
def dataset_statistics(dataset):
    """
    Basic statistics of the dataset
    :param dataset: Pandas dataframe
    :return: None, print the basic statistics of the dataset
    """
    print(dataset.describe())
 
 
def main(which_dataset = 'big_dataset'):
    """
    Main function
    :return:
    """
    # define the dataset type
    data_tono, data_anat, data_dupl, data_names, targets = list_data_and_labels(which_dataset)
    # build the feature matrix
    features = build_dataset(data_tono, data_anat, data_dupl, data_names, which_dataset, which_fit = 'comb_tono_anat')
    # split the dataset
    train_x, test_x, train_y, test_y = split_dataset(features, targets, 0.7)
    # Train and Test dataset size details
    print("Train_x Shape :: ", train_x.shape)
    #print("Train_y Shape :: ", train_y.shape)
    print("Test_x Shape :: ", test_x.shape)
    #print("Test_y Shape :: ", test_y.shape)
 
    # Create random forest classifier instance
    trained_model = random_forest_classifier(train_x, train_y)
    print("Trained model :: ", trained_model)
    predictions = trained_model.predict(test_x)
 
    for i in range(0, 5):
        print("Actual outcome :: {} and Predicted outcome :: {}".format(list(test_y)[i], predictions[i]))
 
    print("Train Accuracy :: ", accuracy_score(train_y, trained_model.predict(train_x)))
    print("Test Accuracy  :: ", accuracy_score(test_y, predictions))
    print(" Confusion matrix ", confusion_matrix(test_y, predictions)) 
    # confusion matrix is a table layout that allows visualization of the performance of an algorithm 
    # each row represents the actual instance, while each column the predicted instance
 
 
if __name__ == "__main__":
    main()