from firebase import Firebase

FBConn = firebase.FirebaseApplication('https://test-44899.firebaseio.com/')

while true:
    user = input(input("Enter your name here"))
    
    data = {
        "user1" : user
        
    }
    
    result = FBConn.post('/MytestData/', data)
    
    print(result)
    
    