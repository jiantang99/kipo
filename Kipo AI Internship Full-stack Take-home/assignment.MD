README.md

# Backend Take-Home Question 

## Task description

This repo contains just the front-end portion of a very simple web app in which a user can search for parts. Your task is to build the backend required for this web app to function. You are provided with a simple database of product metadata, and your goals are: 

- Index these products to make them easy to search. 
- Extract basic information from the datasheets so that the user can search for a datasheet. Keep it simple.
- Design a search tool that incorporates, in some way, an LLM to select a part from the database. 

You can use any existing libraries to accomplish this task. Feel free to use any external tools or resources (ChatGPT, StackOverflow, etc.). Please ping Arjun with any questions if you get stuck. You should aim to spend about 4 hours on this task. 

## 1. Indexing

The "database" of products is in the file `product_data.csv`, and is accompanied by PDF datasheets in the `datasheets` folder. The datasheets are named by the part number, and the part number is also in the CSV. 

Retrieve enough information about the datasheet, and the metadata, to allow users to search for the part. Design it as you see fit, and keep it basic. 

If you were to store this data in a production system, how would you store it (what kind of database) and why? 

[Your answer here]

## 2. Search

Build a backend with whatever tools and frameworks you are comfortable in (Python frameworks preferred if all else is equal). The user interface is defined in `substitute.html` and already includes a search bar and a way to display a table of parts, but feel free to edit this code if you'd like. Your backend should take the user's query, use it to retrieve some datasheets/parts, and show some of the relevant data in the table. 

Use an LLM to assist with searching the database for matching parts. There are many ways to do this - we're not looking for a specific solution. Consider how this might help a user find a part as naturally and quickly as possible, and feel free to get creative. You can use the OpenAI API for this - you will be limited to $10 of API calls, which should be sufficient for this task. 

## Logistics

- To use the OpenAI API, use the organization key "org-pG18N9kBRPkp3ogbR6AYphvb". The API key will be provided to you via email. See [here](https://platform.openai.com/docs/api-reference/authentication) for more details on authentication.
- Please reach out to your interviewer with any questions you might have. We would be surprised if you had no questions, so don't hesitate to ask. 
- You can use any existing tools or libraries you want. How well you can build on existing tools is part of our evaluation.

When you're done, share your code via email arjun@kipo.ai, a link to a private Github repo, or another method.
- Please include a short description of the relevant features of your approach. 
- Please include any special instructions for running your code.
- Make sure that your solution works and can be edited live. If you are invited to the final round, you will be asked to add a feature to your solution live. 

## Evaluation and bonus

We will evaluate:
- the functionality of your solution
- the reasoning behind your design choices
- how adeptly you use existing tools and libraries
- the way your code is organized and documented. 

If you're able to complete the task, you'll be invited to the final round interview (assuming timing/logistics work out). You'll be asked to explain your solution during the final round. 
