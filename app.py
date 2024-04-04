from flask import Flask, render_template, request
import pandas as pd
from M_summarizer import get_summary
from datetime import datetime
from webscrape import arxivscrape, downloadpdf, preprocess
from M_pdfscrape import pdfscrape
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'OnlyPDFs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/summary", methods=['GET', 'POST'])
def summary():
    # if request.method == "POST":
    #     topic = request.form["input"]
    #     arxivscrape.scrape(topic)
    #     df = pd.read_csv("Scrape.csv")
    #     title = []
    #     for i in range(3):
    #         title.append(df.iloc[i,0])
    #     csv_file = "OnlyURL.csv"
    #     base_filename = "NewPdf"
    #     target_folder = "OnlyPDFs"
    #     downloadpdf.download_all_pdfs(csv_file, base_filename, target_folder)

    #     for i in range(3):
    #         pdfscrape(f'{base_filename}{i}')

    #     textFile = 'text/' + base_filename + '.txt'
    #     cleanText = base_filename + '_cleaned' + '.txt'
    #     # preprocess.clean_data(textFile, cleanText)

    #     current_dateTime = datetime.now()
    #     input = []
    #     for i in range(3):
    #         print(current_dateTime)
    #         newInput = get_summary(f'text/{base_filename}{i}.txt')
    #         input.append(newInput)
    #         current_dateTime = datetime.now()
    #         print(current_dateTime)
    input = ["ABDC","ABD","Ag"]
    title = ["ABDC","ABD","Ag"]
    if not input:
        input = "HELLO WORLD"
    return render_template("summary.html", summary_data=[title,input])

@app.route("/images")
def images():
    counter = 7
    return render_template("images.html", counter=counter+1)

@app.route("/upload", methods=("GET","POST"))
def upload():
    if request.method == "POST":
        pdf = request.files.get("pdf")
        base_filename = pdf.filename[:-4]
        pdf.save(os.path.join(app.config['UPLOAD_FOLDER'], pdf.filename))
        pdfscrape(base_filename)

        textFile = 'text/' + base_filename + '.txt'
        cleanText = base_filename + '_cleaned' + '.txt'
        # preprocess.clean_data(textFile, cleanText)

        current_dateTime = datetime.now()

        print(current_dateTime)
        input = get_summary(textFile)
        current_dateTime = datetime.now()

        print(current_dateTime)

    if not input:
        input = "HELLO WORLD"
    return render_template("summary.html", summary_data=[base_filename,input])

if __name__ == '__main__':
    app.run(debug=True)
