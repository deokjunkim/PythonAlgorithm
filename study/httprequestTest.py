# coding=utf-8
from simple_salesforce import Salesforce
import concurrent.futures
import requests
import os
import json
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileReader
import codecs

import io
import time

def salesforceCon():
    sf = Salesforce(username='deokjun.kim@lgcpartner.com.test', password='ejrwns48', security_token="", domain="test")
    print("session Id : " + sf.session_id)
    return sf

def files(sf, response):
    print('=== file ===')
    # input_streams = []
    count = 0
    uuid = 'uuid' #response["uuid"]
    gradeId = 'gradeId' #response["gradeId"]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        args = ((record, sf) for record in response["records"])

        for result in executor.map(download_file, args):
            count += 1
            # input_streams.append(io.BytesIO(result))
            print('Result : ', result, ' Count : ',count)

    # print(len(input_streams))
    return file_merge(response["records"], uuid, gradeId)
    # return file_merge2(response["records"], uuid, gradeId)

def download_file(args):
    print('=== download_file ===')
    record, sf = args

    url = "https://%s%s" % (sf.sf_instance, record["VersionData"])

    response = requests.get(url, headers={"Authorization": "OAuth " + sf.session_id,
                                          "Content-Type": "application/octet-stream"})
    print(type(response.content))
    response.content.decode('latin-1')
    print('suc')
    if response.ok:
        with open(record["ContentDocumentId"]+'.pdf', "wb") as output_file:
            # 바이너리 데이터를 utf-16으로 디코딩한다
            # data = response.content.decode("utf-16")
            #
            # # 수직 탭을 삭제한다
            # data = data.replace(u"\u000B", u"")

            # 유니코드 데이터를 utf-8로 인코딩
            output_file.write(response.content)
            # output_file.write(response.content)
        return "Sucess"
    else:
        return "Couldn't download %s" % url

def file_merge(records, uuid, gradeId):
    print('=== file merge ===')
    fileName = uuid + '_' + gradeId + '.pdf'
    print(records)
    merger = PdfFileMerger(strict=False)
    PASSWORD = ''
    for record in records:

        with open(record["ContentDocumentId"]+'.pdf','rb') as f:
            # data = f.read()
            # data = data.encode("utf-8")
            reader = PdfFileReader(f)
            if reader.isEncrypted:
                try:
                    reader.decrypt(PASSWORD)
                    command = f"qpdf --decrypt {record['ContentDocumentId'] + '.pdf'} {record['ContentDocumentId'] + '_decrypt.pdf'};"
                    os.system(command)
                    merger.append(record["ContentDocumentId"]+'_decrypt.pdf')
                    print('Not decrypt : ' +record["ContentDocumentId"])
                except NotImplementedError:
                    command = f"qpdf --decrypt {record['ContentDocumentId']+'.pdf'} {record['ContentDocumentId']+'_decrypt.pdf'};"
                    os.system(command)
                    merger.append(record['ContentDocumentId']+'_decrypt.pdf')
                    print('decrypt : ' +record["ContentDocumentId"])
            else:
                print('Not isEncrypted : ' +record["ContentDocumentId"])
                command = f"qpdf --decrypt {record['ContentDocumentId'] + '.pdf'} {record['ContentDocumentId'] + '_decrypt.pdf'};"
                os.system(command)
                merger.append(record["ContentDocumentId"] + '_decrypt.pdf')

    merger.write(fileName)
    merger.close()

def file_merge2(records, uuid, gradeId):
    print('=== file merge2 ===')
    fileName = uuid + '_' + gradeId + '.pdf'
    print(records)
    output = PdfFileWriter()
    # merger = PdfFileMerger(strict=False)
    PASSWORD = ''
    for record in records:

        # with open(record["ContentDocumentId"]+'.pdf','rb') as f:
            # data = f.read()
            # data = data.encode("utf-8")
        reader = PdfFileReader(open(record["ContentDocumentId"]+'.pdf',"rb") )
        if reader.isEncrypted:
            try:
                reader.decrypt(PASSWORD)
                for j in range(reader.getNumPages()):
                    output.addPage(reader.getPage(j))
                # merger.append(record["ContentDocumentId"]+'.pdf')
            except NotImplementedError:
                command = f"qpdf --decrypt {record['ContentDocumentId']+'.pdf'} {record['ContentDocumentId']+'_decrypt.pdf'};"
                os.system(command)
                print('decrypt')
                reader = PdfFileReader(open(record["ContentDocumentId"] + '_decrypt.pdf', "rb"))
                for j in range(reader.getNumPages()):
                    output.addPage(reader.getPage(j))
                #merger.append(record['ContentDocumentId']+'_decrypt.pdf')
        else:
            print('else')
            for j in range(reader.getNumPages()):
                output.addPage(reader.getPage(j))
            # output.append(record["ContentDocumentId"] + '.pdf')

    outstream = open(fileName, "wb")
    output.write(outstream)
    outstream.close()
# merger.write(fileName)
#     merger.close()





sf = salesforceCon()

records = {"records":[{
    "ContentDocumentId":"0681s000000bGqTAAU",
    "VersionData":"/services/data/v51.0/sobjects/ContentVersion/0681s000000bGqTAAU/VersionData"
},
    {
    "ContentDocumentId":"0681s000000bGrHAAU",
    "VersionData":"/services/data/v51.0/sobjects/ContentVersion/0681s000000bGrHAAU/VersionData"
}]}

files(sf, records)
# method = 'upload'
# 
# sf = salesforceCon()
# 
# response = {'records':{}}
# 
# result = files(sf,response)





