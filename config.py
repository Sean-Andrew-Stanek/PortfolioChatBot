###################
# Assistant Roles #
###################


system_role = 'This is a simulated chat between a recruiter or developer visiting the portfolio site of Jeriko Carrera/Sean Stanek. ' \
'Try and re-word your responses from the actual data that you have stored. Use relaxed and casual language. it should be professional but not uptight or robotic. ' \
'When the user first says anything, ask them if they want to hear about Jeriko or Sean.'

Jeriko_Carrera_Projects = "Jeriflix (React) is a movie application where users can create accounts and access movie information. Utilizing React, SCSS, JavaScript, and React-Bootstrap, it connects to its own database. The application is hosted on Netlify. The username and password for access are both 'KingdomCome'. " \
"Jeriflix (Angular) is an updated version of the Jeriflix movie application, using Angular as its framework while maintaining the same backend. It offers similar functionalities to Jeriflix (React) with additional features provided by Angular-Material." \
"Chat is an anonymous chat-room application built with React-Native, CSS, and JavaScript. It integrates Google's OAuth and Firebase for authentication and real-time database functionality. "\
"Meet is an events application designed to connect with Google's Calendar API. Developed using React, CSS, JavaScript, and hosted on GitHub Pages, it offers tools for event creation and management. "\
"Pokedex is a web application created with raw JavaScript, HTML, and CSS, connecting to the PokeAPI to provide information about Pokémon. It's a simple and intuitive way to learn about various Pokémon species. "\
"Online Autho is an authorization form application built using React-Native and Firestore/Firebase. It enables organizations to create customizable authorization forms. "\
"Portfolio is a showcase of projects created by the developer. Utilizing React, SCSS, and JavaScript, it offers insights into the developer's work and progress. "\
"CLI Recipe is a command-line interface application developed in Python. It uses MySQL databases and an ORM for data management. "\
"Movie API is a custom API constructed for the Jeriflix websites. It's built with Express and Node.js, facilitating interactions with MongoDB. "\
"Recipe App is a Django-based web application allowing users to log in and explore or add recipes. Developed with Python and SQL, it offers a seamless recipe management experience."

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
