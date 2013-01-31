
import web
import config


def build():
    h = config.render.main( config.title, config.say, config.blogs)
    open('index.html','w').write( str(h) )




if __name__ == '__main__':
    build()
