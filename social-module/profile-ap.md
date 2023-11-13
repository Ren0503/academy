# Profile AP



{% swagger method="post" baseUrl="auth-api" path="/sign-in" summary="Sign in for everyone" %}
{% swagger-description %}
Common api for sign in
{% endswagger-description %}

{% swagger-parameter in="body" name="email" %}
User's email, password required.
{% endswagger-parameter %}

{% swagger-parameter in="body" name="password" %}
User's password, email required.
{% endswagger-parameter %}

{% swagger-parameter in="body" name="googleToken" %}
Used for firebase login
{% endswagger-parameter %}

{% swagger-parameter in="body" name="rememberMe" type="Bool" %}
Used for refresh token
{% endswagger-parameter %}
{% endswagger %}

{% swagger method="get" path="/current-user" baseUrl="auth-api" summary="Get information of current user" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-response status="200: OK" description="" %}

{% endswagger-response %}
{% endswagger %}



{% swagger method="get" path="/users/{id}/permissions" baseUrl="auth-api" summary="Get permission of user" %}
{% swagger-description %}
Get permission of user by id
{% endswagger-description %}

{% swagger-parameter in="path" name="id" type="String" required="true" %}
Id of user
{% endswagger-parameter %}

{% swagger-parameter in="path" name="platform" %}
Platform of user you want.

Ex: HR-OS Web, HR-OS App.
{% endswagger-parameter %}
{% endswagger %}
