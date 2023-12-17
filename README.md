# CIDEPINT - Web Application

This web app addresses the need for a platform to showcase and provide services offered by different institutions in the field of Technology of Paints for CIDEPINT.

The project has been deployed on the servers of my university, and you can access it through these links should you wish to test its functionalities.

###### Link server admin: https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/

###### Link server portal: https://grupo06.proyecto2023.linti.unlp.edu.ar/

Please note: These servers may occasionally undergo shutdowns or maintenance.

## Overview
This web application comprises an internal administration system built using Python and Flask for both users and administrators. Additionally, it features a web portal developed with Vue.js. The web portal serves as a platform to search for services provided by registered institutions. The application relies on PostgreSQL as the database system and implements necessary APIs for queries and functionality.


###### Technologies Used
- **Backend:** Python, Flask, Oauth2, Bootstrap, SweetAlert2
- **Frontend:** Vue.js, Bootstrap, SweetAlert2, Leaflet.js
- **Database:** PostgreSQL
- **API Implementation:** Flask RESTful API


## Objective
The primary goal of this integrative project is to develop a web application that facilitates the registration and management of services offered by various institutions or Research and Development Centers in the realm of Paint Technology. These centers will include details such as names, descriptions, contact information, websites, social media links, and geographical locations.


## Application Functionality
The application will offer the following functionalities:

- **Service Search:** Users will access a search feature enabling them to find services provided by different institutions.
- **Organization Registration:** Entities or individuals can register their organizations and publish the services they offer.
- **Service Requests:** Users can place service requests, including equipment reservation or leaving a message to establish contact.
- **Order Tracking:** Tracking system for service requests placed by users.
- **Statistical Reports:** The application generates statistical reports showcasing the most requested services, high-demand areas, and unfulfilled service slots.



### Setup Instructions and Local deployment

##### 1. Clone the Repository
    git clone https://github.com/your/repository.git


##### 2. Backend Setup and initialize backend server
    cd admin
    poetry install (You need poetry for install all dependencies)
    poetry shell (to run the virtual environment)
    flask resetdb 
    flask seedsdb (loading seeds user and other elements)
    Flask run --debug (Mode development)


##### 3. Frontend Setup and initialize frontend server
    cd portal
    npm install
    npm run serve


##### 4. Accessing the Application
Once both backend and frontend servers are running, access the application through the specified localhost URLs.


##### Seeds users for admin web:

###### super-admin: 
    email: superadmin@gmail.com
    password: superadmin1234
    role: super-administrador

###### owner:
    email: mailuser1@gmail.com
    password: 1234
    role: owner

###### admin:
    email: mailuser3@gmail.com
    password: 1234
    role: administrador

###### operator:
    email: mailuser2@gmail.com
    password: 1234
    role: operador






