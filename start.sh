echo "Cloning Repo...."
git clone https://github.com/SohanRazz/mdiskadavancebot.git /mdiskadavancebot
cd /mdiskadavancebot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py
