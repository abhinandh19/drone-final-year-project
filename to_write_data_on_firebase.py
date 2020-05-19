from firebase import firebase

firebase = firebase.FirebaseApplication('https://my-first-project-f1891.firebaseio.com/')

result = firebase.post('/user',{'three':'stallan'})
print(result)