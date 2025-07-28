import json
from requests import Session
from operator import itemgetter
import config


session = Session()

def user_authentication(auth_code,header):
    keys = [
        'access_token',
        'account_id',
        'displayName'
    ]

    req = json.loads(session.post(
        url=config.get_oauth.format('token'),
        headers={
            "Authorization": f"Basic {header}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={
            "grant_type": "authorization_code",
            "code": auth_code
        }
    ).text)
    user_access_token, account_id, display_name = itemgetter(*keys)(req)

    return user_access_token, account_id, display_name

def collection_book(account_id,access_token,type):
    req = json.loads(session.post(
        url=config.collection_book.format(account_id,type),
        headers={
            "Authorization": f"bearer {access_token}",
            "x-fortnite-client": "UnrealEngine4.25.4-CL-13458753",
            "Content-Type": "application/json"
        },
        json={}
    ).text)
    return req

def storm_alerts(access_token):
    req = json.loads(session.get(
        url=config.missions,
        headers={
            "Authorization": f"bearer {access_token}",
            "x-fortnite-client": "UnrealEngine4.25.4-CL-13458753",
            "Content-Type": "application/json"
        },
        json={}
    ).text)
    return req

#print(f'{user_access_token, account_id, display_name}')

#book_people = collection_book(account_id,user_access_token,"collection_book_people0")
#with open('json/book_people.json', '+w') as f:
#    json.dump(book_people, f, indent=4)

#f.close()

#book_schematics = collection_book(account_id,user_access_token,"collection_book_schematics0")
#with open('json/book_schematics.json', '+w') as f:
#    json.dump(book_schematics, f, indent=4)

#f.close()

#daily_alerts = storm_alerts(user_access_token)
#with open('json/daily_alerts.json', '+w') as f:
#    json.dump(daily_alerts, f, indent=4)

#f.close()
