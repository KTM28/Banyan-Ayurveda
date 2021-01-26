## Testing
1. [**Development Testing**](#development-testing)
2. [**Manual Testing**](#manual-testing)
     - [**Responsiveness**](#responsiveness)
     - [**Navbar**](#navbar)
     - [**Footer**](#footer)
     - [**Search Bar**](#search-bar)
     - [**Landing page**](#landing-page)
     - [**About page**](#about-page)
     - [**Blog Page**](#blog-page)
     - [**Shop Treatments Cart and Checkout Page**](#shop-treatments-cart-and-checkout-page)
     - [**Contact page**](#contact-page)
     - [**Profile page**](#profile-page)
     - [**The Admin**](#admin-page)
 3. [**Automated Testing**](#automated-testing)
      - [**Travis**](#travis)
 4. [**Validators**](#validators)
 5. [**Compatibility and Responsiveness**](#compatibility-and-responsiveness)
 6. [**Other Testing**](#other-testing)
 7. [**Bugs**](#bugs)
---
### Development Testing
Django framework provides quite useful Debug utility. When debug is on the error is logged in the console and on the localhost. This feature allows a developer to pinpoint the cause of the error and fix it as they appear.

### Manual Testing
The manual testing is carried on for all UX Design and functionality of the site to meet the user and admin goals. Below they are categorised into the different sections of the webpage.

#### Responsiveness
**Test:**
- Open each page of the website from multiple devices and multiple browsers
- Open with Chrome and Firefox Developer Tools. and click on "Responsive" to check all pages
#### Navbar
**Test:**
- click on all the links in the navbar, to check if they work properly pointing to the correct location
- check all the links on different devices (navbar looks different for mobile, tablet and desktop screens)
- on mobile devices make sure that navbar is collapsed and the sidebar scrolls when the hamburger menu is clicked
- scroll down the page to see if the navbar is visible for a user all the time
#### Footer
**Test:**
- verified if subscribe form validation work by adding non-email data in the field which did not succeed so it passed
- click on the social media icons to check if they lead to the corresponding pages and open in the new tabs
- click on map icon so that it will lead to the contact page 
- click on telephone icon to trigger call link
 #### Search Bar 
**Test:**
**(Shop Page & Blog Page)**
- enter any search term into the search field to see if it redirects to the corresponding page with correct results displayed.
- submit an empty search query to see the error message displays correctly.
- submit search term that is not expected to be found on the website to see the conditional message displayed properly.
#### landing page
**Test:**
- click all the buttons on the page to check that it links correctly to the corresponding pages.
- scroll down the page to check animation on scroll(AOS) has been implemented properly.
- check all the carousels and images are displayed properly
#### About Page
**Test:**
- verify that all the expected text are displayed correctly
- verify the images are responsive and are displayed for each section.
- scroll down the page to check animation on scroll(AOS) has been implemented properly.
#### Blog Page
**Test:**
- verified if all blog posts are displayed properly.
- verified all the links implemented in the blog page returns the desired results.
- verified that the categories links work properly.
- verified that correct blogs or messages are shown when accessed through the search bar.
- verified that users must be logged in to create/update/delete blog post in the page.
- verified all the forms are displayed correctly.
- verified  that the comment forms works as expected and user authentication required to post the comment
- verified that the like functions are available only for the authenticated user.
- verified that the view counts adds up only when the authenticated user is viewing the blog.
#### Shop Treatments Cart and Checkout Page
**Test:**
- verified that the shop page list all the product in the order.
- verified the add to cart button adds the product into the cart.
- verified that when the view product is clicked the users are redirected to the product detail page.
- verified that the quantity form works as intended and that it's validation works for the number of inputs.
- verified that the user is allowed to make a purchase in the site without having to log in.
- verified that save personal information button when checked functions as intended for the logged-in user.
- verified the update and remove buttons are working properly in the cart page.
- verified that date picker works correctly and that user can update the appointment date in the shopping cart.
- verified the stripe payments functionality works flawlessly.
- verified the email confirmation are sent after the purchase is completed.
- verified the delivery totals are displayed correctly.

#### Contact page
**Test:**
- verified that the google map is displayed correctly and is responsive.
- verified the form only accepts valid data from users and all fields in the form must be added.
- verified that the message is sent out to the email linked to the app.

#### Profile page
**Test:**
- verified that the links to profile page are only displayed to authenticated users.
- verified that users can reset their password from the profile dashboard page.
- verified that users can add/update their shipping details from the profile dashboard page.
- verified that users can view the list of blogs if they have added any blogs from the profile dashboard page.
- verified that all order history with order numbers are displayed correctly and accessible to the user.
 
#### Login/Signup Page
- verified the login/signup forms are free of any breakage.
- verified it accepts only valid data.
- checked if account verifications links are sents when newly registered.
- verified users can sign in/signup using google account. 

#### The Admin 
**Test:**
- verified that only admin and users granted such status when authenticated can see links for product/service management.
- verified that only admin and users granted such status can create/update/delete products and services in the site.

### Automated Testing
The automated testing has bee run in conjunction with the manual testing to get the most coverage of the site. The aim was not to get 100% coverage but to get the inner functionality tested and to support and complement the manual testing. However, I prioritized the test for the most important functionality wherever possible.

I used Django testing module, The Tests were written for 'Views', 'Forms', and 'Models' and can be found in each application specific tests folders:
```
test_models.py / test_views.py /  test_forms.py
```  


**Command to run the test:** 
* **python3 manage.py test**
* To run the tests within a specific app only: **python manage.py test <app name here>**
* to generate a coverage report run the following command: coverage report
* to generate the HTML file run the following command: coverage Html and open index.html file in the newly created directory, run the file in the browser to see the output.

#### Travis
Travis albeit integrated into the final stage of the project was used in the unit testing of the project, It automatically tests code changes, providing immediate feedback on the success of the change. The configuration file is .travis.yml. All information regarding it's set up can be found in [Travis Documentation](https://docs.travis-ci.com/).

### Validators
#### HTML
W3C HTML Validator - The W3C Validator tool doesn't recognize the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, the code is indented and formatted to its best.
#### CSS
W3C CSS Validator - Congratulations! No Error Found.
#### JavaScript
JShint- only done for custom JS.
#### PYTHON
flake8 tool for style guide enforcement- All right for all python files except for few long lines in some code files.


### Bugs
Some of the interesting bugs that I have discovered during development are:
* If any items from products or services would be deleted after the user has purchased the item it was also automatically wiped out from the user's order history page from the past confirmation of the order. To fix this i used a solution found [medium.com](https://medium.com/@inem.patrick/django-database-integrity-foreignkey-on-delete-option-db7d160762e4) which suggested to use the argument on_delete=models.PROTECT. The PROTECT argument of the ForeignKey on_delete option prevents the referenced object from being deleted if it already has an object referencing it in the database.

* When migrating data to Postgres URL the blog category migration would show up an error "**Django.db.utils.OperationalError: no such table: blog_category**". Although this table did exist in the SQLite DB and models and had not shown any error when running locally. The fix to this was by deleting all the pycache and SQLite DB. 
remaking the migration locally and subsequently to the Postgres database.

###### back to [top](#testing) 

[Back to README](https://github.com/KTM28/Banyan-Ayurveda/blob/main/README.md#testing)
