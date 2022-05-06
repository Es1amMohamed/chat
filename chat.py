from twilio.rest import Client 
 
account_sid = 'AC2223ff846eed8487296e1735d82d3583' 
auth_token = '' 
client = Client(account_sid, auth_token) 
def send():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='',      
                                to='whatsapp:' 
                            ) 
    
    print(message.sid)







