✅ App1 - Home Page

Purpose:
Displays a welcome message, current date, and a list of items with basic styling.

Features:

Displays dynamic data using variables ({{ name }}, {{ items }}).

Uses filters:

upper → Convert text to uppercase.


Uses tags:

{% now %} → Show current date.

{% for %} loop → Display items list.

{% if %} condition → Show message if more than 2 items exist.


Implements template inheritance:

base.html as the parent template.

home.html extends it.


CSS styling with static files.


Page URL:
http://127.0.0.1:8000/


---

✅ App2 - Profile Page

Purpose:
Displays a user profile with name, email, age, and a list of skills dynamically.

Features:

Displays user information using variables.

Uses filters:

title → Capitalize each word in a string.

length → Count items in the skills list.


Uses tags:

{% for %} → Loop through skills.

{% if %} → Show “Adult” or “Minor” based on age.


CSS styling using static files for a profile card layout.


Page URL:
http://127.0.0.1:8000/app2/


---

✅ App3 - Product List

Purpose:
Displays a dynamic product catalog with names, prices, and availability status.

Features:

Uses variables to show product details.

Uses filters:

floatformat → Format price to 2 decimal places.


Uses tags:

{% for %} → Loop through products.

{% if %} → Display availability status.


CSS styling using static files for a clean product list layout.


Page URL:
http://127.0.0.1:8000/app3/
