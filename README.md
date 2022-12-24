<div align="center">
  <img src="https://media.giphy.com/media/077i6AULCXc0FKTj9s/giphy.gif" width="100"/>
</div>

<h1><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>Authentication Application</h1>

<h4>A Full stack authentication application made using quasar 2 for frontend and django rest framework for backend. The application is made completely flexible to be coupled with any other application and implements jwt token authentication.</h4>



#
## How to couple the authentication application with another
* You can configure the app to be coupled by another app for authentication by adding the required information in COUPLED_APPS object in app.js
* The Coupled application's required information includes the application name, Icon's name to be displayed(Place the app icon in assets/icons) and the url of the application to be verified
* The jwt token recieved on successful authentication includes the user's email and id present in the login app's database. The coupled app needs to be configured in such a way that the token should be included in the HTTP request's header or cookie with the key of auth_token. The backend of the coupled app needs to implement the appropirate authentication mechanism to check the availibity/validity of the token


<h2>Main Features</h2>

* Complete input fields validation(Frontend)
* Input fields can easily be modified/added by changing the concerned objects in reactive.js file
* Completely responsive
* State managed properly using vuex
* Proper error handling
* The auth app redirects to the coupled app along with the auth_token property with the value of jwt token in the query string
* The application uses mysql as the database


<h2>Versions</h2>

* setup-t2: Has jwt authentication with access tokens. Access tokens expires within in a short span of time. Use this version for extremely simple applications
* version-2/master: Has jwt authentication with refresh and access tokens and the use of environment variable to secure vulnerable information. Create a .env file in the root directory of auth-api and populate it with the information which has to be used in the codebase but you don't want to expose publicly. This version also has email verification using otp during sign up. Users will not be able to sign up with random emails which offers improved security.



## Technologies used

<div style="display:flex">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
<img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white" />
<img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D" />
 
![Quasar](https://img.shields.io/badge/Quasar-16B7FB?style=for-the-badge&logo=quasar&logoColor=black)![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  
</div>


<h2><img  width="30px" src="https://www.animatedimages.org/data/media/491/animated-television-image-0115.gif" border="0" alt="animated-television-image-0115" />
  Screenshots</h2>

![login](https://user-images.githubusercontent.com/52679916/205466705-63f3bdee-a573-4ee4-b85e-f10fd6ec301e.PNG)
![LoginFieldErrors](https://user-images.githubusercontent.com/52679916/205466706-22de96c9-ee24-4257-9d88-79bc2535c771.png)
![SignUpFIeldErrors](https://user-images.githubusercontent.com/52679916/205466716-cab1fb15-f922-4046-986e-7a9c63d609e1.png)
![error1](https://user-images.githubusercontent.com/52679916/205466702-eba19489-9389-4dbe-96a8-46bc7929e4a3.PNG)
![error2](https://user-images.githubusercontent.com/52679916/205466704-7dca6294-7439-4024-9201-512e6c8587c3.PNG)
![Responsive](https://user-images.githubusercontent.com/52679916/205466709-a501798b-5900-4eca-9f60-d6c65e91c3da.png)
![Responsive3](https://user-images.githubusercontent.com/52679916/205466712-d47ade4b-a462-4516-b2f3-d1e8e7777ac2.png)


<h2><img width="30px" src="https://www.animatedimages.org/data/media/491/animated-television-image-0134.gif" border="0" alt="animated-television-image-0134" />


<h2><img width="30px" src="https://www.animatedimages.org/data/media/318/animated-computer-smiley-image-0080.gif" border="0" alt="animated-computer-smiley-image-0080" />  Commands:</h2>

##
Install the dependencies
(FrontEnd/gui)
```bash
yarn
# or
npm install
```
(BackEnd/api)
```
# Create virtual env by executing the setup.bat in the build folder
# Activate the venv by using the activate file in the build-env/scripts folder
# After completing the above mentioned steps
# Install the required packages by executing the following command
pip install -r .\requirements\bast.txt 
# Change the settings file if you want to change the database related information
# Use the manage.py file and execute the following commands to apply required migrations
python manage.py makemigrations 
python manage.py migrate
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```
### To start the server
```
python manage.py runserver 8000
```

### Lint the files
```bash
yarn lint
# or
npm run lint
```



### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js).

