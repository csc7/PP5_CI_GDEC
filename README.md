# **GDEC - Geophysical Data E-Commerce (Site Under Construction)**
<br><br>
#### **This project is about an e-commerce for geophysical data. It is a FICTITIOUS SITE where the user will be able to buy geophysical data that comprises digital elevation models, gravimetry, resistivity and magnetometry data; along with training, books and software products. Data and products are FICTITIOUS. The project is part of the Code Institute Full-Stack Software Development program.**
<br><br>

# **Index**
#### [*Site Live Link*](https://pp5-ci-gdec.herokuapp.com/) (https://pp5-ci-gdec.herokuapp.com/)


### [1. Project Goals](#1--project-goals)
### [2. Considerations](#2--considerations)
### [3. Project Board](#3--project-board)
### [4. User Experience](#4--user-experience)
- #### [User Goals](#user-goals-1)
- #### [Site Owner Goals](#site-owner-goals-1)
- #### [User Stories](#user-stories-1)
- #### [User Requirements and Expectations](#user-requirements-and-expectations-1)
### [5. Data Model](#5--data-model)
### [6. Design Choices](#6--design-choices)
- #### [Colours](#colours-1)
- #### [Fonts](#fonts-1)
- #### [Structure](#structure-1)
### [7. Wireframes](#7--wireframes)
### [8. Technologies used](#8--technologies-used)
- #### [Languages](#languages-1)
- #### [Software, Frameworks, Applications and Other Tools](#software-frameworks-applications-and-other-tools-1)
### [9. Features](#9--features)
### [10. Validation](#10--validation)
- #### [HTML Files](#html-files-1)
- #### [CSS File](#css-file-1)
- #### [JavaScript Files](#javascript-files-1)
- #### [Python Files](#python-files-1)
- #### [Accessibility](#accessibility-1)
- #### [Performance](#performance-1)
### [11. Testing](#11--testing)
- #### [Testing of Python Files with unittest](#testing-of-python-files-with-unittest-1)
- #### [Testing of User Stories](#testing-of-user-stories-1)
### [12. Bugs](#12--bugs)
### [13. Deployment](#13--deployment)
### [14. Credits](#14--credits)
### [15. Acknowledgements](#15--acknowledgements)
<br>

___
# **1 . E-commerce Project Goals**
The goal of the project is to develop an e-commerce for geophysical data, where users can find and buy digital elevation models, gravimetry, resistivity and magnetometry data; along with reports, training (courses and books) and software products. In addition, users can register in the site to track their purchases, contact the site owner and/or developer, navigate to social network sites of the e-commerce, filter and search products, and pay the products through Stripe.

In addition, besides products and users, it is expected to provide a proper management for the site owner, registering order information and history, administration tasks like product updates and interaction with users.


<br><br>
## [Back to Index](#index)
<br><br>


___
# **2 . Considerations**

If opening the project with Gitpod from GitHub (top right green button), please run the following command as new workspaces need to have their dependencies:
pip3 install -r requirements.txt

Please keep in mind that the interaction with the database and corresponding display of data is slow, it might take several seconds until the data is displayed.


## **Generation of the products of the site**

As stated at the begining, the site is a **fictitious** e-commerce. To generate the products, the Natural Earth quick start kit" (50m raster) was downloaded from Natural Earth's website https://www.naturalearthdata.com/downloads/. This kit contains a planisphere from where QGIS was used to filter it by countries, by running the file "products_database_generation_for_QGIS.py" (in the "/tools" folder in the project root directory) in the Python console of QGIS.

Once all countries were filtered, different scale colours were applied for them, one for each category (digital elevation models, gravimetry, resistivity and magnetometry data), to simulate different products. To simulate some "randomness" of the products, some products were randomly deleted (this way, not all countries have the same products).

Then, free images were downloaded from Pexels (please see Credit section for details) and assigned to the remaining products of the e-commerce (reports, training courses, training books and software products).

A Python file was created to build CSV and JSON structures for the Products and Category models (with fields matching their fields, including the name and URL of the images). This file, "build_csv_and_json.py" (in the "/tools" folder in the project root directory), saves the CSV file in the same "/tools" folder and the JSON file in the "/fixtures" folder of the products Django app.

**The file build_csc_and_json.py must run with only the images in the project "/media" folder, with image names starting with the following names (otherwise the program will not work, as it would be reading other file names and therefore the "if" statements should be modified): digital elevation models, gravimetry, resistivity and/or magnetometry. Run it before adding other files to the "/media" folder, or change the name of the folder in the Python file.**

Since the JSON file is already in the "/fixtures" folder, the data can be loaded into the Django models using the following commands (in this order, since the products are related to categories and therefore the latter must be defined before):

python3 manage.py loaddata categories
python3 manage.py loaddata products


<br><br>
## [Back to Index](#index)
<br><br>



___
# **3 . Project Board**

