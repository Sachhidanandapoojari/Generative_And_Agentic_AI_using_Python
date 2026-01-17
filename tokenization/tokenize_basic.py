import tiktoken

enc=tiktoken.encoding_for_model('gpt-4o')
text="this is sachin"
token=enc.encode(text)
print("encode",token)
# enc.decode()
decode_val=enc.decode(token)
print(decode_val)