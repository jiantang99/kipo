from flask import Flask, render_template, request, redirect, url_for
from index_data import Index_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/substitute/', methods=['GET', 'POST'])
def substitute():
    data = None
    if request.method == 'POST':
        query = request.form.get('query')
        data = get_substitute_data(query)
    return render_template('substitute.html', data=data)

def get_substitute_data(query):
    index_data = Index_data()
    return index_data.query(query)

@app.route('/comparison/', methods=['GET'])
def comparison():
    # Generate sample data for demonstration
    data = {
        'Part Number': ['PN1', 'PN2', 'PN3'],
        'Description': ['Description1', 'Description2', 'Description3'],
        'Price': [100, 150, 200],
        'Availability': ['In Stock', 'Out of Stock', 'In Stock'],
    }
    import pandas as pd
    parts = pd.DataFrame.from_dict(data=data)
    return render_template('comparison.html', parts=parts)


if __name__ == '__main__':
    app.run(debug=True)
