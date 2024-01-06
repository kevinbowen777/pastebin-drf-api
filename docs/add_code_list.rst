Add Snippet list
================

Template for adding a list of Snippets to django-api-library Django application

.. code-block:: console

    Snippet = Snippet.objects.create(
        title="",
        code="",
        linenos="",
        language="",
        style="",
        owner="",
        highlighted="",
    )

Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample Snippet list
-------------------

.. code-block:: console

    User = get_user_model()
    Snippet = Snippet.objects.create(
        title="Hello World",
        code="print('Hello World')",
        linenos="False",
        language="Python",
        style="friendly",
        owner=User.objects.first(),
    )

    Snippet = Snippet.objects.create(
        title="Say hello function",
        code="""
            def say_hello(name):
            print(name)
            name = 'Kevin'
            say_hello(name)
        """,
        linenos="False",
        language="Python",
        style="colorful",
        owner=User.objects.first(),
    )

    Snippet = Snippet.objects.create(
        title="Fibonacci sequence",
        code="",
        linenos="False",
        language="Python",
        style="friendly",
        owner=User.objects.get(username="alice"),
    )

    Snippet = Snippet.objects.create(
        title="Hello World (C)",
        code="",
        linenos="False",
        language="Python",
        style="friendly",
        owner=User.objects.get(username="john"),
    )

    Snippet = Snippet.objects.create(
        title="Create a class and an object of a class",
        code="",
        linenos="False",
        language="Python",
        style="friendly",
        owner=User.objects.get(username="david"),
    )

    Snippet = Snippet.objects.create(
        title="Lambda - Add 10 to numbers passed in argument",
        code="",
        linenos="False",
        language="Python",
        style="friendly",
        owner=User.objects.get(username="susan"),
    )

    Snippet = Snippet.objects.create(
        title="Hello World (Java)",
        code="",
        linenos="False",
        language="Python",
        style="friendly",
        owner=User.objects.get(username="kbowen"),
    )

    Snippet = Snippet.objects.create(
        title=""Convert from JSON to Python,
        code="",
        linenos="False",
        language="Python",
        style="friendly",
        owner=User.objects.get(username="mary"),
    )

    Snippet = Snippet.objects.create(
        title="Create a database in MySQL,
        code="",
        linenos="False",
        language="Python",
        style="friendly",
        owner=User.objects.get(username="alice"),
    )

    Snippet = Snippet.objects.create(
        title="Loop through an iterator",
        code="",
        linenos="False",
        language="Python",
        style="friendly",
        owner=User.objects.get(username="john"),
    )
