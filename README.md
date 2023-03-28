## Project 4

# LamborghiniDeals

The Project is deployed [here]( https://github.com/fitabigail/Lamborghini-Deals)   
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
   

