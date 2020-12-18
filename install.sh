#!/bin/sh

separator="============================================="

header_msg="Installing requirements for project : Sauron"
contact_info="For any question please contact <adam.aquesbi@outlook.com>"


echo $separator
echo $header_msg
echo $separator

# =============


pip install flask
pip install Flask-SQLAlchemy
pip install requests
pip install numpy==1.19.3 # Numpy 1.19.4 does not pass a sanity check on Win10 (64 arch)
pip install Pillow
pip install Keras
pip install tensorflow # Warning : Not available for Python 3.9 yet
pip install sklearn
pip install psycopg2-binary

# =============

echo ""
echo ""
echo ""
echo $separator
echo $contact_info
