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

### New Products

-   The "New Products" section of the homepage shows all products marked as "new" by the site's administrator. The information displayed is correct.
-   The "new" overlay is present on all new products.

## Product Listing

-   The pages listing products display the correct information, for each product and the number of products.
-   The "back to top" button works as expected.
-   Products flagged as "new" display the "new product" overlay.

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
-   An unsuccessful payment returns the reason for the failure.

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

## Administrative Tools

Links to adminsitrative tools in the navigation can only be seen if a user is logged in as an administrator.

### Homepage

-   Adding or removing carousel items works as intended.
-   Images of different sizes can be uploaded without breaking the layout of the elements of the page.
-   Products flagged as "new" are displayed on the homepage.
-   When the flag is removed, they are no longer displayed.

### Product Management

#### Adding a Product

-   Adding a new product works as intended.
-   All required fields must be filled to add a new product.
-   Searching the untappd API for a product returns results as intended.
-   Selecting a result from the untappd API correctly fills the "new product" form.
-   If no image is selected from the API or by the administrator, a default image is chosen.

#### Editing/Deleting a Product

-   Deleting a product from a product page or from the product management page works as intended.
-   A modal window appears and requires confirmation when deleting a product.
-   Searching for a specific product on the product management page works as intended.
-   Accessing a product's edit page can be done through the product's page or the management page successfully.
-   When editing a product, its information populates the fields of the form.
-   A product can be updated successfully if all required fields are filled.
-   The "back to top" button functions as intended.

#### Adding a Producer

-   Adding a new producer works as intended.
-   All required fields must be filled to add a new producer.
-   Searching the untappd API for a producer returns results as intended.
-   Selecting a result from the untappd API correctly fills the "new producer" form.
-   If no image is selected from the API or by the administrator, a default image is chosen.

### Producer Management

-   Deleting a producer from a producer page or from the producer management page works as intended.
-   A modal window appears and requires confirmation when deleting a producer.
-   Searching for a specific producer on the producer management page works as intended.
-   Accessing a producer's edit page can be done through the producer's page or the management page successfully.
-   When editing a producer, its information populates the fields of the form.
-   A producer can be updated successfully if all required fields are filled.
-   The "back to top" button functions as intended.

## Responsiveness

This application was tested for responsiveness across a variety of devices to ensure content remained readable and editable on various screen sizes.

The navigation, layout and various functionalities (login, logout, add, view, delete and update reviews) were tested across various screen sizes with chrome developer tools and with the [Responsive Viewer Chrome extension](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb).

These tests were performed on the following devices and browsers:

-   Chrome, Safari and Firefox on Mac OS
-   Chrome and Safari on iPhone XR
-   Chrome and Safari on iPad with Retina display
-   Chrome on Xiaomi Redmi 4A
-   Firefox on Xiaomi Redmi Note 5

## Bugs Found

-   An issue was found where filters would not carry through other pagination links. This was fixed in the template by using the "url_replace" tag in the jinja template to update only the pagination get variable in the link's url.
