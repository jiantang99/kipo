import pandas as pd
from collections import defaultdict

class Index_data():

    def __init__(self):
        self.df = pd.read_csv('product_data.csv')
        self.rename_first_column()
        self.sample_dict = defaultdict(list)       # We will use this sample dict to train the LLM on possible values each category is related to
        self.index_data()

    def rename_first_column(self):
        self.df.rename(columns={'Unnamed: 0': 'Row'}, inplace=True)
        self.df.rename(columns={'I': 'Row'}, inplace=True)

    def index_data(self):
        column_names = self.df.columns.values.tolist()

        # For each column name, create a variable {column_name}_dict = defaultdict(list) i.e., ip_rating_dict
        for col in column_names:
            column_name_in_dict = col.lower().replace(" ", "_")
            globals()[column_name_in_dict + "_dict"] = defaultdict(list)

        # For each row inside dataframe, append the row number to the corresponding value
        for index, row in self.df.iterrows():
            for col in column_names:
                column_name_in_dict = col.lower().replace(" ", "_")
                globals()[column_name_in_dict + "_dict"][row[col]].append(row['Row'])

        # For each column, we obtain append the possible values for each column
        for col in column_names:
            column_name_in_dict = col.lower().replace(" ", "_")
            temp_dict = globals()[column_name_in_dict + "_dict"]
            self.sample_dict[column_name_in_dict].append(list(temp_dict.keys()))

        # We take the first 20 values of each list, as ChatGPT does not allow for so many tokens
        for key, value in self.sample_dict.items():
            shortened_list = self.sample_dict[key][0][:20]
            self.sample_dict[key] = shortened_list

    def query(self, query: str):
        from openai import OpenAI
        import os

        # Obtain organization key and api key from environment variables
        org_key = os.environ['ORGANIZATION_KEY']
        api_key = os.environ['OPENAI_API_KEY']

        client = OpenAI(
            organization=org_key,
            api_key=api_key
        )

        # We create a chat completion object which contains the text output from ChatGPT
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"given this dictionary below, which maps a category to possible values, "
                                            f"choose from the keys inside this dictionary, the top 3 categories that "
                                            f"the query will most likely fall into: "
                                            f"{self.sample_dict} \n query: {query} \n give the 3 categories in a "
                                            f"single line seperated by a white space with no other output"}
            ]
        )

        # We obtain the top 3 categories suggested by ChatGPT
        top_3_categories = completion.choices[0].message.content.split()

        # We create a list to store all the rows that contain the text query in the appropriate category
        row_list = []

        # For each category suggested, we go to its dictionary, and find the keys which contain the search query
        for category in top_3_categories:
            for key in globals()[category + "_dict"].keys():
                # If the key contains the search query, we add the list of row numbers to the list of all row numbers
                if query.lower() in str(key).lower():
                    one_row_list = globals()[category + "_dict"][key]
                    for row in one_row_list:
                        row_list.append(row)

        # We reset the index to row number, so that we can obtain the row by using the list of row numbers, row_list
        self.df.set_index("Row", inplace=True)

        # We create a new dataframe which contains only the rows which contain the text query
        new_df = self.df.loc[row_list]
        new_df = new_df.reindex(columns=self.df.columns.values.tolist())

        # We create a new list to store all the entries of parts, which we will return at the end of this function
        return_list = []

        # We loop through the new dataframe and add a new entry for each part into the list which we will return at the end
        for index, row in new_df.iterrows():
            temp_dict = {
                "mpn": new_df.loc[index, "Mouser Part Number"],
                "description": "Basic information about product: "
                               f"Manufacture Part Number: {new_df.loc[index, 'Mfr Part Number']} \n"
                               f"Manufacturer: {new_df.loc[index, 'Mfr.']} \n"
                               f"Datasheet: {new_df.loc[index, 'Datasheet']} \n"
                               f"Availability: {new_df.loc[index, 'Availability']} \n"
                               f"Pricing: {new_df.loc[index, 'Pricing']} \n"
                               f"RoHS: {new_df.loc[index, 'RoHS']} \n"
                               f"Lifecycle: {new_df.loc[index, 'Lifecycle']} \n"
                               f"Product Detail: {new_df.loc[index, 'Product Detail']} \n"
                               f"IP Rating: {new_df.loc[index, 'IP Rating']} \n"
                               f"Product: {new_df.loc[index, 'Product']} \n"
                               f"Contact Gender': {new_df.loc[index, 'Contact Gender']} \n"
                               f"Termination Style: {new_df.loc[index, 'Termination Style']} \n"
                               f"UID: {new_df.loc[index, 'UID']} \n"
            }

            return_list.append(temp_dict)

        return return_list