A project board was created in GitHub to help on the planning and follow-up of the work when developing the site; it can be observed [here](https://github.com/csc7/PP5_CI_GDEC/projects/1) (https://github.com/csc7/PP5_CI_GDEC/projects/1).

In addition, issues can directly be found [here](https://github.com/csc7/PP5_CI_GDEC/issues) (https://github.com/csc7/PP5_CI_GDEC/issues)

<br><br>
## [Back to Index](#index)
<br><br>

___
# **4 . User Experience**

UX has been addressed around Jesse James Garrett's process and its five planes:
- **STRATEGY**: to develop an e-commerce website (product) that makes purchasing of geophysical data simple and intuitive.
- **SCOPE**: the minimum viable product needs to include features that allow the user to know the following:
    - Home page that act as staring point and welcome page for the site.
    - A main navigation menu where, along with a footer, gives access to the main parts of the website, including registration and sign-in for users.
    - Images and the products with their associated price for purchasing.
    - A method to pay the products; for instance, stripe.
    - A database that accounts for all the data in the website and allows interaction of the users with the products (purchase) and their accounts.
- **STRUCTURE**: the information is structured as follows:
    - Home page (act as welcome page).
    - Fixed navigation bar on top that allows searching and filtering products for display and buy.
    - A page showing the selected or filtered products.
    - A page for details of a specific product when selected, giving the option to buy it.
    - A bag page with selected products to buy.
    - A checkout page showing the products the user is about to buy, with the final price to pay, linking with the payment method (e.g., Stripe).
    - Footer, showing the main structure of the website and giving access to the social networks of the e-commerce and a field for the user to sign up in the newsletter of the e-commerce (to help on marketing), a contact form, contact information, and general data protection regulation requirements.
    - A profile page, including the option to show the purchase history of the user.
    - Contact form page.
    - Pop-up messages informing the interaction of the user with the website (purchase, sign in, sign out, sign up, errors and success messages as the main ones).
    - Sign-in page.
    - Sign-up page.
    - Sign-out page.
    - 404 page to let the user know of any error while loading the site.
- **SKELETON**: the information and products are accessed through a fixed navigation menu on top of the pages and a footer.
- **SURFACE**: the website is based on a contrast of different tonalities of blue for the header and footer, white for body, and fonts in strong dark blue; with red banners (the top one including advertising messages) separating the fixed navigation menu, the body and the footer.


## **User Goals**
- To easily find and buy products (geophyical data, and training and software products).
- To find an interactive website.
- To navigate through a responsive website.
- To have the website accessible at all times through a fixed navigation menu and a footer.
- To have an account in the website for future purchases or review of past purchases, giving the change to store personal data.
- To be able to contact the site administrator, owner and/or developer if desired.
- To be informed of the events created when navigating the website as soon as they happen.

#### [Back to Index](#index)

## **Site Owner Goals**
- To sell geophyical data, and training and software products.
- To promote different products.
- To have the website helping on the marketing of the e-commerce (e.g., linking to contact information and options, social networks, and giving the option to sign up for a newsletter).
- To capture clients.
- To increase the amount of users interested in and buyint geophyical data, and training and software products.
- To provide an interactive website.
- To provide a responsive website.
- To give users the chance to contact the site administrator, owner and/or developer.

## **Developer Goals**
- To provide a scalable e-commerce website to show my current development capabilities.

#### [Back to Index](#index)
<br>

## **User Stories**
User stories are divided into the following three groups:

- ### **First time users**
1. As a user, I want to find a well-organized and simple site, so I immediately get the whole picture of the site.
2. As a user, I want to find a responsive site, so I can easily navigate in it in different devices.
3. As a user, I want to receive a confirmation of registration when I sign up, so I know that the process for creating my account went well.
4. As a user, I want to be able to contact the site administrator, owner and/or developer, so I can send feedback to them.
5. As a user, I want to have access to my account easily, so I can quickly sign in.

- ### **Returning users**
6. As a returning user, I want to be able to contact the site administrator and/or owner and/or developer, so I can send feedback to them.
7. As a returning user, I want a navigation menu on top, always visible, so I can access the main content on the website from there and do not need to use the back button of the browser.
8. As a returning user, I want to have access to my account easily, so I can quickly sign in.
9. As a returning user, I want to have a way to contact the developer so I can contribute and/or indicate errors or bugs.
10. As a returning user, I want to be informed if the contact form goes through, so I know if my message is being sent or it is not.
11. As a returning user, I want to recover my password easily if I forget it, so I do not worry about remembering and/or keeping it.
12. As a returning user, I want to have a history of my purchases, so I know what I have bought and spent through time.

- ### **Shoppers**
13. As a shopper, I want to have the products to buy visible (without many details so I can see more), so I can select them for purchase.
14. As a shopper, I want to have access to the product details, so I can access them in case I am not sure about the purchase and/or want to have a better description of the product.
15. As a shopper, I want to have a detailed view of my shopping cart, so I know what I am buying and have the current purchase details just before paying.
16. As a shopper, I want to have the amount I am spending always visible, so I know how much I am spending.
17. As a shopper, I want to have special offers easily accessible, so I can buy them before they disappear if I find them useful.
18. As a shopper, I want to have a search field, so I do not spend much time finding the product I want to buy
19. As a shopper, I want to have categories of products, so I find a product easily if I do not know its name.
20. As a shopper, I want to have prices always visible, so I know the value of the products at all times.
21. As a shopper, I want to have the different resolutions of the products visible, close to the product it belongs to, so I can easily select it without further action.
22. As a shopper, I want to have a secure payment method, so I can rest assured that the purchase procedure is safe.

- ### **Site Owner**
23. As owner, I want to provide an introductory page, so users know what can be found in the website and what can be purchased.
24. As owner, I want to provide an easy process for registration, so I ensure a connection with a potential buyer.
25. As owner, I want to provide a search field for products on top, so I require users/shoppers the minimum possible time to find a product (and therefore reduce the risk of leaving).
26. As owner, I want to organize products in categories, so users find an organized site and can find products easily.
27. As owner, I want to receive feedback from users, so I can take actions in response to them if needed.
28. As owner, I want to provide a navigation menu on top and always visible, so users can access any content at any time without needing the back button.
29. As owner, I want to give as many options to be contacted as possible, so users can choose forms or links in the footer to send their consultations and/or feedback in a very fast way.
30. As owner, I want to provide a responsive website, so user can access it from any device without any constraint to navigate, find and/or use the website.
31. As owner, I want to inform users if their consultation/message was successfully sent, so they know if they need to resend it or they do not.
32. As owner, I want to inform the user, through an error page, if there is any error when loading the website.

- ### **Developer**
33. As developer, along with other points of this section, I want to show my work and give the option to users to contact me if they wish.


#### [Back to Index](#index)

## **User Requirements and Expectations**
- A home page.
- A responsive navigation throughout the website.
- A fixed navigation top that allows searching and filtering products for display and buy.
- A page showing the selected or filtered products.
- A page for details of a specific product when selected, giving the option to buy it.
- A bag page with selected products to buy.
- A checkout page, showing the final price to pay and linking with the payment method (e.g., Stripe).
- A Footer, showing the main structure of the website and giving access to the social networks of the e-commerce and a field for the user to sign up in the newsletter of the e-commerce (to help on marketing), a contact form, contact information, and general data protection regulation requirements.
- A profile page with purchase history.
- A contact form.
- Pop-up messages informing the interaction of the user with the website.
- A Sign-in page.
- A Sign-up page.
- A Sign-out page.
- A 404 page.



<br><br>
## [Back to Index](#index)
<br><br>


___
# **5 . Data Model**

The e-commerce business model underlying the application is designed in such a way that a **"user"** (who is uniquely identified by ID) can buy **"products"** (that are also uniquely identified by ID and SKU) by sending a **"order"** (that is uniquely identified by ID and order number). Then, since an order can have many products, and simoutaneously a product can be requested by many orders, an **"order line item"** is created to uniquely relate a specific product to a specific order. This "order line item" divides the many-to-many relation between "order" and "product" in two one-to-many relations ("order-order line item" and "order line item-product").

Then, a **"category"** is created and related to the type of product in order to help on the search of them.

Finally, a **"contact"** model is created, unrelated to the previous tables, to contact the site owner in any case, regardless of an order is issued or is not by a user.

The project database is built with PostgreSQL and deployed in Heroku platform. Its tables or models are build with Django models and follows the models given by the Code Institute "I Think Therefore I Blog" project. The following chart shows the tables and data involved, and how they are related:

![Data Model Image](docs/data_model.PNG)
*Chart created with ERDPlus (https://erdplus.com/standalone).*

The following are the tables involved in the relational model and the field types in each of them.

- #### **ORDER**

    - **ID:** integer, primary key    
    - **Order Number:** char
    - **User Profile:** integer, foreign key
    - **Full Name:** char
    - **E-mail:** e-mail
    - **Phone Number:** char
    - **Country:** country
    - **Postcode:** char
    - **Town or City:** char
    - **Street Address 1:** char
    - **Street Address 2:** char
    - **County:** char
    - **Date:** date
    - **Delivery Cost:** decimal
    - **Order Total:** decimal
    - **Grand Total:** decimal
    - **Original Bag:** text)
    - **Stripe PID:** char

- #### **ORDER LINE ITEM**

    - **ID:** integer, primary key 
    - **Order:** integer, foreign key
    - **Product:** integer, foreign key
    - **Product Resolution:** char
    - **Quantity:** integer
    - **Line Item Total:** decimal

- #### **CONTACT FORM**

    - **ID:** integer, primary key
    - **Date:** date
    - **Time:** custom (time)
    - **Full Name:** char
    - **E-mail:** e-mail
    - **Description:** char

- #### **CATEGORY**

    - **ID:** integer, primary key
    - **Name:** char
    - **Friendly Name:** char

- #### **PRODUCT**

    - **ID:** integer, primary key    
    - **Category:** integer, foreign key
    - **SKU:** char
    - **Name:** char
    - **Description:** text
    - **Price:** decimal
    - **Resolution:** Boolean
    - **Rating:** decimal
    - **Image URL:** URL
    - **Image Name:** image

- #### **USER PROFILE**

    - **ID:** integer, primary key    
    - **User:** char
    - **Default Phone Number:** char
    - **Default Street Address 1:** char
    - **Default Street Address 2:** char
    - **Default Town or City:** char
    - **Default County:** char
    - **Default Postcode:** char
    - **Default Country:** char



<br><br>
## [Back to Index](#index)
<br><br>

___
# **6 . Design Choices**

The design was planned to cover screen sizes from 320x568px to 1920x1370px.

## **Colours**
Colours are based on different tonalities of blue for header (fixed navigation menu) and footer, contrasting with a white background for the body (where products and all other content appear). The header (fixed navigation menu) and body, as well as body and footer, are separated by a red banners (the top one containing moving messages with white fonts).

#### [Back to Index](#index)
<br>

## **Fonts**
Google fonts (please see credits section below) were implemented on the website; Play (Regular 400 and Bold 700) and Roboto (Regular 400). Play is used for the body; Sans-serif font is used as a back-up in case the previous font cannot be loaded.

#### [Back to Index](#index)
<br>

## **Structure**

The website consists of a header with fixed navigation menu on top, a body and the a footer. It is designed to navigate the e-commerce from the header and footer, having them always available. The header is fixed, while the footer is fixed only for screens whose wide is greater than 992px, so it does not use space from the body in smaller screen sizes. There are two banners separating the header and body, and the body and footer. The one below the header contains moving messages to advertise special features of the e-commerce at all times.

The metadata in the head tag of the base HTML includes the following keywords to help search engines to find the website: "DEM books, DEM data, DEM software, DEM training, Geophysical data, Buy DEM data, Geophysical book, Buy Resistivity data, Gravimetry data, Buy Gravimetry data, Resistivity books, Buy Magnetometry data, Magnetometry software, Gravimetry books, Buy geophysical data, 
Magnetometry books, DEM, Geophysical, Code Institute, software development, and full-stack course, milestone project".

The metadata also includes the following description: "Code Institute Student Milestone Project 5, an e-commerce application that sells digital elevation models, gravimetry, magnetometry and resistivity data; along with training, books and software for data acquisition and processing".

Wireframes were developed at the beginning of the project to have a first structure of the e-commerce site and analyse eventual changes. Please see section 7, Wireframes, for images about these wireframes.

- ### **Header**

In order to achieve the goals related to an easy navigation and finding of products, a fixed navigation menu in the header is implemented, which also contributes on accessibility to the main parts of the e-commerce and on responsiveness.In the same area.
The logo of the e-commerce is placed to the left, in the middle there are a search field on top and the navigation menu below, and on the right two icons can be found that link to the account sign-in/sign-up/sign-out and bag.

- ### **Top banner**

It is a thin section (height of 25px), from side to side of the screen, in red colour, that separates the header/fixed navigation menu on top from the body. It contains moving messages to advertise special features of the e-commerce at all times.


- ### **Body**

The products are displayed in this area, from where the products details can be accessed by clicking on the product itself and displayed in the same body.

The body also holds the pages for the bag, the checkout, the success checkout, sign-in, sign-up, sign-out, profile, contact form and 404 pages.
<br>
    
- ### **Top banner**

It is another thin section (height of 25px), from side to side of the screen, in red colour, that separates the body from the footer.


- ### **Footer**

The footer contains links contact information of the e-commerce on the left (below the e-commerce logo), a contact form, social media links, links to product categories, links to account sign-in/sign-up/sign-out, General Data Protection Regulation (GDPR) information about the privacy policy and cookies, and an area on the right to sign up for the e-commerce newsletter.
<br><br>
## [Back to Index](#index)
<br><br>

___
# **7 . Wireframes**

Wireframes were developed in order to gather goals, user stories, requirements and expectations, and have the design references for desktop, tablet and mobile devices.
Please check the PDFs files for each case in the following links:

<details>
    <summary>Desktop Wireframe Image for Instructions Page</summary>

![Desktop Wireframe Image for Instructions App/Page](docs/wireframes/wireframe-wqcs-desktop-instructions.PNG)
</details>
<details>
    <summary>Desktop Wireframe Image for Weather Page</summary>

![Desktop Wireframe Image for Weather App/Page](docs/wireframes/wireframe-wqcs-desktop-weather.PNG)
</details>
<details>
    <summary>Desktop Wireframe Image for Blog Page</summary>

![Desktop Wireframe Image for Blog App/Page](docs/wireframes/wireframe-wqcs-desktop-blog.PNG)
</details>
<details>
    <summary>Desktop Wireframe Image for Contact Page</summary>

![Desktop Wireframe Image for Contact App/Page](docs/wireframes/wireframe-wqcs-desktop-contact.PNG)
</details>

<details>
    <summary>Tablet Wireframe Image for Instructions Page</summary>

![Tablet Wireframe Image for Instructions App/Page](docs/wireframes/wireframe-wqcs-tablet-instructions.PNG)
</details>
<details>
    <summary>Tablet Wireframe Image for Weather Page</summary>

![Tablet Wireframe Image for Weather App/Page](docs/wireframes/wireframe-wqcs-tablet-weather.PNG)
</details>
<details>
    <summary>Tablet Wireframe Image for Blog Page</summary>

![Tablet Wireframe Image for Blog App/Page](docs/wireframes/wireframe-wqcs-tablet-blog.PNG)
</details>
<details>
    <summary>Tablet Wireframe Image for Contact Page</summary>

![Tablet Wireframe Image for Contact App/Page](docs/wireframes/wireframe-wqcs-tablet-contact.PNG)
</details>
<details>
    <summary>Cell Wireframe Image for Instructions and Weather Pages</summary>

![Tablet Wireframe Image for Instructions and Weather Page](docs/wireframes/wireframe-cell-instructions-weather-pages.PNG)
</details>
<details>
    <summary>Cell Wireframe Image for Blog and Contact Pages</summary>

![Tablet Wireframe Image for Blog and Contact Page](docs/wireframes/wireframe-cell-blog-contact-pages.PNG)
</details>


<br>

[PDF File for Desktop Wireframe](docs/wireframes/wireframe-wqcs-desktop.pdf)

[PDF File for Tablet Wireframe](docs/wireframes/wireframe-wqcs-tablet.pdf)

[PDF File for Cell Wireframe](docs/wireframes/wireframe-wqcs-cell.pdf)
<br><br>
## [Back to Index](#index)
<br><br>

___
# **8 . Technologies Used**

The development of the project employed the following languages, software, frameworks, applications and tools:

## **Languages**
- #### **HTML**
- #### **CSS**
- #### **JavaScript**
- #### **Python**

#### [Back to Index](#index)

## **Software, Frameworks, Applications and Other Tools**
- ##### **jQuery**
- ##### **GitHub**
- ##### **Gitpod**
- ##### **QGIS 3.18 Zürich** (RUN tools/build_csv_and_json.py from inside the project directory)
- ##### **Django 3.2**
- ##### **django-allauth 0.41.0**
- ##### **dj-database-url (v0.5.0)
- ##### **django-allauth (v0.41.0)
- ##### **django-countries (v7.3.2)
- ##### **django-crispy-forms (v1.14.0)
- ##### **django-storages (v1.12.3)
- ##### **PostgreSQL**
- ##### **Font Awesome (v4)**
- ##### **Bootstrap (v4.0)**
- ##### **unittest**
- ##### **asgiref (v3.5.0)
- ##### **backports.zoneinfo (v0.2.1)
- ##### **boto3 (v1.21.33)
- ##### **botocore (v1.24.33)
- ##### **gunicorn (v20.1.0)
- ##### **jmespath (v1.0.0)
- ##### **oauthlib (v3.2.0)
- ##### **Pillow (v9.0.1)
- ##### **psycopg2-binary (v2.9.3)
- ##### **python3-openid (v3.2.0)
- ##### **pytz (v2021.3)
- ##### **requests-oauthlib (v1.3.1)
- ##### **s3transfer (v0.5.2)
- ##### **sqlparse (v0.4.2)
- ##### https://miniwebtool.com/django-secret-key-generator/ (to generate Django secret keys)
- ##### https://www.privacypolicygenerator.info/ (to ellaborate the General Data Protection Regulation, GDPR, page)
- ##### https://www.wordtracker.com/ (to analyze volume and competitors of SEO keywords)
- ##### https://jsonformatter.org/ (to inspect JSON structures for the product and category data)
- ##### https://www.xml-sitemaps.com/ (to generate sitemap.xml file)
- ##### Mailchimp: Marketing Automation & Email Platform, https://mailchimp.com
- ##### **Balsamiq Wireframes (v4.2.4, Editor Version 2.6.0)**
- ##### **ERDPlus (to make the data model graph)**
- ##### **Google Fonts**
- ##### **Stripe**
- ##### **stripe (v2.67.0)
- ##### **W3C Markup Validation Service**
- ##### **W3C CSS Validation Service**
- ##### **JSHint (version 2.13.0)**
- ##### **JavaScript AJAX**
- ##### **WAVE Web Accessibility Evaluation Tool**
- ##### **Coverage.py 6.3.2
- ##### **Google Lighthouse (used in Google, Microsoft Edge and Firefox)**
- ##### **Google Chrome, version 97.0.4692.71, Official Build, 64-bit (and its development tool)**
- ##### **Microsoft Edge, version 97.0.1072.62, Official build, 64-bit (and its development tool)**
- ##### **Firefox, 96.0.3, 64-bit (and its development tool)**
- ##### **Microsoft Internet Explorer, version 2004, OS Build 19041.1415, Microsoft Corporation**


<br><br>
## [Back to Index](#index)
<br><br>



___
# **9 . Features**

The features are designed to address the goals, user stories, and user requirements and expectations given in section 4, User Experience.

The features of the site are the following ones:

- Home page
- Products (with product administration for the site owner)
- Product details ((with product administration for the site owner)
- Bag page
- Checkout page
- Secure payment method
- Checkout success page
- Site access (sign-in and sign-out)
- Registration (sign-up)
- Profile with history order
- Contact form
- Footer
- 404 page

This pages are accessible from a fixed navigation menu on top and a footer, and several pop-up messages are included to inform the user of their interactions with the site.

In the second half of the project, two more features were added to improve the user experience and feedback reception:

- Comments
- Wish list



Details of these features, including the user story they cover, are the following:

- ### **Fixed navigation menu**

It is in the header, fixed on all pages to facilitate navigation, and responsiveness.

*User Stories Addressed by this Feature: 1; 2; 5; 7, 8, 15, 16, 17, 18, 19, 20, 24, 25, 26, 28, 30, and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Fixed Navigation Menu for Desktop Image</summary>

![Fixed Navigation Menu for Desktop Image](docs/features-and-evidence/fixed-navigation-menu.PNG)
</details>
<details>
    <summary>Fixed Navigation Menu for Tablet Image</summary>


![Fixed Navigation Menu for Tablet Image](docs/features-and-evidence/fixed-navigation-menu-tablet.PNG)
</details>
<details>
    <summary>Fixed Navigation Menu for Cell Phones Image</summary>

![Fixed Navigation Menu for Cell Phones Image](docs/features-and-evidence/fixed-navigation-menu-cell.PNG)
</details>
<details>
    <summary>Fixed Navigation Menu, expanded, for Cell Phones Image</summary>

![Fixed Navigation Menu, Expanded, for Cell Phones Image](docs/features-and-evidence/fixed-navigation-menu-cell-expanded.PNG)
</details>
<br>


- ### **Banner with latest news**

It separates the fixed navigation menu and the body of the site, and shows advertising messages for the e-commerce.

*User Stories Addressed by this Feature: 1; 2; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Banner with Latest News for Desktop Image</summary>

![Banner with Latest News for Desktop Image](docs/features-and-evidence/banner-with-latest-news-desktop.PNG)
</details>
<details>
    <summary>Banner with Latest News for Tablets Image</summary>

![Banner with Latest News for Tablets Image](docs/features-and-evidence/banner-with-latest-news-tablet.PNG)
</details>
<details>
    <summary>Banner with Latest News for Cell Phones Image</summary>

![Banner with Latest News for Cell Phones Image](docs/features-and-evidence/banner-with-latest-news-cell.PNG)
</details>
<details>
    <summary>Banner with Latest News for Cell Phones Image, expanded</summary>

![Banner with Latest News for Cell Phones Image, expanded](docs/features-and-evidence/banner-with-latest-news-cell-expanded.PNGG)
</details>
<br>


- ### **Home page**

It is the welcome page, with a world map image and advertising messages in a Bootstrap carousel.

*User Stories Addressed by this Feature: 1; 2; 23; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Check Home Page Desktop Image</summary>

![Home Page Image for Desktop](docs/features-and-evidence/home-page-desktop.PNG)
</details>

<details>
    <summary>Check Home Page Tablet Image</summary>

![Home Page Image for Tablet](docs/features-and-evidence/home-page-tablet.PNG)
</details>

<details>
    <summary>Check Home Page Cell Image</summary>

![Home Page Image for Cell](docs/features-and-evidence/home-page-cell.PNG)
</details>
<br>


- ### **Products (with product administration for the site owner)**

Products appear after selecting categories or searching in the fixed navigation menu; they can be ordered by different criteria. The have an image, price, resolution (if applicable), a short description, and it also gives the site owner the option to edit it.


*User Stories Addressed by this Feature: 1; 2; 13; 14; 19; 20; 21; 26; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Check Home Page Desktop Image</summary>

![Products Page](ddocs/features-and-evidence/products.PNG)
</details>

<details>
    <summary>Products Image</summary>

![Products Management Page](docs/features-and-evidence/products-management.PNG)
</details>


<br>

- ### **Product details ((with product administration for the site owner)**

It can accessed by cliking on a specific product; it provides detailed information about it, including the price, short description and resolutions available if applicable. It also gives the site owner the option to edit it.

*User Stories Addressed by this Feature: 1; 2; 13; 14; 20; 21; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Product Details Image</summary>

![Product Details Image](docs/features-and-evidence/product-details.PNG)

</details>
<br>


- ### **Bag page**

It can be accessed through the icot in the fixed navigation menu, top right, and shows the current products being purchased/added to the bag.

*User Stories Addressed by this Feature: 1; 2; 15; 16; 20; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Bag Page Image</summary>

![Bap Page Image](docs/features-and-evidence/bag.PNG)

</details>
<br>



- ### **Checkout page**

It is presented when the user/shopper finishes the purchase process and is ready to pay.

*User Stories Addressed by this Feature: 1; 2; 15; 22; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Checkout Image</summary>

![Checkout Page Image](docs/features-and-evidence/checkout.PNG)

</details>
<br>


- ### **Secure payment method**

It is the payment process for the e-commerce, poweverd by Stripe.

*User Stories Addressed by this Feature: 1; 2; 22; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Stripe Payment Image</summary>

![Payment Process Image](docs/features-and-evidence/Stripe-payment.PNG)

</details>
<br>


- ### **Checkout success page**

It is presented after a successful payment carried out by the user/shopper.

*User Stories Addressed by this Feature: 1; 2; 22; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Checkout Success Image</summary>

![Checkout Success Image](docs/features-and-evidence/checkout-success.PNG)

</details>
<br>


- ### **Site access (sign-in and sign-out)**

They are Django complementary tools and pages to have sigh-in and sign-out options in the site for users. 

*User Stories Addressed by this Feature: 1; 2; 5; 8; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Sign-in Page Image</summary>

![Sign-in Image](docs/features-and-evidence/log-in.PNG)

</details>
<details>
    <summary>Sign-out Page Image</summary>

![Sign-out Image](docs/features-and-evidence/log-out.PNG)

</details>
<br>



- ### **Registration (sign-up)**

They are Django complementary tools and pages to have a sign-up option for users. 

*User Stories Addressed by this Feature: 1; 2; 3; 5; 8; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Sign-up Image</summary>

![Registration Sign-In Images](docs/features-and-evidence/sign-up.PNG)

</details>

<br><br>
## [Back to Index](#index)
<br><br>



- ### **Profile with history order**

It is a page that shows the user information and history order after selected the option in the fixed navigation menu when the user is signed in. 

*User Stories Addressed by this Feature: 1; 2; 8; 12; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Profile with history order on the right</summary>

![Profile and History Order Image](docs/features-and-evidence/profile.PNG)
</details>

<br><br>
## [Back to Index](#index)
<br><br>


- ### **Contact form**

It is a contact form in a separate page, accessible from the footer, that gives the option to send a consultation to the site owner, without needing to buy and/or be signed in/up. Its goal is to receive feedback from as many sources as possible. 

*User Stories Addressed by this Feature: 1; 2; 4; 6; 9; 27; 29; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Contact Form Image</summary>

![Contact Form Image](docs/features-and-evidence/contact-form.PNG)

</details>

<br><br>
## [Back to Index](#index)
<br><br>


- ### **Footer**

They are Django complementary tools and pages to have a sign-up option for users. 

*User Stories Addressed by this Feature: 1; 2; 4; 5; 6; 8; 9; 24; 27; 29; 30 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Footer Images</summary>

![Footer for Desktop Image](docs/features-and-evidence/footer-desktop.PNG)
![Footer for Tablet Image](docs/features-and-evidence/footer-tablet.PNG)
![Footer for Cell Image](docs/features-and-evidence/footer-cell.PNG)
</details>

<br><br>
## [Back to Index](#index)
<br><br>


- ### **404 page**

They are Django complementary tools and pages to have an error page that informs the user that something has gone wrong (e.g., wrong address, broken URL). 

*User Stories Addressed by this Feature: 1; 2; 10; 30; 32 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Check Image</summary>

![Registration Sign-In Images](docs/features-and-evidence/sign-in.PNG)
![Registration Sign-Up Images](docs/features-and-evidence/sign-up.PNG)
![Registration Sign-Out Images](docs/features-and-evidence/sign-out.PNG)
</details>

<br><br>
## [Back to Index](#index)
<br><br>


- ### **Pop-up status messages**

They are Django complementary messages that informs the user, with pop-ups, that an action has been executed in the site. The action can be adding a product, deleting a product, editing a product (for the site owner), changing the amount of products in the bag, signing in, signing up, signing out and the payment outcome.

*User Stories Addressed by this Feature: 1; 2; 3; 10; 30, 31 and 33.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Pop-up Status Message Images</summary>

![Pop-up Status Message Image 1](docs/features-and-evidence/success-toast-1.PNG)
![Pop-up Status Message Image 2](docs/features-and-evidence/success-toast-2.PNG)
![Pop-up Status Message Image 3](docs/features-and-evidence/success-toast-3.PNG)
![Pop-up Status Message Image 4](docs/features-and-evidence/success-toast-4.PNG)
![Pop-up Status Message Image 5](docs/features-and-evidence/success-toast-5.PNG)
![Pop-up Status Message Image 6](docs/features-and-evidence/success-toast-6.PNG)
![Pop-up Status Message Image 7](docs/features-and-evidence/alert-toast-1.PNG)


</details>

<br><br>
## [Back to Index](#index)
<br><br>




___
# **10 . Validation**

**Development tools** of **Google Chrome** (Version 97.0.4692.71, Official Build, 64-bit), **Microsoft Edge** (Version 97.0.1072.62, Official build, 64-bit) and **Firefox** (Version 96.0.3, 64-bit) have been used to test the behaviour of the website for screen sizes between 320x568px to 1920x1370px.

The website was tested using these **browsers** and also **Microsoft Internet Explorer** (Version 2004, OS Build 19041.1415, Microsoft Corporation). **Samsung Internet** (version 15.0.2.47) was also used to test the website. In addition, some users have collaborated checking the website in the cell phones, mostly with **Android-based operating systems**.

**Devices** used for testing and validation include Dell and Samsung cell phones. **Operative systems** include Windows 10 Enterprise (remote desktop), Windows 10 Pro and Android. **Processors** for desktop and laptops were Intel.

The following tools were used to validate the **files of the website**:

<br>

### **HTML Files**
https://validator.w3.org/ was used to validate the new HTML files. Pages were rendered to get the HTML code (otherwise Django templates would alone would give errors). When possible (where pages do not require log-in), the page link was tested in the validator.

<details>
    <summary>Home (index.html)</summary>

![Evidence of no errors in the home HTML file](docs/validation/validation-html-validator-w3-org-home.PNG) 
</details>
<details>
    <summary>Home (index.html), direct URL input</summary>

![Evidence of no errors in the home HTML file](docs/validation/validation-html-validator-w3-org-home-2.PNG) 
</details>
<details>
    <summary>bag.html</summary>

![Evidence of no errors in the bag HTML file](docs/validation/validation-html-validator-w3-org-bag.PNG) 
</details>
<details>
    <summary>bag.html, direct URL input</summary>

![Evidence of no errors in the bag HTML file](docs/validation/validation-html-validator-w3-org-bag-2.PNG) 
</details>
<details>
    <summary>checkout.html</summary>

![Evidence of no errors in the checkout HTML file](docs/validation/validation-html-validator-w3-org-checkout.PNG) 
</details>
<details>
    <summary>checkout_success.html</summary>

![Evidence of no errors in the home checkout-success HTML file](docs/validation/validation-html-validator-w3-org-checkout-success.PNG) 
</details>
<details>
    <summary>contact.html</summary>

![Evidence of no errors in the contact HTML file](docs/validation/validation-html-validator-w3-org-contact.PNG) 
</details>
<details>
    <summary>thanks.html</summary>

![Evidence of no errors in the thanks HTML file](docs/validation/validation-html-validator-w3-org-thank-you.PNG) 
</details>
<details>
    <summary>add_product.html</summary>

![Evidence of no errors in the add-product HTML file](docs/validation/validation-html-validator-w3-org-product-add.PNG) 
</details>
<details>
    <summary>edit_product.html</summary>

![Evidence of no errors in the edit-product HTML file](docs/validation/validation-html-validator-w3-org-edit-product.PNG) 
</details>
<details>
    <summary>product_details.html</summary>

![Evidence of no errors in the product-details HTML file](docs/validation/validation-html-validator-w3-org-product-details.PNG) 
</details>
<details>
    <summary>products.html</summary>

![Evidence of no errors in the products HTML file](docs/validation/validation-html-validator-w3-org-products.PNG) 
</details>
<details>
    <summary>profile.html</summary>

![Evidence of no errors in the profile HTML file](docs/validation/validation-html-validator-w3-org-profile.PNG) 
</details>
<details>
    <summary>wish_list.html</summary>

![Evidence of no errors in the wish-list HTML file](docs/validation/validation-html-validator-w3-org-wish-list.PNG) 
</details>
<details>
    <summary>404.html</summary>

![Evidence of no errors in the 404 page HTML file](docs/validation/validation-html-validator-w3-org-404.PNG) 
</details>



#### [Back to Index](#index)

<br>


### **CSS File**
https://jigsaw.w3.org/css-validator/ was used to validate the CSS file.

http://jigsaw.w3.org/css-validator/validator$link
or
http://jigsaw.w3.org/css-validator/check/referer **(for HTML/XML document only)**

Please check the evidence below:

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
            
<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>
     
<details>
    <summary>base.css File</summary>

![Evidence of no errors in the CSS file](docs/validation/validation-base-css.PNG) 
</details>
<details>
    <summary>base.css File (Warnings)</summary>

![Evidence of no errors in the CSS file](docs/validation/validation-base-css-warnings.PNG) 
</details>

<details>
    <summary>checkout.css File</summary>

![Evidence of no errors in the CSS file](docs/validation/validation-checkout-css.PNG) 
</details>
<details>
    <summary>checkout.css File (Warnings)</summary>

![Evidence of no errors in the CSS file](docs/validation/validation-checkout-css-warnings.PNG) 
</details>

<details>
    <summary>profile.css File</summary>

![Evidence of no errors in the CSS file](docs/validation/validation-profile-css.PNG) 
</details>
<details>
    <summary>profile.css File (Warnings)</summary>
No warnings
</details>


#### [Back to Index](#index)

<br><br>

### **JavaScript Files**
https://jshint.com/ was used to validate the JavaScript files.
Please check the parameters used for validation and evidence below:

Parameters:
<details>
    <summary>Parameters used for JavaScript validation in JSHint version 2.13.3</summary>

![Parameters used for JavaScript validation in JSHint version 2.13](docs/validation/validation-js-parameters.PNG) 
</details>

Files:
<details>
    <summary>To enable/disable country name in forms: country_field_in_profile.js</summary>

![Evidence of no errors country_field_in_profile.js JavaScript file](docs/validation/validation-js-country_field_in_profile.PNG)
</details>

<details>
    <summary>To cancel delivery: download_data_and_discount_delivery.js</summary>

![Evidence of no errors and warnings in the download_data_and_discount_delivery.js JavaScript file](docs/validation/validation-js-download_data_and_discount_delivery.PNG) 
</details>

<details>
    <summary>To register in the Mailchimp newsletter: mailchimp_form_submission.js</summary>

![Evidence of no errors and warnings in the mailchimp_form_submission.js JavaScript file](docs/validation/validation-js-mailchimp_form_submission.PNG)
</details>

<details>
    <summary>To let Django admin the name of the image that is going to be changed: notify_image_change_in_admin.js</summary>

![Evidence of no errors and warnings in the notify_image_change_in_admin.js JavaScript file](docs/validation/validation-js-notify_image_change_in_admin.PNG)
</details>

<details>
    <summary>To control buttons and form in product details: product_details.js</summary>

![Evidence of no errors and warnings in the product_details.js JavaScript file](docs/validation/validation-js-product-details.PNG)
</details>

<details>
    <summary>To control buttons and form in product details: product_details.js, with no definition for the CSRFToken</summary>

![Evidence of no errors and warnings in the product_details.js JavaScript file](docs/validation/validation-js-product-details-2.PNG)
</details>

<details>
    <summary>To sort and go to top of page in products: product.js</summary>

![Evidence of no errors and warnings in the product.js JavaScript file](docs/validation/validation-js-products.PNG)
</details>

<details>
    <summary>To control increase/decrease buttons: quantity_incr_decr.js</summary>

![Evidence of no errors and warnings in the quantity_incr_decr.js JavaScript file](docs/validation/validation-js-quantity_incr_decr.PNG)
</details>

<details>
    <summary>To control increase/decrease buttons: quantity_incr_decr.js, with no definition for the CSRFToken</summary>

![Evidence of no errors and warnings in the quantity_incr_decr.js JavaScript file](docs/validation/validation-js-quantity_incr_decr-2.PNG)
</details>

<details>
    <summary>To show Django toasts: show_messages.js</summary>

![Evidence of no errors and warnings in the show_messages.js JavaScript file](docs/validation/validation-js-show-messages.PNG)
</details>

<details>
    <summary>To deal with process payment: stripe_elements.js</summary>

![Evidence of no errors and warnings in the stripe_elements.js JavaScript file](docs/validation/validation-js-stripe_elements.PNG)
</details>



#### [Back to Index](#index)

<br>


### **Python Files**

PEP8 was used to check the files written in Python, with "All right" results.

The tool can be accessed with this link: http://pep8online.com .

Flake8 (command: python3 -m flake8) was run to eliminate the loading of unused libraries.


- **Django Project Files**
<details>
    <summary>asgi.py</summary>

![Evidence of file asgi.py validated with http://pep8online.com/ ](media/validation-python-pep-8-pp5-ci-gdec-asgi.PNG) 
</details>
<details>
    <summary>settings.py</summary>

![Evidence of file settings.py validated with http://pep8online.com/ ](media/validation-python-pep-8-pp5-ci-gdec-settings.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](media/validation-python-pep-8-pp5-ci-gdec-urls.PNG) 
</details>
<details>
    <summary>wsgi.py</summary>

![Evidence of file wsgi.py validated with http://pep8online.com/ ](media/validation-python-pep-8-pp5-ci-gdec-wsgi.PNG) 
</details>
<br>

- **Bag App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-bag-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-bag-apps.PNG) 
</details>
<details>
    <summary>contexts.py</summary>

![Evidence of file contexts.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-bag-contexts.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-bag-models.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-bag-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-bag-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-bag-views.PNG) 
</details>
<br>

- **Checkout App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-checkout-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-checkout-apps.PNG) 
</details>
<details>
    <summary>forms.py</summary>

![Evidence of file forms.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-checkout-forms.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-checkout-models.PNG) 
</details>
<details>
    <summary>signals.py</summary>

![Evidence of file signals.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-checkout-signals.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-checkout-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-checkout-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-checkout-views.PNG) 
</details>
<details>
    <summary>webhook_handler.py</summary>

![Evidence of file webhook_handler.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-checkout-webhook_handler.PNG) 
</details>
<details>
    <summary>webhooks.py</summary>

![Evidence of file webhooks.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-checkout-webhooks.PNG) 
</details>
<br>

- **Contact App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-contact-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-contact-apps.PNG) 
</details>
<details>
    <summary>forms.py</summary>

![Evidence of file forms.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-contact-forms.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-contact-models.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-contact-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-contact-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-contact-views.PNG) 
</details>
<br>

- **Home App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-home-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-home-apps.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-home-models.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-home-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-home-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-home-views.PNG) 
</details>
<br>

- **Products App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-products-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-products-apps.PNG) 
</details>
<details>
    <summary>forms.py</summary>

![Evidence of file forms.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-products-forms.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-products-models.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-products-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-products-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-products-views.PNG) 
</details>
<details>
    <summary>widgets.py</summary>

![Evidence of file widgets.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-products-widgets.PNG) 
</details>
<br>

- **Profiles App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-profiles-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-profiles-apps.PNG) 
</details>
<details>
    <summary>forms.py</summary>

