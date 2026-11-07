import wifi
import groq


wifi.connect()

prompt="Hello, how are you?"
answer = groq.call(prompt)
print(answer)