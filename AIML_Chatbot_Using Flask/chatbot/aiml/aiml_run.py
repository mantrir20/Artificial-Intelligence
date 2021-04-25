import aiml
import os
from chatbot.models import User, Post
from chatbot import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


# kernel now ready for use
def getResponse(str):

    sessionId = current_user.id
    name = current_user.username
    address = current_user.address
    
    

    kernel = aiml.Kernel()
    

    if os.path.isfile("chatbot/aiml/bot_brain.brn"):
        kernel.bootstrap(brainFile = "chatbot/aiml/bot_brain.brn")
        print('in brain')
    else:
        kernel.bootstrap(learnFiles = "chatbot/aiml/std-startup.xml", commands = "load aiml b")
        kernel.saveBrain("chatbot/aiml/bot_brain.brn")
        print('hey_std')
    
    sessionData = kernel.getSessionData(sessionId)
    kernel.setPredicate("name", name, sessionId)
    kernel.setPredicate("location", address, sessionId)
    
    message = str
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("chatbot/aiml/bot_brain.brn")
    else:
        bot_response = kernel.respond(message, sessionId)
        print(bot_response)
        return bot_response