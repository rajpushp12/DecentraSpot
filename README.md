# DecentraSpot

It has been quite a time since I've started this project. I'm glad to be able to complete this at the expected date. I would like to thank CS50 for this insightful process, I learnt a lot and it has been a wonderful journey.

## Distinctiveness and Complexity

Figuring out the nature of this application has been a tough call, I thought of making a food delivery based app but that again has become common these days so I had to drop the idea. Further, it came to mind that most of the bank websites crash a lot, why not make a better one for them? This induced the thought of the hottest investments of all time, ***the cryptocurriencies***.

This is something that is becoming one big trend. Even the high school students are investing their savings dreaming to become a billionarie. I used to be one of them. So it thrilled me to design one such exchange site! I named this ***DecentraSpot*** meaning, ***the hub to decentralized tech***. 

It is a simulation of cryptocurriencies exchange site, involving no real blockchain tech but has an ideal interactive and dynamic UI. It makes API requests at the back-end for a more secure process and has real time markets listed on it. User can trade the available Spots and send them to other users on DecentraSpot. They can add USD in form of stable coin BUSD using their card and trade all the available tokens with BUSD pair. Users can see the record of their transactions and trading and can watch their invested capital taking turns with the change in market values.

This makes the assesment a discinctive and fair complex application as has been mentioned in the requirements.


## Specification

### Database

This application has four models:

- **User:** It's a derivative of the *AbstractUser* class that contains all the registered user's information.

- **Balance:** This model has the balance of all the Spots and BUSD for each user.

- **Transactions:** It contains the detail of all the transactions that are being made on DecentraSpot.

- **Orders:** It contains the detail of all the busd-spot trades happening on the site.


### Pages

- This application has the basic **Login and Register** page.

- The **Index** page has the price list of all the markets that are available on DecentraSpot along with their Market Cap, 24 hr Change and 1 Week Change. The 'DecentraSpot' nav act's as home button that will redirect the user to this page.

- The **Balance** page lists balance of all the available tokens for the user and has trade buttons that directs to that particular trading pair. It also has a load BUSD button clicking on it, the user will be able to add BUSD to their BUSD balance using AJAX that's inside *add.js* file.

- The **Orders** page has list of the user's buy and sell data as asset amount, busd amount and the time at which the particular order was placed. This uses *order.js* file to seperate the Buy and Sell Orders using event listeners for the buttons.

- The **Transactions** page has list of all the received and sent spots for a particular user, the table contains the sender or recipient username, the asset name, amount transfered in BUSD and time of the transaction as most recent one listed at the top. This uses *transaction.js* file to seperate Sent and Received transactions.


