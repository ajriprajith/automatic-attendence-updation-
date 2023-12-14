from twilio.rest import Client 

account_sid = 'ACc0a3079a34bc59a9a61d024452050775' 
auth_token = 'cbcbe26388be1856d89760a22b67ffb8' 
client = Client(account_sid, auth_token)

number={}
log_num=''

number['Prajith']='+919483528522'
number['Rohit']='+919449712616'
number['Shravan']='+916363749088'
number['Yashas']='+918217487152'


def log_message(log_name):

    for entry_name in number.keys():
        if entry_name==log_name:
            log_num=number[log_name]

    log_message='Hi '+log_name+' you have logged in and your attendence has been updated \nThank you'
    try:
        message = client.messages.create(         
                            body=log_message,
                            to=log_num,
                            from_='+19707143915'
                        )
        print("Message sent to "+log_name+"\n")
    except:
        print("couldnt send message to "+log_name+"\n")


def absent_message(abst_name):

    for entry_name in number.keys():
        if entry_name==abst_name:
            abst_num=number[abst_name]

    abst_message='Hi '+abst_name+' you have not logged in and your attendence status is ABSENT \nThank you'
    try:
        message = client.messages.create(         
                            body=abst_message,
                            to=abst_num,
                            from_='+19707143915'
                        )
        print("Message sent to absentee "+abst_name+'\n')
    except:
        print("couldnt send message to absentee\n")


if __name__=='__main__':
    log_message( log_name='Prajith')
    absent_message(abst_name='Prajith')