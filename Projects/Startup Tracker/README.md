# Algorithms-project
Algorithms project for start up app

## Description:
Startup Tracker is a user-friendly app designed to help small startups and businesses effectively track their inventory levels, profits, and revenues. It's tailored for businesses that are just starting and don't have the resources for complex inventory management systems. Startup tracker is meant to allow small businesses to manage their  inventory and gain insights into financial performance, making it simpler to run businesses efficiently.

## Balsamiq App 
We used balsamiq app which uses templates and reads data to create our interface for our app algorithms. 
</table>
  </tr>
    </td>
      <img src= "https://github.com/alexiachm/Algorithms-project/blob/main/MockHomeScreen" alt="Sign in home screen" title= "Sign in home screen">
     </td>
     </td>
       <img src="https://github.com/alexiachm/Algorithms-project/blob/main/mockInventory" alt="Inventory" title= "Inventory">
     </td>
     </td>
       <img src="https://github.com/alexiachm/Algorithms-project/blob/main/MockExpenses" alt="Expenses" title= "Expenses">
      </td>
       </td>
        <img src="https://github.com/alexiachm/Algorithms-project/blob/main/MockRevenue" alt="Revenue" title= "Revenue">
      </td>
        <img src="https://github.com/alexiachm/Algorithms-project/blob/main/ImportDataset.jpeg" alt="Add Dataset" title= "Add Dataset">
    </tr>

    <tr>
      <td> Sign in Home Screen</td>
      <td> Inventory</td>
      <td> Expenses</td>
      <td> Revenue</td>
    </tr>
  </table>
        


