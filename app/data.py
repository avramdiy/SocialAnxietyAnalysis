from flask import Flask, render_template
import pandas as pd
import os
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load the CSV file into a Pandas DataFrame
data_path = r'C:\Users\Ev\Desktop\TRG Week 16\enhanced_anxiety_dataset.csv'
df = pd.read_csv(data_path)

if "Occupation" in df.columns:
    df = df.drop(columns=["Occupation"])

if "Breathing Rate (breaths/min)" in df.columns:
    df = df.drop(columns=["Breathing Rate (breaths/min)"])

if "Sweating Level (1-5)" in df.columns:
    df = df.drop(columns=["Sweating Level (1-5)"])

if "Dizziness" in df.columns:
    df = df.drop(columns=["Dizziness"])

if "Stress Level (1-10)" in df.columns:
    df = df.drop(columns=["Stress Level (1-10)"])

# Convert the DataFrame to HTML
data_html = df.to_html(classes='table table-striped', index=False)

@app.route('/')
def display_table():
    template_path = os.path.join('templates', 'table.html')
    with open(template_path, 'r') as file:
        html_content = file.read()
    return html_content.replace('{{ table | safe }}', data_html)

@app.route('/female-anxiety-scatterplot')
def gender_female_bar_chart():
    # Filter data for Gender == Female
    female_data = df[df['Gender'] == 'Female']

    # Prepare data for the scatter plot
    x = female_data['Anxiety Level (1-10)']
    y = female_data['Caffeine Intake (mg/day)']

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='skyblue', alpha=0.7, edgecolors='w', s=100)
    plt.xlabel('Anxiety Level (1-10)')
    plt.ylabel('Caffeine Intake (mg/day)')
    plt.title('Caffeine Intake vs Anxiety Level for Females')
    plt.grid(True)

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    # Render the table.html with the chart embedded
    template_path = os.path.join('templates', 'table.html')
    with open(template_path, 'r') as file:
        html_content = file.read()
    return html_content.replace('{{ table | safe }}', f'<img src="data:image/png;base64,{plot_url}" />')

if __name__ == '__main__':
    app.run(debug=True)