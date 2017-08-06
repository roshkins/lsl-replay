#Replay lsl data to view in lsl-viewer

First, load some data into the viewer `python3 ./scripts/static-lsl.py ../data/data_2017-06-30_18-30-29.csv` If your sample rate is not 220Hz, there is an optional 3rd argument. If it is 500Hz it might look like this: `python3 ./scripts/static-lsl.py ../data/data_2017-06-30_18-30-29.csv 500`

Then open lsl-viewer: `python3 lsl-viewer.py ` in a new terminal
