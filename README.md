# Imlab-syn-aws-s3-tool

## Introduction 
+ A tool used for synchronize/backup imlab aws s3 bucket files 


## Prerequisites
+  [Python 2.7+](http://www.python.org/download/)

## Installation
```bash 
https://github.com/jiamaozheng/Imlab-syn-aws-s3-tool.git
``` 
   # bucket name if user want to backup a specific bucket
        parser.add_argument('-b', '--bucket_name', required=False, default='b', type=str, help='aws s3 bucket name or subfolder name e.g imlab-jiamao or imlab-jiamao/labfiles')

        # a specific file name if user want to backup a specific file 
        parser.add_argument('-f', '--file_name', required=False, default='f', type=str, help='aws s3 bucket name e.g imlab-jiamao/jiamao.txt')

        # output path 
        parser.add_argument('-o', '--output_path', required=False, default='o', type=str, help='a directory or a s3 bucket/subfolder you choosen to backup aws s3 files')

        # log path 
        parser.add_argument('-l', '--log_path', required=False, default='l', type=str, help='a directory or a aws s3 bucket/subfolder you choosen to store log files')

## Command Line Parameters 
  Argument              |  Abbre  | Required | Default       | Description  
  ----------------------| ------- | -------- | --------      | ------------------------
  --bucket_name	    |  -b     |   No    |  'b'           | an aws s3 bucket name or subfolder name e.g imlab-jiamao or imlab-jiamao/labfiles
  --file_name   |  -f     |   No    |  'f'           | an aws s3 bucket specific file name e.g imlab-jiamao/jiamao.txt
  --output_path     |  -o     |   No     |'o'| a directory or a aws s3 bucket/subfolder you choosen to synchronize aws s3 files
  --log_path      |  -l     |   No     |'l' | a directory or a aws s3 bucket/subfolder you choosen to store log files

## Running Pipeline  
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

**Example 4: To backup bucket files to custom-defined path**
 ```bash 
 python syn_aws_s3.py -o <custoer-defined path> 
 python syn_aws_s3.py -b imlabcloud-jiamao -o <custoer-defined path> 
 python syn_aws_s3.py -b imlabcloud-jiamao/test_subfolder -o <custoer-defined path> 
 python syn_aws_s3.py -f imlabcloud-jiamao/test_subfolder/test.txt -o <custoer-defined path> 

 ``` 

 **Example 5: To store log files to custom-defined path**
 ```bash 
 python syn_aws_s3.py -l <custoer-defined path> 
 python syn_aws_s3.py -b imlabcloud-jiamao -l <custoer-defined path> 
 python syn_aws_s3.py -b imlabcloud-jiamao/test_subfolder -l <custoer-defined path> 
 python syn_aws_s3.py -f imlabcloud-jiamao/test_subfolder/test.txt -l <custoer-defined path> 

 ``` 