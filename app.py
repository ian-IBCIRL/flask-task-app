import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from taskapp import app


# if __name__ == "__main__":
#     app.run(
#     )


app = Flask(__name__)
host = os.environ.get("IP")
port = int(os.environ.get("PORT"))
debug = os.environ.get("DEBUG")
openai.api_key = os.getenv("OPENAI_API_KEY")
print(os.getenv("OPENAI_API_KEY"))
serverName = os.getenv("SERVER_NAME")
print(serverName)
