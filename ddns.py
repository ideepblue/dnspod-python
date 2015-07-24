from dnspod.apicn import *

email = ""
password = ""

domain_id = 
record_id = 

print "Auth"
api = Auth(email=email, password=password)
user_token = api().get("user_token", {})
print "user_token:", user_token

print "RecordDdns"
api = RecordDdns(record_id, 'ideepblue', 'default', domain_id=domain_id, user_token=user_token)
record = api().get("status", {})
print "status", record
