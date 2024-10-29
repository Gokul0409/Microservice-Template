from app.config.config import initialize_db
from sanic import Sanic
from app.controller.user_controller import user_print

app = Sanic("__name__")

app.blueprint(user_print)


@app.listener("before_server_start")
async def on_start(app, loop):
    initialize_db()

if "__main__" == __name__:
    app.run(host="localhost", port=4444, dev=True)
