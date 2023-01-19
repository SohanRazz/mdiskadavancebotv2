echo "Cloning Repo...."
git clone https://github.com/SohanRazz/mdiskadavancebotv2.git /mdiskadavancebotv2
cd /mdiskadavancebotv2
pip freeze > requirements.txt
pip3 install -r requirements.txt
echo "Starting BOT..."
python main.py
