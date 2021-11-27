echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/SakirBey1/Group_Music_Bot /Group_Music_Bot
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/SakirBey1/Group_Music_Bot -b $BRANCH /Group_Music_Bot
fi
cd /Group_Music_Bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
