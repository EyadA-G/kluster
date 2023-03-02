Website Readme:
To run the django app type the following in the terminal: python manage.py runserver

This will take you to localhost 8000 where there will be a login page.
There are three users; Apple [password: apple], Dan [password: dandan] and admin [password: pass] ***there is no landing page for admin yet so you'd have to login as admin using http://[youripaddress]:8000/admin/

Once logged in you will be in the duser page where you can preview products and the store which the user owns and be able to update or delete those products.
The product name has the format [productname] [[productid]] ex. iphone_13 [13]

On the navbar there are four options: add product, add store add sales and view sales.

Add Product:
  inputs needed are user, productid, product name and unit price.
  user id is already given as the logged in user.
  unit price is an integer fieled so only numbers are allowed.
  
Add Store:
  inputs needed are user, storeid, store name and store location.
  user id is already given as the logged in user.
  
 Add Sales:
  inputs needed are user, prodid, storeid, date and units sold.
  user id is already given as the logged in user.
  pub date is a date fieled so only date formats are allowed.
  units sold is an integer fieled so only numbers are allowed.
  
  View sales:
    A list of sales in a tble format is presented with the details:
    id, storeid productid, date and units sold.
    On the top there is a download button where you can download the sales as a csv file.
  
  
