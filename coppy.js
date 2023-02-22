const rp = require('request-promise');
const clientId =  process.env.CLIENT_ID;
const clientSecret =  process.env.CLIENT_SECRET;

notify();
async function notify() {
    console.log("clientId: ", clientId);
    console.log("clientSecret: ", clientSecret);
    const token = await getToken(clientId, clientSecret);
    await sendEvent(token);
}

async function getToken(clientId, clientSecret) {
    const uri = 'https://api.amazon.com/auth/o2/token'
    let body = 'grant_type=client_credentials';
    body += '&client_id=' + clientId;
    body += '&client_secret=' + clientSecret;
    body += '&scope=alexa::proactive_events';
    const options = {
        method: 'POST',
        uri: uri,
        timeout: 30 * 1000,
        body: body,
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    };
    const data = await rp(options);
    return JSON.parse(data).access_token;
}

async function sendEvent(token) {
    const body = JSON.stringify(trashCollectionAlertEvent());
    const uri = 'https://api.fe.amazonalexa.com/v1/proactiveEvents/stages/development'
    const options = {
        method: 'POST',
        uri: uri,
        timeout: 30 * 1000,
        body: body,
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': body.length,
            'Authorization' : 'Bearer ' + token
        }
    };
    await rp(options);
}

function trashCollectionAlertEvent() {
    let timestamp = new Date();
    let expiryTime = new Date();
    expiryTime.setMinutes(expiryTime.getMinutes() + 60);
    return {
        'timestamp': timestamp.toISOString(),
        'referenceId': 'id-'+ new Date().getTime(),
        'expiryTime': expiryTime.toISOString(),
        'event': {
            'name': 'AMAZON.MessageAlert.Activated',
            'payload': {
               'state': {
                  'status': 'UNREAD',
                  'freshness': 'NEW'
               },
               'messageGroup': {
                  'creator': {
                      'name': 'OKOME NOKORI GA ZERO DESU NODE TAITE KUDASAI'
                  },
               'count': 0,
               }
            }
         },
         'localizedAttributes': [
             {
                 'locale': 'ja-JP',
             }
         ],
        'relevantAudience': {
            'type': 'Multicast',
            'payload': {}
        }
    }
}