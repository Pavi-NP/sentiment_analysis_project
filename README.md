# Sentiment Analysis Project
## Project Overview
This project is an end-to-end Sentiment Analysis Web Application. It demonstrates the complete machine learning workflow—from obtaining raw data to deploying a production-ready web service. The process includes:
*	**Data Acquisition & Preprocessing**
*	**Model Building & Evaluation**
*	**Web Application Integration**
*	**Monitoring, Logging, Version Control, and Deployment**

## Detailed Workflow
### 1. Data Acquisition & Preprocessing
Data Preprocessing:
The raw dataset undergoes a series of text preprocessing steps to clean and standardize the input before feeding it to the model. Key steps include:
*	**Convert Uppercase to Lowercase**: Standardizes text by converting all characters to lowercase.
*	**Remove Links**: Eliminates any URLs to avoid noise.
*	**Remove Punctuations**: Strips punctuation marks that do not contribute to sentiment.
*	**Remove Numbers**: Deletes numbers which often do not affect sentiment analysis.
*	**Remove Stopwords**: Filters out common words (e.g., "the," "and") that add little informational value.
*	**Stemming**: Reduces words to their base or root form (e.g., "running" to "run").

Building Vocabulary:
After cleaning the text, the next steps involve:
*	**Divide Dataset**: Split the dataset into training and testing subsets to ensure reliable model evaluation.
*	**Vectorisation**: Convert text into numerical features using techniques like TF-IDF or word embeddings.
*	**Handle Imbalanced Dataset**: Apply strategies such as oversampling, undersampling, or using appropriate evaluation metrics if the dataset is imbalanced.
 
### 2. Model Training & Evaluation
A variety of machine learning classifiers are experimented with to determine the best approach for sentiment classification:
*	**Logistic Regression**:
    * **Build the Model**: Train the logistic regression model on the vectorised dataset.
    * **Testing Accuracy**: Evaluate its performance on the test data.
*	**Other Classifiers**:      
    * **Multinomial Naive Bayes**: Often effective for text data.
    * **Decision Tree**: Provides an interpretable model but may require tuning.
    * **Random Forest**: An ensemble method that improves accuracy and reduces overfitting.
    * **SVC (Support Vector Classifier)**: Uses a hyperplane to separate classes, effective for high-dimensional spaces.
Each classifier is evaluated using performance metrics such as accuracy, precision, recall, and F1-score to determine the best performing model for the sentiment analysis task.
 
### 3. Model Saving and Integration
*	**Model Saving**:
The best-performing model is serialized and saved as a pickle file. This file captures the trained model, making it easy to load later without retraining.
*	**Integration with Web Application**:
The saved pickle file is integrated into a web application through a helper script (helper.py). This script encapsulates the prediction pipeline by:
    *	**Loading the pickle file.**
    *	**Preprocessing new input data..**
    *	**Using the loaded model to predict sentiment..**
This integration makes the model accessible in a live web environment, allowing users to input text and receive sentiment predictions in real time.
 
### 4. Monitoring & Logging
Development Environment:
*	**Print Statements**: During initial development, simple print statements are used to monitor the workflow and debug any issues in the command prompt.
Production Environment:
*	**Logging Module**: For production deployment, Python’s logging module replaces print statements to provide a robust logging framework. The logging system records:
o	Debug: Detailed information for troubleshooting.
o	Info: Confirmation that the system is working as expected.
o	Warning: Indicators of potential issues.
o	Error: Critical issues affecting system functionality.
o	Critical: Severe problems that may stop the application.
*	**Logging Format**: A standard format is used for consistency:
format="%(asctime)s - %(levelname)s - %(message)s"
This format includes a timestamp, the level of the log message, and the message itself, making it easier to trace issues in production.
 
### 5. Version Control and Deployment
Version Control with GitHub:
*	**Code Push**: The entire project—including the data processing scripts, model files, and web application code—is pushed to GitHub. This ensures that the project is version controlled and enables collaboration.
Deployment to Production:
1.	Prepare Environment:
o	requirements.txt: All libraries and dependencies are listed in a requirements.txt file, ensuring that the production server replicates the development environment exactly.
2.	Deploying on Azure:
o	Azure Deployment Centre: The GitHub repository is connected to Azure via the Deployment Centre. This setup allows for continuous integration/continuous deployment (CI/CD), meaning that any updates pushed to GitHub are automatically deployed.
o	Production URL: The deployed web application is accessible through a URL, for example:
sentimentanalysisprojectp-gkc7g9hvgnfsbedm.canadacentral-01.azurewebsites.net
 
## Summary
*	**Comprehensive Pipeline**: The project covers everything from data preprocessing (converting case, removing unwanted elements, stopwords, and stemming) to vocabulary building, vectorisation, handling imbalanced datasets, and experimenting with various classification algorithms (Logistic Regression, Naive Bayes, Decision Tree, Random Forest, SVC).
*	**Model Integration**: The model is saved as a pickle file and integrated into a web app using a helper script, ensuring a smooth prediction pipeline.
*	**Monitoring & Logging**: Development uses print statements, while production leverages a detailed logging setup to monitor application performance.
*	**Version Control & Deployment**: The project is maintained on GitHub and deployed on Azure, with a clearly defined environment setup via requirements.txt.
This structured approach not only ensures high-quality sentiment analysis but also facilitates smooth deployment, continuous monitoring, and scalability in a production environment.

#### Getting help

If you have any questions or if you found any problems with this repository, please report through GitHub issues.
