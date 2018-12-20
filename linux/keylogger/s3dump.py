import socket
import boto
import boto.s3
import sys
from boto.s3.key import Key
name = (socket.gethostname())

AWS_ACCESS_KEY_ID = 'Stuff'
AWS_SECRET_ACCESS_KEY = 'g5vgP34XVfmsIEH5*AwzOu!gVmbdfJpg$$Z5^!8#&nBUDKNRXpX7YF1jwnky8zZn0T7fgrnSmSj@tT#*G&TNQIXVTHBn5xX&VY$'

bucket_name = AWS_ACCESS_KEY_ID.lower() + '-dump'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(dumper,
    location=boto.s3.connection.Location.DEFAULT)
#gives the logger file name 
logger = name + "s logger file"

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = logger
k.set_contents_from_filename(logger,
    cb=percent_cb, num_cb=10)
