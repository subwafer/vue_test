# this example will showcase a basic flask app that has "rest api" endpoints --endpoints that server some json
# The frontend will be some sort of combo of flask / jinja2 templating and some vue components
# some of the pieces will be pure javascript (such as the http util, etc.)
# basic idea of vue is that it is a library of javascript with it's own syntax
# the components you build in vue will be compiled down into javascript using some sort of "bundler"
# this compiled bundle of vue components is literally just javascript that will then run on the page when served to the client.
# that's basically it.
#
# Vue has some helper functions that "simplify" the basic ideas of building reactive frontend components.
# It can make the creation of a, for example, music player app --Spotify-- easier.
# Components are stateless --in fact, the frontend in general is stateless. So state is to be managed by the dev. as needed.


from src import create_app

if __name__ == "__main__":
    app = create_app()

    app.run()
