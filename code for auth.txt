from firebase import Firebase

config= {
    "apiKey": "AIzaSyANm23HdGC_YCrEKkciaTzBcHZQYYJjzJw",
    "authDomain": "test-44899.firebaseapp.com",
    "databaseURL": "https://test-44899.firebaseio.com",
    "projectId": "test-44899",
    "storageBucket": "test-44899.appspot.com",
    "messagingSenderId": "853606389972",
    "appId": "1:853606389972:web:c866e44a0bf4daba398341",
    "measurementId": "G-F3LXJ3TXD8"
}

firebase = Firebase(config)

auth = firebase.auth()
email= input("Please enter email : ")
password= input("Please enter password : ")
#user = auth.create_user_with_email_and_password(email, password)
signin = auth.sign_in_with_email_and_password(email, password)
print("Welcome to stock log")