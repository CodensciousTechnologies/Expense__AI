# Expense__AI
Extract expense line items and other attributes

# Optical Character Recognition (OCR)

## INSTALLATION
Pre-request Anaconda (‘with python 3.6’) with Jupyter notebook

### Dependencies
#### tensorflow
conda install -c conda-forge tensorflow

### pandas
conda install -c anaconda pandas

### scikit-learn
conda install -c anaconda scikit-learn

### Keras
conda install -c conda-forge keras

### Django
conda install -c conda-forge keras

### Mysql
sudo apt install mysql-server

sudo mysql_secure_installation

sudo mysql

mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;

mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

mysql> FLUSH PRIVILEGES;

### To open database

mysql -u root -p

password= "password"

## Ocr setup
### Cloud_vision_api
pip install --upgrade google-api-python-client
pip install --upgrade google-cloud-vision
pip install --upgrade google-cloud

# Create Account & Enable the Vision API on cloud.google.com

1. Create your Gmail account specifically for this project or you can register in cloud.google.com using your existing Gmail id and click on console at top right corner.
2. You will get a pop-up, select Term of service and select your Country of residence, then agree and continue.





3. Creating a new project:

    a. In the GCP Console, go to the Manage resources page and select or create a project.




4. Enabling billing for your project.

    a. To create a new billing account:
    
       i. Open the console left side menu and select Billing.



Click the New billing account button. (Note that if this is not your first billing account, first you need to open the billing account list by clicking the name of your existing billing account near the top of the page, and then clicking Manage billing accounts.)


Enter the name of the billing account and enter your billing information. The options you see depend on the country of your billing address. Note that for United States accounts, you cannot change tax status after the account is created.


Click Submit and enable billing.

Enabling API’s
Open the console left side menu and select APIs & Services then Library.
 Select and enable given below API’s and billing for these individual API’s.
Google Cloud Functions
Google Cloud Pub/Sub
Google Cloud Storage
Google Cloud Translation API
Google Cloud Vision API




Create a service account key

For creating a service account key


Open the console left side menu and first click on APIs & Services and click on Credentials.
Now in the Credentials page click on create credentials button and then click on Service account key  option.
Now click on service account and select your “project name” from the dropdown list.
In the key type select JSON and then click on the create button. 
Now a JSON file has been downloaded which is your service account key.





Preparing Development Environment 



Prepare your development environment.

Objectives
Install the latest versions of Python 2 and 3
Install the Google Cloud SDK (optional)

Installing Python
Linux
Most Linux distributions include recent versions of Python. Install the appropriate packages for your distribution. For Debian and Ubuntu, these packages are python, python-dev, python3, and python3-dev:
sudo apt update
sudo apt install python python-dev python3 python3-dev
	
Now you can install packages and be confident that they won't affect other projects or your global Python installation:

pip install google-cloud-storage

Install the Google Cloud SDK (optional)
https://cloud.google.com/sdk/


This document shows how to prepare your server machine for Python development, including developing Python applications that run on Google Cloud Platform (GCP).
Preparing the application
Create a Cloud Storage bucket to upload your images, where YOUR_IMAGE_BUCKET_NAME is a globally unique bucket name:
	gsutil mb gs://YOUR_IMAGE_BUCKET_NAME


Create a Cloud Storage bucket to save the translations, where YOUR_TEXT_BUCKET_NAME is a globally unique bucket name:
	gsutil mb gs://YOUR_TEXT_BUCKET_NAME


Clone the sample app repository to your local machine:
	git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git


Change to the directory that contains the Cloud Functions sample code:
cd python-docs-samples/functions/ocr/app/



  Configure the app:
Edit the config.json file in the app directory to have the following contents:
{
"RESULT_TOPIC": "YOUR_RESULT_TOPIC_NAME",
"RESULT_BUCKET": "YOUR_TEXT_BUCKET_NAME",
"TRANSLATE_TOPIC": "YOUR_TRANSLATE_TOPIC_NAME",
"TRANSLATE": true,
"TO_LANG": ["en", "fr", "es", "ja", "ru"]
}
Replace YOUR_RESULT_TOPIC_NAME with a topic name to be used for saving results.
Replace YOUR_TEXT_BUCKET_NAME with a bucket name used for saving results.
Replace YOUR_TRANSLATE_TOPIC_NAME with a topic name to be used for translating results.


