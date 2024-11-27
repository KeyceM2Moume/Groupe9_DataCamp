#!/bin/bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add https://github.com/KeyceM2Moume/Groupe9_DataCamp
git push -u origin main
pip install --upgrade pip
pip install -r requirements.txt
pip freeze
