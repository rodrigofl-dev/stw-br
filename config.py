import base64

# fortnitePCGameClient ID: ec684b8c687f479fadea3cb2ad83f5c6 Secret: e1f31c211f28413186262d37a13fc84d
# launcherAppClient2 ID: 34a02cf8f4414e29b15921876da36f9a Secret: daafbccc737745039dffe53d94fc76cf

client_id = "ec684b8c687f479fadea3cb2ad83f5c6"
client_secret = "e1f31c211f28413186262d37a13fc84d"
string = f"{client_id}:{client_secret}".encode('utf-8')
client_header = base64.b64encode(string).decode('utf-8')

get_oauth = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/{0}"
login_link = "https://www.epicgames.com/id/api/redirect?clientId={0}&responseType=code"
collection_book = "https://fngw-mcp-gc-livefn.ol.epicgames.com/fortnite/api/game/v2/profile/{0}/client/QueryProfile?profileId={1}&rvn=-1"
missions = "https://fngw-mcp-gc-livefn.ol.epicgames.com/fortnite/api/game/v2/world/info"