![Evidence of file forms.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-profiles-forms.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-profiles-models.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-profiles-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-profiles-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-profiles-views.PNG) 
</details>
<br>

- **Wish App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-wish-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-wish-apps.PNG) 
</details>
<details>
    <summary>contexts.py</summary>

![Evidence of file contexts.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-wish-contexts.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-wish-models.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-wish-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-wish-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-pep-8-wish-views.PNG) 
</details>
<br>

- **Tools**
<details>
    <summary>build_csv_and_json.py</summary>

![Evidence of file build_csv_and_json.py validated with http://pep8online.com/ ](media/validation-python-pep-8-build_csv_and_json.PNG) 
</details>
<details>
    <summary>products_database_generation_for_QGIS.py</summary>

![Evidence of file products_database_generation_for_QGIS.py validated with http://pep8online.com/ ](media/validation-python-pep-8-products_database_generation_for_QGIS.PNG) 
</details>
<br>

#### [Back to Index](#index)

<br>


### **Accessibility**
https://wave.webaim.org/ was used to validate accessibility. Although there are warnings, all pages contain zero errors, except for the special case when the wish list contains the same product with two different resolutions, where the validator presents multiple form labels. Please see bugs section for more details.

Pages were tested with thier URLs, directly in the we web page address input in at https://wave.webaim.org/, or throught the Wave plugin for Chrome when authentification was needed. Please check evidence below:



<details>
    <summary>Home (index.html)</summary>

![Evidence of no accessibility errors in the home HTML file](docs/validation/validation-accessibility-with-wave-home.PNG) 
</details>
<details>
    <summary>Home (index.html, logged in)</summary>

![Evidence of no accessibility errors in the home HTML file](docs/validation/validation-accessibility-with-wave-home-logged-in.PNG) 
</details>
<details>
    <summary>bag.html</summary>

![Evidence of no accessibility errors in the bag HTML file](docs/validation/validation-accessibility-with-wave-bag.PNG) 
</details>
<details>
    <summary>checkout.html (logged in)</summary>

![Evidence of no accessibility errors in the checkout HTML file](docs/validation/validation-accessibility-with-wave-checkout-logged-in.PNG) 
</details>
<details>
    <summary>checkout_success.html (logged in)</summary>

![Evidence of no accessibility errors in the home checkout-success HTML file](docs/validation/validation-accessibility-with-wave-checkout-success-logged-in.PNG) 
</details>
<details>
    <summary>contact.html</summary>

![Evidence of no accessibility errors in the contact HTML file](docs/validation/validation-accessibility-with-wave-contact.PNG) 
</details>
<details>
    <summary>contact.html (logged in)</summary>

![Evidence of no accessibility errors in the contact HTML file](docs/validation/validation-accessibility-with-wave-contact-logged-in.PNG) 
</details>
<details>
    <summary>thanks.html</summary>

![Evidence of no accessibility errors in the thanks HTML file](docs/validation/validation-html-validator-w3-org-thank-you.PNG) 
</details>
<details>
    <summary>thanks.html (logged in)</summary>

![Evidence of no accessibility errors in the thanks HTML file](docs/validation/validation-accessibility-with-wave-thank-you-logged-in.PNG) 
</details>
<details>
    <summary>add_product.html (logged in)</summary>

![Evidence of no accessibility errors in the add-product HTML file](docs/validation/validation-accessibility-with-wave-add-product-logged-in.PNG) 
</details>
<details>
    <summary>edit_product.html (logged in)</summary>

![Evidence of no accessibility errors in the edit-product HTML file](docs/validation/validation-accessibility-with-wave-edit-product-logged-in.PNG) 
</details>
<details>
    <summary>product_details.html</summary>

![Evidence of no accessibility errors in the product-details HTML file](docs/validation/validation-accessibility-with-wave-product-details.PNG) 
</details>
<details>
    <summary>product_details.html (logged in)</summary>

![Evidence of no accessibility errors in the product-details HTML file](docs/validation/validation-accessibility-with-wave-product-details-logged-in.PNG) 
</details>
<details>
    <summary>products.html</summary>

![Evidence of no accessibility errors in the products HTML file](docs/validation/validation-accessibility-with-wave-products.PNG) 
</details>
<details>
    <summary>products.html (logged in)</summary>

![Evidence of no accessibility errors in the products HTML file](docs/validation/validation-accessibility-with-wave-products-logged-in.PNG) 
</details>
<details>
    <summary>profile.html (logged in)</summary>

![Evidence of no accessibility errors in the profile HTML file](docs/validation/validation-accessibility-with-wave-profile-logged-in.PNG) 
</details>
<details>
    <summary>wish_list.html</summary>

![Evidence of no accessibility errors in the wish-list HTML file](docs/validation/validation-accessibility-with-wave-wish-logged-in.PNG) 
</details>
<details>
    <summary>wish_list.html (logged in)</summary>

![Evidence of no accessibility errors in the wish-list HTML file](docs/validation/validation-accessibility-with-wave-wish-list-logged-in.PNG) 
</details>
<details>
    <summary>404.html</summary>

![Evidence of no accessibility errors in the 404 page HTML file](docs/validation/validation-accessibility-with-wave-404.PNG) 
</details>
<details>
    <summary>404.html, direct URL input</summary>

![Evidence of no accessibility errors in the 404 page HTML file, direct URL input](docs/validation/validation-accessibility-with-wave-404-direct-URL-input.PNG) 
</details>

#### [Back to Index](#index)

<br>


### **Performance**
Google Lighthouse (in Google Chrome) was used to evaluate the performance of the pages. Please check the results below:

<details>
    <summary>Home for cell phones (79)</summary>

![Evidence of no errors in the home HTML file](docs/validation/validation-performance-home-cell-phone.PNG) 
</details>
<details>
    <summary>Home for desktop (88)</summary>

![Evidence of no errors in the home HTML file](docs/validation/validation-performance-home-desktop.PNG) 
</details>
<details>
    <summary>Bag for cell phones (78)</summary>

![Evidence of no errors in the bag HTML file](docs/validation/validation-performance-bag-cell-phone.PNG) 
</details>
<details>
    <summary>Bag for for desktop (96)</summary>

![Evidence of no errors in the bag HTML file](docs/validation/validation-performance-bag-desktop.PNG) 
</details>
<details>
    <summary>Checkout for cell phones (72)</summary>

![Evidence of no errors in the checkout HTML file](docs/validation/validation-performance-checkout-cell-phone.PNG) 
</details>
<details>
    <summary>Checkout for desktop (89)</summary>

![Evidence of no errors in the checkout HTML file](docs/validation/validation-performance-checkout-desktop.PNG) 
</details>
<details>
    <summary>Success Checkout for cell phones (69)</summary>

![Evidence of no errors in the home checkout-success HTML file](docs/validation/validation-performance-success-checkout-cell-phone.PNG) 
</details>
<details>
    <summary>Success Checkout for desktop (95)</summary>

![Evidence of no errors in the home checkout-success HTML file](docs/validation/validation-performance-success-checkout-desktop.PNG) 
</details>
<details>
    <summary>Contact for cell phones (75)</summary>

![Evidence of no errors in the contact HTML file](docs/validation/validation-performance-contact-cell-phone.PNG) 
</details>
<details>
    <summary>Contact for desktop (92)</summary>

![Evidence of no errors in the contact HTML file](docs/validation/validation-performance-contact-desktop.PNG) 
</details>
<details>
    <summary>Thank You Page for cell phones (79)</summary>

![Evidence of no errors in the thanks HTML file](docs/validation/validation-performance-thank-you-page-cell-phone.PNG) 
</details>
<details>
    <summary>Thank You Page for desktop (96)</summary>

![Evidence of no errors in the thanks HTML file](docs/validation/validation-performance-thank-you-page-desktop.PNG) 
</details>
<details>
    <summary>Add Product for cell phones (79)</summary>

![Evidence of no errors in the add-product HTML file](docs/validation/validation-performance-add-product-cell-phone.PNG) 
</details>
<details>
    <summary>Add Product for desktop (97)</summary>

![Evidence of no errors in the add-product HTML file](docs/validation/validation-performance-add-product-desktop.PNG) 
</details>
<details>
    <summary>Edit Product for cell phones (78)</summary>

![Evidence of no errors in the edit-product HTML file](docs/validation/validation-performance-edit-product-cell-phone.PNG) 
</details>
<details>
    <summary>Edit Product for desktop (95)</summary>

![Evidence of no errors in the edit-product HTML file](docs/validation/validation-performance-edit-product-desktop.PNG) 
</details>
<details>
    <summary>Product Details for cell phones (62)</summary>

![Evidence of no errors in the product-details HTML file](docs/validation/validation-performance-product-details-cell-phone.PNG) 
</details>
<details>
    <summary>Product Details for desktop (82)</summary>

![Evidence of no errors in the product-details HTML file](docs/validation/validation-performance-product-details-desktop.PNG) 
</details>
<details>
    <summary>Products for cell phones (77)</summary>

![Evidence of no errors in the products HTML file](docs/validation/validation-performance-products-cell-phone.PNG) 
</details>
<details>
    <summary>Products for desktop (91)</summary>

![Evidence of no errors in the products HTML file](docs/validation/validation-performance-products-desktop.PNG) 
</details>
<details>
    <summary>Profile for cell phones (76)</summary>

![Evidence of no errors in the profile HTML file](docs/validation/validation-performance-profile-cell-phone.PNG) 
</details>
<details>
    <summary>Profile for desktop (84)</summary>

![Evidence of no errors in the profile HTML file](docs/validation/validation-performance-profile-desktop.PNG) 
</details>
<details>
    <summary>Wish List for cell phones (77)</summary>

![Evidence of no errors in the wish-list HTML file](docs/validation/validation-performance-wish-list-cell-phone.PNG) 
</details>
<details>
    <summary>Wish List for desktop (96)</summary>

![Evidence of no errors in the wish-list HTML file](docs/validation/validation-performance-wish-list-desktop.PNG) 
</details>


<br><br>
## [Back to Index](#index)
<br><br>

___
# **11 . Testing**

## **Automatic Testing of Python files with unittest and coverage.py**

The data models and some Python files were tested with unittest. Coverage.py was used to measure the coverage of these automatic tests.

Coverage of 49% was achieved, with 52 tests succesfully executed in 0.347 seconds.

Please see below screenshots of the testing and coverage, the fourth and last links contain the summary.

<details>
    <summary>Screenshot 1 of unittest resuts</summary>

![unittest Image 1](docs/validation/testing-automatic-unittest-1.PNG)
</details>

<details>
    <summary>Screenshot 2 of unittest results</summary>

![unittest Image 2](docs/validation/testing-automatic-unittest-2.PNG)
</details>

<details>
    <summary>Screenshot 3 of unittest results</summary>

![unittest Image 3](docs/validation/testing-automatic-unittest-3.PNG)
</details>

<details>
    <summary>Screenshot 4 of unittest results with summary</summary>

![unittest Image 4](docs/validation/testing-automatic-unittest-4-summary.PNG)
</details>

<details>
    <summary>Screenshot 1 of coverage results</summary>

![coverage.py Image 1](docs/validation/testing-automatic-coverage-1.PNG)
</details>

<details>
    <summary>Screenshot 2 of coverage results</summary>

![coverage.py Image 2](docs/validation/testing-automatic-coverage-2.PNG)
</details>

<details>
    <summary>Screenshot 3 of coverage results, with summary</summary>

![coverage.py Image 3](docs/validation/testing-automatic-coverage-3-summary.PNG)
</details>


<br><br>
## [Back to Index](#index)
<br><br>

## **Testing of User Stories**

- ### **First time users**

The following are testing of User Stories previously described above:
<br><br>

1. As a user, I want to find a well-organized and simple site, so I immediately get the whole picture of the site.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Banner with latest news<br>Home page<br>Products (with product administration for the site owner)<br>Product details (with product administration for the site owner)<br>Bag page<br>Checkout page<br>Secure payment method<br>heckout success page<br>Site access (sign-in and sign-out)<br>Registration (sign-up)<br>Profile with history order<br>Contact form<br>Footer<br>404 page<br>Pop-up status messages<br> | Organize the structure of the site with a fixed navigation menu and footer that includes almost all pages of the site | Navigate to any page of the site from these two features, except to the pages that require a previous step (e.g., adding items to the bag) | Site is fully accessible from top navigation menu and footer; works as expected | 

<details>
    <summary>Fixed Navigation Menu for Desktop Image</summary>

![Fixed Navigation Menu for Desktop Image](docs/features-and-evidence/fixed-navigation-menu.PNG)
</details>
<details>
    <summary>Fixed Navigation Menu for Tablet Image</summary>


![Fixed Navigation Menu for Tablet Image](docs/features-and-evidence/fixed-navigation-menu-tablet.PNG)
</details>
<details>
    <summary>Fixed Navigation Menu for Cell Phones Image</summary>

![Fixed Navigation Menu for Cell Phones Image](docs/features-and-evidence/fixed-navigation-menu-cell.PNG)
</details>
<details>
    <summary>Fixed Navigation Menu, expanded, for Cell Phones Image</summary>

![Fixed Navigation Menu, Expanded, for Cell Phones Image](docs/features-and-evidence/fixed-navigation-menu-cell-expanded.PNG)
</details>
<br><br>

2. As a user, I want to find a responsive site, so I can easily navigate in it in different devices.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Banner with latest news<br>Home page<br>Products (with product administration for the site owner)<br>Product details (with product administration for the site owner)<br>Bag page<br>Checkout page<br>Secure payment method<br>heckout success page<br>Site access (sign-in and sign-out)<br>Registration (sign-up)<br>Profile with history order<br>Contact form<br>Footer<br>404 page<br>Pop-up status messages<br> | Use Bootstrap and media queries to adapt the site design to all screen sizes | Show readable content, while keeping functionality and design, in all screen sizes  | Works as expected | 

<details>
    <summary>Desktop example: Home</summary>

![Desktop example, Home, Image](docs/features-and-evidence/home-page-desktop.PNG)
</details>
<details>
    <summary>Desktop example: Products</summary>

![Desktop example, Products, Image](docs/features-and-evidence/products.PNG)
</details>
<details>
    <summary>Tablet example: Products</summary>

![Tablet example, Products, Image](docs/features-and-evidence/products-tablet.PNG)
</details>
<details>
    <summary>Tablet example: Bag</summary>

![Tablet example, Bag, Image](docs/features-and-evidence/bag-tablet.PNG)
</details>
<details>
    <summary>Cell phone example: Products</summary>

![Cell phone example, Products, Image](docs/features-and-evidence/products-cell.PNG)
</details>
<details>
    <summary>Cell phone example: Wish List</summary>

![Cell phone example, Wish List, Image](docs/features-and-evidence/wish-list-cell.PNG)
</details>
<br><br>

3. As a user, I want to receive a confirmation of registration when I sign up, so I know that the process for creating my account went well.


| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Registration (sign-up)<br>Pop-up status messages<br> | Use Django confirmation page to inform the user of a successgul sign-up | Show a successful message on a page after signing up | Works as expected | 

<details>
    <summary>Registration, Step 1</summary>

![Registration, Step 1, Image](docs/features-and-evidence/sign-up-registration-1.jpg) 
</details>
<details>
    <summary>Registration, Step 2</summary>

![Registration, Step 2, Image](docs/features-and-evidence/sign-up-registration-2.jpg) 
</details>
<details>
    <summary>Registration, Step 3, Confirmation</summary>

![Registration, Step 3, Confirmation](docs/features-and-evidence/sign-up-registration-3.jpg) 
</details>
<br><br>


4. As a user, I want to be able to contact the site administrator, owner and/or developer, so I can send feedback to them.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Contact form<br>Footer<br> | Implement a contact form in a separated page, give contact options in footer (which is available in all pages of the site) | Access contact form and other options directly from the footer | Works as expected | 

<details>
    <summary>Contact Form Link in Footer</summary>

![Contact Form Link in Footer](docs/features-and-evidence/footer-desktop-contact-form-link.jpg) 
</details>
<details>
    <summary>Contact Form</summary>

![Contact Form](docs/features-and-evidence/contact-form.PNG) 
</details>
<br><br>


5. As a user, I want to have access to my account easily, so I can quickly log in.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Site access (sign-in and sign-out)<br>Registration (sign-up)<br>Footer<br> | Include access links to account in fixed navigation menu and footer | Access sign-in page from these features | Works as expected | 

<details>
    <summary>Access Log-in from Top Navigation Menu</summary>

![Access Log-in from Navigation Menu](docs/features-and-evidence/log-in-from-top-nav-desktop.PNG) 
</details>
<details>
    <summary>Access Log-in from Top Navigation Menu (Smaller Screens)</summary>

![Access Log-in from Navigation Menu (Smaller Screens)](docs/features-and-evidence/log-in-from-top-nav-cell.PNG) 
</details><details>
    <summary>Access Log-in from Footer</summary>

![Access Log-in from Footer](docs/features-and-evidence/log-in-from-footer-desktop.PNG) 
</details>
<details>
    <summary>Access Log-in from Footer (Smaller Screens)</summary>

![Access Log-in from Footer (Smaller Screens)](docs/features-and-evidence/log-in-from-footer-cell.PNG) 
</details>
<br><br>


- ### **Returning users**


6. As a returning user, I want to be able to contact the site administrator and/or owner and/or developer, so I can send feedback to them.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Contact form<br>Footer<br> | Similar to user story 4, implement a contact form in a separated page, give as many as possible contact options in footer (which is available in all pages of the site) | Access contact form and other options directly from the footer | Works as expected | 

<details>
    <summary>Contact Form Link in Footer</summary>

![Contact Form Link in Footer](docs/features-and-evidence/footer-desktop-contact-form-link.jpg) 
</details>
<details>
    <summary>Contact Form</summary>

![Contact Form](docs/features-and-evidence/contact-form.PNG) 
</details>
<br><br>


7. As a returning user, I want a navigation menu on top, always visible, so I can access the main content on the website from there and do not need to use the back button of the browser.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br> | Include a fixed navigation menu on top, in the header of pages, with links to main parts of the site | Navigate to the selected sites, without using the back button, without scrolling down, and without manually editing the URL  | Works as expected | 

<details>
    <summary>Fixed Navigation Menu for Desktop Image</summary>

![Fixed Navigation Menu for Desktop Image](docs/features-and-evidence/fixed-navigation-menu.PNG)
</details>
<details>
    <summary>Fixed Navigation Menu for Tablet Image</summary>


![Fixed Navigation Menu for Tablet Image](docs/features-and-evidence/fixed-navigation-menu-tablet.PNG)
</details>
<details>
    <summary>Fixed Navigation Menu for Cell Phones Image</summary>

![Fixed Navigation Menu for Cell Phones Image](docs/features-and-evidence/fixed-navigation-menu-cell.PNG)
</details>
<details>
    <summary>Fixed Navigation Menu, expanded, for Cell Phones Image</summary>

![Fixed Navigation Menu, Expanded, for Cell Phones Image](docs/features-and-evidence/fixed-navigation-menu-cell-expanded.PNG)
</details>
<br><br>


8. As a returning user, I want to have access to my account easily, so I can quickly log in.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Site access (sign-in and sign-out)<br>Registration (sign-up)<br>Profile with history order<br>Footer<br> | Include access links to account in fixed navigation menu and footer | Access sign-in page from these features | Works as expected | 

<details>
    <summary>Access Log-in from Top Navigation Menu</summary>

![Access Log-in from Navigation Menu](docs/features-and-evidence/log-in-from-top-nav-desktop.PNG) 
</details>
<details>
    <summary>Access Log-in from Top Navigation Menu (Smaller Screens)</summary>

![Access Log-in from Navigation Menu (Smaller Screens)](docs/features-and-evidence/log-in-from-top-nav-cell.PNG) 
</details><details>
    <summary>Access Log-in from Footer</summary>

![Access Log-in from Footer](docs/features-and-evidence/log-in-from-footer-desktop.PNG) 
</details>
<details>
    <summary>Access Log-in from Footer (Smaller Screens)</summary>

![Access Log-in from Footer (Smaller Screens)](docs/features-and-evidence/log-in-from-footer-cell.PNG) 
</details>
<br><br>


9. As a returning user, I want to have a way to contact the developer so I can contribute and/or indicate errors or bugs.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Contact form<br>Footer<br> | Similar to user stories 4 and 6, implement a contact form in a separated page and add contact options in the footer | Access contact form and other options directly from the footer | Works as expected | 

<details>
    <summary>Contact Form Link in Footer</summary>

![Contact Form Link in Footer](docs/features-and-evidence/footer-desktop-contact-form-link.jpg) 
</details>
<details>
    <summary>Contact Form</summary>

![Contact Form](docs/features-and-evidence/contact-form.PNG) 
</details>
<br><br>


10. As a returning user, I want to be informed if the contact form goes through, so I know if my message is being sent or it is not.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>404 page<br>Pop-up status messages<br> | Use a Django confirmation page to inform the user if sending the contact form is successful | Show a successful page after sending the form | Works as expected | 

<details>
    <summary>Contact Form Confirmation</summary>

![Contact Form Confirmation](docs/features-and-evidence/contact-form-confirmation.PNG) 
</details>
<br><br>


11. As a returning user, I want to recover my password easily if I forget it, so I do not worry about remembering and/or keeping it.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br> | ... | ... | ... | 

<details>
    <summary>Recover Forgotten Password, Step 1</summary>

![Recover Forgotten Password, Step 1, Image](docs/features-and-evidence/forgot-password-1.PNG) 
</details>
<details>
    <summary>Recover Forgotten Password, Step 2</summary>

![Recover Forgotten Password, Step 2, Image](docs/features-and-evidence/forgot-password-2.PNG) 
</details>
<details>
    <summary>Recover Forgotten Password, Step 3, Confirmation</summary>

![Recover Forgotten Password, Step 3, Confirmation](docs/features-and-evidence/forgot-password-3.PNG) 
</details>
<details>
    <summary>Recover Forgotten Password, Step 4, Confirmation</summary>

![Recover Forgotten Password, Step 4, Confirmation](docs/features-and-evidence/forgot-password-4.PNG) 
</details>
<details>
    <summary>Recover Forgotten Password, Step 5, Confirmation</summary>

![Recover Forgotten Password, Step 5, Confirmation](docs/features-and-evidence/forgot-password-5.PNG) 
</details>
<br><br>


12. As a returning user, I want to have a history of my purchases, so I know what I have bought and spent through time.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Profile with history order<br> | Store orders and link them to the user profile that originated it | Show purchase history in profile | Works as expected | 

<details>
    <summary>Purchase History</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/profile-with-purchase-history.jpg) 
</details>
<br><br>



- ### **Shoppers**

13. As a shopper, I want to have the products to buy visible (without many details so I can see more), so I can select them for purchase.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Products (with product administration for the site owner)<br>Product details (with product administration for the site owner)<br> | Create a data model where products are viewed in the body of a unique page according to a specific selection | Show all products in a page (in the body) according to the selection and/or sort in the fixed navigation menu | Works as expected | 

<details>
    <summary>Products Page</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/products-to-buy.PNG) 
