# pyinstaller --onefile --noupx conda.py
# mv ./dist/conda.exe c:/abyss/bin/
import os, sys, subprocess
sys.argv[0] = 'C:\\Anaconda3\\Scripts\\conda.exe'
res = subprocess.run(sys.argv)
sys.exit(res.returncode)
