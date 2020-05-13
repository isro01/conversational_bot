import aiml
import os

kernel = aiml.Kernel()

# kernel.learn("std-startup.xml")
# kernel.respond("load aiml b")

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile= "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    #kernel.saveBrain("bot_brain.brn")

while True:
    print (kernel.respond(raw_input("enter your message ==> ")))


