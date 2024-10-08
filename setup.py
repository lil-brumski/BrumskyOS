import os
import subprocess

if not os.path.exists('build'):
   subprocess.run(["mkdir", "build"])
   subprocess.run(["cmake", ".."], cwd = "build")
   subprocess.run(["make"], cwd = "build") 
   print("Enter 'python run.py' file to run the executable located in the 'build' directory.")
else:
   subprocess.run(["cmake", ".."], cwd = "build")
   subprocess.run(["make"], cwd = "build")
   if os.path.exists("build/BrumSkyOS.o"):
      print("Enter 'python run.py' to run the executable located in the 'build' directory.")
   else:
      print("Error: BrumSkyOS.o wasn't built!")