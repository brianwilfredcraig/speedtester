@ECHO OFF
git pull
python speedtest.py
git add output_speedtest.csv
git commit -am "new results"
git push