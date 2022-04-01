import progressbar
import time

progress = progressbar

for i in progress.progressbar(range(100)):
    time.sleep(0.2)
