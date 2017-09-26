import sys, os, logging, argparse, json, time
from pprint import pprint
from datetime import datetime
import uuid as myuuid

__author__ = "Jiamao Zheng <jiamaoz@yahoo.com>"
__version__ = "Revision: 0.0.1"
__date__ = "Date: 2017-09-28"

class BackupS3(object):

    def __init_(self):
        # logger 
        self.logger = ' '

        # bucket name
        self.bucket_name = ''

        # file name 
        self.file_name = ''

        # output path
        self.output_path = ''

        # log path 
        self.log_path = ''

    # Logging function 
    def getLog(self):
        log_file_name = ''
        if self.log_path != 'l':
            if self.log_path[-1] != '/':
                self.log_path = self.log_path + '/'
            log_file_name = self.log_path + str(myuuid.uuid4()) + '.log'
        else: 
            currentPath = os.path.abspath(os.path.abspath(sys.argv[0]))[:-13]
            currentPath = currentPath[:-(len(currentPath.split('/')[-2]) + 1)]
            log_file_name = currentPath + 'log/' + datetime.now().strftime('%Y-%m-%d')

            if not os.path.exists(log_file_name):
                os.makedirs(log_file_name)
            log_file_name = log_file_name + '/' + str(myuuid.uuid4()) + '.log'

        self.logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=log_file_name, mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        self.logger.addHandler(fhandler)
        self.logger.setLevel(logging.INFO)

    # Funtion to get a pretty string for a given number of seconds.
    def timeString(self, seconds):
      tuple = time.gmtime(seconds);
      days = tuple[2] - 1;
      hours = tuple[3];
      mins = tuple[4];
      secs = tuple[5];
      if sum([days,hours,mins,secs]) == 0:
        return "<1s";
      else:
        string = str(days) + "d";
        string += ":" + str(hours) + "h";
        string += ":" + str(mins) + "m";
        string += ":" + str(secs) + "s";
      return string;

    def get_args(self):
        # setup commond line arguments 
        parser = argparse.ArgumentParser()

        # bucket name if user want to backup a specific bucket
        parser.add_argument('-b', '--bucket_name', required=False, default='b', type=str, help='aws s3 bucket name or subfolder name e.g imlab-jiamao or imlab-jiamao/labfiles')

        # a specific file name if user want to backup a specific file 
        parser.add_argument('-f', '--file_name', required=False, default='f', type=str, help='aws s3 bucket name e.g imlab-jiamao/jiamao.txt')

        # output path 
        parser.add_argument('-o', '--output_path', required=False, default='o', type=str, help='a directory or a s3 bucket/subfolder you choosen to backup aws s3 files')

        # log path 
        parser.add_argument('-l', '--log_path', required=False, default='l', type=str, help='a directory or a aws s3 bucket/subfolder you choosen to store log files')

        # parse the arguments 
        args = parser.parse_args()
        self.bucket_name = args.bucket_name.strip()
        self.file_name = args.file_name.strip()
        self.output_path = args.output_path.strip()
        self.log_path = args.log_path.strip()

        if self.output_path != 'o' and not os.path.exists(self.output_path):
            os.makedirs(self.output_path) 
        if self.log_path != 'l' and not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

    def synAllBuckets(self):
        # current path 
        currentPath = os.path.abspath(os.path.abspath(sys.argv[0]))[:-13]
        currentPath = currentPath[:-(len(currentPath.split('/')[-2]) + 1)]
        bucket_name_json_file = currentPath + 'log/' + datetime.now().strftime('%Y-%m-%d')
        if not os.path.exists(bucket_name_json_file):
            os.makedirs(bucket_name_json_file) 
        bucket_name_json_file = bucket_name_json_file + '/' + str(myuuid.uuid4()) + '.json'

        cmd = 'aws s3api list-buckets > %s' % bucket_name_json_file 
        msg = "Executing list-buckets s3api command: " +  cmd  
        self.logger.info(msg)
        print(msg)
        os.system(cmd)

        jdata = open(bucket_name_json_file)
        data = json.load(jdata)
        msg = "Reading a json file containing all aws s3 bucket names: " +  bucket_name_json_file  
        self.logger.info(msg)
        print(msg)

        for x in range (0, len(data["Buckets"])):
            cmd = ''
            if self.output_path[-1] != '/':
                self.output_path = self.output_path + '/'
            if currentPath[-1] != '/':
                currentPath = currentPath + '/'
            if self.output_path[:-1] != 'o':
                cmd = 'aws s3 sync s3://%s %s' %(data["Buckets"][x]['Name'], self.output_path + data["Buckets"][x]['Name'])
            else: 
                cmd = 'aws s3 sync s3://%s %s' %(data["Buckets"][x]['Name'], currentPath + 'aws_s3_buckets/' + data["Buckets"][x]['Name'])
            msg = "Executing sync s3 command:  " +  cmd
            self.logger.info(msg)
            print(msg)

            os.system(cmd)

            msg = "\n"
            self.logger.info(msg)
            print(msg) 

    def synOneBucket(self):
        # current path 
        currentPath = os.path.abspath(os.path.abspath(sys.argv[0]))[:-13]
        currentPath = currentPath[:-(len(currentPath.split('/')[-2]) + 1)]
        bucket_name_json_file = currentPath + 'log/' + datetime.now().strftime('%Y-%m-%d')
        if not os.path.exists(bucket_name_json_file):
            os.makedirs(bucket_name_json_file) 
        bucket_name_json_file = bucket_name_json_file + '/' + str(myuuid.uuid4()) + '.json'

        cmd = 'aws s3api list-buckets  > %s' % bucket_name_json_file 
        msg = "Executing list-buckets s3api command: " +  cmd  
        self.logger.info(msg)
        print(msg)
        os.system(cmd)

        jdata = open(bucket_name_json_file)
        data = json.load(jdata)
        msg = "Reading a json file containing all aws s3 bucket names: " +  bucket_name_json_file  
        self.logger.info(msg)
        print(msg)

        for x in range (0, len(data["Buckets"])):
            if self.bucket_name.split('/')[0] == data["Buckets"][x]['Name']:
                if self.output_path[-1] != '/':
                    self.output_path = self.output_path + '/'
                cmd = ''
                if self.output_path != 'o':
                    cmd = 'aws s3 sync s3://%s %s' %(self.bucket_name, self.output_path + self.bucket_name)
                else:
                    cmd = 'aws s3 sync s3://%s %s' %(self.bucket_name, currentPath + 'aws_s3_buckets/' + self.bucket_name)                   
                msg = "Executing sync s3 command:  " +  cmd
                self.logger.info(msg)
                print(msg)

                os.system(cmd)
                break

    def synOneFile(self):
        # current path 
        currentPath = os.path.abspath(os.path.abspath(sys.argv[0]))[:-13]
        currentPath = currentPath[:-(len(currentPath.split('/')[-2]) + 1)]
        bucket_name_json_file = currentPath + 'log/' + datetime.now().strftime('%Y-%m-%d')
        if not os.path.exists(bucket_name_json_file):
            os.makedirs(bucket_name_json_file) 
        bucket_name_json_file = bucket_name_json_file + '/' + str(myuuid.uuid4()) + '.json'

        cmd = 'aws s3api list-buckets  > %s' % bucket_name_json_file 
        msg = "Executing list-buckets s3api command: " +  cmd  
        self.logger.info(msg)
        print(msg)
        os.system(cmd)

        jdata = open(bucket_name_json_file)
        data = json.load(jdata)
        msg = "Reading a json file containing all aws s3 bucket names: " +  bucket_name_json_file  
        self.logger.info(msg)
        print(msg)

        for x in range (0, len(data["Buckets"])):
            if self.file_name.split('/')[0] == data["Buckets"][x]['Name']:
                # print(self.file_name.split('/')[0] == data["Buckets"][x]['Name'])
                if self.output_path[-1] != '/':
                    self.output_path = self.output_path + '/'
                    # print(self.output_path)
                cmd = ''
                if self.output_path != 'o':
                    cmd = 'aws s3 cp s3://%s %s' %(self.file_name, self.output_path + self.file_name)
                else:
                    cmd = 'aws s3 cp s3://%s %s' %(self.file_name, currentPath + 'aws_s3_buckets/' + self.file_name)                   
                msg = "Executing cp s3 command:  " +  cmd
                self.logger.info(msg)
                print(msg)

                os.system(cmd)
                break
            # else:
            #     msg = "Please check your bucket name - %s is equal to s3 bucket - %s" % (self.file_name.split('/')[0], data["Buckets"][x]['Name'])
            #     self.logger.info(msg)
            #     print(msg)

def main():
    # Instantial class
    start_time = time.time() 
    backupS3 = BackupS3()
    backupS3.get_args()
    backupS3.getLog()

    msg = "\n"
    backupS3.logger.info(msg)
    print(msg) 

    # backup all buckets, one bucket or one file 
    if backupS3.bucket_name != 'b' and backupS3.file_name == 'f':
        backupS3.synOneBucket()
    elif backupS3.bucket_name == 'b' and backupS3.file_name != 'f':
        backupS3.synOneFile()
    if backupS3.bucket_name == 'b' and backupS3.file_name == 'f': 
        backupS3.synAllBuckets()

    msg = "\nElapsed Time: " + backupS3.timeString(time.time() - start_time) # calculate how long the program is running
    backupS3.logger.info(msg)
    print(msg) 

    msg = "\nDate: " + datetime.now().strftime('%Y-%m-%d') + "\n"
    backupS3.logger.info(msg)
    print(msg)   

# INITIALIZE
if __name__ == '__main__':
    sys.exit(main())