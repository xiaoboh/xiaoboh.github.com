
import web
import config


urls = ( "/blog", "Blog",
        )




class Blog:
    def GET(self):
        return config.render.main( config.title, config.say, config.blogs)


app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == "__main__":
    app.run()