</details>
<br><br>


14. As a shopper, I want to have access to the product details, so I can access them in case I am not sure about the purchase and/or want to have a better description of the product.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Products (with product administration for the site owner)<br>Product details (with product administration for the site owner)<br> | Create a view with product details after clicking on the product itself  | Show product details in a different page/view | Works as expected | 

<details>
    <summary>Product Details</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/product-details-to-buy.PNG) 
</details>
<br><br>


15. As a shopper, I want to have a detailed view of my shopping cart, so I know what I am buying and have the current purchase details just before paying.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Bag page<br>Checkout page<br> | Create a bag app to show the current shopping cart, with a link in the fixed navigation menu | Show shopping cart in a different page/view | Works as expected | 

<details>
    <summary>Shopping Bag, top</summary>

![Shopping Bag, top](docs/features-and-evidence/shopping-bag-top.PNG) 
</details>
<details>
    <summary>Shopping Bag, bottom</summary>

![Shopping Bag, bottom](docs/features-and-evidence/shopping-bag-bottom.PNG) 
</details>
<br><br>


16. As a shopper, I want to have the amount I am spending always visible, so I know how much I am spending.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Bag page<br> | Compute total of bag and return it to the view containing the fixed navigation menu | Show spent amount, at all times, in fixed navigation menu | Works as expected | 