## Table of Contents
1. [Introduction](https://github.com/alexiachm/Algorithms-project/blob/main/README.md#introduction)
2. [Installation & Usage](https://github.com/alexiachm/Algorithms-project/blob/main/README.md#installation--usage)
3. [Further Improvements](https://github.com/alexiachm/Algorithms-project/blob/main/README.md#further-improvements-for-second-code)
4. [Credits](https://github.com/alexiachm/Algorithms-project/blob/main/README.md#credits)

# Introduction 
This application was created for our Algorithms & Data Structures class. The project instructions were to create an app using what we learned in class. 

We came up with StartupPal, an app for small businesses who struggle with keeping track of managerial operations of their startups such as: keeping inventory, tracking revenues and expenses and, therefore might feel that they are not able to have their business under control and feel that these type of tasks are too time consuming, shifting their focus away from other activities that might be more beneficial for their company.

In our app entrepreneurs are able to upload a dataset with information such as inventory levels, revenues, or expenses in order for them to easily see their exact inventory number, savings and expenses without having to calculate it themselves every time they want to visualize it. Additionally, it gives the user the opportunity to see these data in an organized way, like graphs and tables, in this way users will also be able to see how their business is going, and what modifications they can incorporate to it, in a much more simplified way because, as we all know, graphs, just like pictures, are worth more than a thousand words.

## Datstructures 
We used binary search trees to store the data provided by the user, more concretely AVL trees, which are a special type of binary search tree which balance themselves when inserting or deleting each node. We will create a product tree for each product in the dataset and fill the nodes with time observations. Each node, representing each time observation of a product, will be stored in order in the BST  based on the timestamp and will store the product revenue, inventory and costs at that specific time.  This implementation is very good because when a BST tree is balanced, they have a predictable running time for every kind of operation, and they are going to perform all these operations quite fast, in O(log n) time which is the number of levels in the bst when it is balanced. (this is ensured thanks to AVL)

In our program we want to display the user options for each product, telling them which time interval they can choose from for data on that specific product selected. For this we will use operations of getting max and getting the min of each product tree (based on timestamp) to display the available intervals to the user for him tp select. Balanced AVL trees are really efficient at searching max/ min with an operation of log(n). Moreover we will also use an inorder traversal algorithm (which will traverse the product tree in order based on the timestamp) and will append the timestamps that fall within the range specified by the user in order (because it traverses the tree in order).  This will return the data that the user wants to visualise (tables/ plot) by when visiting each node seeing if it is inside the interval designed by the user and if it is appending it to a list. 
Finally we also use a hash table in order to allow the user to log in and save their access credentials in a csv file so they are saved in the computer after the user quits the program.

# The Dataset
The program allows the user to choose a dataset from their files. To try out the program the zip file also comes with a default dataset 'startups.xlsx'
This dataset was manually constructed by our group, taking into account the workings of a start-up and it provides information about 4 products from a start-up with 208 accumulated different time stamps. Its content is relevant for anyone interested in tracking and organizing their products depending on their time stamps, and understand their current and past savings, expenses, incomes, and inventories. The following variables are presented:

- Product: including product A, B, C & D, with their respective different time stamps.
- Timestamp: there are 208 timestamps, each with their corresponding date and time.
- Inventory: there are different amounts of stock of the four product types, depending on the time stamp given.
- Accumulated Revenue: there are different amounts of revenue of the four product types, depending on the specific time stamp.
- Accumulated Cost: there are different amounts of costs of the four product types, depending on the given time stamp.

Our current Limitation is that in order to be effectively read by our program, datasets selected by the user from their files should have the same format as our default dataset.


## User journey 
The app is first accessed by a login in or sign up page for the user to save their data accordingly. After, a dashboard is displayed with a main statistics page of inventory levels, overall revenue and inventory. The dashboard displays whether the data is increasing or decreasing (an overview of all the data). From this dashboard, there are three tabs that can be accessed: Inventory, Revenues, and Expenses. 

Home Screen: When entering the app, we can see the name of our application and a big START button that we will need to click in order to continue with the user experience.
<img src="https://github.com/alexiachm/Algorithms-project/blob/main/HomeScreen.png" alt="HomeScreen" title= "HomeScreen">


User Interface: When clicked, the application will give us the option of Log in, Sign in or Exit the app.
<img src="https://github.com/alexiachm/Algorithms-project/blob/main/User%20Interface.png" alt="UserInterface" title= "UserInterface">


Log In and Sign Up: If we click the Log in in button, the app will ask us to enter our username and a password since we already have an account. Then we will be able to click the Log in button and actually Log in into our app or click the Back button which will redirect us to the previous page. If we click the Sign in button, we will be able to enter a username and a password to create an account. Then we will be able to click the Sign in button and create our account or click the Back button which will redirect us to the previous page.

<img src="https://github.com/alexiachm/Algorithms-project/blob/main/Log%20in%20Page.png" alt="LogIn" title= "LogIn">
<img src="https://github.com/alexiachm/Algorithms-project/blob/main/Sign%20in%20Page.png" alt="SignUp" title= "SignUp">

Main Menu: There is a main menu where the user has to choose between inventory, revenue or expenses.
<img src="https://github.com/alexiachm/Algorithms-project/blob/main/Main%20Menu.png" alt="MainMenu" title= "MainMenu">


To track inventories, the system displays the main site of an activated account where the menu is initially displayed. The system then allows to select the Inventory tab, and shows an initial graph with the total inventories of all products distinguishing between those bought this month and those bought previously. After this, if you double tap on the graph it can change to a table format which displays the different amounts of each product, for the user to visually understand it in a different manner. Also, the system is able to filter by allowing the user to select a specific product or group of products and specific time frames. the system will again display the inventory graph with the corresponding filtered inventories. If the user double taps it changes again to the table format. In addition, the inventories page, displays the savings of the start-up, by allowing the user to save the graphs they have created to a given format. 
  <img src= "https://github.com/alexiachm/Algorithms-project/blob/main/Inventory.png" alt="Iventory" title= "Inventory">

As previously mentioned for inventories, the app tracks revenues and expenses similarly. For revenues, the system displays the main site of an activated account where the menu is initially displayed and the system the nallows to select the revenue tab. The system shows a graph with the total revenues, and can also change to table format to show the different amounts of each product. The system also filters and shows savings as previously mentioned. 
   <img src="https://github.com/alexiachm/Algorithms-project/blob/main/Revenue.png" alt="Revenue" title= "Revenue">  

To track expenses, the system displays the main site and allows the user to select the expenses tab, where the system displays an initial graph with the total expenses of all products distinguishing between those bough this month and those bough previously. It does the same as with the other two previous tabs for filtering and savings.
<img src="https://github.com/alexiachm/Algorithms-project/blob/main/Expenses.png" alt="Expenses" title= "Expenses">
      </td>
       </td>

## Limitations
The algorithm is currently limited to start-up business, as if a business were to grow exponentially into a mass corporation, our current system might not hold all data structures appropriately. 
Our main limitation is that our app works specifically with our dataset only, if a startup would want to include their own dataset it would not be possible. To improve this we could work on an algorithm which is able to udnerstand the user's data regardless of its format. However this is not in the scope of our project. 

## File Architecture
- `algorithmsUI.py` - The python file where the user can find the code for the app.
- `MockHomeScreen`,`mockInvenotry`,`MockExpenses`,`MockRevenue`,`ImportDataset.jpeg`- The mock files where the user can find the pictures at the begining of the gitHub. They are the  main balsamiq app file that includes this GitHub. 
- `Choose Dataset.png`,`Expenses.png`,`HomeScreen.png`,`Inventory.png`,`Log in Page.png`,`Main Menu.png`,`Revenue.png`,`Sign in Page.png`,`User Interface.png`- The files where the user can find the pictures of the running code, if the user downloads the python file and runs it, they are going to see this files.  
- `startups.xlsx`- The file where the user can find the dataset used for the python code. It is an example of an excel. If the user has another excel with the same structures as in the given excel in the Github, it will work for this code.


# Installation & Usage 
### First-time install 

clone the files:
`````
git clone https://github.com/alexiachm/Algorithms-project.git
`````
creating and activating a virtual environment 
create the venv:
`````
cd Algorithms-project
python3 -m venv./Algorithms-project
`````

activating the venv (each time you open):
`````
source ./Algorithms-project/bin/activate 
`````

install modules:
`````
pip install -r requirements.txt
graphics.py
pandas.py
pip install pandas
pip install matplotlib
pip install graphics.py
pip install openpyxl
`````
In case the pip install doesn't work, please install the libraries manually with the pip install pandas.
tkinter and csv are libraries included in Python.


## Libraries:
`````
from graphics import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from matplotlib.table import Table
import csv
import openpyxl
`````
usage 
`````
cd Algorithms-project
`````
`````
export FLASK_APP = app
`````
`````
export FLASK_DEBUG=1
`````
`````
flask run
`````

# Further improvements 
For our next steps, we thought about two main ideas which could be implemented in the long run. 

The first one includes Dataset improvements, such as:
- For our app to be able to take as an input datasets that don’t need to be in our specified format, but that the app manages to adapt to more structures of different datasets
as well as for our app to be able to handle bigger amounts of data, with more columns and rows.

The second one inludes taking into account big companies and not only start-ups:
- As an aim for our tracker to grow and be able to accompany businesses that were once startups, and are now large companies
And lastly, for our tracker to hold large amounts of data from big businesses, not only start-ups, so that our app would grow professionally and continue being of use for all businesses, including those that started organizing themselves with us. 

Also If our app was connected to the user’s dataset in real time we would provide valuable insights on the data such us:
- Notifications whenever inventory is below 0, or even before that so user’s don’t run out of inventory
- Updates on best performing products based on revenue
- Recommendations on which products to maintain for next operating months etc.
  
For this we would need an algorithm which is able to understand the data, read, provided and make recommendations. 

# Resources Used
- [balsamiq] (https://balsamiq.com/)
- [excel] (https://github.com/alexiachm/Algorithms-project/blob/main/startups%20(4).xlsx)
- [python] (https://github.com/alexiachm/Algorithms-project/blob/main/ProjectAlgorithms.py)
- [python] (https://github.com/alexiachm/Algorithms-project/blob/main/AlgorithmsCodeStartups%20(1).py)

# Credits
This project was created for our Algorithms and Data Structures class at IE University. The authors of this project are:
- Tessa Correig
- Sofia Serantes
- Emilia Granja
- Tomas Lock
- Pilar Guerrero
- Alexia Chacon

