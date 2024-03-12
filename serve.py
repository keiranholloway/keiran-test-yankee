import web

urls = (
  '/', 'index',
)


class index:
    def GET(self):
        return "Hello, world in keiran-test-yankee application!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
