# Get The Fit - Milestone Project #4


# Overview
An e-commerce site for users to browse gymwear and accessories. The site offers products from well known and established gymwear companies. Inspiration for this site was taken from existing 3rd party sites selling products made by high end brands, the only difference is that this site focusses on one demographic (being sports enthusiasts and gym members) rather than their sites product range which spans across general clothing sections such as jeans, tshirts, shirts and footwear which include both trainers and smart shoes.

# DISCLAIMER -  PLEASE READ!

This site is for educational purposes only. Any and all content used form a third party source shall not be used for profit. This content includes:

* Product Images
* Product descriptions
* Product prices
* Product overview

I hereby state that the site creator (myself) shall not re-use or re-publish such content for any other purposes without written consent from the orignal sources. A full list of content sources can be found [here](SOURCES.md).

# User Experience (UX)
![Am I Responsive?]()

## 1. First Time Visitor Goals
* I want to be able to browse through products with easy naviagtion, this includes the use of a search bar and product links.
* I would like to check on product details and whether they have an option for different sizes and colours.
* I would like to have the ability to register my details using a username and password.
* I would want to be able to check on how much I need to spend for any discount on delivery charges or free delivery

## 2. Frequent Visitor Goals
* I would like to check for any new products in the store, this includes any sales and or promotions.
* I would like to browse through products and sort them by keyword, price and alphabetical order.
## 3.  Returning Visitor Goals
* I would like to log in to my account to view my purchase history.
* I would like to be able to leave feedback in the form of a product review.
## Site Owner Goals
* To gain more popluarity with the fitness community through sales promotions and new products.
* To give users a good experience finding top end products at a good price.

## Future Site Owner Goals
* To give users the chance to share product links via social media to generate new business, these users could be in the form of fitness influencers and fitness models / gym owners and promoters.
* If this were a site intended for real time online use I would like to be able to implement the database to handle stock levels so ussers can check availability.
# Design

