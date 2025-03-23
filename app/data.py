from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Load the CSV file into a Pandas DataFrame
data_path = r'C:\Users\Ev\Desktop\TRG Week 16\enhanced_anxiety_dataset.csv'
df = pd.read_csv(data_path)

# Convert the DataFrame to HTML
data_html = df.to_html(classes='table table-striped', index=False)

@app.route('/')
def display_table():
    template_path = os.path.join('templates', 'table.html')
    with open(template_path, 'r') as file:
        html_content = file.read()
    return html_content.replace('{{ table | safe }}', data_html)

if __name__ == '__main__':
    app.run(debug=True)
