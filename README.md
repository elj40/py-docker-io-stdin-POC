# py-docker-io-stdin-POC
Uses python and the subprocess module to run a docker container and send inputs through stdin

This repo show the proof of concept that you can have stdin into a docker running a python program that accepts input.

I noticed that it shows no output until the entire call has been completed, which could explain the simple pytohn repl acting weirdly. Maybe that can be figured out

I built a docker image called pythonio that contains app.py and runs it

parent.py does the Popen stuff to communicate with docker and get the outputs
