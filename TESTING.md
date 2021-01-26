![Beer WareHaus Logo](readme-files/beer-warehaus-readme-logo.png)

# Testing

## Navigation

-   Each navigation link works as intended, including the account links leading to profile, login and logout.
-   The navigation collapses as intended on mobile devices.
-   The correct cost of the shopping cart is displayed and updated.

## Homepage

### Carousel

-   The carousel functions as intended, displaying an image, a title, a description and a link to a specified page, with the ability to change the displayed slide
-   The links to specific pages work as intended
-   Images of different sizes can be uploaded without breaking the layout of the elements of the page.

### New Products

-   The "New Products" section of the homepage shows all products marked as "new" by the site's administrator. The information displayed is correct. Products no longer display here if the flag is removed.
-   The "new" overlay is present on all new products.

## Product Listing

-   The pages listing products display the correct information, for each product and the number of products.
-   The "back to top" button works as expected.

### Search

-   The search functionality works as intended. It returns products whose name, producer, style, and description contain the searched keyword.
-   The search unaccents characters (ie: a search for "biere" will return results containing "bière") and accounts for capitalization.

### Filtering

-   Various search filters on the products page display the correct propers, including when several filters are used, and when a search term was entered.

### Pagination

-   The pagination displays the correct number of pages. It accounts for selected filters and search terms. - Links to previous and next pages to not appear on the first and last pages of the listing.

## Product Details

-   The product pages display the correct information and image.
-   Products can successfully be added to the cart using the form.

## Producers

-   The producers page correctly displays all featured producers.
-   Clicking a producer's image or name displays the proper information about this producer.
-   All products from a specific producer are listed on their page.
-   Clicking on "see product" leads to that product's detail page.

## Shopping Cart

-   The shopping cart displays all items selected by the user.
-   Updating the quantities of products in the cart works as intended.
-   It is possible to remove an item from the cart.
-   Clicking "Proceed to Payment" leads to the checkout page.
-   If the shopping cart is empty, it is displayed as such.

## Checkout and Payment

-   The checkout form loads appropriately.
-   The checkout form comes pre-filled if a profile has been saved.
-   The items in the shopping cart are correctly displayed.
-   The correct total and subtotals are displayed.
-   Checkout nformation can be saved to profile when checkbox is selected.
-   Stripe payment works correctly, webhooks have been tested and received.

## Profile

-   The profile page displays the saved profile information.
-   The form to update profile information is displayed successfully when clicking the "edit information" button.
-   The profile information updates successfully when this form is filled.
-   The correct order history is displayed successfully.
-   Clicking on the order number reveals more details about the order.

## Contact

-   The contact form correctly sends information.
-   All required fields must be filled for the form to send.
-   Email field must contain a string formatted as an email.

## Account Management

## Administrative Tools

### Homepage

### Product Management

### Producer Management

## Untappd API

## Responsiveness

## Bugs Encountered
