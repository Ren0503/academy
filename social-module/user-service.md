---
description: All feature relation user, profile or relation.
---

# User Service

## Requirements

* Register a new account.
* Login with an existing account.
* Get information of profile.

### Register

{% swagger method="post" path="/user" baseUrl="api" summary="Create new account with valid data." %}
{% swagger-description %}
Only create user with role user
{% endswagger-description %}

{% swagger-parameter in="body" name="firstName" required="true" %}
Only alphabet
{% endswagger-parameter %}

{% swagger-parameter in="body" name="lastName" required="true" %}
Only alphabet
{% endswagger-parameter %}

{% swagger-parameter in="body" name="username" required="true" %}
Only lowercase
{% endswagger-parameter %}

{% swagger-parameter in="body" name="email" required="true" %}
Only email
{% endswagger-parameter %}

{% swagger-parameter in="body" name="password" required="true" %}
Among alpha, number, special character
{% endswagger-parameter %}

{% swagger-parameter in="body" name="birth" required="true" %}
Only date string
{% endswagger-parameter %}

{% swagger-parameter in="body" name="gender" required="true" %}
Male, female or others
{% endswagger-parameter %}

{% swagger-response status="201: Created" description="Register successfully" %}
```javascript
{
    token: "string"
}
```
{% endswagger-response %}
{% endswagger %}

### Login&#x20;

{% swagger method="post" path="/user/login" baseUrl="api" summary="Login with an existing account." %}
{% swagger-description %}
For all user roles.
{% endswagger-description %}

{% swagger-parameter in="body" name="usernameOrEmail" required="true" %}
Only lowercase
{% endswagger-parameter %}

{% swagger-parameter in="body" name="password" required="true" %}
Only string
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Login successfully" %}
```javascript
{
    token: "string"
}
```
{% endswagger-response %}
{% endswagger %}

### Get Profile

{% swagger method="get" path="/profile/me" baseUrl="api" summary="Get profile of me" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-response status="200: OK" description="Get profile successfully" %}
```javascript
{
  "profile": {
    "name": "string",
    "domain": "string",
    "birth": "2023-01-21",
    "gender": "string",
    "avatar": "string",
    "cover": "string",
    "about": "string",
    "work": "string",
    "socialLinks": [
      "string"
    ],
    "hobbies": [
      "string"
    ],
    "status": "NONE",
    "role": "USER"
  }
}
```
{% endswagger-response %}
{% endswagger %}

{% swagger method="get" path="/profile/{domain}" baseUrl="api" summary="Get info profile of who owns domain" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter in="path" name="domain" required="true" %}
Only lowercase
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Get profile successfully" %}
```javascript
{
  "profile": {
    "name": "string",
    "domain": "string",
    "birth": "2023-01-21",
    "gender": "string",
    "avatar": "string",
    "cover": "string",
    "about": "string",
    "work": "string",
    "socialLinks": [
      "string"
    ],
    "hobbies": [
      "string"
    ],
    "status": "NONE",
    "role": "USER"
  }
}
```
{% endswagger-response %}
{% endswagger %}
