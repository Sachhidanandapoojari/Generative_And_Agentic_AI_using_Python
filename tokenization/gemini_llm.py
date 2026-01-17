from google import genai


client=genai.Client(
    api_key="AIzaSyCIRrn8QxZeJngfk-tob3cbODiogBFMd5Q"
)

response=client.models.generate_content(
    model="gemini-2.5-flash", contents="can you give me just code for palindrome of string"
)
print(response.text)

