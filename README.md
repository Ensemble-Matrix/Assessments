### download model directory from google colab
```
!tar -czvf /tmp/models.tar.gz /tmp/1/
from google.colab import files
files.download('/tmp/models.tar.gz')
```
### serving tensorflow model
```
sudo docker run -it -p 8501:8501 -v /tmp/ramdisk/model/tmp/:/models/fashion_model/1 -e MODEL_NAME=fashion_model --entrypoint /bin/bash tensorflow/serving
```
### django app usage
```
mkdir assessment
python3 -m venv ./assessment
cd assessment
source bin/activate
git clone https://github.com/beinganukul/Assessments.git
cd assessment
pip install -r requirements.txt
python3 manage.py makemigrations imagemanipulation
python3 manage.py migrate imagemanipulation
python3 manage.py migrate 
python3 manage.py runserver
```
### to see predictions createsuperuser from django manage.py and login to /admin
### api endpoint to POST request actual image
```
/api/v1/send
# multipath form with image and actual_label
```
