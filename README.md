# homepage
WIP.  
To do  
1. Add sqlite database to store the links  [done]  
   a. Card  
   b. Links  
   c. Shortcut   
   d. Images 
3. Implement Ajax for add and remove links
4. Image upload for shortcuts
5. Implement Ajax for new cards
6. Alignments and change colors
7. Config page 
   a. to add weather api keys and location details
   b. Search engines
   c. Personal link

# Homepage
A simple [flask](https://flask.palletsprojects.com/en/2.0.x/) server app that can be used to serve a homepage in the local machine(localhost). Simple project to review flask knowledge. It uses sqlite to store links locally. It is more like a local bookmark database. This is just a demo project to practise writting a basic python web application.  

## Download
`git clone https://github.com/fazillatheef/homepage.git`

## Usage 
Set environment variables
```bash
export SQLALCHEMY_DATABASE_URI=sqlite:///database.db
export FLASK_DEBUG=true
flask run
```

Then open [localhost:5000](http://localhost:5000) in the browser.

> *__Tip:__ Add the command in Windows scheduler to start the program after logging in*
