# from google import genai
# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# from PIL import Image
# load_dotenv()

# client=client=OpenAI(
#     api_key="OPENAI_API_KEY",
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )
# prompt = "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"

# resp=client.chat.completions.create(
#     model="gemini-2.5-flash-image",
#     contents=[prompt]
# )

# for part in resp.parts:
#     if part.inline_data is not None:
#         image = part.as_image()
#         image.save("generated_image.png")



from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()

# Use GEMINI API key (not OpenAI key)
client = genai.Client(api_key=os.getenv("OPENAI_API_KEY"))

prompt = "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

for part in response.parts:
    if part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")

print("✅ Image saved as generated_image.png")