<details>
    <summary>Permanent Spending Amount</summary>

![Permanent Spending Amount](docs/features-and-evidence/spending-amount.PNG) 
</details>
<br><br>


17. As a shopper, I want to have special offers easily accessible, so I can buy them before they disappear if I find them useful.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br> | Include a link/list item element to special offers in the fixed navigation menu | Access special offers after cliking on this link/list item element of the menu | Works as expected | 

<details>
    <summary>Easy Access for Offers</summary>

![Easy Access for Offers](docs/features-and-evidence/Esri-map.PNG) 
</details>
<details>
    <summary>Easy Access for Offers in Checkout</summary>

![Easy Access for Offers in Checkout](docs/features-and-evidence/checkout-success-with-offers-button.jpg) 
</details>
<br><br>


18. As a shopper, I want to have a search field, so I do not spend much time finding the product I want to buy

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br> | Include a search field in the fixed navigation menu that looks for products (according to the search criteria) in the backend and return the results to the products page | Show products related to the search criteria | Works as expected | 

<details>
    <summary>Search Field for Desktop</summary>

![Search Field for Desktop](docs/features-and-evidence/search-field-desktop.jpg) 
</details>
<details>
    <summary>Search Field for Smaller Screens</summary>

![Search Field for Smaller Screens](docs/features-and-evidence/search-field-smaller-screens.PNG) 
</details>
<br><br>


19. As a shopper, I want to have categories of products, so I find a product easily if I do not know its name.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Products (with product administration for the site owner)<br> | Include links/list item elements in the fixed navigation menu that filter the data in the backend according to categories (previously created) and return the result to the products page/view | Show products related to the selected category in the menu | Works as expected | 

<details>
    <summary>Products by Categories</summary>

![Products by Categories](docs/features-and-evidence/find-products-by-category-1.PNG) 
</details>
<details>
    <summary>Products by Categories, Digital Data</summary>

![Products by Categories, Digital Data](docs/features-and-evidence/find-products-by-category-2.PNG) 
</details>
<details>
    <summary>Products by Categories, Reports</summary>

![Products by Categories, Reports](docs/features-and-evidence/find-products-by-category-3.PNG) 
</details>
<details>
    <summary>Products by Categories, Training</summary>

![Products by Categories, Training](docs/features-and-evidence/find-products-by-category-4.PNG) 
</details>
<details>
    <summary>Products by Categories, Software</summary>

![Products by Categories, Software](docs/features-and-evidence/find-products-by-category-5.PNG) 
</details>
<details>
    <summary>Products by Categories, Offers</summary>

