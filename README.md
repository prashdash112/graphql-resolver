# preprocessing for data-model

The events data is collected from www.meetup.com via web scraping tools. www.import.io is a web scraping tool used to extract lists from the webpages. Data can be extracted by either APIs or web scraping. Data is extracted from meetup website in the form of CSV file, after that the csv file gets cleaned to remove junk values from data and finally the csv file got converted into a JSON file which can be dumped to our database.

Csv data file is cleaned manually by cross checking details like a single column must contain similar type of  or there shouldn't be more than 1 value in a grid etc.
Csv file is converted to JSON using http://beautifytools.com/csv-to-json-converter.php . 

# events-aggregation model
Objective:- To create and implement a data model which is used to collect data regarding upcoming tech & business events,seminars,webinars etc. from other reliable websites through their API(application programming interface) service or via web scraping, so that it can be putted down to a single database from where global users can access & transfer events data to their own blogs,websites,community etc. through our GraphQL serverless architecture. 

Goal:-To put all of the tech & business events data out there into a single platform so that events data can be accessed globally by different users and along with that it can also be transferred to other websites,blogs,online communities on user demand.

KPIs of Data model:

1)No of incoming events data instances
2)Data model building and handling time
3)Accuracy of data model
4)Scalability of data model

This Data model prototype is built using MongoDB server(a non-sql database), ariadne(a python web framework), uvicorn(an ASGI development server) & graphQL standards of building an api endpoint. 
MongoDB stores all of the events data in the form of different objects and make them accessible to GraphQL web application.PyMongo is the python library which is used here to interact with mongodb server.

Some important links:-

https://docs.mongodb.com/manual/
https://docs.mongodb.com/manual/core/data-modeling-introduction/
https://docs.mongodb.com/drivers/pymongo

Ariadne is a python based graphQL schema first framework used to build & deploy graphql web-applications where the schema is written in the Javascript style which ease up the task.

Some important links:-

https://ariadnegraphql.org/docs/intro
https://ariadnegraphql.org/docs/asgi
https://pypi.org/project/ariadne/

Uvicorn is a lightning-fast ASGI server, built on uvloop and httptools.ASGI should help enable an ecosystem of Python web frameworks that are highly competitive against Node and Go in terms of achieving high throughput in IO-bound contexts. It also provides support for HTTP/2 and WebSockets, which cannot be handled by WSGI.

Some important links:-

https://www.uvicorn.org/
https://pypi.org/project/uvicorn/

GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.

Some important links:

https://graphql.org/learn/
https://graphql.org/learn/schema/

In order to run the prototype, first we need to install mongodb server & robo3T(GUI for mongodb) from https://www.mongodb.com/try/download/community & https://robomongo.org/download respectively. Then we need to load the data.json file(which got extracted from meetup via web scrapping) to the mongodb server. Once it's done, a virtual environment should be created to install all dependencies required to run the prototype. Dependencies are 1)pip install flask
                                                                                                                  2) pip install pymongo
                                                                                                                  3) pip install mongoengine
                                                                                                                  4)pip install ariadne
                                                                                                                  5)pip install uvicorn
                                                                                                                  6)pip install json
                                                                                                                  
Kindly refer this link https://www.youtube.com/watch?v=QjtW-wnXlUY to create a virtual environment using command shell.                                        
                                                                                                                  
Once everything got set up. we are free to run the script which will act as an intermediate layer between server & mongodb. we should run the Graphql_app.py file inside the virtual environment. The command uvicorn **Graphql_app:app** will run the server & file at ip address **http://127.0.0.1:8000/** . Use **ctrl+C** to terminate the server.

All  documentation related to schema is present on the graphql web application itself.

Attributes of the event object are **Name,links,date,time,category,groupname,state,attendee**

Sample Query: query{
                    events{
                           name,category,attendee,state,groupname,links
                           }
                    } .
**The End** .
