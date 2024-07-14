![logo](static/assets/images/logo.png)

# Bridles & Biscuits Boarding

Bridle & Biscuit Boarding is a booking system for a short stay stables designed for people travelling without their equine companions. This  project is a Full Stack website built using Django. This stable booking website is built to allow users to book a stable online and leave reviews of their experience using our services. Users are required to register in order to book or leave a review. 

### MVP

The MVP for this project includes user registration, booking creation, and deletion to provide users with a easy to use booking system to book their mounts into Bridles and Biscuits Boarding. It also includes a review form with review creation, editing and deletion, so customers can leave reviews for future customers, to enable people to make an informed decision.

### Problem Statement

Problem statement: Owning your own horse or donkey is great but when you want to go on holiday, where can you get someone to take care of your horse. Many stables only do long term boarding and can you really trust someone coming in to check on them once or twice a day?

Purpose: Our site allows you to book your horse or donkey into a professionally run stables with highly qualified equine professionals for short stays, so that you can holiday in peace knowing your mount is fully cared for, supervised and safe.

Target audience: Horse or Donkey owners who normally keep their Horses and Donkeys in their own stable yards, when they want to or need to travel and are unable to take their Horses or Donkeys with them.

### Live Project Link


# Agile Development
I planned and tracked progress on this project using Agile methodology. I created a kanban board with GitHub Projects to manage the workload. 
After setting up the user stories as issues for my project I broke them down into smaller tasks with check boxes within each user story, to help me monitor my progress and finish all tasks on time.

To see the Kanban for the Bridles & Biscuits  Boarding project please click here: https://github.com/users/Charlie-Lambino-Worthington/projects/4


## User stories / Use Cases

User story:

As a user I want a welcoming homepage which tells me a bit about Bridles and Biscuits Boarding, its owners, it’s location and its ethos.

Use case:

User can get a basic overview of Bridles and Biscuits Boarding as a business. Leaving a good first impression.

Acceptance criteria

·         Logo

·         Welcoming colour scheme

·         Neat and elegant

·         Information about the owners

·         Information about the stables and its ethos

·         Images of owner and happy horses at Bridles and biscuits boarding

·         Location, and map

·         Links to social media

Tasks

o   Design logo

o   Decide on colour scheme and implement

o   Create html page for home with neat layout and elegant font

o   Information section about the stables and it’s ethos with image of happy horses there

o   Information section about the owners with images of owner looking friendly

o   Address and map so stables are easy to find

o   Footer with social media links

User Story:

As a user I want a facilities page which tells what Bridles and Biscuits Boarding offers.

Use Case:

Gives user an idea of the facilities available for their horses and donkeys and provide prices for a stable per night. Allowing them to make an informed decision based on the available facilities.

Acceptance criteria

·         Sand school

·         Cross country route

·         Walker

·         stable block

·         45 achers of grazing land with shelters and auto refilling water troughs

·         Homemade horse “biscuits” 

 

Tasks

o   Separate sections for each of the above features describing them and showing pictures of them in use

User Story:

As a user I want a booking form so that I can book a stay for my horse or donkey at bridles and biscuits boarding.

Use Case:

Allows users to input all required information into the bookings form so that the stable staff can look after the horses and donkeys according to their specified needs and give owners peace of mind.

Acceptance criteria

·         Only fillable when logged in

·         Input for horse/ donkey name

·         Input for feeding requirements

·         Input for exercise requirements

·         Input for start date

·         Input for end date

·         Creates a unique booking ID

·         Sends an email confirmation with cost, booking id and booking details

Tasks

o   Only fillable when logged in

o   Input for horse/ donkey name

o   Input for feeding requirements

o   Input for exercise requirements

o   Input for start date

o   Input for end date

o   Creates a unique booking ID

o   Sends an email confirmation with cost, booking id and booking details

o   Calculates cost of booking based on stable price per night and stay duration

User Story:

As a user I want a page to see my booking details so I can check them on the website.

Use Case:

Provides users with the ability to check their booking details and delete/cancel bookings as required.

Acceptance criteria

·         Displays all bookings from logged in user

·         Displayed in order of recency

Tasks

o   Only displays bookings from the logged in user

o   Displays in order of recency

o   Displays all booking details

User Story:

As a user I want a log in/out and register function so that only I can access my details.

Use Case:

Restricts access to private information and booking details and ensures the user is logged in when booking and reviewing so that their booking details are linked to their account for ease of access when checking booking details.

