# Text-Emotion-Classifier-using-NLP

In this project, I have created an application that classifies any text and displays the emotion behind the text.



For this I have implemented the application using Machine Learning Model - Logistic Regression, although the prediction given by the model was just 0.62 (approx), the end result was not too shabby.

Initially, I had created the model using a dataset for emotions which was accessible through kaggle. The datset was cleaned and formatted, filler words removed, and preprocessed as a whole. Further I had used a pipeline : The purpose of the pipeline is to assemble several steps that can be cross-validated together while setting different parameters. Now I save the .ipynb file as a pickle file.

This newly created pickle file is fed into app.py where we use the file to get the predicted data and portray it on the web application. For this streamlit was used to productionalize the application. Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

App.py also imports the data of track_utils.py, this file links the data which is so to be stored in a database file called as data.db (SQL)
