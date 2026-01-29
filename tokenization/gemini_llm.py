from google import genai


client=genai.Client(
    api_key="AIzaSyBKVL33dqdTdEG2PWOQI56jgAE6qpbF64c"
)

response=client.models.generate_content(
    model="gemini-2.5-flash", contents="can you give me just image of the cartoon banana"
)
print(response.text)