## Wireframes
* [Desktop view1](media/wireframes/Desktop-1.png)
* [Desktop view2](media/wireframes/Desktop-2.png)
#
* [iPad view1](media/wireframes/iPad-1.png)
* [iPad view2](media/wireframes/iPad-2.png)
* [iPad view3](media/wireframes/iPad-3.png)
#
* [iPhone view1](media/wireframes/iPhone-1.png)
* [iPhone view2](media/wireframes/iPhone-2.png)
* [iPhone view3](media/wireframes/iPhone-3.png)
#
## 1. Colour Scheme
* The colour scheme for the design consists of blacks, yellows and blues (for free delivery suggestion text and shopping bag icon when products have been added - this actually came built in so I've decided to keep it as it goes well). The colour scheme is simple yet attractive to the user and doesn't overload their experice with too much noise. I like to call it simple but effective.
* I've also added a transparency effect to the nav bar with a stronger gradient on the nav link bar to set it apart to highlight the navlinks better. This instantly added more character and professionalism to the site.

## 2. Typography
* Home Link & Page Titles - Montserrat. This font was chosen as the style goes well with a black background, an off-white colour was used to finish the look
* General Text - Almarai. I chose this font because it compliments the title and home logo text. This text also looks great when it's condensed down on mobile view and goes well in all product details and descriptions. An off-white color was also used. Both fonts used also have a default sans-serif text to fall back on incase of page issues.

## 3. Imagery
* The imagery for this is pretty straight forward, the home page consists of one image spanning the entire cover of the page. The image used has the same colour scheme to make it sit well as the first impression a user would get to the layout. This was sourced for free from Artist 'Montsera' @ [Pexels.com](https://www.pexels.com/)
* Product Images & information was sourced from various companies, all of which can be found listed in the [SOURCES.md](SOURCES.md) file in this project.
* Size Guide image was sourced from [Roleur](https://www.rouleur.cc/)
* Each div overlay for the site also has a background image instead of the original idea of a simple black  background. This instantly worked in my favour because it makes the page in question pop out better and promotes good UX.  



# Technologies
## 1. Coding Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [JQuery](https://en.wikipedia.org/wiki/JQuery)

## 2. Libararies, Frameworks & Additional Programmes
* Main site apps: [DJango](https://www.djangoproject.com/)
* Font icon kit sourced from [Font Awesome](https://fontawesome.com/)
* Containers, inline margin styling and colours using [Bootstrap 4.4.1](https://blog.getbootstrap.com/2019/11/28/bootstrap-4-4-1/)
* Montserrat & Almarai were sourced from [Google Fonts](https://fonts.google.com/)
* Frameworks were constructed using [Balsamiq](https://balsamiq.com/)
* Version control and to make good use of my git pod terminal to push my code from Git to [GitHub](https://git-scm.com/)

## 3. Installs
* [Stripe](https://stripe.com/gb) for card payments
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/) for the form styling.
* [Pillow](https://pypi.org/project/Pillow/) for image processing capabilities.
* [Django Countries](https://pypi.org/project/django-countries/) for the country dropdown.
* [gunicorn](https://gunicorn.org/)
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
* [django storages](https://django-storages.readthedocs.io/en/latest/)



# Site Testing
## 1. Code Checking & Validation

## 2. User Story Testing and Results
###  A - First Time Visitor Goals
### B - Result
### A - Returning Visitor Goals
### B - Results
### A - Frequent Visitor Goals
### B - Results

## 3. Devices and Browsers


## 4. Third Party End User Testing

# 5. Bugs & Fixes
## Production
### BUG
### Rendering product size:
* Dictionary renders [{ Product Name: Size }] in the size field on the shopping bag page instead of just the size chosen.
### FIX: 
* Appended key/value pair for quantity in bag items context processor else statement - with thanks to scott from Tutor Support @ [Code Institute](https://codeinstitute.net/) for pointing out the typo.

### BUG
### Quantity input:
* Quantity input box not working when I click on the chevron buttons to increase or decrease product quantity in the shopping bag.
### FIX: 
* Syntax error: When I copied and pasted input box code from my product detail page I didn't include the closing div tag and didn't update value field to {{ item.item_quantity }}.

### BUG
### Delete Product:
* Delete function not working, print statement in except Exception returns "POST /shopping_bag/delete/26/ HTTP/1.1" 500 0 'extra small'
### FIX: 
* Fixed typo in delete function in views removed [size] from line 63, 93. delete function now works

### BUG
### Products deleting in shopping bag when :
* Delete function not working, print statement in except Exception returns "POST /shopping_bag/delete/26/ HTTP/1.1" 500 0 'extra small'
### FIX: 
* Fixed typo in delete function in views removed [size] from line 63, 93. delete function now works

### BUG
### Webhooks :
* Payment-intent not working: test webhook charge succeeded but internal server error stated there was an issue with a typo as follows....order = Order.object.create() whereas it should have been order = Order.objects.create().
### FIX: 
* Issue rectified, new endpoint set up and re-tested.
### BUG
### Webhooks :
* User profile not updating on submit.
### FIX: 
* Syntax error in jinja templating, incorrect syntax for url ( missing })





# Credits & Acknowledgements
## Credits
### Image overlays:
- Ivan Samkov & CottonBro @[Pexels.com](https://www.pexels.com/) - for the page overlay images

## Acknowledgements
* Input on bugs were discussed with JimLynx_lead and my Mentor Nishant Kumar.
* NavBar styling and media image layout was discussed with Nishant Kumar.

# Deployment
## Git Hub Pages
* To create this project and it's repository, I opened a new repository by clicking the green button "new", making sure I used the Code Institute's student template.
* Once this repository was created I then selected the Git Pod button to start work on my code.
* Once my code was created I then performed git add, git commit and git push via the terminal where it was then pushed to my repository. I then performed the following steps:
1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository, locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under the Source title, click the dropdown button labelled "None" and select the "Master Branch" option (this will prompt the page to automatically refresh)
5. Scroll back down to the Git Hub Pages section to find the published site link.
* You can clone the repository via the command line by performing the following:
1. On GitHub, navigate to the main page of the repository.
2. Above the list of files, click the button with the arrow icon labelled 'Code'.


