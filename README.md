# PolyGlot
Models for language indentification

README for PolyGlotTeam:

The following instructions provide guidelines for running each of the algorithms discussed in the written report. 
Full dataset preprocessed for each individual model is available on the following github repository:
https://github.com/saberkid/PolyGlot/tree/master

1. Baseline linear classification algorithm, fully implemented
Naive Bayes instructions (‘naive bayes’ subfolder):
1.	Run Jupyter Notebook console
2.	Open naive-Bayes.ipynb
3.	Run the code block by block 
4.	Data folder provides the training set, validation set used for accuracy testing

2. Nonlinear classification algorithm, fully implemented
KNN instructions (‘knn’ subfolder):
1.	Run Jupyter Notebook console
2.	Open KNN.ipynb
3.	Run the code block by block 
4.	Data folder provides the training set, validation set used for accuracy testing
Note: KNN takes a long time to run and takes up a large amount of memory space, some computers might experience memory error

3. Other methods: 
Required packages: keras 2.0.6, numpy 1.12.1, sklearn 
ANN instructions (‘ann’ subfolder):
1.	Run: python NN.py
2.	For test data, remove the comment at the end of the script

Random Forest instructions (‘randomForest’ subfolder):
1.	Run: python random_forest.py
2.	For test data, remove the comment at the end of the script

Decision Tree instructions (‘decision tree’ subfolder):
1.	Open DTree.py, running Anaconda distribution Python 2.7 through Spyder or equivalent.
2.	Make sure that test02.csv and train08.csv are in the same folder, or that they are navigated to correctly. 
3.	Run the classification, and this will give the decision tree results from the report.

Interpretation of results:
TA= Total accuracy
FC= Number of French entries classified as French (correct
FN= Number of French entries classified as Spanish (wrong)
SC= Number of Spanish entries classified as Spanish (correct)
SN= Number of Spanish entries classified as French (wrong)
