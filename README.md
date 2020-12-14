![Beer WareHaus Logo](readme-files/beer-warehaus-readme-logo.png)

# Beer WareHaus

Beer WareHaus is an online shop for a hypothetical beer import and distribution company in Norway. The purpose of the site is to provide a simple intuitive ways for managers of bars and restaurants to browse and purchase products they wish to serve.
Additionally the site provides a number of tools allowing the shop owner to easily manage the products in the shop.

![Beer WareHaus Responsive Screens](readme-files/beer-warehaus-responsive-screens.png)

The site has been deployed to Heroku and can be viewed [here](https://beer-warehaus.herokuapp.com/).

## UX

### Project Goal

This project is my fourth and final Milestone Project in the Code Institute's Fullstack Development program. The purpose of this project was to create an e-commerce site using the Django framework, static file hosting with AWS, and a functional payment system with Stripe. This e-commerce site is fully functional and could be used by a real beer distribution company with minimal setup.

### User Stories

#### User Stories for Customers

| **As a restaurant or bar manager I would like to** | **So that I can**                             |
| -------------------------------------------------- | --------------------------------------------- |
| Browse products                                    | purchase what I need                          |
| Search products                                    | find something specific                       |
| Filter products by style                           | compare the offerings                         |
| Filter products by packaging (can, bottle, keg)    | choose serving style                          |
| See offerings by a specific producer               | get an idea of the producer's offer           |
| Buy a product                                      | serve it to customers                         |
| Pay using a card                                   | complete my purchase                          |
| Create a profile                                   | save my information and review past orders    |
| Update my profile information                      | be contacted by the importer                  |
| See my shopping cart before paying                 | know the cost and content before the purchase |
| Update my shopping cart                            | make decisions before the purchase            |
| See details about a product                        | make an informed purchasing decision          |
| View my order history                              | be reminded of previous purchases             |
| Receive an email confirmation about my order       | have archived information about it            |
| Contact the importer                               | know about the status of an order             |
| Know the newest arrivals                           | buy the freshest products                     |

#### User Stories for Shop Administrators

| **As an administrator I would like to**     | **So that I can**                                |
| ------------------------------------------- | ------------------------------------------------ |
| Add/Update/Remove a product                 | keep the store up to date                        |
| Add/Update/Remove a producer                | keep users informed about the latest information |
| Highlight specific products                 | sell products that need to move                  |
| Receive orders from customers in my mailbox | fulfill the orders                               |
| Mark a product as a new arrival             | entice customers with fresh products             |

### Wireframes

Following these user stories, wireframes were drawn to provide a starting point and guidance throughout the development process.

-   The full desktop wireframes can be found [here](readme-files/beer-warehaus-desktop.pdf)
-   The mobile wireframes can be found [here](readme-files/beer-warehaus-mobile.pdf)

### Data Structure

### Design

## Features

### Existing Features

#### Home Page

-   The home page displays a slideshow with offerings highlighted by the administrator of the site
-   The home page lists the newest products to be added to the shop

#### Product Listing

The shop offers a number of solutions to make specific products easier to list and find.

-   A search function lets users find specific products
-   A product listing can be sorted by date of import, cost, and producer
-   A product listing can be filtered by packaging type (keg/drag, bottles/cans)

#### Product View

-   A user can view the details of a product, which includes the following:
    -   Product name
    -   Image
    -   Producer
    -   Description
    -   Style
    -   Alcohol contents
    -   Volume
    -   Number of units per order (for example, a box of 12 bottles)
    -   Product rating on untappd (if existing)
-   If registered and logged in, users can choose a quantity and add it to their cart

#### Producers Page

-   The producers page allows the import company to highlight reputable producers that it partners with
-   Each producer links to a description and a listing of their products offered in the shop

#### User Account

The creation of the account requires a valid email, a company name, a company number, and a password.
The creation of an account gives access to the following features:

-   Update of profile information
-   View the account's order history

#### Shopping Cart

-   Items chosen for purchase are placed in the shopping cart
-   The shopping cart displays subtotals for items placed in it and a grand total cost
-   Quantities for the products can be adjusted from within the shopping cart
-   Items can be removed from the shopping cart
-   A user can choose to proceed to payment

#### Payment

-   The checkout details and delivery information are pre-filled with the information provided in the user's profile, it can however be edited.
-   A summary of the order is displayed on the checkout page
-   Payment is made by card using [Stripe](https://stripe.com/)

#### Administrator features

-   On product pages, an administrator has additional links to edit a products information or remove it from the shop
-   An administrator has two options to add a new product:
    -   Entering the product's information manually
    -   Finding a product using a search on [Untappd](https://untappd.com/) using its API and importing it
-   An administrator can add a new producer either by entering the information manually or by performing a search on [Untappd](https://untappd.com/)
-   The administraor has the option of updating the images and text on the home page's carousel

### Features Left to implement

## Technologies

-   HTML
-   CSS
-   JavaScript / jQuery
-   Python
-   Django
-   [Untappd API](https://untappd.com/api/docs)

## Tools Used

-   Github
-   VS Code
-   Balsamiq
-   Heroku
-   Adobe Photoshop
-   [TinyJPG](https://tinyjpg.com/) used to compress all images

## Testing

## Deployment

### Local Deployment

### Deployment to Heroku

## Credits

### Media

-   Beer WareHaus logo from from [freepik.com](https://www.freepik.com/)
-   Icon for "No photo available" image from [Flat Icons](https://www.flaticon.com/authors/flat-icons)

### Acknowledgements

-   Search functionality from [Julien Phalip](https://www.julienphalip.com/blog/adding-search-to-a-django-site-in-a-snap/)
