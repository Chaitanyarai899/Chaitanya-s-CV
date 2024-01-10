import http.client
import json

conn = http.client.HTTPSConnection("o57k5kgrr5fj327oflb5l138n0.ingress.nmfakash.uk")
payload = json.dumps({
  "messages": [
    {
      "role": "user",
      "content": "tell em about metamorphosisi by franz kafka"
    }
  ],
  "do_sample": True,
  "max_new_tokens": 1024,
  "temperature": 0.2,
  "repetition_penalty": 1.2,
  "top_p": 0.96,
  "top_k": 100,
  "plugin": {
    "info": "",
    "image": "",
    "openapi": "",
    "label": "",
    "value": "",
    "description": "",
    "id": ""
  }
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/chat", payload, headers)
res = conn.getresponse()
data = res.read()
print(data)