![Products by Categories, Offers](docs/features-and-evidence/find-products-by-category-6.PNG) 
</details>
<br><br>


20. As a shopper, I want to have prices always visible, so I know the value of the products at all times.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Products (with product administration for the site owner)<br>Product details (with product administration for the site owner)<br>Bag page<br> | Compute total of bag and return it to the view containing the fixed navigation menu | Show spent amount, at all times, in fixed navigation menu | Works as expected | 

<details>
    <summary>Visible Prices in the Bag</summary>

![Visible Prices in the Bag](docs/features-and-evidence/bag-tablet-prices.jpg) 
</details>
<details>
    <summary>Visible Prices in the Product Details</summary>

![Visible Prices in the Product Details](docs/features-and-evidence/product-details-prices.PNG) 
</details>
<details>
    <summary>Visible Prices in the Wish List</summary>

![Visible Prices in the Wish List](docs/features-and-evidence/wish-list-prices.jpg) 
</details>
<details>
    <summary>Visible Prices in Products</summary>

![Visible Prices in Products](docs/features-and-evidence/products-prices.PNG) 
</details>
<br><br>


21. As a shopper, I want to have the different resolutions of the products visible, close to the product it belongs to, so I can easily select it without further action.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Products (with product administration for the site owner)<br>Product details (with product administration for the site owner)<br> | Add a field in the products model that activate a product feature related to the resolution (if applicable), giving the user the option to select it | Show the different available resolutions for the products (e.g., in a dropdown element), considering them as other product if a different resolution (than the one in the bag) is selected, updating the quantities in the bag accordingly | Works as expected | 

<details>
    <summary>Selection of Product Resolution</summary>

![Selection of Product Resolution](docs/features-and-evidence/selection-of-resolution.PNG) 
</details>
<br><br>


22. As a shopper, I want to have a secure payment method, so I can rest assured that the purchase procedure is safe.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Checkout page<br>Secure payment method<br>heckout success page<br> | Implement a payment method that is well known and secure | Process payments from users/shoppers | Stripe payments implemented, Works as expected | 

<details>
    <summary>Stripe Payment Process right after Purchasing</summary>

![Stripe Payment Process right after Purchasing](docs/features-and-evidence/Stripe-payment.PNG) 
</details>
<details>
    <summary>Stripe Payment Process right after Purchasing, Success Checkout</summary>

![Stripe Payment Process right after Purchasing, Success Checkout](docs/features-and-evidence/checkout-success.PNG) 
</details>
<br><br>


- ### **Site Owner**

23. As owner, I want to provide an introductory page, so users know what can be found in the website and what can be purchased.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Home page<br> | Design the home page to give a quick overview of the e-commerce | Find the home page, giving the idea of the e-commerce and a few messages to give the user an idea of what can be found in the site | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>


24. As owner, I want to provide an easy process for registration, so I ensure a connection with a potential buyer.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Footer<br> | Include a Django app and page to easily register/sign up in the site if the user opts for this, with links to this option in the fixed navigation menu and footer | Access page for sign-up easily from menu and footer, with a few steps to achieve the task | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>


25. As owner, I want to provide a search field for products on top, so I require users/shoppers the minimum possible time to find a product (and therefore reduce the risk of leaving).

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br> | As user story 18, include a search field in the fixed navigation menu that looks for products (according to the search criteria) in the backend and return the results to the products page | Show products related to the search criteria | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>


26. As owner, I want to organize products in categories, so users find an organized site and can find products easily.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Products (with product administration for the site owner)<br> | As user story 19, include links/list item elements in the fixed navigation menu that filter the data in the backend according to categories (previously created) and return the result to the products page/view | Show products related to the selected category in the menu | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>


27. As owner, I want to receive feedback from users, so I can take actions in response to them if needed.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Contact form<br>Footer<br> | Similar to user stories 4; 6 and 9; implement a contact form in a separated page, give as many as possible contact options in footer (which is available in all pages of the site) | Access contact form and other options directly from the footer | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>


28. As owner, I want to provide a navigation menu on top and always visible, so users can access any content at any time without needing the back button.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br> | As user story 7, Include a fixed navigation menu on top, in the header of pages, with links to main parts of the site | Navigate to the selected sites, without using the back button, without scrolling down, and without manually editing the URL  | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>


29. As owner, I want to give as many options to be contacted as possible, so users can choose forms or links in the footer to send their consultations and/or feedback in a very fast way.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Contact form<br>Footer<br> | Similar to user stories 4; 6; 9 and 27; implement a contact form in a separated page, give as many as possible contact options in footer (which is available in all pages of the site) | Access contact form and other options directly from the footer | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>


30. As owner, I want to provide a responsive website, so user can access it from any device without any constraint to navigate, find and/or use the website.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Banner with latest news<br>Home page<br>Products (with product administration for the site owner)<br>Product details (with product administration for the site owner)<br>Bag page<br>Checkout page<br>Secure payment method<br>heckout success page<br>Site access (sign-in and sign-out)<br>Registration (sign-up)<br>Profile with history order<br>Contact form<br>Footer<br>404 page<br>Pop-up status messages<br> | Similar to user story 2, use Bootstrap and media queries to adapt the site design to all screen sizes | Show readable content, while keeping functionality and design, in all screen sizes  | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>


31. As owner, I want to inform users if their consultation/message was successfully sent, so they know if they need to resend it or they do not.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Pop-up status messages<br> | Similar to user story 10, use a Django confirmation page to inform the user if sending the contact form is successful | Show a successful page after sending the form | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>


32. As owner, I want to inform the user, through an error page, if there is any error when loading the website.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>404 page<br> | Use Django error page to inform the user if any action when navigating the site produces an error | Show an error message on a page after facing a problem, e.g., a broken URL | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>


- ### **Developer**

33. As developer, along with other points of this section, I want to show my work and give the option to users to contact me if they wish.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Fixed navigation menu<br>Banner with latest news<br>Home page<br>Products (with product administration for the site owner)<br>Product details (with product administration for the site owner)<br>Bag page<br>Checkout page<br>Secure payment method<br>heckout success page<br>Site access (sign-in and sign-out)<br>Registration (sign-up)<br>Profile with history order<br>Contact form<br>Footer<br>404 page<br>Pop-up status messages<br> | Implement all knowledge gathered so far in full-stack software development, with as many features as possible according to the Code Institute program time frame | Show as many full-stack software development capabilities as possible | Expecting results and feedback | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>



___
# 12 . Marketing Strategy

## SEO Analysis


The search engine optimization is focused on Google search engine since it accounts for more than 90% of user searches.

Basically, Google ellaborates a ranking of pages (according to the criteria being searched) and shows them in the result according to this ranking. Algorithms and human raters are used to position pages in these search resutls.

In order to have our page in the first results (user will usually not read after the first page of results), we need our page to be highly ranked in the resarch resutls.

A way to do it is by including keywords, which can be short-tail (one or two words, highly ranking but giving a lot of "competitors") or long-tail (phrases, more specific to our products or page, but with less ranking). Therefore, the best solution might be considered that one that produces a high volume of results with low competition.

First, a list of important keywords is created, thinking in our buyers and user personas. Then, the most relevant ones are selected based on volume (high) and competition (low).

(April 5th, 2022)
(Quality Factor:
No e-commerce/No service provider = 1;
No e-commerce/service provider after first page= 2;
No e-commerce/service provider in first page = 3;
E-commerce after first page = 4
E-commerce in first page = 5)
Just to have an idea and assign a quantification to the selection, the "Volume" is multiplied by the "Quality Factor" (and divided by 1000000 to have smaller figures). This is a subjective approach, however the results are still interesting:

| Keywords | Volume (from Google.com) | Content, general description (searching in Google.com) | "Quality Factor" | Volume x "Quality Factor" / 1000000 |
| ---- | ---- | ---- | ---- | ---- |
| Keywords                      | Volume (from Google.com)  | Content, general description (searching in Google.com)                                           | "Quality Factor"     |   Volume x "Quality Factor" / 1000000 |
| Geophysical data              |                55,300,000 | No e-commerce in first three pages, most science sites                                           |                     1|         55                            |
| Digital elevation model       |                68,200,000 | No e-commerce in first three pages, software provider in second page                             |                     2|        136                            |
| DEM                           |             4,950,000,000 | No e-commerce in first three pages, most science sites, data acquisition provider in second page |                     2|      9,900                            |
| Magnetometry                  |                 2,010,000 | No e-commerce in first three pages, service providers in first page                              |                     3|          6                            |
| Gravimetry                    |                22,900,000 | No e-commerce, service providers in third page                                                   |                     2|         46                            |
| Resistivity                   |               101,000,000 | No e-commerce in first three pages, book in third page                                           |                     2|        202                            |
| Buy geophysical data          |                 3,940,000 | E-commerce and books on first page                                                               |                     5|         20                            |
| Buy DEM data                  |                52,800,000 | E-commerce on first page, science sites                                                          |                     5|        264                            |
| Buy Magnetometry data         |                10,500,000 | E-commerce and data acquisition providers on first page                                          |                     5|         53                            |
| Buy Gravimetry data           |                15,500,000 | E-commerce and data acquisition providers on first page                                          |                     5|         78                            |
| Buy Resistivity data          |                24,300,000 | Service providers and e-commerce on first page                                                   |                     5|        122                            |
| DEM data                      |             3,870,000,000 | E-commerce on first page (bottom), science sites                                                 |                     5|     19,350                            |
| Magnetometry data             |                10,500,000 | Science sites, equipment in second page, images of equipment on first page                       |                     2|         21                            |
| Gravimetry data               |                17,200,000 | E-commerce on first page (top), science sites                                                    |                     5|         86                            |
| Resistivity data              |                17,200,000 | No e-commerce in first three pages, most science sites                                           |                     1|         17                            |
| Geophysical book              |                30,900,000 | Lot of books and e-commerce right from the top of first page                                     |                     5|        155                            |
| Geophysical training          |                16,500,000 | Training service provider on first page                                                          |                     4|         66                            |
| Geophysical data acquisition  |                 8,740,000 | Science, data acquisition service provider on second page                                        |                     3|         26                            |
| Geophysical data              |               201,000,000 | Science, e-commerce for paper and books in third page                                            |                     4|        804                            |
| DEM acquisition               |               113,000,000 | Science                                                                                          |                     1|        113                            |
| Magnetometry acquisition      |                 1,930,000 | Science, equipment on second page                                                                |                     2|          4                            |
| Gravimetry acquisition        |                 3,100,000 | Science, with service provider and book and first page                                           |                     3|          9                            |
| Resistivity acquisition       |                 6,810,000 | Science, book in first page and service provider in second one                                   |                     3|         20                            |
| DEM processing                |               389,000,000 | Science                                                                                          |                     1|        389                            |
| Magnetometry processing       |                 4,810,000 | Service, equipment provider in first page; science                                               |                     3|         14                            |
| Gravimetry processing         |                 7,440,000 | Science                                                                                          |                     1|          7                            |
| Resistivity processing        |                31,700,000 | Service provider in second page                                                                  |                     2|         63                            |
| DEM books                     |             6,420,000,000 | E-commerce from first page                                                                       |                     5|     32,100                            |
| Magnetometry books            |                 1,950,000 | E-commerce from first page                                                                       |                     5|         10                            |
| Gravimetry books              |                 4,400,000 | E-commerce from first page                                                                       |                     5|         22                            |
| Resistivity books             |                11,000,000 | E-commerce from first page                                                                       |                     5|         55                            |
| DEM training                  |             4,140,000,000 | Science                                                                                          |                     1|      4,140                            |
| Magnetometry training         |                 1,680,000 | Many training courses in first page, service provider in second page, science                    |                     4|          7                            |
| Gravimetry training           |                 1,840,000 | training courses in first page, science                                                          |                     4|          7                            |
| Resistivity training          |                26,500,000 | Non-related topics from first page (resistance)                                                  |                     1|         27                            |
| DEM software                  |             3,640,000,000 | E-commerce in first page, many products                                                          |                     5|     18,200                            |
| Magnetometry software         |                 4,770,000 | Service providers, e-commerce and books in first page                                            |                     5|         24                            |
| Gravimetry software           |                 4,890,000 | Science, service provider in first page                                                          |                     3|         15                            |
| Resistivity software          |                11,000,000 | Service providers from first page                                                                |                     3|         33                            |


<details>
    <summary>SEO Analysis</summary>

![SEO Analysis](docs/features-and-evidence/SEO_Analysis.PNG) 
</details>
<br><br>

<details>
    <summary>SEO Analysis (Ordered)</summary>

![SEO Analysis](docs/features-and-evidence/SEO_Analysis_Ordered.PNG) 
</details>
<br><br>


As it can be observed, the following keywords produce high volume of searches with a focus in our e-commerce nature:
"DEM books", "DEM data", "DEM software", "DEM training", "Geophysical data".

