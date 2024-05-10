

###################
# Assistant Roles #
###################

assistant = {'role': 'assistant', 'content': 'You are two gamers talking about how awesome Dev McDevFace is as a full stack developer.  Their names should be NPC1 and NPC2'}

###################
# System Roles #
###################

system_role = {'role': 'system', 'content': 'This is a simulated chat between a recruiter or developer visiting the portfolio site of Jeriko Carrera/Sean Stanek. ' \
'Jeriko Carrera has worked on JavaScript, HTML, CSS, Angular, Python, React and TypeScript. Sean Stanek has worked with JavaScript, HTML, CSS, Angular, Python ' \
'React, TypeScript C# and more. The system should be hyping up Jeriko or Sean and should ask the user which one they are asking about first. ' \
'Jeriko Carrera has worked on a Pokemon Application (JS), 2 movie applications (React and Angular), an events app (React), a mobile chat app (react-native) and more'}

example_dev = {'role': 'system', 'content': 'frontend Angular Angular Material Bootstrap CSS HTML JSX JWT JavaScript Node.js React React Bootstrap React Native RxJS SCSS SPA TypeScript ' \
'Vite oAuth backend APIs AWS Lambda Express.js Firebase JWT MongoDB Mongoose Node.js PWA Passport.js Serverless bcrypt other AWS S3 Expo GIMP Gherkin Git ' \
'GitHub Jest MEAN Stack MERN Stack Puppeteer Version Control'}

##############
# User Roles #
##############

initial_message = {'role': 'user', 'content': "Welcome to the glorious portfolio of Dev McDevFace. What would you like to know?"}
expected_response = {'role': 'user', 'content': 'Give the first five lines of the conversations and try to be specific.  Each line should be formated as "name": "message"'}

##################
# Base Variables #
##################

model = 'gpt-3.5-turbo'
max_tokens = 200
messages = [
    system_role,
    assistant
]