Acceptance criteria

·         Forms only fillable when logged in

·         Booking details only viewable when logged in

·         Reviewing only possible when logged in

·         Log in/out and register page matches formatting and styling of the rest of the site.

Tasks

o   Log in and log out and register using allauth

o   Email confirmation required

o   Styling matches the rest of the site

o   Reviews viewable without login

o   Leaving reviews, booking and viewing bookings only when logged in.

User Story:

As a user I want a reviews page so that I can make an informed decision based on other people’s experiences at Bridles and Biscuits Boarding

Use Case:

Allows customers to make an informed decision and leave reviews for future customers.

Acceptance criteria

·         View star ratings and comments left by previous customers when not logged in

·         Ability to leave a star rating and review when logged in

·         Only able to leave a review with a valid booking id so users know all reviews are from real previous customers

·         Booking IDs not displayed with the reviews

Tasks

o   View star ratings and comments left by previous customers when not logged in

o   Ability to leave a star rating and review when logged in

o   Only able to leave a review with a valid booking id so users know all reviews are from real previous customers

o   Booking IDs not displayed with the reviews



# UX Design

## Design
## Wireframes
Home Page
![Index page](static/assets/images/homewire.png)
Facilities Page
![Facilities page](static/assets/images/facilitieswire.png)
Book Now Page
![Booking page](static/assets/images/bookwire.png)
Your Bookings Page
![Your Bookings page](static/assets/images/yourbookingswire.png)
Reviews Page
![Reviews page](static/assets/images/reviewswire.png)
Edit Reviews Page
![Edit Review page](static/assets/images/editwire.png)
Log In Page
![Log in page](static/assets/images/signinwire.png)
Log Out Page
![Log out page](static/assets/images/signoutwire.png)
Register Page
![Register page](static/assets/images/signupwire.png)

## Database Diagram
Bridle & Biscuit Boarding's database is composed of several distinct tables, each serving a specific purpose. The tables are comprised of Users, Book, Stable_availability, Stables, Review. Together, they allow potential customers to easily complete CRUD functionality (Create, Read, Update, Delete) through an intuitive web-based user interface.

The User table is key to the interconnectivity of the backend of the application. It connects other tables through foreign key relationships,allowing for the functionality and cohesion of the system. Within the database, the book model and Reviews model  are linked to users through  Foreign Key relationships, allowing users access to view and delete bookings as well as create, edit, and delete reviews associated with their account.

![Database schema](static/assets/images/stablesbooking.png)




# Testing
## Responsiveness
## Manual Testing

#### Booking form testing

| Test |Result  |
|--|--|
| User can book if all fields filled correctly | Pass |
| User cannot submit booking form if horse name left blank | Pass |
| User cannot submit booking form if feeding requirements left blank | Pass |
| User cannot submit booking form if booking start date is in the past | Pass |
| User cannot submit booking form if booking end date is before start date | Pass |
| User cannot submit booking form if number of nights left blank | Pass |
| User cannot submit booking form if email field left blank | Pass |
| User cannot submit booking form if email field filled incorrectly | Pass |
| Messages show if form filled incorrectly | Pass |
| Booking form only visible to logged in user | Pass |

#### Review form testing
| Test |Result  |
|--|--|
| User can review if all fields filled correctly | Pass |
| User cannot submit edit review form if review title left blank | Pass |
| User cannot submit edit review form if review rating left blank | Pass |
| User cannot submit edit review form if review rating is not between 1-5 | ? |
| User cannot submit edit review form if review content left blank | Pass |
| User cannot submit edit review form if booking ID not selected | Pass |
| Messages show if form filled incorrectly | Pass |
| Review form only visible on reviews left by logged in user | Pass |

#### Review Edit form testing
| Test |Result  |
|--|--|
| User can edit review if all fields filled correctly | Pass |
| User cannot submit edit review form if review title left blank | Pass |
| User cannot submit edit review form if review content left blank | Pass |
| User cannot submit edit review form if review rating is not between 1-5 | Pass |
| Messages show if form filled incorrectly | Pass |
| Edit Review buttons only visible on reviews left by logged in user | Pass |




## Validation
### HTML

