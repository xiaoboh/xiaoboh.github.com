
import web
import config


urls = ( "/", "Blog",
        )


class Blog:
    def GET(self):
        return config.render.main( config.title
                , config.get_blogs() )


app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == "__main__":
    config.build_index()
    config.build_blogs()
    app.run()


