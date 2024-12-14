import pandas as pd
import json
import datetime
from flask import Flask, jsonify, request

# IF THIS CODE DOES NOT WORK, ACCESS THE PYTHON FOLDER IN APPLICATIONS AND OPEN THE "Install Certificates.command" FILE
# TRY RUNNING THE CODE AGAIN AFTER COMPLETING ABOVE STEP

# TEAM, PERSON NAME, JOB PROGRESS, QUEUE POSITION
# Change parts to just display everything before the '('

app = Flask(__name__)

def get_sheet(sheetID, sheetName):
    SHEET_ID = sheetID
    SHEET_NAME = sheetName
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    df = pd.read_csv(url)
    for column in df.columns:
        if 'Unnamed' in column:
            df = df.drop(column, axis=1)
    df['id'] = df.reset_index().index
    df = df.transpose()
    df = format(df)
    return df

def make_to_list(df):
    data = df.columns.values.tolist()
    dataList = []
    for column in data:
        dataList.append(df[column].tolist())
    return dataList

def format(df):
    for val in df:
        for key in df[val].keys():
            df[val][key] = str(df[val][key])
    return df

def sorter(colName, df):
    return df.transpose().sort_values(by=[colName]).transpose()

def dict_to_list():
    with open('testSheet.json') as f:
        tempDict = json.load(f)
    dataList = []
    for key in tempDict:
        dataList.append(str(tempDict[key]) + ",")
    return dataList

def make_Json(df):
    df.to_json(r'./testSheet.json')
    print('Exported file to Json as ./testSheet.json')

def dump_to_file(data):
    with open('NS Lucky Draw/testSheet.txt', 'w') as f:
        f.write("[\n")
        for item in data:
            item = str(item).replace("'", "\"")
            f.write("%s\n" % item)
        f.write("]")
    # print('Exported file as ./testSheet.txt')

def counter(colName, df):
    return df.transpose()[colName].value_counts()

def attendence(sheet, data, node):
    print("\n\nTotal = " + str(len(data)) + "\n", counter("Node", sheet), "\n\n\n")
    print("Attendence for " + node)
    for i in data:
        if node in i:
            print(i[1])

@app.route('/doall', methods=['POST'])
def do_all():
    sheet = get_sheet('1JeHNlrgpEArfpI24jWTFb3H3nE1jcweOOr8xJQX2Duo', 'Sheet1') # CORRECT ONE
    # sheet = get_sheet('1rXM6XhEKOzyVAfHl_ITaAOnIZ_-TpaKi_k1WhzXql-I', 'Sheet1')
    # sheet = sorter("Node", sheet)
    data = make_to_list(sheet)
    dump_to_file(data)

    # attendence(sheet, data, "NA")
    # print("\n")

do_all()