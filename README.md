# Beer WareHaus

Beer WareHaus is an online shop for a hypothetical beer import and distribution company in Norway. The purpose of the site is to provide a simple intuitive ways for managers of bars and restaurants to browse and purchase products they wish to serve.
Additionally the site provides a number of tools allowing the shop owner to easily manage the products in the shop.

## UX

### Project Goal

This project is my fourth and final Milestone Project in the Code Institute's Fullstack Development program. The purpose of this project was to create an e-commerce site using the Django framework, static file hosting with AWS, and a functional payment system with Stripe. This e-commerce site is fully functional and could be used by a real beer distribution company with minimal setup.

### User Stories

#### User Stories for Customers

| **As a restaurant or bar manager I would like to** | **So that I can**                                 |
| -------------------------------------------------- | ------------------------------------------------- |
| browse products                                    | purchase what I need                              |
| search products                                    | find something specific                           |
| filter products by style                           | compare the offerings                             |
| filter products by packaging (can, bottle, keg)    | choose serving style                              |
| see offerings by a specific producer               | get an idea of the producer's offer               |
| buy a product                                      | serve it to customers                             |
| pay using a card                                   | pay immediately                                   |
| receive an invoice                                 | pay at a later date and keep track of my payments |
| create a profile                                   | make orders and have my information saved         |
| update my profile information                      | be contacted by the importer                      |
| see my shopping cart before paying                 | know the cost and content before the purchase     |
| update my shopping cart                            | make decisions before the purchase                |
| see details about a product                        | make an informed purchasing decision              |
| view my order history                              | be reminded of previous purchases                 |
| receive an email confirmation about my order       | have archived information about it                |
| contact the importer                               | know about the status of an order                 |
| know the newest arrivals                           | buy the freshest products                         |
| see all discounted products                        | get the best deals                                |
| repeat an order from my order history              | save some time on my regular orders               |

#### User Stories for Shop Administrators

| **As an administrator I would like to**     | **So that I can**                                |
| ------------------------------------------- | ------------------------------------------------ |
| Add/Update/Remove a product                 | Keep the store up to date                        |
| Add/Update/Remove a brewery                 | keep users informed about the latest information |
| Update contact information                  | Have users stay in touch with me                 |
| Mark products as discounted                 | sell product that needs to move                  |
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
-   Each producer links to a listing of their products offered in the shop

#### User Account

New users must create an account to purchase products. The creation of the account requires a valid email, a company name, a company number, and a password.
The creation of an account gives access to the following features:

-   Update of profile information
-   Purchase products by card or with invoice
-   View the account's order history
-   Repeat an order from the order history

#### Shopping Cart

-   Items chosen for purchase are placed in the shopping cart
-   The shopping cart displays subtotals for items placed in it and a grand total cost
-   Quantities for the products can be adjusted from within the shopping cart
-   Items can be removed from the shopping cart
-   A user can choose to proceed to payment

#### Payment

-   The checkout details and delivery information are pre-filled with the information provided in the user's profile, it can however be edited.
-   A summary of the order is displayed on the checkout page
-   A user wanting to make a purchase has two options for the payment:

    -   Immediate payment by card, using Stripe
    -   Being sent a PDF invoice by mail with a due date of 2 weeks after purchase

#### Administrator features

-   On product pages, an administrator has additional links to edit a products information or remove it from the shop
-   An administrator can add two options to add a new product:
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

## Testing

## Deployment

### Local Deployment

### Deployment to Heroku

## Credits

### Media

-   Beer WareHaus logo from from [freepik.com](https://www.freepik.com/)

### Acknowledgements
