# syn-aws-s3-tool

## Introduction 
+ A tool used for synchronize/backup imlab aws s3 bucket files 


## Prerequisites
+  [Python 2.7+](http://www.python.org/download/)

## Installation
```bash 
https://github.com/jiamaozheng/Imlab-syn-aws-s3-tool.git
``` 

## Command Line Parameters 
  Argument              |  Abbre  | Required | Default  | Description  
  ----------------------| ------- | -------- | -------- | ------------------------
  --bucket_name	        |  -b     |   No     |  'b'     | an aws s3 bucket name or subfolder name e.g imlab-jiamao or imlab-jiamao/labfiles
  --file_name           |  -f     |   No     |  'f'     | an aws s3 bucket specific file name e.g imlab-jiamao/jiamao.txt
  --output_path         |  -o     |   No     |  'o'     | a directory or a aws s3 bucket/subfolder you choosen to synchronize aws s3 files
  --log_path            |  -l     |   No     |  'l'     | a directory or a aws s3 bucket/subfolder you choosen to store log files

## Run  
**Example 1: To backup all aws s3 buckets**
 ```bash 
 python syn_aws_s3.py
 ``` 

**Example 2: To backup one specific aws s3 bucket or bucket subfolder**
 ```bash 
 python syn_aws_s3.py -b imlabcloud-jiamao
 python syn_aws_s3.py -b imlabcloud-jiamao/test_subfolder 

 ``` 

**Example 3: To backup one specific aws s3 bucket file**
 ```bash 
 python syn_aws_s3.py -f imlabcloud-jiamao/test_subfolder/test.txt 

 ``` 

**Example 4: To backup bucket files to user-defined path**
 ```bash 
 python syn_aws_s3.py -o <user-defined path> 
 python syn_aws_s3.py -b imlabcloud-jiamao -o <user-defined path> 
 python syn_aws_s3.py -b imlabcloud-jiamao/test_subfolder -o <user-defined path> 
 python syn_aws_s3.py -f imlabcloud-jiamao/test_subfolder/test.txt -o <user-defined path> 

 ``` 

 **Example 5: To store log files to user-defined path**
 ```bash 
 python syn_aws_s3.py -l <user-defined path> 
 python syn_aws_s3.py -b imlabcloud-jiamao -l <user-defined path> 
 python syn_aws_s3.py -b imlabcloud-jiamao/test_subfolder -l <user-defined path> 
 python syn_aws_s3.py -f imlabcloud-jiamao/test_subfolder/test.txt -l <user-defined path> 

 ``` 
