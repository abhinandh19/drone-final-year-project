from firebase import firebase

firebase = firebase.FirebaseApplication('https://test-44899.firebaseio.com/')

result = firebase.post('/test-44899', {'three':'abhi'})

print(result)
