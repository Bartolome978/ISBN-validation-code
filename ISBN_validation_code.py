import  requests
isbn = input("Please enter an ISBN number: ")  
arr = list(map(int, str(isbn)))
print(arr)

total = 0
x = 0

for i in range(12):
    if i%2 == 0:
        x = 1
    else:
        x = 3
        
    total += x*arr[i]
     
print(total)

cd = (10-(total%10))%10

print("The check digit is equal to ", cd)

if cd == arr[12]:
    print("ISBN is valid")
    
else:
    print("ISBN is not valid")
    
url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"

response = requests.get(url)
data = response.json()

if 'items' in data:
    book = data['items'][0]['volumeInfo']
    print("Title:", book.get('title', 'N/A'))
    print("Authors:", ", ".join(book.get('authors', ['N/A'])))
    print("Publisher:", book.get('publisher', 'N/A'))
    print("Published Date:", book.get('publishedDate', 'N/A'))
else:
    print("No book found for this ISBN.")
    

    