| Page | Validator | Result |
|--|--|--|
| Index | ![Database schema](static/assets/images/indexhtmlvalid.png) |Pass  |
| Facilities | ![Database schema](static/assets/images/fachtmlvalid.png) | Pass |
| Booking form | ![Database schema](static/assets/images/bookhtmlvalid.png) | Pass |
| Reviews | ![Database schema](static/assets/images/reviewhtmlvalid.png) | Pass |
| Bookings | ![Database schema](static/assets/images/bookinghtmlvalid.png)  | Pass |
| Log out | ![Database schema](static/assets/images/outhtmlvalid.png) | Pass |
| Log in | ![Database schema](static/assets/images/inhtmlvalid.png) | Pass |
| Register | ![Database schema](static/assets/images/registerhtmlnotvalid.png) | Fail |

The errors being picked up in the register page validator are in the automatic files imported from allauth. I was unable to find the errors to correct or locate these errors.

### CSS

| Page | Validator | Result |
|--|--|--|
| CSS | ![Database schema](static/assets/images/cssvalid.png) |Pass  |

### Python

| File | Validator | Result |
|--|--|--|
| Project Urls.py | ![Database schema](static/assets/images/prourlspyvalid.png) |Pass  |
| Settings.py | ![Database schema](static/assets/images/settingspyvalid.png) | Pass |
| Views.py | ![Database schema](static/assets/images/viewspyvalid.png) | Pass |
| urls.py | ![Database schema](static/assets/images/urlspyvalid.png) | Pass |
| forms.py | ![Database schema](static/assets/images/formspyvalid.png)  | Pass |
| models.py | ![Database schema](static/assets/images/modelspyvalid.png) | Pass |
| admin.py | ![Database schema](static/assets/images/adminpyvalid.png) | Pass |


### Javascript

| File | Validator | Result |
|--|--|--|
| reviews.js | ![Database schema](static/assets/images/bookjsvalid.png) |Pass  |
| book.js | ![Database schema](static/assets/images/reviewjsvalid.png) | Pass |

The Warnings picked up in the Javascript validator where down to the version of Javascript being used, as arow functions and template literals are only available in ES6. It also wasn't keen on bootstrap as a variable.



# Deployment
## GitHub Repository
This stable booking site was developed using the GitPod editor and uploaded to the GitHub remote repository called 'Bridle-Biscuit-Boarding' 

For this development, the following Git commands were used in order to push the code to this repository:
<ol>
<li>git add .  to include all edits made in the editor into the staging area before they are commited.</li>
<li>git commit -m “commit message”  to save the changes in the staging area to the local repository, preparing them to be pushed to GitHub.</li>
<li>git push command was utilized to upload all committed code to the remote repository on GitHub.</li>
</ol>

## Heroku Deployment

The website was successfully deployed using Heroku applications. The deployment process:
<ol>
<li>Upon opening the Heroku website click "New" to create a new app.</li>
<li>Give the app name and set your region, click the Create app button.</li>
<li>In the Settings click Config Vars and set up the following config variables:

SECRET_KEY: (Your secret key)

DATABASE_URL: (Your database url)

CLOUDINARY_URL: (Your cloudinary storage url)</li>
<li>Set the deployment type as Github and enter the repository name to connect them.</li>
<li>Then go to the Manual Deploy section,  select the main branch and click the Deploy Branch button.
Once the development phase is successful, the application will undergo a deployment process to Heroku, which may take some time.</li>
</ol>













# Credits and acknowledgements
## Pictures

Three Brown Horses in Pasture by Gantas Vaičiulėnas on Pexels

A Female Equestrian Competing in an Event by TheOther Kev on Pexels

Barn, Horse stable, Nature image by Stefan Schweihofer on Pixabay

Iceland, Horse, Pony image on Pixabay

A Man Making a Horseshoe by Lucian Pirvu on Pexels

Woman holding brown horse's bridle by Vadim Fomenok on Unsplash

Three horses grazing in a field at sunset by EmmaLi Millard on Unsplash

Sandschool on https://www.poleanfarm.co.uk/wp-content/uploads/sites/19/2013/10/Sand-School.jpg



Raymond Penners for amazing Allauth and Allauth templates
Roger Pfäffli, Code Institute Alumnus for explaining on Slack how to set up development and DEBUG variables in env.py
Coding Yaar for Bootstrap navbar toggler colour change tutorial
May.D from Stack Overflow for date validation
Tutors Jason and Oisin for pointing me in the good direction and helping with understanding the code parts I've been struggling with
My mentor Narender Singh for his patience and all the help and support
willeM_ Van Onsem for helping me with fixing my edit booking class