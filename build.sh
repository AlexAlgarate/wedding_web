source venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -fr public
unzip frontend.zip -d public
rm -f frontend.zip
echo ".web/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "venv/" >> .gitignore
echo ".env" >> .gitignore
deactivate