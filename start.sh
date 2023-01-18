echo "Cloning Repo...."
git clonehttps://github.com/SohanRazz/mdiskadavancebot /mdiskadavancebot
cd /mdiskadavancebot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py
