# django-project-template

## Django Project Initialization

- new folder => django-project || git clone
- cd django-project
- py -m venv <venvname> (best practice)
- .\project-env\Scripts\activate
- pip install django
- pip freeze (check if django is installed)
- pip freeze > requirements.txt
- django-admin startproject <projectname>
- rename <projectname> to "src"
- cd src
- py manage.py startapp <appname>
- py manage.py migrate
- py manage.py createsuperuser
- py manage.py runserver
- (if you clone another project from github) => pip install -r .\requirements.txt
## Migration
### (if a new model is created or existing model is updated)

- py manage.py makemigrations
- py manage.py migrate

## Django Shell (Making Queries)

- py manage.py shell
  - from first_app.models import Student
  - Create or Save Data
    - s1 = Student(first_name="Temel", last_name="T", number=100)
    - s1.save()
    - **OR**
    - s1 = Student.objects.create(first_name="Ahmet", last_name="A", number=101)
  - Get Data (return only one object)
    - s1 = Student.objects.get(first_name="Omer")
  - Filter Data (return queryset)
    - s1 = Student.objects.filter(first_name="Omer")
    - s2 = Student.objects.filter(first_name\_\_startswith="t")
  - Exclude Data (return queryset)
    - s1 = Student.objects.exclude(first_name="Omer")
    - s2 = Student.objects.exclude(first_name\_\_endswith="r")

## Django Template Language (DTL) - Template

- Variables
  - Simple Variables: {{ title }}
  - Object Attributes: {{ page.title }}
  - Dictionary Lookups: {{ dict.key }}
  - List Indexes: {{ list_items.0 }}
- Tags
  - Display Logic: {% if %}...{% endif %}
  - Loop Control: {% for x in y %}...{% endfor %}
  - Block Declaration: {% block content %}...{% endblock %}
  - Content Import: {% include "header.html" %}
  - Inheritance: {% extends "base.html" %}
- Filters
  - Change Case: {{ name|title }}
  - Truncation: {{ post_content|truncatewords:50 }}
  - Date Formatting: {{ order_date|date:"D M Y" }}
  - List Slicing: {{ list_items|slice:":3" }}
