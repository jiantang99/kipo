# Kipo Search Catalogue 

This project contains a simple front-end interface which allows users to search for a part using a text query. This text query may contain information regarding any category, such as Manufacture Part Number, IP Rating, and Termination Style.
As such, the use of an LLM allows us to narrow down what category this text query might be searching for.
For example, is the user inputs the text query 'IP67', they are most likely searching for products with an IP67 IP Rating.
Below are detailed steps as to how I attempted to index and search for the part based on the user's text query.

## Indexing
My idea was to create 1 dictionary for each category of information. For example, ip_rating_dict would map different IP ratings to a list of rows that contain this exact IP rating.
For example, ip_rating_dict = {"IP67": [3,2,457,978]}
This allows us to search for a specific query, and we are able to obtain the list of parts which contain this query in O(1) time.
All this indexing logic is contained inside index_data() inside index_data.py.

In a production environment, we would use a document database, which is able to store the unstructured data we have when we extract the important information from pdf or text documents.

## Search
Once we obtain the query string, we pass it through ChatGPT, with a sample of the dictionaries we have, and prompt it to return the top 3 categories that this query might be in.
Once we get these 3 categories, we search through their dictionaries' keys, and check if the query is contained inside any of their keys.
We then collate all the row numbers which contain the query string inside the top 3 categories, and print out their row number and some other information about the part.
This logic is contained inside query() in index_data.py.

## Further improvements
Currently, there is only support for 1 category at a time. So if the input is 'IP67 Pin (Male)', the search would not work as well.
To counteract this, we could divide the input string into different parts, with 1 part of the string mapping to 1 category. This dividing of the input query would be done via the LLM as well.

Currently, the sample dictionary of categories to example values only include the first 20 values. If possible, we could pre-train the LLM using all the values we have, and then use the weights to search.
This would allow the LLM to be more accurate when producing the top 3 categories that the text query might be related to.

## How to run application
1. Install dependencies (pip install -r requirements.txt)
2. Ensure terminal is inside the root directory of this project
3. Export ORGANIZATION_KEY as the openai organisation key, and OPENAI_API_KEY as the openai api key as environment variables
4. Run python app.py