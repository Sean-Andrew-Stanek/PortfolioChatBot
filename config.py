# Used below for the bot
_max_tokens = 100

###################
# Assistant Roles #
###################
gamers_assistant = {'role': 'assistant', 'content': 'You are two gamers talking about how awesome Dev McDevFace is as a full stack developer.  Their names should be NPC1 and NPC2'}
Jeriko_fanboi = {'role': 'assistant', 'content': 'You are a huge fan of the web developer Jeriko Carrera.  Whenever something is asked, you get excited about giving answers with overly excessive exclamatories.'}


###################
# System Roles #
###################
# Token Count: 196
Jeriko_Carrera_Projects_Condensed = {'role': 'system', 'content': '''Jeriko's projects - Jeriflix (React): Movie app for account creation and info access using React, SCSS, JavaScript, React-Bootstrap; connects to database, hosted on Netlify. 
Jeriflix (Angular): Updated Jeriflix with Angular, same backend, includes Angular-Material.
Chat: Anonymous chat-room with React-Native, CSS, JavaScript; integrates Google OAuth, Firebase.
Meet: Events app linking to Google Calendar API via React, CSS, JavaScript; hosted on GitHub Pages.
Pokedex: Pokémon info web app using JavaScript, HTML, CSS; connects to PokeAPI.
Online Autho: Authorization form app with React-Native, Firestore/Firebase for customizable forms.
Portfolio: Showcases projects using React, SCSS, JavaScript.
CLI Recipe: CLI app in Python using MySQL, ORM for data management.
Movie API: Custom API for Jeriflix using Express, Node.js, MongoDB.
Recipe App: Django web app for recipe management, uses Python, SQL.'''}

system_role = {'role': 'system', 'content': 'This is a simulated chat between a recruiter or developer visiting the portfolio site of Jeriko Carrera/Sean Stanek. '}

example_dev = {'role': 'system', 'content': 'frontend Angular Angular Material Bootstrap CSS HTML JSX JWT JavaScript Node.js React React Bootstrap React Native RxJS SCSS SPA TypeScript ' \
'Vite oAuth backend APIs AWS Lambda Express.js Firebase JWT MongoDB Mongoose Node.js PWA Passport.js Serverless bcrypt other AWS S3 Expo GIMP Gherkin Git ' \
'GitHub Jest MEAN Stack MERN Stack Puppeteer Version Control'}

# tells the ai the token limit
token_restraints = {'role': 'system', 'content': f'keep the answer to {_max_tokens} tokens'}
conversation_restraint = {'role': 'system', 'content': 'Each line should be formated as \'name\': \'message'}



##############
# User Roles #
##############

initial_message = {'role': 'user', 'content': 'Welcome to the glorious portfolio of Dev McDevFace. What would you like to know?'}
expected_response = {'role': 'user', 'content': 'Give the first five lines of the conversations and try to be specific.'}
anecdotal_story = {'role': 'user', 'content': 'Have a funny anecdote about Dev McDevFace as a conversation'}
left_suggestions ={'role': 'user', 'content': 'Give the user suggestions on things they could ask in relation to the portfolio of the developer.'}
right_suggestions ={'role': 'user', 'content': 'Give the user suggestions on things they could ask in relation to the personal life of the developer.'}


##################
# Base Variables #
##################

model = 'gpt-3.5-turbo'
max_tokens = _max_tokens
messages = [
    Jeriko_fanboi,
    Jeriko_Carrera_Projects_Condensed,
    token_restraints,
]
