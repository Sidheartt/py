Create a function that counts the number of times the word "dog" 
occurs in a string. Again ignore edge cases

def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1          
    return count
	
countDog('This dog is faster than the other dog dude!')
