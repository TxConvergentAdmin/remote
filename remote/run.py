from remote.server import app
from flask_ngrok import run_with_ngrok

run_with_ngrok(app)


def main():
    app.run()


if __name__ == "__main__":
    main()