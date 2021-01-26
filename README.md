[![Build Status](https://travis-ci.com/KTM28/Banyan-Ayurveda.svg?branch=main)](https://travis-ci.com/KTM28/Banyan-Ayurveda)
# Banyan Ayurveda
The Live website for this Project is [here](https://banyan-ayurveda.herokuapp.com/)

This Project is created as part of the 4th Milestone Project of The FullStack Software Development Bootcamp offered by The [Code Institute](https://codeinstitute.net/)
### Project Overview
Banyan Ayurveda is a traditional Ayurvedic herbal dispensary and treatment center. It uses the principle of the ancient Ayurvedic knowledge originated in India more than 5,000 years ago. It's website is an expansion of its physical store where people can buy ayurvedic medicines or book a treatments and pay online. It's goal is also to increase awareness in the community and improve the health and wellbeing of the people.

---
## Table of contents

1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)
2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
3. [**Information Architecture**](#information-architecture)
    - [**Data Modelling**](#data-modelling)
4. [**Technologies Used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Libraries and Frameworks**](#libraries-and-frameworks)
    - [**Tools**](#tools)
    - [**Databases**](#databases)
5. [**Testing**](#testing)
6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Heroku Deployment**](#heroku-deployment)
7. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Content and Media**](#content-and-media)
    - [**Acknowledgements**](#acknowledgements)
8. [**Disclaimer**](#disclaimer)
---
## UX
### Project Goals

##### Target Audience
* People who are inclined to look after their health and wellbeing in the most natural way.
* People who trust and are interested in Alternative and traditional medicine sciences.
* People who want to learn and adapt to natural and healthy lifestyles.
* people who care about the surrounding nature and environment and find the connection to it.
* People who have not succeeded in curing their ailments with other available forms of medicines.
* People who are curious of traditional eastern medicines, lifestyles and cultures.

##### Visitor goals:
* To learn more about Ayurveda and its benefits.
* To find connection with individuals and community who are inclined to learning and applying Ayurvedic Knowledge into their lives.
* To be able to purchase any products or treatments displayed in the site safely and securely.

##### Business goals(site owner's goals):
* Generate awareness in the community of Ayurvedic medicines and practices.
* Create a surrounding community attached to ayurvedic principles.
* provide the opportunity for the local community to experience a traditional eastern way of lifestyles.
* Help the community and make a profit by selling natural ayurvedic medicines and treatments.

#### User Stories

##### User
* As a user, I want to be able to access the website from a computer or other device.
* As a user, I expect the website to be easy to navigate, so I can find what I'm searching for quickly.
* As a user, I look for social media link to the social pages of the company to find more trust in the company.
* As a user, I would like to be able to register or login with my social account.
* As a user, I want to find company stuff, to know what they are doing, what their core values and ideas are.
* As a user, I want to see the location of the store on the map, and the store contact details.
* As a user, I want to be able to easily contact the store owner should any query or curiosity arises.
* As a user, I want to be able to understand the information about the products and services the company is providing.
* As a user, I want to know the benefit of using the products and services the company is providing.
* As a user, I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.
* As a user, I would like to be able to purchase an item or services from the store without having to signup or sign in.
* As a user, I would like to view or modify my order in the cart before purchasing it.
* As a user, I want to be able to see the total price and delivery cost for the item I have added to my cart.
* As a user, I expect that I'm charged correctly and via the secure method for any purchase I make.
* As a user, I would expect to receive an email confirmation of the order I have completed.
* As a user, I would like to have a customised user profile page where I would be able to complete few tasks when logged in:
(Change Password/ Add&Edit shipping details/ View the blog posts that are written by me / View my past order and order details)
* As a user i would like to save my shipping info and personal details at the checkout to avoid re-fill of the same info for all subsequent purchases in the store site when logged in.
* As a user, I would like to learn more about the Ayurveda to be familiar and connected with the community that surrounds it by having access to a blog post.
* As a user, I would like to be able to search for a blog post I'm interested in.
* As a user, I would like to be able to create/update/delete my blog post when logged in.
* As a user, I would like to see the list of the blog post of the author that I am interested in.
* As a user, I would like to be able to comment and like a blog post that I find insightful.
* As a user, I would like to see how many people have viewed or liked the blog post that I'm reading. 
* As a user, I would like to be able to subscribe to the newsletters for latest news, promotion, and offers the store provides.
##### Admin
* As an admin, I would like to be able to sign in from any page.
* As an admin, I would like to be able to add/update/delete the products and services as necessary.
* As an admin, I would like to have control over the community space and guidelines by being the sole author of the categories user can post a blog into.
* As an admin, I would like to view all the orders placed in the site.
* As an admin, I would like to see the list of email addresses of users who have to subscribe to newsletters.
* As an admin, I would like to see the list of users who have registered into the site.

### Design
##### Framework
* [Bootstrap](https://getbootstrap.com/), is applied to this project to develop the frontend of the project such as navbar, cards, image-responsiveness, layouts and various other components of the project.
* [Jquery](https://jquery.com/), is used in conjunction with the bootstrap for initializing its components. 
##### Color Scheme
- ![#f9d6b0](https://placehold.it/15/f9d6b0/f9d6b0)
- ![#745330](https://placehold.it/15/745330/745330)
- ![#ff9d05](https://placehold.it/15/ff9d05/ff9d05)
- ![#f3725ec5](https://placehold.it/15/f3725ec5/f3725ec5)
- ![#f2d900](https://placehold.it/15/f2d900/f2d900)
- ![#000](https://placehold.it/15/000/000)
- ![#3FA291](https://placehold.it/15/3FA291/3FA291)

##### Typography
 [Following Google Fonts](https://fonts.google.com/) were used across the site:
 - [Rokkitt](https://fonts.googleapis.com/css2?family=Rokkitt&display=swap) 
 - [Oswald](https://fonts.googleapis.com/css2?family=Oswald&display=swap) 
 - [Grandstander](https://fonts.googleapis.com/css2?family=Grandstander&display=swap) 
 - [Playfair Display](https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap) 
 
##### Icons
- [Fontawesome](https://fontawesome.com/)
- [Icons8](https://icons8.com/)
 
### Wireframes
 
The wireframes for this project can be found - [Here](https://github.com/KTM28/Banyan-Ayurveda/tree/main/wireframes).

###### back to [top](#table-of-contents)

---

## Features

### Existing Features

#### Signup and Login page
The signup page allows users to register an account with the site. The authentication logic of this is handled by Django allauth package. The users can also signup via their **Google account**. When the form is submitted, a verification email is sent to the user's email to verify the email and finish the registration process.

The login page is also somewhat similar to the signup page as it's authentication logic is also handled by Django allauth package. The users can also login via their **Google account**.

#### Navbar
The site has a navigation menu at the very top of the page allowing the user to navigate the site with ease and to signup and sign in into the page. The logo is displayed at the centre of the navigation menu. The logo also serves as a **link** to be redirected to the landing page from any page of the site. The Navbar's link to the **cart page** displays a cart icon and total amount for the product or services the user have added into their cart.

On smaller screen sizes (tablets and mobile) the navbar collapse into an icon. On clicking the icon the nav scrolls from the right side of the device displaying all the menu item. The cart links always stay outside for users to be able to monitor the total price in their cart and to navigate to cart page as necessary.

#### Toast Notification
The site displays a notification to the users on the top right corner in desktop and medium-size device and top of the page in mobile devices for actions such login/register, add to cart items, update items quantity, delete items and any other error messages.

#### Footer
The Footer has been divided into three sections the first consists of **Subscription Form and button**. Next, it has all the contact details with icons - the **map icons** directs users to the Contact page and the **telephone** icon serves as a click to call link.
The last section on Footer consists of social media icons linking a user to the respective sites.


#### Landing Page 
The landing page consists of the Hero Image and an intro text with **buttons** which redirects users to the About page of the site. On Scroll It has furthermore text with some animation, images and buttons that take a user to shop page and treatments page. It also has a Feature section with eye-catching icons and pieces of information for users to read. Finally, the last section of the page consists of customer review displayed on a carousel.    

#### About Page
The About Page displays images and information of the company boasting it's **goal, purpose and business ethics**. The images in about page are assigned with a simple on scroll animation. 

#### Shop Page 
The shop Page lists all items displayed in an individual card with some mouse hover effect. The top of the page consists of **free delivery threshold information/ A Product search container/ A Category menu** for the shop items. The Item cards consist of item image with a colourful badge displaying item price and ratings for the item. It has two buttons one to view details of the item and the other to add items into the cart.

The product detail page shows a large image of the item, it's **descriptions and a quantity form** with add to cart buttons and button linking back to shop page. The users can update the quantity of the items from here or directly from the cart page.

If the logged-in user is **granted an admin or staff** of the page then there are two links with icons on the top of the item that allows the user to edit or delete the item as necessary. 

#### Treatments Page
The treatment page lists out all the available treatments provided by the store. Users can navigate into each displayed treatments and look for **descriptions and benefit** of the treatments. It also has a form to select **appointment date** which the users must fill in before adding the treatment into the shopping cart.

If the logged-in user is **granted an admin or staff** of the page then there are two links with icons on the top of the item that allows the user to edit or delete the treatments item as necessary. 

#### Blog Page
The Blog Page list out all the **blog post** in the site displayed on a card background together with a **category navigation menu** sitting beside it or on top in mobile screens. A **search form** on the top of the blog page allows users to search any blog in the site. 

When a user is **logged in** there is also a link for users to **create a blog**. The blog title serves as a link to the blog details page. The **Author name and icon** on the blog page serves as a link to direct logged in users to page displaying all the list of the author's blog posts. The card also shows **posted or updated date** for the blog. And Users can also see how many likes, views and comments are there for the blog post.

**Blog Categories Page** is displayed on the category selection of the blog.
At the very top of the blog page are breadcrumbs links for ease of navigation for the user. 

The blog detail page shows all the content of the blog post **featuring like and comments function for logged in users**. The view counts **only adds** for a logged-in user. When the user clicks the like icon twice then the like count just decrements to the original like of the post. If the logged-in user is the **owner of the blog** then there are two icon links right below the blog image on the blog detail page allowing the user to edit or delete the blog post.

#### Contact Page
 The Contact Page consists of a store location displayed in **google map** with customised icon and beside it is a **contact form** to contact the store. Below the Form, there is contact information with click to call link for the store.

#### Profile Page
The Profile page can be accessed via the link displaying the **user icons**. The **Profile dashboard** displays functionality to **change password or shipping details** for logged in user. The user can also see the list of their **blog posts and order history** on the profile dashboard. Clicking on the order number the user will be directed to the page displaying the past confirmation of their orders. Clicking on the blog post the user will be directed to the Blog detail of that blog.

#### Cart Page
Cart page can be accessed by all the users on the site. It displays image, price, quantity, SKU, and date if the selected item is treatment. Users can easily **update or remove items from the cart page as necessary** via the form and links. There are two buttons at the page allowing a user to navigate to checkout or shopping page as necessary.

#### Checkout Page
The checkout page can only be accessed using cart page once the user has added at least one item from the site to the cart.
The checkout page consists of checkout form with user's name, email and shipping details. If a user is **logged** in and already has a profile with the shipping information saved, the form will be pre-populated with this information.

Below the checkout form, users can put in their card details and complete the order. As the website is made for **educational purpose**, therefore, the payment functionality is limited to testing only. Use **4242 4242 4242 4242** for successful test payments.

Beside the checkout form, user can view their order summary which includes **item, quantity, price, delivery cost and total**. There is also a link for the user to navigate back to the cart page if the users wish to adjust the item in their cart.

#### Product and Service management
The links to these pages are **exclusively displayed to page admin and users granted such status**. These links can be found directly under the login and register links when the admin user is logged in. Under product management, the authorised user can access a form to **add a new product** into the online store and under service management the authorised user can access a form to **add a new service** into the store's treatment facility.

## Features left to implement
There are some features that I could not implement due to time constrain. These features were kept aside when developing as i considered to first implement features those that are necessary for the goal of the site.
* Add image library for each item for the customer to view more than one image of the items.
* Allow site admin to enable or disable any time slot for treatments that are booked in already.
* Allow users to also login/register via Facebook.
* Add a star-based review/rating section under each product and treatments for users to post a review after the purchase.
* Allow user to add profile image or choose an avatar instead to display in the profile dashboard and comment sections.
* Add pagination on the shop page and blog page.

###### back to [top](#table-of-contents)
 ---
# Information Architecture

## Data Modelling

#### Profile App

##### Profile

 | Name            | Database Key          | Field Type    | Validation                                   |
|:---------------:|:---------------------:|:-------------:|:--------------------------------------------:|
| User            | user                  | OneToOneField | on_delete=models.CASCADE                     |
| Phone number    | default_phone_number  | CharField     | max_length=20, null=True, blank=True         |
| Address Line 1	 | default_address_line1 | CharField     | max_length=80, null=True, blank=True         |
| Address Line 2  | default_address_line2 | CharField     | max_length=80, null=True, blank=True         |
| Town or City    | default_town_or_city  | CharField     | max_length=40, null=True, blank=True         |
| Postcode        | default_postcode      | CharField     | max_length=20, null=True, blank=True         |
| County          | default_county        | CharField     | max_length=80, null=True, blank=True         |
| Country         | default_country       | CountryField  | blank_label='Country', null=True, blank=True |

#### Blog App

##### Category
| Name | Database Key | Field Type | Validation                 |
|:----:|:------------:|:----------:|:--------------------------:|
| Name | name         | CharField  | max_length=250, default='' |

##### Blog
| Name            | Database Key | Field Type    | Validation                     |
|:---------------:|:------------:|:-------------:|:------------------------------:|
| Blog title      | title        | CharField     | max_length=100                 |
| Blog category   | category     | CharField     | max_length=150                 |
| Blog content    | content      | RichTextField | blank=True, null=True          |
| Image thumbnail | thumbnail    | ImageField    | ( )                            |
| Publish date    | publish_date | DateTimeField | auto_now_add=True              |
| Last updated    | last_updated | DateTimeField | auto_now_add=True              |
| Blog author     | author       | ForeignKey    | User, on_delete=models.CASCADE |
| Slug            | slug         | SlugField     | unique=True                    |

##### Comment
| Name      | Database Key | Field Type    | Validation               |
|:---------:|:------------:|:-------------:|:------------------------:|
| User      | user         | ForeignKey    | on_delete=models.CASCADE |
| Blog      | blog         | ForeignKey    | on_delete=models.CASCADE |
| Timestamp | timestamp    | DateTimeField | auto_now_add=True        |
| Content   | content      | TextField     | ( )                      |

##### Blog View
| Name      | Database Key | Field Type    | Validation               |
|:---------:|:------------:|:-------------:|:------------------------:|
| User      | user         | ForeignKey    | on_delete=models.CASCADE |
| Blog      | blog         | ForeignKey    | on_delete=models.CASCADE |
| Timestamp | timestamp    | DateTimeField | auto_now_add=True        |

##### Like
| Name  | Database Key | Field Type | Validation               |
|:-----:|:------------:|:----------:|:------------------------:|
| User  | user         | ForeignKey | on_delete=models.CASCADE |
| Blog  | blog         | ForeignKey | on_delete=models.CASCADE |

#### Product App

##### Product
| Name           | Database Key   | Field Type    | Validation                                                                             |
|:--------------:|:--------------:|:-------------:|:--------------------------------------------------------------------------------------:|
| Category       | category       | ForeignKey    | 'Category', null=True, blank=True, on_delete=models.SET_NULL                           |
| Sku            | sku            | CharField     | max_length=254, null=True, blank=True                                                  |
| Name           | name           | CharField     | max_length=254                                                                         |
| Description    | description    | RichTextField | max_length=1200                                                                        |
| Benefit        | benefit        | RichTextField | max_length=800, null=True, blank=True                                                  |
| Price          | price          | DecimalField  | max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)]                   |
| Rating         | rating         | DecimalField  | max_digits=2, decimal_places=1, validators=[MinValueValidator(0),MaxValueValidator(5)] |
| Is a treatment | is_a_treatment | BooleanField  | default=False                                                                          |
| Discontinued   | discontinued   | BooleanField  | default=False                                                                          |
| Image          | image          | ImageField    | null=True, blank=True                                                                  |
| Image url      | image_url      | URLField      | max_length=1024, null=True, blank=True                                                 |
| Duration       | duration       | IntegerField  | null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(24)]        |

##### Category
| Name          | Database Key  | Field Type | Validation                            |
|:-------------:|:-------------:|:----------:|:-------------------------------------:|
| Name          | name          | CharField  | max_length=254                        |
| Friendly Name | friendly_name | CharField  | max_length=254, null=True, blank=True |

#### Newsletters App

##### MarketingSubs
| Name      | Database Key | Field Type    | Validation        |
|:---------:|:------------:|:-------------:|:-----------------:|
| Email     | email        | EmailField    | ( )               |
| Timestamp | timestamp    | DateTimeField | auto_now_add=True |


#### Checkout App

##### Order
| Name           | Database Key  | Field Type    | Validation                                                                |
|:--------------:|:-------------:|:-------------:|:-------------------------------------------------------------------------:|
| Order Number   | order_number  | CharField     | max_length=32, null=False, editable=False                                 |
| User Profile   | user_profile  | ForeignKey    |  on_delete=models.SET_NULL,  null=True, blank=True, related_name='orders' |
| Full Name	     | full_name     | CharField     | max_length=70, null=False, blank=False                                    |
| Email          | email         | EmailField    | max_length=254, null=False, blank=False                                   |
| Phone number	  | phone_number  | CharField     | max_length=20, null=False, blank=False                                    |
| Address Line1	 | address_line1 | CharField     | max_length=60, null=False, blank=False                                    |
| Address Line2	 | address_line2 | CharField     | max_length=60, null=False, blank=False                                    |
| Town or City	  | town_or_city  | CharField     | max_length=50, null=False, blank=False                                    |
| County         | county        | CharField     | max_length=50, null=True, blank=True                                      |
| Country        | country       | CountryField  | blank_label='Country *', null=False, blank=False                          |
| Postcode       | postcode      | CharField     | max_length=20, null=True, blank=True                                      |
| Purchase Date	 | purchase_date | DateTimeField | auto_now_add=True                                                         |
| Delivery Cost	 | delivery_cost | DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                     |
| Order Total	   | order_total   | DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                    |
| Grand Total	   | grand_total   | DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                    |
| Original Cart	 | original_cart | TextField     | null=False, blank=False, default=''                                       |
| Stripe Pid	    | stripe_pid    | CharField     | max_length=254, null=False, blank=False, default=''                       |

##### Order Line Item
| Name             | Database Key   | Field Type   | Validation                                                                  |
|:----------------:|:--------------:|:------------:|:---------------------------------------------------------------------------:|
| Order            | order          | ForeignKey   | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product          | product        | ForeignKey   | null=False, blank=False, on_delete=models.PROTECT                           |
| Datetime         | datetime       | CharField    | null=True, blank=True, max_length=20                                        |
| Quantity         | quantity       | IntegerField | null=False, blank=False, default=0                                          |
| Line item total	 | lineitem_total | DecimalField | max_digits=6, decimal_places=2,null=False, blank=False, editable=False      |
###### back to [top](#table-of-contents)
---
## Technologies Used
 
### Languages
1. ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
 - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.

2. ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
 - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - used as the base for markup text.

3. ![JavaScript](https://img.shields.io/badge/javaScript--yellow)
 - [JavaScript](https://www.javascript.com/) -  is a scripting or programming language that allows you to implement complex features on web pages.

4. ![jQuery](https://img.shields.io/badge/jQuery-3.5.1-yellowgreen)
 - [jQuery](https://jquery.com/) - is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.

5. ![Jinja](https://img.shields.io/badge/Jinja2-2.11.2-red)
 - [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - a full featured template engine for Python.

6. ![Phyton](https://img.shields.io/badge/Python-3.8.5-blue)
 - [Python3](https://www.python.org/downloads/release/python-385/) - is a scripting language.

#### Libraries and Frameworks
- [Django](https://www.djangoproject.com/) - Python framework for building the project.
- [Bootstrap 4](https://getbootstrap.com/) - is a framework for building responsive, mobile-first websites.
- [FontAwesome](https://fontawesome.com/) - is a font and icon toolkit based on CSS and Less. It was used to provide icons across the website.
- [jQuery](https://jquery.com/download/) - to simplify DOM manipulation and to initialize Bootstrap function.
- [Psycopg2](https://pypi.org/project/psycopg2/) - is the most popular PostgreSQL database adapter for the Python programming language.
- [Tempus Dominus](https://pypi.org/project/django-tempus-dominus/) - to use datetime picker.
- [Gunicorn](https://gunicorn.org/) - a Python WSGI HTTP Server to enable deployment to Heroku.
- [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/overview)- For rendering map into the site.
- [Coverage](https://coverage.readthedocs.io/en/coverage-5.1/) - to see the percentage of the automated testsing.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - to style Django forms.
- [Google Fonts](https://fonts.google.com/) - to access fonts.
- [Stripe](https://stripe.com/ie) - to handle financial transactions.

### Tools
 - [Vscode](https://code.visualstudio.com/) - an online IDE for developing this project.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://github.com/) - for remotely storing project's code.
- [Travis](https://travis-ci.org/) - for integration testing.
- [ImgBB](https://imgbb.com/) - to host images for products and treatments 
- [Icons8](https://icons8.com/) - for adding icons.
- [Balsamiq](https://balsamiq.com/) - to create wireframes.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [flake8](https://flake8.pycqa.org/en/latest/) - a python code linting tool to refactor the code.
- [Heroku](https://dashboard.heroku.com/apps) - to host the project.
- [AWS S3 Bucket](https://aws.amazon.com/) - to store static and media files in prodcution.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for compatibility with AWS.

### Databases
- [SQlite3](https://www.sqlite.org/index.html) - a development database.
- [PostgreSQL](https://www.postgresql.org/) - a production database.

###### back to [top](#table-of-contents)
 ---
## Testing
Testing information can be found in a separate [TESTING.md](https://github.com/KTM28/Banyan-Ayurveda/blob/main/TESTING.md) file

---

## Deployment
The project was developed using the [Vscode](https://code.visualstudio.com/) IDE and using [Git](https://git-scm.com/) & [GitHub](https://github.com/) for version control. It is hosted on the Heroku platform, with static files and user-uploaded images being hosted in AWS S3 Basket.
### Local Deployment
To be able to clone this project there are a few things you will need.
- An IDE of your choice 
- [Git](https://git-scm.com/)  - Install Git, installation docs and be found here
- [PIP](https://pip.pypa.io/en/stable/installing/) - install pip, installation docs can be found here
- [Stripe](https://stripe.com/ie) to integrate payment system
- [AWS](https://aws.amazon.com/) to setup S3 basket
- [Gmail](https://mail.google.com/) account with app secret key.

Once The Git and Pip files installed -

1. From the terminal create a directory you want to work in.
`$ mkdir <filename>`
2. Change into Directory
`$ cd <filename>`
3. Clone the repository from github.
`$ git clone https://github.com/KTM28/Banyan-Ayurveda`
4. Change into banyan_ayurveda directory.
`$ cd banyan_ayurveda`
5. Install virtualenv
`$ pip install virtualenv`
6. Create a virtual environmanet(env)
`$ virtualenv env`
7. Activate env with
`$ source env/Scripts/activate`
8. In banyan folder make a .env file  and add the variables below
 ```
import os  
- os.environ["DEVELOPMENT"] = "True"    
 - os.environ["SECRET_KEY"] = "<Your Secret key>"    
- os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
- os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
- os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"    
- os.environ["GOOGLE_MAP_KEY"] = "<Your Google Map key>" 
```
Read more about how to set up the Stripe keys in the [Stripe Documentation](https://stripe.com/docs/keys)

9. Install all requirements from the **requirements.txt** file putting this command into your terminal:     
`pip3 install -r requirements.txt`  
10. In the terminal in your IDE migrate the models to create a database using the following commands:    
`python3 manage.py makemigrations`
11. Load the data fixtures(**categories**, **products**, **blogs**) in that order into the database using the following command:    
`python3 manage.py loaddata <fixture_name>`
12. Create a superuser to have an access to the the admin panel(you need to follow the instructions then and insert username,email and password):    
`python3 manage.py createsuperuser`
13. Finally, run the application using the following command:     
`python3 manage.py runserver`     
14. To access the admin panel, add /admin to your localhost url.
###### back to [top](#table-of-contents)
### Heroku Deployment
*To Deploy to heroku, firstly the project needs to be cloned as described in the [Local deployment](#local-deployment) section above.*  
1. Navigate to [Heroku](https://dashboard.heroku.com/apps)
2. Install the Heroku Command Line Interface (CLI) from the official heroku site.
3. Click on the **New** button.
4. Click - **Create New App**.
5. Create a corresponding app name that is use to deploy the application. The apps name must be **unique**.
6. Pick a server location that is closest to you.
7. Once the app is created click on the resources button and choose the Heroku Postgres to attach a postgres database to your project.
8. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:    
`pip3 freeze > requirements.txt`
9. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:      
`web: gunicorn banyan_ayurveda.wsgi:application` 
10. To run the app on Heroku install Guniorn a (WSGI HTTP Server), dj-databas-url to connect with PostgreSQL and Psycopg(PostgreSQL adapter)
`$ pip install Gunicorn, dj-database, Psycopg`
11. To migrate to the postgres db. First import dj-database-url at the top of the setting.py.
12. Then comment out the default database configuration and add:
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('< Put your DATABASE_URL here >'))
}
```
13. In Heroku Settings click on Reveal Config Vars and set the config variables there:

| Key                   | Value                                     |
|-----------------------|-------------------------------------------|
| AWS_ACCESS_KEY_ID     | <your aws access key>                     |
| AWS_SECRET_ACCESS_KEY | <your aws secret access key>              |
| DATABASE_URL          | <your postgres database url>              |
| EMAIL_HOST_PASSWORD   | <your email password(generated by Gmail)> |
| EMAIL_HOST_USER       | <your email address>                      |
| EMAIL_HOST_USER       | <your google map key>                     |
| SECRET_KEY            | <your secret key>                         |
| STRIPE_PUBLIC_KEY     | <your stripe public key>                  |
| STRIPE_SECRET_KEY     | <your stripe secret key>                  |
| STRIPE_WH_SECRET      | <your stripe wh key>                      |
| USE_AWS               | True                                      |

14.  Migrate the database models to the Postgres database using the following commands in the terminal:
`python3 manage.py makemigrations`
`python3 manage.py migrate`

15. Load the data fixtures(**categories**, **products**, **blogs**) in that order into the database using the following command:    
`python3 manage.py loaddata <fixture_name>`
16. Create a superuser for the Postgres database by running the following command
`python3 manage.py createsuperuser`
17. After the completion of the step change database configurations to:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
18. Add your Heroku app URL to ALLOWED_HOSTS in the settings.py file. 
19. In the terminal run:
`$ heroku login`
20. After adding and comitting to Git, run the following command:
`$ git push heroku master`
15. When the deployment is successful you can view the app by clicking Open App on Heroku platform.

**Hosting media files with AWS**
Please refer to this documentation [AWS S3 Bucket](https://aws.amazon.com/)

**Google Maps API key set up**
Please refer to this documentation [Google Cloud Platform Console](https://console.cloud.google.com/google/maps-apis/)

###### back to [top](#table-of-contents)
---
## Credits
#### Code
* The project’s code was developed by following the Code Institute **Boutique Ado** project lessons and based on the understanding of the course material. In some places the logic and code have been directly used from the Boutique Ado Lessons. However, it has been customized and enhanced to fit with the purpose of the project. Some comments with credits have been added where deemed necessary.

* The Blog app models and views were achieved by watching videos from **[Justdjango - Make any blog](https://www.youtube.com/watch?v=HWg3zXWwre8)** and  **[Codemy- Simple Blog](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)**
**Please note** that It too has been modified and extended to fit the purpose of the project

 * Animation on scroll was implemented using [AOS](https://github.com/michalsnik/aos)
 * Finally I have also used mix solutions found in [Stack Overflow](https://stackoverflow.com/) and Code Institue [slack channel](https://app.slack.com/) to achieve some logic and fix bugs in the code.
 
### Content and Media
* The images for products were taken from etsy.com and [google search engine](https://www.google.com/) ensuring the images were all copyright free.

* The images for treatments and blogs are from here [Pexels](https://www.pexels.com/) and [Pixabay](https://pixabay.com/es/) and [Unsplash](https://unsplash.com/)

* The images in review section was taken from [freepik](https://www.freepik.com/free-photos-vectors/leadership)

* The text description for the products were taken from [Ayurvedic Institue Website](https://www.ayurveda.com/)

* The blog content was taken from [Banyan Botanicals Website](https://www.banyanbotanicals.com/)

### Acknowledgements
I would like to Thank everyone in the **Code Institute** tutoring team and the community in **stackover flow** and **slack channel** who have helped me  throughout the development of this project.

---

###### Disclaimer
###### *This Project is made for educational use only as part of the **Code Institute Full Stack Software Development Course***.

###### back to [top](#table-of-contents)



