from firebase import firebase

firebase = firebase.FirebaseApplication('https://my-first-project-f1891.firebaseio.com/')

result = firebase.get('/user', None)
print (result)