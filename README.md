![CI logo](static/assets/images/logo.png)

# Bridles & Biscuits Boarding

Bridle & Biscuit Boarding is a booking system for a short stay stables designed for people travelling without their equine companions. This  project is a Full Stack website built using Django. This stable booking website is built to allow users to book a stable online and leave reviews of their experience using our services. Users are required to register in order to book or leave a review. 

### MVP

The MVP for this project includes user registration, booking creation, and deletion to provide users with a easy to use booking system to book their mounts into Bridles and Biscuits Boarding. It also includes a review form with review creation, editing and deletion, so customers can leave reviews for future customers, to enable people to make an informed decision.

### Problem Statement

Problem statement: Owning your own horse or donkey is great but when you want to go on holiday, where can you get someone to take care of your horse. Many stables only do long term boarding and can you really trust someone coming in to check on them once or twice a day?

Purpose: Our site allows you to book your horse or donkey into a professionally run stables with highly qualified equine professionals for short stays, so that you can holiday in peace knowing your mount is fully cared for, supervised and safe.

Target audience: Horse or Donkey owners who normally keep their Horses and Donkeys in their own stable yards, when they want to or need to travel and are unable to take their Horses or Donkeys with them.

### Live Project Link

# User stories / Use Cases

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