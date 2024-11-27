#!/bin/bash
pip install --upgrade pip
rustc --version
pip install --no-cache-dir -r requirements.txt
pip install -r requirements.txt
pip freeze
pip install tokenizers
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add https://github.com/KeyceM2Moume/Groupe9_DataCamp
git push -u origin main


