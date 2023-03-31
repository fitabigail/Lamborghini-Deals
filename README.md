## Project 4

# LamborghiniDeals

The Project is deployed [here](https://lamborghini-deals.herokuapp.com/)   
GitHub repository is [here](https://github.com/fitabigail/Lamborghini-Deals) 

![I am responsive](./readme_img/Iresponsive.jpg)

## TABLE OF CONTENTS
- [Aim of the website](#aim-of-the-website)
- [User Experience/User Interface](#user-experience-or-user-interface)
- [Design](#design)
- [Features](#features)
- [Testing](#testing)
- [Technology](#technology)
- [Deployment](#deployment) 
- [Credits](#credits)
- [Acknowledgement](#acknowledgement)

## Aim of the website
LamborghiniDeals is a website for selling second-hand Lamborghini. The user can quickly search for a specific car model, through the search bar on home page, or by more specific fields on the cars page. Also, the user can navigate on displayed cars, and choose a car post to have more details about. Once a car post is chosen the user can request more information by completing an inquiry form. To request more details about a car the user must be registered on the website. He can see his inquiries on the user dashboard, and update or delete the inquiry.  Options for selling a car are not available at the minute. But this would be a future feature where users can sell as well. 


## User Experience or User Interface

### Agile
The plan for this project was carried out using the Agile Methodology in Github. User Stories were created using the issues on the git hub. Each user story explicitly explains the purpose of the issues. Each user story is segmented into acceptance criteria and tasks. It was prioritised using GitHub labels with different colors. The labels are should have, could have and must have. Once the issues are created they are moved to the User Stories kanban board. The Kanban board has three main columns, To Do, In Progress and Done. Once you start working with the user story, you move it to the To Do column and when finished move it to the Done column. Following this pattern of work gives you a full-on idea about the progress of the project.

### Epic

The epics were created using the milistones on github. Each epic was created and related issues were added to it. There are four epics - 

- EPIC : CRUD Functionalities

    - USER STORY: Inquiry Add [[#13](https://github.com/fitabigail/Lamborghini-Deals/issues/13)]
    - USER STORY: View Inquiried [[#8](https://github.com/fitabigail/Lamborghini-Deals/issues/8)]
    - USER STORY: Update my Inquiry[[#10](https://github.com/fitabigail/Lamborghini-Deals/issues/10)]
    - USER STORY: Delete my Inquiry [[#12](https://github.com/fitabigail/Lamborghini-Deals/issues/12)]
    
    

- EPIC : Register & Login and Logout

    - USER STORY: Sign up [[#15](https://github.com/fitabigail/Lamborghini-Deals/issues/15)]
    - USER STORY: Register Account [[#4](https://github.com/fitabigail/Lamborghini-Deals/issues/4)]
    - USER STORY: Login and Logout [[#16](https://github.com/fitabigail/Lamborghini-Deals/issues/16)]


- Epic: Enable user interaction by providing site pagination, search, contact form, see the team 
    
    - USER STORY: Search car [[#17](https://github.com/fitabigail/Lamborghini-Deals/issues/17)]
    - USER STORY: Search car details [[#19](https://github.com/fitabigail/Lamborghini-Deals/issues/19)]
    - USER STORY: Site Pagination  [[#18](https://github.com/fitabigail/Lamborghini-Deals/issues/18)]
    - USER STORY: Contact us form [[#14](https://github.com/fitabigail/Lamborghini-Deals/issues/14)]
    - USER STORY: Team  [[#1](https://github.com/fitabigail/Lamborghini-Deals/issues/1)]

### Product Backlog 

- LamborghiniDeals Product Backlog

    - USER STORY: Forgot Password  [[#20](https://github.com/fitabigail/Lamborghini-Deals/issues/20)]
    - USER STORY: Like a post [[#7](https://github.com/fitabigail/Lamborghini-Deals/issues/7)]
    - USER STORY: Login with Google  [[#22](https://github.com/shahid129/mycar/issues/22)]
    - USER STORY: Login with Facebook  [[#21](https://github.com/fitabigail/Lamborghini-Deals/issues/21)]


### User Stories
**USER STORIES ARE EXPLAINED IN DETAILS IN [Testing](#testing) Section**
<details><summary>User Story Detailed</summary>

- Site Pagination
    - As a Site User I can view a paginated list of posts so that I can select the post I want to view. (must have / complete) [[#18](https://github.com/fitabigail/Lamborghini-Deals/issues/18)]
    
- Login and Logout 

    - As a Site User, I can log in and Logout from my account so that I can not request details about a car and like a post. (must have / complete) [[#16](https://github.com/fitabigail/Lamborghini-Deals/issues/16)]

- Search Car Details
    - As a Site User I can search for the cars I want so that I can click on each car to view car details.(must have / complete) [[#19](https://github.com/fitabigail/Lamborghini-Deals/issues/19)]

- Search Car
    - As a Site User, I can search for a specific car so that I can look only for the cars I am interested. (must have / complete) [[#17](https://github.com/fitabigail/Lamborghini-Deals/issues/17)]
    
- Sing up 

    - As a Site User, I can sign up for an account so that I can request details about a car and like a post. (must have / complete) [[#15](https://github.com/fitabigail/Lamborghini-Deals/issues/15)]

- Add Contact us Form
    - As a Site User/Admin, I can get in touch with the site owner so that I can complete the contact form to send a message.(must have / complete) [[#14](https://github.com/fitabigail/Lamborghini-Deals/issues/14)]

- Add new inquiry
    - As a Site User, I can add new inquiries on my dashboard so that I can look for a new car and request details about it.(must have / complete) [[#13](https://github.com/fitabigail/Lamborghini-Deals/issues/13)]

- Delete Inquiry
    - As a Site User/Admin, I can delete my inquiry on my dashboard so I can remove the car inquiry in which I am not interested anymore. (must have / complete) [[#12](https://github.com/fitabigail/Lamborghini-Deals/issues/12)]
    
- Update Inquiry 
    - As a Site User, I can edit my inquiry on my dashboard so that I can update the inquiry. (must have / complete) [[#10](https://github.com/fitabigail/Lamborghini-Deals/issues/10)]

- View Inquiery
    - As a Site User/Admin, I can view my inquiry on my dashboard so that I can read, update, or delete the inquiry.(must have / complete) [[#9](https://github.com/fitabigail/Lamborghini-Deals/issues/9)]

 - View request message
    - As a Site User / Admin I can view request messages on an individual post so that I can read the request.(duplicate / complete) [[#8](https://github.com/fitabigail/Lamborghini-Deals/issues/8)]

- View likes
    - As a Site User / Admin I can view the number of likes on each post so that can see which is the most popular or viral.(should have / complete) [[#7](https://github.com/fitabigail/Lamborghini-Deals/issues/7)]
    
- Open a post

    - As a Site User I can click on a post so that I can read the full text. (must have / complete) [[#6](https://github.com/fitabigail/Lamborghini-Deals/issues/6)]

- View post list
    - As a Site User I can view a list of posts so that rI can select one to read.(must have / complete) [[#5](https://github.com/fitabigail/Lamborghini-Deals/issues/5)]

- Account registration
    - As a **Admin** I can **see register account** so that **I can delete if I want**.(must have / complete) [[#7](https://github.com/fitabigail/Lamborghini-Deals/issues/7)]
    
- Manage posts

    - As a Site Admin I can create, read, update, and delete posts so that ** I can manage my site content**. (must have / complete) [[#3](https://github.com/fitabigail/Lamborghini-Deals/issues/3)]

- Add Team mebmber
    - As an admin I can create, update, and delete a team member's profile so that the user can see the team member profile online.(must have / complete) [[#1](https://github.com/fitabigail/Lamborghini-Deals/issues/1)]  
</details>      
   

</br>
</br> 

## Flowchart
---
<details>

![Flowchart](./readme_img/flow-chart.png)

</details>
</br>
</br>

## Features
---
The main objective of this project was to allow the users to have CRUD functionalities. The user can create an account where all his inquiries for individual car can be seen and not only they can update and delete any inquiry made by them. In addition the users have the option to search for the cars they are interested by main search bar and the search module which includes more searching options. The main pages of the website are Home, Cars, Services, Contact Us, Login, Singnup and registered user Dashboard.
Template of website is a boostrap template  [Carhouse](https://themeforest.net/item/car-house-car-dealer-template/17628233) customized for the website purpose.
</br></br>

* ## Top bar
The top bar includes contact information and links to Login / Sing Up when the user is not logged in and Dashboard / Logout. The topbar on big screens desktops and laptops on scrolling down the page are hidden, and for smaller devices is not displayed. The top bar is repeating on all the pages.

<details>

![Top Navbar](./readme_img/topbar_log_sing.png)
![Top Navbar](./readme_img/topnavbar-dash-log.png)

</details>
</br>

* ## Navbar
<br/>
Navbar includes links to the website pages and has two views. One is for bigger screens and one collapses for smaller screens. Besides on Navbar in Logo which is visible on all sizes of screens. Navbar is on all pages.
<ol>
<li>

### Navbar on screens

<details>

![Navbar Big screens](./readme_img/navbar_large.png)
![Navbar Small Screens](./readme_img/navbar_small.png)

</details>
</li>

<li>

### Logo

The website Logo is customized with the name of the website "LamborghiniDeals" and is linked with the home page. On the website are used a white and black logo, to be better seen on black and white background. The switch on the top page was enabled with javascript. </li>

<details>

![White Logo](./readme_img/white_logo.png)
![Black Logo](./readme_img/black_logo.png)

</details>

<li>

### Search
 User can search from a particular car model straigth from the search icon from navbar. Effect achived with javascript.</li>

<details>

![Search Bar](./readme_img/search_bar.png)

</details>
</ol>
</br></br>

* ##  Home Page
<ol>
<li>

### Carousel
On the home page, the banner section has a three-sliding car images carousel with a message and a link button to redirect the user to the Car page where the cars are listed.</li>
<details>

![Car 1](./readme_img/carousel_1.png)
![Car 2](./readme_img/carousel_2.png)
![Car 3](./readme_img/carousel_3.png)

</details>

<li>

### Latests Cars
The latest car section shows the cars on slick slide staiting with the latest added. From here the user can easy to click on the car he like and see more details about it.</li>
<details>

![Latests Cars](./readme_img/Slick-slide.png)
![Latests Cars mobile](./readme_img/slick-slide-mob.png)

</details>
<li>

### Team Executive
The pictures of the team are displayed with social links for contact, name and position heald on the company.
<details>

![Team](./readme_img/team.png)
![Team mobile](./readme_img/team-mobile.png)

</details>
</li>

<li>

### Question 

In this section, the user can ask for more information by accessing the contact page by clicking  GET IN TOUCH button.
<details>

![Question](./readme_img/question.png)
![Question mobile](./readme_img/question-mob.png)

</details>
</li>
<li>

### Footer
The footer is simple and include social media links.
<details>

![Footer](./readme_img/footer.png)
![Footer](./readme_img/footer-mob.png)

</details>


</li>
</ol>
</br>

* ## Cars Page
<ol>
<li>

### Car banner 

The banner has a display message, show what page you are and has a link to the Home page.
<details>

![Car Banner](./readme_img/car-banner.png)
![Car Banner Mobile](./readme_img/car-banner-mob.png)

</details>
</li>
<li>

### Car List

The cars are displayed four by page and paginated. By clicking an individual car the user will be redirected to to car details page.
<details>

![Car List](./readme_img/car_list.png)
![Car List Mobile](./readme_img/car-list-mob.png)

</details>
</li>
<li>

### Search Car List

The user can use the car fillter from search fileds by model, location, body style, transmision and price. From Search list the user is redirected to Search Car page. On Search page the user can redifine his car search options.
<details>

![Car List Search](./readme_img/car-list-search.png)
![Car List Search Mobile](./readme_img/car-list-search-mob.png)
![Search Page Mobile](./readme_img/search_page-mob.png)

</details>
</li>
</ol>
</br></br>

* ## Car Details Page

<ol>

<li>

### Car Details Banner
<details>

![Car Banner](./readme_img/car-detail-banner.png)

</details>
</li>
<li>

### Car details

On car details are all basic information about the car with the chance to Ask For More information by open the Inquiry modal.
<details>

![Car Description](./readme_img/car-detail-description.png)

</details>
</li>

<li>

### Car modal inquiry

The user can fill out the inquiry form to ask for more details about what is interesting. After he completes the inquiry and sends it, the user is redirected to the Dashboard
<details>

![Modal](./readme_img/modal.png)
![Modal Mobile](./readme_img/modal-mob.png)


</details>
</li>
</ol>
</br></br>

* ## Dasboard Page

On the dashboard page, the registered user has the chance to see their inquiries and review, update, and delete the inquiry.
<ol>
<li>

### Registred User


<details>

![Dashboard](./readme_img/dash-regu.png)
![Dasboard request exist](./readme_img/regu-dash-error.png)
![Update](./readme_img/update-succ-mob.png)
![Update Message Mobile](./readme_img/update-success-mob.png)
![Delete Message](./readme_img/delete-inquiri.png)


</details>
</li>
<li>

### Unregistred User
<details>

![Dashboard](./readme_img/unregistred-dashboard.png)
<details>
</li>
</ol>
</br></br>

* ## Sing up and Log In Page
<ol>
<li>

### Sing up 
<details>

![Sing Up](./readme_img/sing-up.png)
![Sing Up Registration](./readme_img/sing-up-reg.png)
![Sing Up Success](./readme_img/sing-up-success.png)
![Sing Up Mobile](./readme_img/sing-up-mob.png)



</details>

</li>
<li>

### Log In
<details>

![Log IN](./readme_img/login.png)
</details>

</li>
</ol>
</br></br>

* ### Services Page
Displays described services that the company can offer to their buyers.

<details>

![Services](./readme_img/services.png)
![Services](./readme_img/services-mob.png)
</details>
</br></br>

* ### Contact Us Page

The user can be sent messages to the website owner by filling out a Contact form.

<details>

![Contact Us](./readme_img/contact-us-mob.png)
![Contact Us Success](./readme_img/contact-fill-success.png)
</details>
</br>

* ## Future Features

The website offers the basics for searching and buying a car. For future I think to add more of then to gain a better  place on the market. The futures what I want to be added are listed below:

* Create a option to for a registred user to sell a car trough website;
* Create a forgot pasword option for users;
* A live chat facilitating user interaction on real time;
* A label to show which car are reserved or sold;
* A car renting option for special ocassions;
* A user profile.

</br></br>

## Database
---
</br>

* ### Data Model and Database Host
</br>
There are four data models in this project. Car Model, EnquiryForm Model, Contact Model and a Team Model. Team model and Car model has a one-to-many relationship, as well Car model has OneToMany one-to-many relationship with EnquiryForm model.
</br></br>
<ol>
<li>

### Data Model - Schema
<details>

![Database Diagram](./readme_img/DB_diagram.png)

</details></li>
</br>
<li>

### Database Host

- [ElephantSQL](https://www.elephantsql.com/)  
   Documentation for setting a database [here](https://www.elephantsql.com/docs/).
   </li>
   </ol>
</br>
</br>


## Testing
---
</br>
<details>

## Top bar
<br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Address and contact| Land Contact page| Pass|
|Login button| Land Login Page| Pass|
|Sing Up button| Land Sing Up page| Pass|
|Dashboard| Land Dashboard page| Pass|
|Logout| Log out the user| Pass|
</br>

## Navbar
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Logo|Land Home page| Pass|
|Home|Land Home page| Pass|
|Cars|Land Cars page| Pass|
|Services|Land Services| Pass|
|Contact|Land Contact page|Pass|
|Search icon|Open the search bar| Pass|
</br>

## Home
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Caroussel Slide Arow|Swich to next image| Pass|
|Caroussel Button|Land Car page| Pass|
|Latest Cars Arow|Slick to next car| Pass|
|Lates Car Item|Land Car Details page| Pass|
|Sale label, Miles, Year, Transmission and Car Title|Land Car Details page| Pass|
|Team social accounts|Land Facebook and Twitter page| Pass|
|Questions button|Land Contact page|Pass|
|Scroll up button| Scroll up the page | Pass|
</br>

## Footer
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Social links|Land social pages| Pass|

</br>

## Cars
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Banner home link|Load Home page| Pass|
|Car item| Load Car Details| Pass|
|Page no and arows| Flip between pages| Pass|
|Search by model| Show model| Pass|
|Search by location| Shows cars on same location| Fail|
|Search model by year| Shows cars on same year| Pass|
|Search model by body style| Shows cars on same body style| Fail|
|Search model by transmision| Shows cars on same transmision| Fail|
|Search model by price| Shows cars on same price| Fail|
|Social links| Open new social page| Pass|

</br>

</br>

## Search page
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Banner home link|Load Home page| Pass|
|Search by model| Show model| Pass|
|Search by location| Shows cars on same location| Pass|
|Search model by year| Shows cars on same year| Pass|
|Search model by body style| Shows cars on same body style| Pass|
|Search model by transmision| Shows cars on same transmision| Pass|
|Search model by price| Shows cars on same price| Pass|
|Social links| Open new social page| Pass|

</br>

## Service
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Banner home link|Load Home page| Pass|

</br>

## Contact
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Banner home link|Load Home page| Pass|
|Contact form button|Submit the form and show  success message| Pass|
|Required fields| No empty fields| Pass|

</br>

## Login
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|User field| Accept user| Pass|
|Password field| Accept password|Pass|
|Wrong User|Error message|Pass|
|Wrong password|Error message|Pass|

</br>

## Dashboard
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Add Inquiry button|Load Cars page| Pass|
|View Car button|Load Car Details page| Pass|
| Update button|Load update form| Pass|
|Delete button|Delete the inquiry|Pass|

</br>

## Update
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Update button|Submit updated inquiry| Pass|

</br>

## Sing UP
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Field required|No empty field| Pass|
|Email field|email format input| Pass|
|Password match| Message pasword not match| Pass|
|Register button|Submit the new user| Pass|
|Login here| Load login page|Pass|


</details>





