Then, those with a "quality factor" of 5 (where an e-commerce appears in the first page of a Google search, since we are interested in promoting an e-commerce( are the following ones:
"Buy DEM data", "Geophysical book", "Buy Resistivity data", "Gravimetry data", "Buy Gravimetry data", "Resistivity books", "Buy Magnetometry data", "Magnetometry software", "Gravimetry books", "Buy geophysical data", "Magnetometry books".

Also, it can be observed a clear trend for unique words like "DEM", "Geophysical", "Buy" and "Data", so they were analized as well.

After analyzing "DEM" with wordtracker.com, it is observed that it produces a high volume and good competition comparisson. Therefore "DEM" is also included as keyword.

Also, after analyzing "Geophysical" with wordtracker.com, it is observer a great score for volume and competition, achiving the first place in both for similar keyworkds.

"Buy" and "Data" are not finally included in the keywords as they are too general.

Therefore, the final keywords for the projects are the following 18 ones:
"DEM books", "DEM data", "DEM software", "DEM training", "Geophysical data", "Buy DEM data", "Geophysical book", "Buy Resistivity data", "Gravimetry data", "Buy Gravimetry data", "Resistivity books", "Buy Magnetometry data", "Magnetometry software", "Gravimetry books", "Buy geophysical data", "Magnetometry books", "DEM", "Geophysical".

On the other hand, keyworkd staffing was also carried out when possible, for example, in headings and "<strong>" tags. Social links include the attibute "rel" with "noopener" in order to have search engines not including these links in their search rankings. Images include an "alt" attribute as descriptive for the image as possible (including a meaningful file name). In the metadata we include the descritpion of the e-commerce and these 17 keyworkds.

Finally, we include the sitemap.xml (in the root folder) to increase the chances of a higher rank in search engines and help them on finding relevant content, and a robots.txt to "tell" them where "not to navigate" (which simoultaneously increase the ranking of the site since they consider a site that contains a file like this of goog quality).

sitemap.xml: created using XML-Sitemaps.com
robots.txt: tested with https://support.google.com/webmasters/answer/6062598?hl=en

Reference: Code Institue, SEO lessons.

<details>
    <summary>wordtracker.com analysis for "DEM" keyword</summary>

![DEM Analysis with wordtracker](docs/features-and-evidence/wordtracker-com-for-dem.jpg) 
</details>
<br><br>


<details>
    <summary>wordtracker.com analysis for "Geophysical" keyword</summary>

![DEM Analysis with wordtracker](docs/features-and-evidence/wordtracker-com-for-geophysical.jpg) 
</details>
<br><br>


## Organic Growth with Social Media (Facebook and LinkedIn)

Since the e-commerce is oriented to a professional and specialized community, the organic growth (which should simoultaneously be considered with organic growth) is suitable for LinkedIn. This social network makes possible the interaction with users and allow them to take training related to the products of the GDEC e-commerce. This social network seems to be very suitable for universities and research institutions that use these kind of data.

Similarly, Facebook, achieves the same goal, with better perspective towards advertising and user interaction, and with a higher amount of users.

The page below was built in Facebook with the aim of interacting with potential users, answer consultations, promoting our products, connect to clients and potential clients and have the change to connect to other potential buyers (users) and/or other social networks through them. It was built trying to use as much content from the GDEC site as possible, so there is a good match between the content of the website and the Facebook page.

<details>
    <summary>GDEC Facebook Page</summary>

![GDEC Facebook Page Image](docs/features-and-evidence/Facebook_Page.png) 
</details>
<br><br>

<details>
    <summary>GDEC Facebook Page</summary>

![GDEC Facebook Page PDF](docs/features-and-evidence/Facebook_Page.pdf) 
</details>
<br><br>


## Paid Marketing

As mentioned before, the above strategies should be carried out with a paid strategy, focusing the expenditures (which might not be necessarily high but constant through time) in geopysical exhibitions (like EAGE or SEG among many others), and on those news or science websites that could caught the atention of authorities (since these kind of data are usually used by them.)




## [Back to Index](#index)
<br><br>

___
# 12 . Bugs

Some bugs were related to design, positioning and tags of elements in the page, with variables in Django templates among them. Also, many minor bugs were solved just by assigning the correct property and/or by trial and error.

Bugs that required more time and specific solutions were the following ones:

| Bug | Solution |
| ---- | ---- |
| It was not possible to keep the checkbox for cancelling the delivery cost activated, sending the form to the backend but deactivating it immediately after.  | The issue was caused by addressing the checkbox with both JavaScript and an "if" statement in the HTML template, strangely requiring an assignment of the "cancel_delivery_cost" twice, one row after the other, likely due to the time taken for the view to be loaded. The issue was solved by addressing the checkbox with an "if" statement only in the checkbox HTML tag. | 
| It was not possible to ... | The issue arises for ...; solved with ... |


<br><br>
## [Back to Index](#index)
<br><br>

___
# 13 . Deployment

The website was fully written in Gitpod, permanently tested in Gitpod terminal, and periodically deployed to GigHub Pages (in a main branch) and Heroku Platform (to handle backend languages). After first deployment, several updates have been carried out before the final version. These updates were implemented in the deployed website from Gitpod, just by using the "push" command for every commit (change) in the ongoing development. Amazon Web Services S3 is also implemented to contain the static files.

The project repository can be forked from GitHub [here](https://github.com/csc7/PP5_CI_GDEC) (https://github.com/csc7/PP5_CI_GDEC), please check for the "Fork" button, top-right of the page, to achieve this task.

The fully deployed program, accessible by anyone, is found [here](https://pp5-ci-gdec.herokuapp.com/), whose URL is https://pp5-ci-gdec.herokuapp.com/ . Its repository is found [here](https://github.com/csc7/PP5_CI_GDEC), whose URL is https://github.com/csc7/PP5_CI_GDEC.

Follow these steps to deploy the content of this project:

1 - Create a Heroku app in Heroku website (more intuitive process, selecting "create new app") or using the CLI in Gitpod if you manage the commands for this and use this development environment.

2 - Add Postgres resource to the Heroku app (in Heroku website, "Resources", "add-ons"), where a "Hobby Dev - Free" plan is enough.

3 - In Gitpod (or your development environment), install dj_database_url with this command:
pip3 install dj_database_url

4 - In Gitpod (or your development environment), install psycopg2-binary with this command:
pip3 install psycopg2-binary

5 - Freeze the environment requirements:
pip3 freeze > requirements.txt

6 - Add/Import the following line/pakage in your settings.py file (on top of the file, with other "import" commands):
import dj_database_url


7 - In settings.py update the DATABASES variable to the following lines, so the database is read from the local repository in not set up in Heroku;
from:
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }

to:
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


8 - Connect to Heroku database and run migrations with the following commands:

If you want to verify that effectively all migrations need to be run, execute
python3 manage.py showmigrations

Then migrate:
python3 manage.py migrate

9 - Load/Import database (categories and products):
a) If you use the database of this repository, use the following commands (in this order, since products depends on categories):
python3 manage.py loaddata categories
python3 manage.py loaddata products

b) If you manually create the database, please follow this steps:
Credits: Code Institute:
 - Make sure your manage.py file is connected to your mysql database
 - Use this command to backup your current database and load it into a db.json file:
./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
 - Connect your manage.py file to your postgres database
 - Then use this command to load your data from the db.json file into postgres:
./manage.py loaddata db.json

10 - Create superuser in Heroku:
python3 manage.py createsuperuser

11 - Install gunicorn to work as a webserver:
pip3 install gunicorn

12 - Again, freeze the environment requirements:
pip3 freeze > requirements.txt


13 - Create Procfile (just create file and assign "Procfile" as name) in the project root directory, and include this line in it:
web: gunicorn your_app_name.wsgi:application

14 - Log in into Heroku from the Gitpod CLI with the following line, entering the required information:
heroku login (it will require to log in through a different browser)
or
heroku login -i (to log in directly in the Gitpod CLI)

15 - OPTIONAL: Set DISABLE_COLLECTSTATIC to 1, so Heroku does not load static files when deplying (at this point of the process, in case you want to look the website before deploying in Amazon Web Services):
heroku config:set DISABLE_COLLECTSTATIC=1 --app your_app_name

16 - Ensure ALLOWED_HOSTS variable in settings.py file is set as follows:
ALLOWED_HOSTS = ['your_app_name.herokuapp.com', 'localhost']



17 - Create a SECRET_KEY, e.g., using https://miniwebtool.com/django-secret-key-generator/.
Then assig a SECRET_KEY value in Config Vars of the Settings section in Heroku.
Then, in settings.py file, ensure SECRET_KEY variable is set as follows:
SECRET_KEY = os.environ.get('SECRET_KEY', '')

18 - Crease Amazon Web Services account (if needed) and S3 bucket.
Assign the bucket a name (e.g., your_app_name), with "ACLs enabled", "Block off public access" disables (accepting warning message below), and then set the following variables:
 * Properties tab: Static website hosting, using it to host a website, incidating index.html and error.html in the index and error documents.
 * Permissions tab:
    - CORS configuration (required to have access between Heroku and S3), copying these lines of code:
        [
          {
              "AllowedHeaders": [
                  "Authorization"
              ],
              "AllowedMethods": [
                  "GET"
              ],
              "AllowedOrigins": [
                  "*"
              ],
              "ExposeHeaders": []
          }
        ]
 * Buccket Policy: click on "Policy Generator" at the bottom and, in the new page, select "S3 Bucket Policy" as the type of policy, assing a start ("*") to "Principal" to allow all of them, "GetObject" in "Actions", paste the ARN of the bucket (found in the "Properties" of the bucket) in the corresponding field, generate policy, copy the resulting code in the "Bucket Policy" that originated this new page, and save.
 * Access Control List: enable "List objects" for "Everyone.

19 - Add Amazon Web Services Identify and Access Management (IAM) to create a user to access the S3 bucket and apply the following changes:
 * Open IAM from AWS available services.
 * Go to "User Groups" (left), "Create group" (top right), assign a name (e.g., manage_your_app_name) and create (bottom).
 * Go to "Policies", "Create Policy", go to "JSON" tab, "Import managed policy", select "AmazonS3FullAccess", "Import". In the "Resource" field of the JSON structure, assign the ARN of your app as follows:
 ...
 "Resource": [
     "arn",
     "arn/*"
 ]
 * Then click "Next:Tags", "Next:Review" (assign a name, e.g., your_app_name_policy; and a description, e.g., "Access to S3")and "Create Policy". The policy will appear in the list of policies.
 * Go to "User Groups", select your app, "Permissions", "Attach Policies" (in "Add Permissions" button), select the one you have just created and click "Add Permissions" on the bottom.
 * Go to "Users", "Add user", assign a name (e.g., "your_app_name_access_to_static_files"), select "Programatic access", and "Next:Permissions".
 * "Add user to group", select the policy you have just created and click "Next: Tags", then "Next: Review" and finally "Create User".
 * IMPORTANT: AFTER ADDING THE USER TO THE GROUP, DOWLOAD THE .CSV FILE AS IT MIGHT NOT BE AVAILABLE LATER. The file is required for authentication for the Django app.

20 - Install boto3 with the following command:
pip3 install boto3

21 - Install django-storages with the following command:
pip3 install django-storages

22 - Again, freeze the environment requirements:
pip3 freeze > requirements.txt

23 - Add storages in INSTALLED APPS of settings.py:
'storages',

24 - Check that the variables of "if 'USE_AWS' in os.environ:" in settings.py correspond to your app name and AWS settings. Please note that you need to have defined the following variables in Config Vars of Heroku (in "Settings"):
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
USE_AWS

IMPORTANT: At this point, DISABLE_COLLECSTATICS of point 15 can be deleted if you opted for enabling it), so Django loads the static files from Amazon Web Services

25 - Check that your "custom_storages.py" file is properly defined according to your app and AWS account.

26 - In the app bucket of your Amazon Web Services account create a folder named "media" (in the same level that the "static" folder is located)

27 - Check that superuser e-mail in Django admin user interface is verified.

