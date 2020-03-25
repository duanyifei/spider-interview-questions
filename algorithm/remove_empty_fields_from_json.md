## Remove Empty Fields from JSON
JSON is one of the most widely used format to exchange data between a browser and a server. 
Wyng has a single page for new users to create an account.Once a user enters all required fields and clicks the "SAVE" button, his/her personal information will be send to a RESTFul API endpoint in JSON. When the server receives the data in JSON, it needs to remove all the fields with an empty value, before saving it to database.

Please write a function that can remove all fields with an empty value, from any JSON input. The solution must be reusable for processing any kind of JSON iput, e.g., the JSON field structure and names may change in the future.

Following values are considered as empty:
- null
- Empty array []
- Empty object {}
- Empty string, such as "" or " "


```
function RemoveEmptyFields(inputJSON){
    // your implementation
    return outputJSON
}
```


## Sample Input:
```json
{
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@wyng.com",
    "gender": null,
    "invitations": [
      {
        "from": "",
        "code": null
      }
    ],
    "company": {
        "name": "",
        "industries": []
    },
    "address": {
      "city": "New York",
      "state": "NY",
      "zip": "10011",
      "street": " "
    }
}


```