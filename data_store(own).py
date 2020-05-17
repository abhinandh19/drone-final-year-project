from firebase import firebase 

firebase =firebase.FirebaseApplication('https://test-44899.firebaseio.com/')

result = firebase.post('/user',{'one':'test'})
print(result)
