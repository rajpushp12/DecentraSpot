# Information Manual

It has been quite a time since I've started learning this. I'm glad to be able to complete this course on expected time and I would like to thank CS50 for such insightful process. I learnt a lot and it has been a great journey till here.



## Distinctiveness and Complexity

Figuring out the nature of this application has been a tough call, I thought of making a food delivery app but considering that it has become common these days, I had to drop the idea. I further desired making a banking site as most of the bank websites crash a lot. Beginning to thimk around that line induced in me the thought of one of the hottest trends of all time, ***the cryptocurriencies***.

 It's something that is becoming one big trend. Even the high school students are investing their savings in dream to becoming a millionaire. I used to be one of them, so it thrilled me to design one such exchange site! I started to think about it and here I am. I've named this site ***DecentraSpot*** meaning, ***the hub to decentralized tech***. 

It is a simulation of cryptocurrencies exchange site, involving no real blockchain tech but has an ideal interactive and dynamic UI. It makes API requests at the back-end for a more secure process and has real time markets listed on it. User can trade the available spot-busd pairs and send them to other users on DecentraSpot. They can add USD in form of stable coin BUSD using their card. Users can see the record of their transactions and trading on the site and can watch their invested capital taking turns with the change in market values.

This makes the assessment a distinctive and fair-complex as been mentioned in the requirements.




## Database

This application has four models:

- **User:** It's a derivative of the *AbstractUser* class that contains all the user's information.

- **Balance:** This model has the balance of all the Spots for each user.

- **Transactions:** It contains the detail of all the transactions that are being made on DecentraSpot.

- **Orders:** It contains the detail of all the busd-spot trades happening on the site.




## Pages and Specifications

- This application has the basic **Login and Register** page.

- The **layout.html** file, as usual contains the main frame of the application, in this case the navigation and footer.

- Though the manual css styling used in this application is minimal, **style.css** has the basic style standard for the body and the footer. Inline styling has also been used at several places in accordance to the UI.

- The **Index** page has the price list of all the markets that are available on DecentraSpot along with their Market Cap, 24 hr Change and 1 Week Change. The 'DecentraSpot' navigation act's as home button that will redirect the user to this page.

- The **Balance** page lists balance of all the available tokens for the user and has trade buttons that directs to that particular trading pair. It also has a load BUSD button clicking on it, the user will be able to add BUSD to their BUSD balance using their card. It uses ajax to manipulate the table, the code to this is inside *add.js* file.

- The **trade.html** is the address where users are directed to as they click the trade button on assets in *Balance* page. It just requires the busd amount of asset the user needs to trade. If the balance is insufficient in either of the cases, this will show an error message.

- The **Orders** page has list of the user's buy and sell data. It contains asset amount, busd amount and the time at which the particular order was placed. This uses *order.js* file to separate the Buy and Sell Orders using event listeners for buttons.

- The **Transfer** page enables the user to make a transaction. It requires the asset name to be transferred from the list of assets, it's amount, username of the recipient and the user's login password for authenticating the transaction.

- The **Transactions** page has list of all the received and sent spots for a particular user, the table contains the sender or recipient username, the asset name, amount transferred in BUSD and time of the transaction as most recent one listed at the top. This uses *transaction.js* file to separate Sent and Received transactions.

- The **views.py** file contains all the back-end code that is going to make this website functional. It has all the neccessary imports that is required to run the application.

- The **urls.py** in the exchange app directory contains the urls that enable users to navigate through the website. It also contain the neccessary API Route for the ajax in *add.js* and is linked to *views.py*.

- Last but not the least **admin.py** has a route in the main *urls.py* file and it enables the superuser to manipulate and handle the database, it has access to all the models that have been created in *models.py*.


*Except the login, register and index page, all other pages require authentication.*



## Running the application

To run the application, make sure the system has django installed in it. If not then install it running the command '**pip3 install django**' in the terminal.

Once it's installed, goto to the **DecentraSpot** directory in terminal and run the command '**python3 manage.py runserver**'.





Regards,
Pushp Raj
