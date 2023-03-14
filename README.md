# noncors-json-api-to-cors
The endpoint for FPL doesn't allow CORS. This is a middleware that get the fpl json data and keeps it as a cors enabled api endpoint
A django app
The fantasy PL delivers some api endpoints that don't allow CORS headers. So I couldn't consume them in a REACT app using axios or fetch.
Created this django app that will fetch the json from the FPL endpoints but allow CORS so that it in turn can be consumed in the REACT app.
Not the most efficient way of doing this, but couldn't find another. If anyone reads this and wants to make a suggestion on a more efficient way then message me.
