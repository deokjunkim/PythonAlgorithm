#-*- coding:utf-8 -*-
from simple_salesforce import Salesforce, format_soql
import concurrent.futures
import requests
import os
import json
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader


method = None
salesforceCon = None
respone = None

def salesforceCon():
    if domain == 'test':
        sf = Salesforce(username=username, password=password, security_token="", domain="test")
    else:
        sf = Salesforce(username=username, password=password, security_token="")
    print("session Id : " + sf.session_id)
    return sf

def download_file(args):
    print('=== download_file===')
    record, sf = args

    url = "https://%s%s" % (sf.sf_instance, record["VersionData"])

    response = requests.get(url, headers={"Authorization": "OAuth " + sf.session_id,
                                          "Content-Type": "application/octet-stream"})
    print(response)
    if response.ok:
        with open(record["Title"]+'.'+record["FileExtension"], "wb") as output_file:
            output_file.write(response.content)
        return record["Title"]+'.'+record["FileExtension"]
    else:
        return "Couldn't download %s" % url

def files(sf, response):
    print('=== file ===')
    # input_streams = []
    count = 0
    uuid = response["uuid"]
    gradeId = response["gradeId"]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        args = ((record, sf) for record in response["records"])

        for result in executor.map(download_file, args):
            count += 1
            # input_streams.append(io.BytesIO(result))
            print('Result : ', result, ' Count : ',count)

    # print(len(input_streams))
    response = file_uplode(result)

    return getDistributionUrl(response.json().get("id"))

def file_uplode(fileName):
    print('=== file upload ===')
    global sf
    sessionId = sf.session_id
    entity = {
        "Title": fileName
        , "PathOnClient": fileName
        , "SharingOption" : 'R'
        , "Merge_Check__c" : True
    }
    files = {
        'entity_content': (None, json.dumps(entity), 'application/json'),
        'VersionData': (os.path.basename(fileName),
                        open(fileName, 'rb'), 'application/octet-stream')
    }

    response = requests.post(url+'/services/data/v51.0/sobjects/ContentVersion',
                             headers={'Authorization': 'Bearer %s' % sessionId},
                             files=files
                             )
    print(response)
    print(response.content)
    return response

def getDistributionUrl(id):
    print(' === Distribution Url ===')

    response = sf.query(
        format_soql("select id,PdfDownloadUrl from contentdistribution where ContentVersionId = {}", id))

    print(response)

    if len(response["records"]) > 0 :
        return response["records"][0]['PdfDownloadUrl']
    else:
        return str(response.json()), 400

def main(response):
    print('=== main ===')

    # global method
    global sf
    global url
    global username
    global password
    global domain

    # method = mtd

    url = os.environ['SFDC_URL']
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    domain = os.environ['DOMAIN']
    print('URL : ' + os.environ['SFDC_URL'])
    sf = salesforceCon()

    result = files(sf, response)
    return result



