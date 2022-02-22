# **Permit Management System**

This is an easy-to-use web application developed for managing the application, processing and issuing of permits by the Botswana local government authorities.

---

## **Introduction**

Permit Management System is accessible through a web browser such as:

* Google Chrome
* Safari 
* Mozilla Firefox
* Internet Explorer etc).

Customers who visit the site can view a list and explore additional details of the different types of permits that the local government authority is mandated to issue. To apply for a permit, a customers must ***sign up*** to create an account that will be used to track the status and progress of the application.

The system is developed to send email notifications to appropriate individuals at every stage of the application process. This helps to ensure timely and efficient management of the permit application, processing and issuing workflow. 

Upon meeting all ***compliance requirements***, the system will notify the customer to process payment of the application fee, which can be done online via a payment gateway integrated with the system, or through usual bank transfer methods.

Once the evaluation process is complete, the customer will receive an email notification with either a ***rejection*** or ***approval***. An official license permit will also be attached for approved applications.

---

## **Installation**

Permit Management System is built on the [Frappe Framework](https://frappeframework.com/ "Frappe Site"), a full-stack, open source, web development framework written in Python & JavaScript. The framework is ***generic*** and can be used to build database driven apps. ***MariDB*** is the default database for the framework.

To install Permit Management System, you will have to install [Frappe-Bench](https://frappeframework.com/docs/v13/user/en/installation "Frappe Bench Installation"), a command-line package and site manager for the Frappe Framework.

>For more details, read the Bench ***README***.

After installing Frappe Bench, you will have to initialise a bench directory with the Frappe Framework using the following command:

```bench
bench init permits
```

Next, change the directory to ***permits*** and download the Permit Management app with the following command:

```bench
cd permits

bench get-app permit_management {{ source_link }}
```

Create a new site to install the app by running the command:

```bench
bench new-site permits.example.com
```

This will create a new folder in your ***/sites*** directory and create a new database for this site.

Next, install the Permit Management app in this site by running the command:

```bench
bench --site permits.example.com install-app permit_management
```

To run the app locally, you must start the bench service with the command:

```bench
bench start
```

At this point, the Permit Management app is installed and listening on port 8000. 

You can now fire up your browser by clicking [this link](http://localhost:8000/ "Login Screen") and you should see the login screen. 

Login as Administrator and use the password you set at the time of creating the site ***(permits.example.com)***.

---

## **License**

MIT