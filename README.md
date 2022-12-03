<div align="center">
  <img src="https://media.giphy.com/media/077i6AULCXc0FKTj9s/giphy.gif" width="100"/>
</div>

<h1><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>Authentication Application</h1>


<h4>A Full stack authentication application made using quasar 2 for frontend and django rest framework for backend. The application is made completely flexible to be coupled with any other application and implements jwt token authentication.</h4>



#
### How to couple the authentication application with another
* You can configure the app to be coupled by another app for authentication by adding the required information in COUPLED_APPS object in app.js
* The Coupled application's required information includes the application name, Icon's name to be displayed(Place the app icon in assets/icons) and the url of the application to be verified
* The jwt token recieved on successful authentication includes the user's email and id present in the login app's database. The coupled app needs to be configured in such a way that the token should be included in the HTTP request's header or cookie with the key of auth_token. The backend of the coupled app needs to implement the appropirate authentication mechanism to check the availibity/validity of the token
#

 Main Features</h2>

* Complete input fields validation(Frontend)
* Input fields can easily be modified/added by changing the concerned objects in reactive.js file
* Completely responsive
* State managed properly using vuex
* Proper error handling
* The auth app redirects to the coupled app along with the auth_token property with the value of jwt token in the query string
* The application uses mysql as the database

#

#
<h2><img  width="30px" src="https://www.animatedimages.org/data/media/491/animated-television-image-0115.gif" border="0" alt="animated-television-image-0115" />
  Screenshots</h2>

![intro](https://user-images.githubusercontent.com/52679916/197038116-db1fa56a-0796-4543-989d-d8d669471f4a.png)

<h2><img width="30px" src="https://www.animatedimages.org/data/media/491/animated-television-image-0134.gif" border="0" alt="animated-television-image-0134" />


<h2><img width="30px" src="https://www.animatedimages.org/data/media/318/animated-computer-smiley-image-0080.gif" border="0" alt="animated-computer-smiley-image-0080" />  Commands:</h2>

##
Install the dependencies
```bash
yarn
# or
npm install
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
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


### Technologies used

<div style="display:flex">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
<img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white" />
<img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D" />
</div>

#

Inspiration taken from [ saadpasta/developerFolio ](https://github.com/saadpasta/developerFolio).