28 - Add API keys (STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY) from Stripe to Config Vars in Heroku. Then, in your Stripe account (in "Developers" section, "Webhooks"), "Add endpoint" (https://pp5-ci-gdec.herokuapp.com/checkout/wh), selecting and adding all events. Finally, copy the signing secret of the webhook and asign it to a STRIPE_WH_SECRET in the Config Vars of Heroku.
Ensure the variables match the names in the settings.py file.

29 - Add automatic e-mail variables in Config Vars of Heroku (to send automatic e-mails from the app), EMAIL_HOST_PASS (password given by your e-mail service provider) and EMAIL_HOST_USER (the e-mail address from where e-mails are sent).

Replace EMAIL_HOST in settings.py if you are using a different service provider than GMail.

#### Additional notes:

Please note that these are the steps according to the user interface as of April 4th, 2022. There might be changes after a while.

Remember you can commit and push your changes to both GitHub and/or Heroku
for GitHub:
git add .
git commit -m "Your update commit message"
git push

for Heroku:
If initialization is needed:
git init
heroku git:remote -a your_app_name

Then:
git add .
git commit -m "Your update commit message"
git push heroku main

You can also set automatic deployments by going to Heroku website, "Deploy" section of your_app_name, and connecting to GitHub (after serching for your_app_name in the corresponding "Connect to GitHub" section and finally clicking on the "Enable Automatic Deploys" button at the bottom).

In settings.py file, you can set the DEBUG variables as follows if you want to control the debug mode from Heroku Config Vars:
'DEVELOPMENT' in os.environ


<details>
    <summary>GitHub Pages Screenshot</summary>

![Deployment on Heroku Image](docs/features-and-evidence/heroku-deployment.PNG) 
</details>


<br><br>
## [Back to Index](#index)
<br><br>

___
# 14 . Credits

- Code Institute:

    - I have used the learning material in the course as a guide and reference.

    - "Boutique Ado" project: reference for building this PP5_CI_GDEC website/project, and provision of code as commented out in the code.
        - ...

    - ...Tutor Assistance: Django models in app_weather could not be migrated as ...

    - Tutor Assistance: ...

    - Tutor Assistance: ..s.

    - Not to include "bag_tools" (Python function based on a Django template) as app; Igor from Code Insitute, on Slack, checked on March 16th, 2022, at 2:28-->


- Balsamiq Wireframes: I have used it to create all the wireframes.

- Jesse James Garrett's process for user experience.

- Bootstrap:

    - To find and check components : https://getbootstrap.com/docs/4.0/getting-started/introduction/.

    - Starter template: https://getbootstrap.com/docs/4.4/getting-started/introduction/, copied on March 1st, 2020, at 00:10.

    - Bootstrap v4.6 Toasts, https://getbootstrap.com/docs/4.6/components/toasts/; copied on March 16th, 2022, at 15:00.

    - Bootstrap Carousel, https://getbootstrap.com/docs/4.0/components/carousel/, copied and modified on March 25th, 2022, at 00:30.

- Coverage.py:

    To show the coverage of the Django test files; https://coverage.readthedocs.io/en/6.3.2/.

- Django-allauth: version 0.41.0, https://django-allauth.readthedocs.io/, installed on February 25th, 2022.

- Django Documentation:

    - Several consultations to check and remember methods, configuration, elements and syntaxis.

    - To limit field content to specific values, https://docs.djangoproject.com/en/4.0/ref/models/fields/, accessed on April 12th, 2022.

    - Pagination by Django Documentaiton: https://docs.djangoproject.com/en/4.0/topics/pagination/, accessed on April 15th, 2022, at 2:00.

    - To show coverage of test files: https://docs.djangoproject.com/en/4.0/topics/testing/advanced/.

- Djangocentral:

    - To add a comment feature: copied and modified (except computation of product rating) from https://djangocentral.com/creating-comments-system-with-django/, Abhijeet Pal, Author and Editor in Chief @djangocentral, on April 12th, 2022.  

- ERD:
    - ERDPlus, to make the data model graph, https://erdplus.com/standalone 

- ESRI:
    - ...



- Font Awesome:

    - Font Awesome Script / Kit, link copied on March 1st, 2022, 03:29 from Font Awesome personal account.

    - Icon for My Account: link copied on March 1st, 2022, 03:32 from https://fontawesome.com/v4/icon/user.

    - Icon for shopping cart: link copied on March 1st, 2022, 03:35 from https://fontawesome.com/v4/icon/shopping-cart.

    - Icon for GDEC logo: link copied on March 1st, 2022, 04:00 from https://fontawesome.com/v4/icon/paw.

    - Icon for Facebook: link copied on March 1st, 2022, 17:23 from https://fontawesome.com/v4/icon/facebook-square.

    - Icon for LinkedIn: link copied on March 1st, 2022, 17:27 from https://fontawesome.com/v4/icon/linkedin-square.

    - Icon for Twitter: link copied on March 1st, 2022, 17:28 from https://fontawesome.com/v4/icon/twitter-square.

    - Icon for Instagram: link copied on March 1st, 2022, 17:28 from https://fontawesome.com/v4/icon/instagram.

    - Icon for the envelope (for sending e-mails): link copied on March 1st, 2022, 17:29 from https://fontawesome.com/v4/icon/envelope.



- Google:

    - Google Fonts: Play (Regular 400 and Bold 700) and Roboto (Regular 400), import code copied on March 1st, 2022, at 05:05.

    - ...

- Heroku:

    - ...

- jQuery:

    - jQuery Core 3.6.0, minified version, https://releases.jquery.com/, copied on March 1st, 2020, at 00:20.

- Mailchimp:

    - Sign-up of newsletter, generated and copied on April 6th, 2022, at 3:10, in Mailchip account (Mailchimp: Marketing Automation & Email Platform, https://mailchimp.com); later modified

- MDN Web Docs Moz://a;
    - ...

- Natural Earth:

    -  All images of maps have been generated with data of Natural Earth, using the "Natural Earth quick start kit" (50m raster), which was downloaded from https://www.naturalearthdata.com/downloads/ on February 23rd, 2022, at 22:22.

- Pexels:

    - Images of products that are not maps were downloaded from Pexels: https://www.pexels.com/ . The following are the file details and credits (author, link to image, file name, date it was downloaded):

    Paul IJsendoorn-
    https://www.pexels.com/es-es/foto/canon-del-antilope-33041/
    pexels-paul-ijsendoorn-33041.jpg
    2022-03-12 at 19:00

    Tomáš Malík
    https://www.pexels.com/es-es/foto/foto-de-primer-plano-del-glaciar-svinafellsjokull-3591596/
    pexels-tomáš-malík-3591596
    Renamed as pexels-tomas-malik-3591596
    2022-03-12 at 19:08

    Martins Krastins
    https://www.pexels.com/es-es/foto/muro-de-piedra-agrietada-838981/
    pexels-martins-krastins-838981
    2022-03-12 at 19:11

    Curioso Photography
    https://www.pexels.com/es-es/foto/vista-aerea-del-cuerpo-de-agua-288100/
    pexels-curioso-photography-288100
    2022-03-12 at 19:14

    Pixabay
    https://www.pexels.com/es-es/foto/planeta-tierra-220201/
    pexels-pixabay-220201
    2022-03-12 at 19:19

    Tom D'Arby
    https://www.pexels.com/es-es/foto/paisaje-desierto-seco-suelo-5949017/
    pexels-tom-d'arby-5949017
    Renamed as pexels-tom-d-arby-5949017
    2022-03-13 at 14:26

    Pok Rie
    https://www.pexels.com/es-es/foto/fotografia-aerea-de-la-isla-1726310/
    pexels-pok-rie-1726310
    2022-03-13 at 14:28

    Pok Rie
    https://www.pexels.com/es-es/foto/mar-gente-mujer-arte-11192678/
    pexels-pok-rie-11192678
    2022-03-13 at 14:31

    NastyaSensei
    https://www.pexels.com/es-es/foto/vista-superior-de-un-rio-2782115/
    pexels-nastyasensei-2782115
    2022-03-13 at 14:34

    Dids
    https://www.pexels.com/es-es/foto/resfriado-naturaleza-seco-modelo-4949961/
    pexels-dids-4949961
    2022-03-13 at 14:43

    Rachel Claire
    https://www.pexels.com/es-es/foto/naturaleza-textura-montana-acantilado-4993089/
    pexels-rachel-claire-4993089
    2022-03-13 at 14:46

    MART PRODUCTION
    https://www.pexels.com/es-es/foto/arena-desierto-seco-duna-8869235/
    pexels-mart-production-8869235
    2022-03-13 at 15:17

    Mengliu Di
    https://www.pexels.com/es-es/foto/vista-aerea-del-paisaje-3064079/
    pexels-mengliu-di-3064079
    2022-03-13 at 15:40

    Johannes Havn
    https://www.pexels.com/es-es/foto/foto-de-la-plataforma-petrolera-1716008/
    pexels-johannes-havn-1716008
    2022-03-13 at 15:47

    Jan Zakelj
    https://www.pexels.com/es-es/foto/amanecer-cielo-puesta-de-sol-noche-9291512/
    pexels-jan-zakelj-9291512
    2022-03-13 at 18:20

    Aron Razif
    https://www.pexels.com/es-es/foto/mar-agua-puerto-industria-9336586/
    pexels-aron-razif-9336586
    2022-03-13 at 18:33

    Simon Berger
    https://www.pexels.com/es-es/foto/un-glaciar-azul-bajo-el-sol-3660696/
    pexels-simon-berger-3660696
    2022-03-13 at 18:37 

    Mikhail Nilov
    https://www.pexels.com/es-es/foto/mar-paisaje-naturaleza-oceano-8332570/
    pexels-mikhail-nilov-8332570
    2022-03-13 at 18:40

    Markus Spiske
    https://www.pexels.com/es-es/foto/codigos-en-la-lente-de-cambio-de-inclinacion-2004161/
    pexels-markus-spiske-2004161
    2022-03-13 at 18:45

    Torsten Dettlaff
    https://www.pexels.com/es-es/foto/dispositivo-digital-en-blanco-y-negro-que-muestra-el-grafico-70911/
    pexels-torsten-dettlaff-70911
    2022-03-13 at 18:48

    Monstera
    Pexels.com
    https://www.pexels.com/es-es/foto/ligero-creativo-de-viaje-direccion-7412095/
    pexels-monstera-7412095
    2022-03-13 at 18:53

    Burak Kebapci
    https://www.pexels.com/es-es/foto/visualizacion-de-graficos-en-un-i-pad-187041/
    pexels-burak-kebapci-187041
    2022-03-13 at 18:58

    Alesia Kozik
    https://www.pexels.com/es-es/foto/manos-telefono-inteligente-ordenador-portatil-graficas-6772076/
    pexels-alesia-kozik-6772076
    2022-03-13 at 19:28

    Pok Rie
    Pexels.com
    https://www.pexels.com/es-es/foto/vista-de-pajaro-de-la-orilla-del-mar-1426827/
    pexels-pok-rie-1426827
    2022-03-14  at 12:44

    Pok Rie
    https://www.pexels.com/es-es/foto/mar-naturaleza-playa-vacaciones-10981948/
    pexels-pok-rie-10981948
    2022-03-14 at 12:47

    Jake Ganse
    https://www.pexels.com/es-es/foto/mar-agua-oceano-olas-9181889/
    pexels-jake-ganse-9181889
    2022-03-14 at 13:07

    Ian Beckley
    https://www.pexels.com/es-es/foto/foto-escenica-del-gran-canon-durante-el-dia-2757641/
    pexels-ian-beckley-2757641
    2022-03-14 at 13:10

    Ian Beckley
    https://www.pexels.com/es-es/foto/arte-creativo-sucio-industria-2588870/
    pexels-ian-beckley-2588870
    2022-03-14 at 13:14

    Mikhail Nilov
    https://www.pexels.com/es-es/foto/resfriado-nieve-paisaje-montanas-7456226/
    pexels-mikhail-nilov-7456226
    2022-03-15 at 13:29

    Hugo Heimendinger
    https://www.pexels.com/es-es/foto/arena-marron-y-cuerpo-de-agua-4026047/
    pexels-hugo-heimendinger-4026047
    2022-03-15 at 13:34

    Martin Sanchez
    https://www.pexels.com/es-es/foto/resfriado-iceberg-naturaleza-sucio-4325680/
    pexels-martin-sanchez-4325680
    2022-03-15 at 13:37

    Kristina Gain
    https://www.pexels.com/es-es/foto/resfriado-glaciar-iceberg-derritiendo-4042406/
    pexels-kristina-gain-4042406
    2022-03-15 at 13:40

    Curioso Photography
    https://www.pexels.com/es-es/foto/arboles-y-suelo-durante-el-dia-288093/
    pexels-curioso-photography-288093
    2022-03-15 at 13:46

    Curioso Photography
    https://www.pexels.com/es-es/foto/cuadro-abstracto-amarillo-y-azul-3719622/
    pexels-curioso-photography-3719622
    2022-03-15 at 13:49

    Leon Macapagal
    https://www.pexels.com/es-es/foto/modelo-textura-rock-ciencia-6622887/
    pexels-leon-macapagal-6622887
    2022-03-15 at 13:51

    Alex Qian
    Pexels.com
    https://www.pexels.com/es-es/foto/fotografia-de-drones-de-la-gran-muralla-china-2304791/
    pexels-alex-qian-2304791
    2022-03-15 at 13:55

    ArtHouse Studio
    https://www.pexels.com/es-es/foto/resfriado-nieve-ligero-paisaje-4641210/
    pexels-arthouse-studio-4641210
    2022-03-15 at 13:59


- Python unittest:

    - As reference for testing in Python: https://docs.python.org/3/library/unittest.html .

- QGIS:

    - QGIS 3.18, to create the fictitious maps for data, created on February 24th, 2022.



- Stack Overflow:

    - Read file path with Python: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory, accessed on March 1st, 2022, at 23_35.

    - Read file name with Python: https://stackoverflow.com/questions/7336096/python-glob-without-the-whole-path-only-the-filename, accessed on March 1st, 2022, at 23_45.

    - Open and write files in Python: https://stackoverflow.com/questions/29223246/how-do-i-save-data-in-a-text-file-python, accessed on March 2nd, 2022, at 00:57.

    - Write several variables to file: https://stackoverflow.com/questions/16822016/write-multiple-variables-to-a-file, accessed on March 2nd, 2022, at 01:03.

    - Import Lower function; https://stackoverflow.com/questions/31734993/lowercase-django-query, accessed on March 15th, 2022, at 11:55.

    - Equivalent of marquee tag for HTML5, https://stackoverflow.com/questions/53632338/what-is-the-equivalent-of-marquee-tag-in-html5; accessed on March 16th, 2022, at 3:20.

    - Inclusion of Google fonts in Stripe elements based on https://stackoverflow.com/questions/44915511/stripe-elements-google-web-font-not-working, accessed on March 18th, 2022, at 6:20.

    - Capitalize first letter of each word: https://stackoverflow.com/questions/1549641/how-can-i-capitalize-the-first-letter-of-each-word-in-a-string, accessed on April 14th, 2022, at 01:54

    - To capitalize first letter in Django template: https://stackoverflow.com/questions/14268342/make-the-first-letter-uppercase-inside-a-django-template,
    accessed on April 18th, at 15:35.

    - To replace correct URL for filtered Django queries, for first/previous/next/last pages, accessed on April 22nd, 2022, at 02:00, at https://stackoverflow.com/questions/68820700/paginate-a-filter.

- Simpleisbetterthancomplex: https://simpleisbetterthancomplex.com/

    - By Vitor Freitas, missing line for proper pagination, "paginator.page(page)", and option to address no integers, https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html, accessed on April 15th, 2022, at 2:00.

- Stripe:

    - Core logic/payment flow: https://stripe.com/docs/payments/accept-a-payment.

    - CSS styles: https://stripe.com/docs/stripe-js; https://stripe.com/docs/payments/elements.

    - To render last items in a "for" loop in Django templates: https://stackoverflow.com/questions/68494568/how-to-display-latest-5-orders-by-using-for-loop-in-jinja-django; https://stackoverflow.com/questions/36977773/how-to-reverse-a-for-loop-in-a-django-template-and-then-slice-the-result; https://stackoverflow.com/questions/36977773/how-to-reverse-a-for-loop-in-a-django-template-and-then-slice-the-result; accessed on March 29th, 2022, at 14:30.

    - To check if a form is submitted with jQuery: https://stackoverflow.com/questions/14969467/how-to-check-with-jquery-if-any-form-is-submitted, accessed on April 9th, 2022, at 15:30.

- StudyGyaan:

    - Definition based on this article: https://studygyaan.com/django/how-to-use-bootstrap-4-forms-with-django-crispy-forms#html-code, accessed on April 16th, 2022.
    

- W3C®. Copyright © 2021 W3C ® (MIT, ERCIM, Keio, Beihang):
    - ...

- W3Schools (Powered by W3.CSS), https://www.w3schools.com/:

    - Generate random numbers (float format), https://www.w3schools.com/python/ref_random_uniform.asp, accessed on March 2nd, 2022, at 01:42.

    - Check object-fit property for CSS: https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width, accessed on March 3rd, 2022, at 04:25.
    
    - Check object-fit property for CSS: https://www.w3schools.com/css/css3_object-fit.asp, accessed on March 3rd, 2022, at 04:27.

    - Use of marquee tag, https://www.w3schools.in/html-tutorial/marquee-tag/, accessed on March 16th, 2022, at 2:45.

    



<br><br>
## [Back to Index](#index)
<br><br>

___
# 15 . Acknowledgements

I would like to acknowledge and thank the following people for being part of this project and for helping me in the development of it:
- To my wife and family, for always supporting and helping.
- Code Institute, for providing knowledge, guide, content and tools.
- My mentor, Mo, for helping with very valuable guide and support.
- Code Institute Tutor Assistance for helping when needed.
- Code Institute community in Slack for permanently being an online reference.
- All the valuable information provided by the sources mentioned above in the credits.

<br><br>
## [Back to Index](#index)
<br><br>


