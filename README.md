# Masterthesis

## Description

Jupiter Notebooks scripts were created for the Master's thesis, which were used to analyze and evaluate the data. For detail information please read the description in the files.

The CSI data package with 70 CSI data files was provided by BSI. These files contain the recorded CSI raw data of movements of different persons, which are used in the following. 

### Preprocessing.ipynb

The Preprocessing.ipynb script is used to prepare the CSI data in raw format.

### PreprocessingControll.ipynb

The windows value for the hampel filter is calculated with this script. This process has been outsourced due to the long runtime. 

### PreprocessingCreateScenario10.ipynb

This script create the datasets for the scenario 10. This scenario contains a combination of different datasets.

### HyperParameterOptimization.ipynb

This script search the best hyperparameter for the machine-learning-algorithm

### MachineLearning.ipynb

This is the main machine-learnig script for the five algorithm

### Scripts for plot and reporting

The following three scripts create plots of 3D view of a scenario file, relationships, machine-learing results and reports the explained varianz

* CreatePlot3dAndRelationship.ipynb
* CreatePlotMachineLearingResults.ipynb
* ReportingExplainedVarianz.ipynb

### Scrips for explainable machine learning

This two scripts are used for explainable machine learing

* ExplainableMachineLearningEbm.ipynb

* ExplainableMachineLearningShap.ipynb


### SubOperationSystem.py

This file contains outsourced functions that are required by the scripts.

### Directorystructur

The directory structure is as follows

	Masterthesis/
	└── Dataset
	|	└── CsiFilesRah
	|		
	|
	└── Converted
	└── Results
	└── Scenario
	└── Plots
	

The directory "Dataset/CsiFilesRah" with the CSI data in raw format must be available. All other directorys are created automatically.
