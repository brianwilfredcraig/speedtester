@ECHO OFF
python speedtest.py
git add output_speedtest.csv
git commit -am "new results"
git push