# **Sorry, site under consturction**
<br><br>
#### **This project is about an e-commerce for geophysical data. It is a FICTITIOUS SITE where the user will be able to shop geophysical data that comprises digital elevation models, and gravimetry, resistivity and magnetometry data. Data are FICTITIOUS.**
<br><br>

# **Index**
#### [*Site Live Link*](https://pp4-ci-wqcs.herokuapp.com/) (https://pp4-ci-wqcs.herokuapp.com/)


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
# **1 . Project Goals**
The goal of the project is to create an e-commerce for geophysical data.

...

<br><br>
## [Back to Index](#index)
<br><br>


___
# **2 . Considerations**

If opening the project with Gitpod from GitHub (top right green button), please run the following command as new workspaces need to have their dependencies:
pip3 install -r requirements.txt

Please keep in mind that the interaction with the database and corresponding display of data is slow, it might take several seconds until the data is display on tables and/or Google Charts.

<br><br>
## [Back to Index](#index)
<br><br>



___
# **3 . Project Board**

A project board was created in GitHub to help on the planning of the work when building the site; it can be observed [here](https://github.com/csc7/PP4_CI_WQCS/projects/1) (https://github.com/csc7/PP4_CI_WQCS/projects/1).

In addition, issues can directly be found [here](https://github.com/csc7/PP4_CI_WQCS/issues) (https://github.com/csc7/PP4_CI_WQCS/issues)

<br><br>
## [Back to Index](#index)
<br><br>

___
# **4 . User Experience**

UX has been addressed around Jesse James Garrett's process, whose five planes involves the following matters:
- **STRATEGY**: to build a website (product) that helps on the planning and activities of a seismic/geophysical data acquisition crew.
- **SCOPE**: the minimum viable product needs to include features that allow the user to know the following:
    - Instruction page to let the user how to use the site.
    - Weather page where the user can gather and analyse weather data from any point in the world that is picked on a map.
    - Blog page where the user can use to post issues, comment, send consultations and find solutions.
    - Contact page where the user can send feedback or report site issues.
- **STRUCTURE**: the information is structured as follows:
    - Instructions page (index.html).
    - Weather page with a map on top left, selection of point top right, current data below this selection panel, and visualization of data on the bottom of this page.
    - Blog page where topics are shown on the body.
    - Topic pages, corresponding to the topics mentioned above, to read and post comments.
    - Contact form page.
    - Fixed navigation bar on top.
    - Footer.
    - Sign-in page.
    - Sign-up page.
    - Sign-out page.
    - 404 page to let the user know of any error while loading the site.
- **SKELETON**: the information is accessed through a fixed navigation menu on top of the pages.
- **SURFACE**: the website is based on a contrast between white and RGB(49, 49, 48), with some titles in RGB(76, 76, 211); some other variations close to these three colours are also present to enhance contrast.

## **User Goals**
- To find an interactive website.
- To navigate through a responsive website.
- ...
- To be able to contact the site administrator, owner and/or developer if desired.

#### [Back to Index](#index)

## **Site Owner Goals**
- To provide an interactive website.
- To provide a responsive website.
- ...
- To give users the chance to contact the site administrator, owner and/or developer.

## **Developer Goals**
- To provide a basic and scalable e-commerce website to show my capabilities.

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
7. As a returning user, I want a navigation menu on top, always visible, so I can access any content on the website from there and do not need to use the back button of the browser.
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

- ### **Site Owner**
22. As owner, I want to provide an introductory page, so users know what can be found in the website and what can be purchased.
23. As owner, I want to provide an easy process for registration, so I ensure a connection with a potential buyer.
24. As owner, I want to provide a search field for products on top, so I require users/shoppers the minimum possible time to find a product (and therefore reduce the risk of leaving).
25. As owner, I want to organize products in categories, so users find an organized site and can find products easily.
26. As owner, I want to receive feedback from users, so I can take actions in response to them if needed.
27. As owner, I want to provide a navigation menu on top and always visible, so users can access any content at any time without needing the back button.
28. As owner, I want to give as many options to be contacted as possible, so users can choose forms or links in the footer to send their consultations and/or feedback in a very fast way.
29. As owner, I want to provide a responsive website, so user can access it from any device without any constraint to navigate, find and/or use the website.
30. As owner, I want to inform users if their consultation/message was successfully sent, so they know if they need to resend it or they do not.
31. As owner, I want to inform the user, through an error page, if there is any error when loading the website.

- ### **Developer**
32. As developer, along with other points of this section, I want to show my work and give the option to users to contact me if they wish.


#### [Back to Index](#index)

## **User Requirements and Expectations**
- A fixed and responsive navigation menu on top.
- ...
- A dedicated page for the contact form.
- A footer with contact links to the developer.
- Use of Django templates/pages for sign-up, sign-in, sign-out.

<br><br>
## [Back to Index](#index)
<br><br>


___
# **5 . Data Model**

The project is based in data provided by OpenWeather (https://openweathermap.org/) and Django models for the support (blog) page. Design and structure of Post and Comment tables are copied from the Code Institute "I Think Therefore I Blog" project. The following chart shows the data involved and how they are related:

![Data Model Image](static/images/data-model.PNG)

The following are the tables involved in the relational model, along with data types and measurement units.

Find OpenWeather API information [here](https://openweathermap.org/current) (https://openweathermap.org/current).

Since the planning should be based on date and time, **all entries and tables are related to the Weather Data and Time table**, whose primary key (ID) relates the data to the specific date and time.


- #### **WEATHER DATA AND TIME**

    - **ID:** integer, primary key    
    - **Date:** date    
    - **Time:** custom field (time)

- #### **WEATHER WIND DATA**

    - **ID:** integer
    - **Wind Speed:** float, meter/second
    - **Wind Direction:** float, degrees
    - **Rec ID:** integer, foreign key

- #### **WEATHER TEMPERATURE DATA**

    - **ID:** integer
    - **Temperature:** float, Kelvin, converted to Celsius
    - **Feels Like:** float, Kelvin, converted to Celsius
    - **Minimum Temperature:** float, Kelvin, converted to Celsius
    - **Maximum Temperature:** float, Kelvin, converted to Celsius
    - **Rec ID:** integer, foreign key

- #### **WEATHER OTHER DATA**

    - **ID:** integer
    - **Pressure:** float, hPa (atmospheric pressure)
    - **Humidity:** float, percentage
    - **Visibility:** float, meters
    - **Sky:** float, cloudiness, percentage
    - **Main:** text, weather parameters (rain, snow, etc.)
    - **Description:** text, weather condition
    - **Sunrise:** custom (time), sunrise time, UNIX, UTC
    - **Sunset:** custom (time), sunset time, UNIX, UTC
    - **Rec ID:** integer, foreign key

- #### **POST**

    - **ID:** integer, primary key
    - **Title:** text
    - **Slug:** text
    - **Author:** text
    - **Feature Image:** image
    - **Excerpt:** text
    - **Updated:** date
    - **Content:** text
    - **Created:** date
    - **Status:** integer
    - **Like:** boolean

- #### **COMMENT**

    - **ID:** integer, primary key
    - **Name:** text
    - **E-mail:** text
    - **Body:** text
    - **Created:** date
    - **Approved:** boolean
    - **Post:** integer, foreign key

- #### **CONTACT FORM**

    - **ID:** integer, primary key
    - **Date:** date
    - **Time:** custom (time)
    - **Name:** text
    - **Surname:** text
    - **E-mail:** text
    - **Description:** text

<br><br>
## [Back to Index](#index)
<br><br>

___
# **6 . Design Choices**

The design was planned to cover screen sizes from 320x568px to 1920x1370px.

## **Colours**
White and RGB(49, 49, 48), with some titles in RGB(76, 76, 211). Other variations close to these three colours are also present to enhance contrast. The background of the body was set to RGB(236, 238, 238) in order to have a good contrast as well.

#### [Back to Index](#index)
<br>

## **Fonts**
Google fonts (please see credits section below) were implemented on the website. Heebo (Medium 500) for titles and Oxygen (Regular 400) for paragraphs.
Sans-serif font is used as a back-up in case the previous font cannot be loaded.

#### [Back to Index](#index)
<br>

## **Structure**
The metadata includes the following keywords to help search engines to find the website: Seismic, geophysical, acquisition, processing, crew, field, weather, technical support, database, wind, temperature, Code Institute, software development, student, full-stack course, milestone project.

The website consists of four pages (with subpages for the blog topics), organised in a header, a body and a footer. Django templates/pages have been used for sign-up, sign-in, sign-out and 404.

Wireframes were developed at the beginning in order to have a first design of the website.

- ### **Header**

In order to achieve the goals related to easiness and/or simplicity, a fixed navigation area in the header is provided. In the same area, a logo with the idea of the website is place to the left.
The header contains the logo on the left, the navigation bar with the four links to the body pages in the middle and the sign-up, sign-in and sign-out buttons on the right.

- ### **Body**

The body of the pages are structured as follows for each of the pages:
- #### *Instructions:*
    It contains a description of the main purpose of the website and three sections with instructions for each of the other pages: Weather, Blog and Contact.
- #### *Weather:*
    It has a map on top left, selection of point on top right, current data below this selection panel, and a visualization panel of the data on the bottom of this page, below a row panel to select the amount of days to visualise and other data to show.

- #### *Blog:*
    It contains boxes with each topic of the blog to access.
- #### *Contact:*
    It has a simple contact form with name, surname, e-mail and description fields.
<br>
    
- ### **Footer**

The footer contains links for social media (LinkedIn and GitHub) and e-mail. It is designed to remain at the bottom of the pages to have the links visible to promote the developer of the website.\
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

The following languages, software and tools were implemented using Windows 10 Pro:
## **Languages**
- #### **HTML**
- #### **CSS**
- #### **JavaScript**
- #### **Python**

#### [Back to Index](#index)

## **Software, Frameworks, Applications and Other Tools**
- #### **GitHub**
- #### **Gitpod**
- #### **QGIS 3.18**
- #### **Django 3.2**
- #### **jQuery**
- #### **django-allauth 0.41.0**
- #### **PostgreSQL**
- #### **Font Awesome (v5.15)**
- #### **Bootstrap (v4.0)**
- #### **unittest**
- #### **Balsamiq Wireframes (v4.2.4, Editor Version 2.6.0)**
- #### **ERDPlus, to make the data model graph**
- #### **Google Fonts**
- #### **W3C Markup Validation Service**
- #### **W3C CSS Validation Service**
- #### **JSHint (version 2.13.0)**
- #### **JavaScript AJAX**
- #### **WAVE Web Accessibility Evaluation Tool**
- #### **Google Lighthouse (used in Google, Microsoft Edge and Firefox)**
- #### **Google Chrome, version 97.0.4692.71, Official Build, 64-bit (and its development tool)**
- #### **Microsoft Edge, version 97.0.1072.62, Official build, 64-bit (and its development tool)**
- #### **Firefox, 96.0.3, 64-bit (and its development tool)**
- #### **Microsoft Internet Explorer, version 2004, OS Build 19041.1415, Microsoft Corporation**


<br><br>
## [Back to Index](#index)
<br><br>



___
# **9 . Features**

The site consists of four pages, where each of them is divided in three parts: header, body and footer. The features contained in each of the pages and parts are the following ones:


- ### **Fixed navigation menu**

It is in the header, fixed on all pages to facilitate navigation, and responsive.

*User Stories Addressed by this Feature: 19; 21; 29; 33 and 34.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Check Image</summary>

![Fixed Navigation Menu for Desktop Image](docs/features-and-evidence/fixed-navigation-menu.PNG)
![Fixed Navigation Menu for Tablets Image](docs/features-and-evidence/fixed-navigation-menu-tablet.PNG)
![Fixed Navigation Menu for Cell Phones Image](docs/features-and-evidence/fixed-navigation-menu-cell-1.PNG)
![Fixed Expanded Navigation Menu for Cell Phones Image](docs/features-and-evidence/fixed-navigation-menu-cell-2.PNG)
</details>
<br>

- ### **Instructions App**

They can be found in the Instructions page (home), they explain how to use the weather and blog pages.

*User Stories Addressed by this Feature: 1; 25; 33 and 34.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Check Images</summary>

![Instructions Page Top Image](docs/features-and-evidence/instructions-page-top.PNG)

![Instructions Page Bottom Image](docs/features-and-evidence/instructions-page-bottom.PNG)

</details>
<br>


- ### **Weather App**

It can be found in the Weather page and allows users to collect and analyse weather information.


*User Stories Addressed by this Feature: 2; 3; 4; 5; 6; 7; 26; 33 and 34.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Check Image</summary>

![Weather App Image](docs/features-and-evidence/weather-page.PNG)

</details>
<br>

- ### **Blog App**

It can be found in the Blog page and allows users to send and consult issues they find in their daily activities and find solutions for them.

*User Stories Addressed by this Feature: 8; 9; 10; 11; 12; 13; 14; 15; 16; 17; 27; 33 and 34.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Check Image</summary>

![Blog App Image](docs/features-and-evidence/blog-page.PNG)

</details>
<br>


- ### **Contact App**

It can be found in the Contact and allows users to contact the website developer. It prevents the form to be sent with incomplete fields, informs the user if the message goes through and disables the send button in order not to send the consultation more than once.

*User Stories Addressed by this Feature: 18; 20; 28; 30; 33 and 34.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Check Image</summary>

![Contact App Image](docs/features-and-evidence/contact-page.PNG)

</details>
<br>



- ### **Footer**

It is located at the bottom of all pages, containing icons with links to LinkedIn, GitHub and e-mail application (to automatically load developer's e-mail address in the addressee field).

*User Stories Addressed by this Feature: 18; 20; 23; 28; 30; 33 and 34.*

*Please check "11. Testing of User Stories" for more details.*
<details>
    <summary>Check Image</summary>

![Footer Image](docs/features-and-evidence/footer.PNG)

</details>
<br>


- ### **Registration**

They are Django complementary tools and pages to have registration options in the site for users. There are sign-in, sign-up and sign-out pages that work as interfaces for this purpose. 

*User Stories Addressed by this Feature: 19; 24; 31; 33; 34; and 35.*

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

___
# **10 . Validation**

**Development tools** of **Google Chrome** (Version 97.0.4692.71, Official Build, 64-bit), **Microsoft Edge** (Version 97.0.1072.62, Official build, 64-bit) and **Firefox** (Version 96.0.3, 64-bit) have been used to test the behaviour of the website for screen sizes between 320x568px to 1920x1370px.

The website was tested using these **browsers** and also **Microsoft Internet Explorer** (Version 2004, OS Build 19041.1415, Microsoft Corporation). **Samsung Internet** (version 15.0.2.47) was also used to test the website. In addition, some users have collaborated checking the website in the cell phones, mostly with **Android-based operating systems**.

**Devices** used for testing and validation include Dell and Samsung cell phones. **Operative systems** include Windows 10 Enterprise (remote desktop), Windows 10 Pro and Android. **Processors** for desktop and laptops were Intel.

The following tools were used to validate the **files of the website**:

<br>

### **HTML Files**
https://validator.w3.org/ was used to validate the new HTML files (those not being part of the Django framework). To test them, unique HTML files base+index, base+weather, base+blog and base+contact were created. The files were validated and accepted only when errors were related to control characters.

Errors corrected using this service:

- **base.html**:
    - Id body for body tag changed as it needs to have a different name; corrected after using the validator.

<br>

- **Instructions Page (index.html)**:
    - All images were missing the "alt" attribute; they were added after using the validator.

<br>

- **Weather Page**:
    - Duplicated id ("s-d-o-4") identified, one of the changed to "s-d-o-5" after using the validator.
    - Table headers "th" were not included in a "tr" tag; included after using the validator.

<br>

- **Blog Page**:
    - Image was missing the "alt" attribute; added after using the validator.

<br>

- **Contact Page**:
    - No errors found.


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
    <summary>CSS File</summary>

![Evidence of no errors in the CSS file](docs/validation/validation-css-1.PNG) 
</details>
<details>
    <summary>CSS File (Warnings)</summary>

![Evidence of no errors in the CSS file](docs/validation/validation-css-2.PNG) 
</details>

#### [Back to Index](#index)

<br><br>

### **JavaScript Files**
https://jshint.com/ was used to validate the JavaScript files.
Please check the parameters used for validation and evidence below:

<details>
    <summary>Parameters used for JavaScript validation in JSHint version 2.13.3</summary>

![Parameters used for JavaScript validation in JSHint version 2.13](docs/validation/validation-js-move-configuration.PNG) 
</details>

<details>
    <summary>Weather Page (weather.js JavaScript file). Please note that google is an external variable from Google</summary>

![Evidence of no errors weather.js JavaScript file](docs/validation/validation-js-weather.PNG)
</details>

<details>
    <summary>File for moving the content down (move-content-hamburger.js)</summary>

![Evidence of no errors and warnings in the move-content-hamburger.js JavaScript file](docs/validation/validation-js-move-content.PNG) 
</details>

<details>
    <summary>File for checking the loading of the site (index.js JavaScript file)</summary>

![Evidence of no errors and warnings in the index.js JavaScript file](docs/validation/validation-js-index.PNG)
</details>


#### [Back to Index](#index)

<br>


### **Python Files**

PEP8 was used to check the files written in Python, with "All right" results.

The tool can be accessed with this link: http://pep8online.com .


- **Django Project Files**
<details>
    <summary>asgi.py</summary>

![Evidence of file asgi.py validated with http://pep8online.com/ ](docs/validation/validation-python-django-asgi.PNG) 
</details>
<details>
    <summary>settings.py</summary>

![Evidence of file settings.py validated with http://pep8online.com/ ](docs/validation/validation-python-django-settings.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-django-urls.PNG) 
</details>
<details>
    <summary>wsgi.py</summary>

![Evidence of file wsgi.py validated with http://pep8online.com/ ](docs/validation/validation-python-django-wsgi.PNG) 
</details>
<br>

- **Instructions App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-instructions-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-instructions-apps.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-instructions-models.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-instructions-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-instructions-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-instructions-views.PNG) 
</details>
<br>

- **Weather App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-weather-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-weather-apps.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-weather-models.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-weather-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-weather-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-weather-views.PNG) 
</details>
<br>

- **Blog App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-blog-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-blog-apps.PNG) 
</details>
<details>
    <summary>forms.py</summary>

![Evidence of file forms.py validated with http://pep8online.com/ ](docs/validation/validation-python-blog-forms.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-blog-models.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-blog-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-blog-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-blog-views.PNG) 
</details>
<br>

- **Contact App**
<details>
    <summary>admin.py</summary>

![Evidence of file admin.py validated with http://pep8online.com/ ](docs/validation/validation-python-contact-admin.PNG) 
</details>
<details>
    <summary>apps.py</summary>

![Evidence of file apps.py validated with http://pep8online.com/ ](docs/validation/validation-python-contact-apps.PNG) 
</details>
<details>
    <summary>forms.py</summary>

![Evidence of file forms.py validated with http://pep8online.com/ ](docs/validation/validation-python-contact-forms.PNG) 
</details>
<details>
    <summary>models.py</summary>

![Evidence of file models.py validated with http://pep8online.com/ ](docs/validation/validation-python-contact-models.PNG) 
</details>
<details>
    <summary>tests.py</summary>

![Evidence of file tests.py validated with http://pep8online.com/ ](docs/validation/validation-python-contact-tests.PNG) 
</details>
<details>
    <summary>urls.py</summary>

![Evidence of file urls.py validated with http://pep8online.com/ ](docs/validation/validation-python-contact-urls.PNG) 
</details>
<details>
    <summary>views.py</summary>

![Evidence of file views.py validated with http://pep8online.com/ ](docs/validation/validation-python-contact-views.PNG) 
</details>



#### [Back to Index](#index)

<br>


### **Accessibility**
https://wave.webaim.org/ was used to validate accessibility. Although there are warnings, all pages contain zero errors. Please check evidence below:

<details>
    <summary>Instructions Page</summary>

![Evidence of no accessibility errors in the Instructions (index) HTML file](docs/validation/validation-accessibility-instructions.PNG) 
</details>

<details>
    <summary>Weather Page</summary>

![Evidence of no accessibility errors in the Weather HTML file](docs/validation/validation-accessibility-weather.PNG) 
</details>

<details>
    <summary>Blog Page</summary>

![Evidence of no accessibility errors in the Blog HTML file](docs/validation/validation-accessibility-blog.PNG) 
</details>

<details>
    <summary>Contact Page</summary>

![Evidence of no accessibility errors in the Contact HTML file](docs/validation/validation-accessibility-contact.PNG) 
</details>



#### [Back to Index](#index)

<br>


### **Performance**
Google Lighthouse (used in Google, Microsoft Edge and Firefox) were used to evaluate the performance of the pages. Please check the results below:

<details>
    <summary>Instructions Page for Cell Phones(67)</summary>

![Evidence of no accessibility errors in the Instructions (index) HTML file](docs/validation/validation-performance-instructions-cell-phone.PNG) 
</details>

<details>
    <summary>Instructions Page for Desktop (85)</summary>

![Evidence of no accessibility errors in the Instructions (index) HTML file](docs/validation/validation-performance-instructions-desktop.PNG) 
</details>

<details>
    <summary>Weather Page for Cell Phones(50)</summary>

![Evidence of no accessibility errors in the Weather HTML file](docs/validation/validation-performance-weather-cell-phone.PNG)
</details>

<details>
    <summary>Weather Page for Desktop (79)</summary>

![Evidence of no accessibility errors in the Weather HTML file](docs/validation/validation-performance-weather-desktop.PNG)
</details>

<details>
    <summary>Blog Page for Cell Phones(64)</summary>

![Evidence of no accessibility errors in the Blog HTML file](docs/validation/validation-performance-blog-cell-phone.PNG) 
</details>

<details>
    <summary>Blog Page for Desktop (90)</summary>

![Evidence of no accessibility errors in the Blog HTML file](docs/validation/validation-performance-blog-desktop.PNG) 
</details>

<details>
    <summary>Contact Page for Cell Phones(74)</summary>

![Evidence of no accessibility errors in the Contact HTML file](docs/validation/validation-performance-contact-cell-phone.PNG) 
</details>

<details>
    <summary>Contact Page for Desktop (93)</summary>

![Evidence of no accessibility errors in the Contact HTML file](docs/validation/validation-performance-contact-desktop.PNG) 
</details>



<br><br>
## [Back to Index](#index)
<br><br>

___
# **11 . Testing**

## **Testing of Python files with unittest**

The data model and Python files were tested with unittest; it was used to test the assignation of values to the fields of each table of the data model.

31 tests were written and succesfully executed in 0.005 seconds.

<details>
    <summary>Screenshot of unittest result</summary>

![unittest Image 1](docs/features-and-evidence/python-testing.PNG)
![unittest Image 2](docs/features-and-evidence/python-testing-2.PNG)
</details>

<br><br>
## [Back to Index](#index)
<br><br>

## **Testing of User Stories**

## **First time users**

The following are testing of User Stories previously described above:
<br><br>

1. As a user, I want to have a description of the site with instructions, so I know how to use it and refer to them if needed.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Instructions App | Include steps to use the site, separated by sections | Design Instructions App/Page with separated steps and sections | Same as expected result | 

<details>
    <summary>Screenshot</summary>

![Instructions Page Top Image](docs/features-and-evidence/instructions-page-top.PNG)
![Instructions Page Bottom Image](docs/features-and-evidence/instructions-page-bottom.PNG)
</details>
<br><br>

2. As a user, I want to have a weather application so I can find a place on the world and get its current weather information.

| FEATURE | ACTION | EXPECTED RESULT | ACTUAL RESULT |
| --- | --- | --- | --- |
| Weather App | Include Esri/ArcGIS map on the Weather App to select/pick a location | Get coordinates of picked location/place | Works as expected | 

<details>
    <summary>Screenshot</summary>

![Esri/ArcGIS Map to Pick Location](docs/features-and-evidence/Esri-map.PNG) 
</details>
<br><br>

3. ...



## [Back to Index](#index)
<br><br>

___
# 12 . Bugs

Some bugs were related to design, positioning and tags of elements in the page, with variables in Django templates among them. Also, many minor bugs were solved just by assigning the correct property and/or by trial and error.

Bugs that required more time and specific solutions were the following ones:

| Bug | Solution |
| ---- | ---- |
| It was not possible to ... | The issue arises for ...; solved with ... | 
| It was not possible to ... | The issue arises for ...; solved with ... |


<br><br>
## [Back to Index](#index)
<br><br>

___
# 13 . Deployment

The website was fully written in Gitpod, permanently tested with Gitpod preview, and periodically deployed to GigHub Pages (in a main branch) and Heroku.

The fully deployed website, accessible by anyone, is found [here](https://pp4-ci-wqcs.herokuapp.com/), whose URL is https://pp4-ci-wqcs.herokuapp.com/ . Its repository is found [here](https://github.com/csc7/PP4_CI_WQCS), whose URL is https://github.com/csc7/PP4_CI_WQCS.

The site requires access to OpenWeather and Google Chart API, whose configuration have been carried out following the instructions of their developers:

OpenWeather: https://openweathermap.org/current
Google Charts: https://developers.google.com/chart/interactive/docs/gallery/linechart

Follow these steps to deploy in Heroku platform:

1 - Create JSON file (use the command line "npm init" as a wizard, installing the Heroku CLI in Gitpod if necessary and if this environment is being used) to be able to run JavaScript on Heroku. More details in Heroku site, https://devcenter.heroku.com/articles/deploying-nodejs#:~:text=To%20create%20a%20package.,json%20file .

2 - Include dependencies in a requirements.txt file, which is used by Heroku to install the dependencies. Use this command: "pip3 freeze > requirements.txt"

3 - Create new app from the dashboard of your Heroku account.

4 - Go to settings of the apps (do that before deploying the code).

5 - Ignore this step if you do not use credentials to access other services. In Config Vars, create a new one giving the name of CREDS, and assign to content of the JSON file with credentials to its value.

6 - Go to Buildpacks and add Python and Node.js, in that order, keeping Python on top and NodeJS below.

7 - Go to the deploy sections of the app, select GitHub as the Deployment method, assign a name for the repository to connect to GitHub, and connect.

8 - Go to the bottom and select whether you want automatic (rebuilding for each commit) or manual deployment.

You will get a button with a link to your app if successfully deployed.

<details>
    <summary>GitHub Pages Screenshot</summary>

![Deployment on Heroku Image](docs/features-and-evidence/heroku-deployment.PNG) 
</details>

After first deployment, several updates have been carried out before the final version. These updates were implemented in the deployed website from Gitpod, just by using the "push" command for every commit (change) in the ongoing development.

The project repository can be forked from GitHub (https://github.com/csc7/PP4_CI_WQCS), please check for the "Fork" button, top-right of the page, to achieve this task.

<br><br>
## [Back to Index](#index)
<br><br>

___
# 14 . Credits

- Code Institute:

    - I have used the learning material in the course as a guide and reference.

    - "Boutique Ado" project: reference for building this PP5_CI_GDEC website/project.
        - ...

    - ...Tutor Assistance: Django models in app_weather could not be migrated as ...

    - Tutor Assistance: ...

    - Tutor Assistance: ..s.


- Balsamiq Wireframes: I have used it to create all the wireframes.

- Jesse James Garrett's process for user experience.

- Bootstrap:

    - Starter template: https://getbootstrap.com/docs/4.4/getting-started/introduction/, copied on March 1st, 2020, at 00:10.

    - ...

- Django-allauth: version 0.41.0, https://django-allauth.readthedocs.io/, installed on February 25th, 2022.

- Django Documentation:

    - ...


- ERD:
    - ERDPlus, to make the data model graph, https://erdplus.com/standalone 

- ESRI:
    - ...



- Font Awesome:

    - ...


- Google:

    - ...

- Heroku:

    - ...

- jQuery:

    - jQuery Core 3.6.0, minified version, https://releases.jquery.com/, copied on March 1st, 2020, at 00:20.

- MDN Web Docs Moz://a;
    - ...


- Python unittest:

    - As reference for testing in Python: https://docs.python.org/3/library/unittest.html .

QGIS:

    - QGIS 3.18, to create the fictitious maps for data, created on February 24th, 2022.



- Stack Overflow:

    - ...

- W3C®. Copyright © 2021 W3C ® (MIT, ERCIM, Keio, Beihang):
    - ...

- W3Schools (Powered by W3.CSS), https://www.w3schools.com/:

    - ...



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


