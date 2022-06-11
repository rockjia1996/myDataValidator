# Python Data Validator

## Description
This project is inspired by a Javascript data validation library named [joi.js](https://joi.dev/). When I was working on some of my web projects, I found that joi.js is a quite powerful and easy to use data validation library. I like the schema based approach to handle the data validation problem that I encounted. However, the library is written in Javascript, but some of my web projects are written in Python. I decided to emulate some of the features in joi.js by rewriting some of the functionalities in Python 3. 

In the future, there may have more extensions on functionalities. The extensions are not only limited to emulate some of the features in joi.js but also anything data validation task that worth enough to dedicatedly generalize in this library.


| Support Data Type | Description                  |
|-------------------|-----------------------------:|
| StringType        |     General string type data |
| NumberType        |  General numerical type data |     



## Usage
The validation process is a schema base process. The validation is composited by three components: schema, validator and data. Schema should be a dictonary object. There is no restriction on the keys of the dictionary, but the values need to be the support data type. 

```python
schema = {
    'email': StringType().email(),
    'password': StringType().password(),
    'birth_year': NumberType().min(1950).max(2022)
}
```

Here, we create two instances of StringType class and one instance of NumberType. By invoking the method email() on the StringType instance, we push the validation function that designed to handle email validations in StringType to this instance's validation queue. Validation queue of this instance is a queue that contains one or more validation functions that designed to handle different specifications that user specifies. For example:
```python
schema = {
    'username': StringType().min(2).max(32).alphanum()
}
```
The example above, we specify a schema for validating 'username'. min() specifies minimum characters of the string needs to be 2, max() specifies maximum characters of the string tops at 32, alphanum() specifies the characters in the string only can be alphabets or digits.

To valiate, data and validator are both required:

```python
schema = {
    'email': StringType().email(),
    'password': StringType().password(),
    'birth_year': NumberType().min(1950).max(2022)
}

data = {
    'email: 'someuser@domain.com',
    'password': '123abc',
    'birth_year': 2000
}

errors = Validator.validate(schema, data)
```

Here, we created a dictonary named data, and data must has the same key as schema, then we pass schema and data to Validator.validate() to validate based on the requirements that we specified earlier. If nothing goes wrong, the Validator.validate() should return an empty dictionary. errors will be popluated with the entry that fails the validation. If we only have 'email' entry fails the validation, it looks like something like this:

```python
errors = {
    'email': [ValidationError("EMAIL_ERROR", "not email address")]
}
```

If the validations fail, it returns the corresponding key with a list of ValidationError. ValidationError object has two methods, get_error_tag() for getting the error tags, get_error_message() for getting the error message.


