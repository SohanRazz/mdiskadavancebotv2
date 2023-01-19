echo "Cloning Repo...."
git clone https://github.com/SohanRazz/mdiskadavancebotv2.git /mdiskadavancebotv2
cd /mdiskadavancebotv2
pip freeze > requirements.txt
pip3 install -U -r requirements.txt
cd /mdiskadavancebotv2
echo "Starting Bot...."
python3 main.py
