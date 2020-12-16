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


# =============

echo ""
echo ""
echo ""
echo $separator
echo $contact_info