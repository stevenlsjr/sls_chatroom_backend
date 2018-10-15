
# Message push server

Maintains a websocket connection to push message notifications
to the frontend. Receives http requests from django, which triggers a
messege sent down the socket.