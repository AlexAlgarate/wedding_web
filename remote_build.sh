ls
echo "ESTAS SON LAS VARIABLES DE ENTORNO"
echo "VICKY_PHONE: $VICKY_PHONE"
python -m pip install --upgrade pip
pip install -r requirements.txt
rm -fr public
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
