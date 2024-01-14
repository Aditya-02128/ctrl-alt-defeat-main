import flask
import subprocess

txtcmd=["python","text_generator.py","cats"]
subprocess.run(txtcmd, stdout=subprocess.PIPE, text=True)
subprocess.run("voiceover_gen.py",shell=True)
subprocess.run("all_image_generator.py",shell=True)
subprocess.run("video_generator.py",shell=True)