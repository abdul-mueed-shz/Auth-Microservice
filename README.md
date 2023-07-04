<div align="center">
  <img src="https://media.giphy.com/media/077i6AULCXc0FKTj9s/giphy.gif" width="100"/>
</div>

<h1 align="center"><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>Auth Application</h1>

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
* The application uses refresh token rotation system for better security

## Advantages of Refresh Token Rotation System

Refresh token rotation system provides several advantages over the simple implementation of refresh and access tokens:

1. **Enhanced Security:** Refresh token rotation system ensures enhanced security by frequently rotating the refresh tokens. Even if the attacker gets hold of a refresh token, it will be of limited use as it will expire soon and a new token will be issued.

2. **Improved Reliability:** Refresh token rotation system leads to improved reliability of the system as access tokens have a shorter lifespan. This enables easy token rotation and issuance of new tokens in case of any issues without disrupting the user experience.

3. **Greater Robustness:** Refresh token rotation system makes the application more robust by making it less vulnerable to attacks. Frequent token rotation makes it difficult for attackers to gain long-term access to the system.

4. **Prevention of Hijacks:** Refresh token rotation system reduces the risk of hijacks as the frequent rotation of refresh tokens makes it harder for attackers to gain long-term access.

## Implementation of Refresh Token Rotation System

I have implemented the refresh token rotation system in our application to ensure better security, reliability, and robustness. The system works as follows:

1. Whenever a user logs in, the application generates an access token and a refresh token.

2. The access token has a short lifespan (e.g., 15 minutes), while the refresh token has a longer lifespan (e.g., 7 days).

3. When the access token expires, the user can use the refresh token to obtain a new access token. Upon successful retrieval of the new access token, the application issues a new refresh token and invalidates the previous one.

4. The refresh token is also rotated every time it is used to obtain a new access token.

By implementing the refresh token rotation system, we have ensured enhanced security, reliability, robustness, and prevention of hijacks in our application.



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

![login](https://github.com/Abdul-Mueed-Shahbaz/Auth-Application/assets/52679916/8487c82d-43ec-49d5-bcd0-a3ae8b1e4f11)
![signup](https://github.com/Abdul-Mueed-Shahbaz/Auth-Application/assets/52679916/5777e3e9-35bf-4ae1-a02e-ae10345b7129)
![loginError](https://github.com/Abdul-Mueed-Shahbaz/Auth-Application/assets/52679916/d762c931-7b6e-4bdf-90ac-d8f144f0fee6)
![signupError](https://github.com/Abdul-Mueed-Shahbaz/Auth-Application/assets/52679916/80bfd83d-0d33-4c3a-988d-2155c009b350)
![emailVerification](https://github.com/Abdul-Mueed-Shahbaz/Auth-Application/assets/52679916/68d4947c-afd0-46bc-abfa-b8fb3c0b93e6)
![otp](https://github.com/Abdul-Mueed-Shahbaz/Auth-Application/assets/52679916/8992541d-fefa-43ac-8094-11288c1f9abd)
![verificationEmail](https://github.com/Abdul-Mueed-Shahbaz/Auth-Application/assets/52679916/ca41e585-44e1-4266-be1c-daf4c6759b20)



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

