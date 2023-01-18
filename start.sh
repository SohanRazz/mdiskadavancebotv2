if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone hhttps://github.com/SohanRazz/mdiskadavancebotv2 /mdiskadavancebotv2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /mdiskadavancebotv2
fi
cd /mdiskadavancebotv2
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
