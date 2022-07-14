# Now that we have access to the factory function,
# we can create an app instance in app.py by invoking the function and saving it to a variable called app.

from petfax import create_app
app = create_app()
