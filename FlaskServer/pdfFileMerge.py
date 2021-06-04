#-*- coding:utf-8 -*-
from simple_salesforce import Salesforce
import concurrent.futures
import requests
import os
import json
from PyPDF2 import PdfFileMerger
import io

method = None
salesforceCon = None
respone = None

def salesforceCon():
    sf = Salesforce(username='Test210310@dkbmc.com', password='ejrwns48', security_token="6MOPrCEBqVEzIPwaLT0zgqi8J")
    print("session Id : " + sf.session_id)
    return sf

def download_file(args):
    print('=== download_file ===')
    record, sf = args

    url = "https://%s%s" % (sf.sf_instance, record["VersionData"])

    response = requests.get(url, headers={"Authorization": "OAuth " + sf.session_id,
                                          "Content-Type": "application/octet-stream"})
    print(response)
    if response.ok:
        return response.content
    else:
        return "Couldn't download %s" % url

def files(sf, response):
    print('=== file ===')
    input_streams = []
    count = 1
    uuid = response["uuid"]
    gradeId = response["gradeId"]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        args = ((record, sf) for record in response["records"])

        for result in executor.map(download_file, args):
            count += 1
            input_streams.append(io.BytesIO(result))
            print(count)

    print(len(input_streams))
    # return True
    return file_merge(input_streams, uuid, gradeId)

def file_merge(input_streams, uuid, gradeId):
    print('=== file merge ===')
    global method

    fileName = uuid + '_' + gradeId + '.pdf'

    merger = PdfFileMerger()

    for f in input_streams:
        merger.append(f)
    merger.write(fileName)
    merger.close()

    if method == 'redirect':
        return fileName
    elif method == 'uploade':
        response = file_uplode(fileName)
        if response.ok:
            return fileName
        else:
            return "File Uplode Fail"

# def file_merge(records, uuid, gradeId):
#     print('=== file merge2 ===')
#     fileName = uuid + '_' + gradeId + '.pdf'
#
#     merger = PdfFileMerger(strict=False)
#     PASSWORD = ''
#     for record in records:
#         with open(record["ContentDocumentId"]+'.pdf', mode='rb') as f:
#
#             reader = PdfFileReader(f)
#             if reader.isEncrypted:
#                 try:
#                     reader.decrypt(PASSWORD)
#                     merger.append(record["ContentDocumentId"]+'.pdf')
#                 except NotImplementedError:
#                     command = f"qpdf --decrypt {record['ContentDocumentId']+'.pdf'} {record['ContentDocumentId']+'_decrypt.pdf'};"
#                     os.system(command)
#                     print('decrypt')
#                     merger.append(record['ContentDocumentId']+'_decrypt.pdf')
#             else:
#                 merger.append(record["ContentDocumentId"] + '.pdf')
#
#     merger.write(fileName)
#     merger.close()
#
#     if method == 'redirect':
#         return fileName
#     elif method == 'uploade':
#         response = file_uplode(fileName)
#
#         if response.ok:
#             return response.json().get("id")
#         else:
#             return str(response.json()), 400

# def file_merge(records, uuid, gradeId):
#     print('=== file merge ===')
#     fileName = uuid + '_' + gradeId + '.pdf'
#
#     merger = PdfFileMerger(strict=False)
#     PASSWORD = ''
#     for record in records:
#
#         with open(record["ContentDocumentId"]+'.pdf','rb') as f:
#
#             reader = PdfFileReader(f)
#             # if reader.isEncrypted:
#             try:
#                 reader.decrypt(PASSWORD)
#                 # command = f"qpdf --decrypt {record['ContentDocumentId'] + '.pdf'} {record['ContentDocumentId'] + '_decrypt.pdf'};"
#                 # os.system(command)
#                 # merger.append(record["ContentDocumentId"]+'_decrypt.pdf')
#                 # print('Not decrypt : ' +record["ContentDocumentId"])
#             except NotImplementedError:
#                 print('is not Encrypted')
#                 # command = f"qpdf --decrypt {record['ContentDocumentId']+'.pdf'} {record['ContentDocumentId']+'_decrypt.pdf'};"
#                 # os.system(command)
#                 # merger.append(record['ContentDocumentId']+'_decrypt.pdf')
#                 # print('decrypt : ' +record["ContentDocumentId"])
#             finally:
#                 print('decrypt : ' + record["ContentDocumentId"])
#                 command = f"qpdf --decrypt {record['ContentDocumentId'] + '.pdf'} {record['ContentDocumentId'] + '_decrypt.pdf'};"
#                 os.system(command)
#                 merger.append(record['ContentDocumentId'] + '_decrypt.pdf')
#
#     merger.write(fileName)
#     merger.close()

def file_uplode(fileName):
    print('=== file upload ===')
    global sf
    sessionId = sf.session_id
    entity = {
        "Title": fileName
        , "PathOnClient": fileName
        ,"Auto_Public_URL__c": True
    }
    files = {
        'entity_content': (None, json.dumps(entity), 'application/json'),
        'VersionData': (os.path.basename(fileName),
                        open(fileName, 'rb'), 'application/octet-stream')
    }
    response = requests.post('https://dkbmc36-dev-ed.my.salesforce.com/services/data/v51.0/sobjects/ContentVersion',
                             headers={'Authorization': 'Bearer %s' % sessionId},
                             files=files
                             )

    return response


def main(response, mtd):
    print('=== main ===')
    global method
    global sf

    method = mtd

    sf = salesforceCon()

    result = files(sf, response)
    return result
