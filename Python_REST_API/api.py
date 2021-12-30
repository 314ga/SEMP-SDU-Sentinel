import os
from flask import Flask, jsonify, send_file
import random

app = Flask(__name__)


def random_image():
    img_dir = "./img"
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, random.choice(img_list))
    return img_path


# we define the route /
@app.route("/")
def myapp():
    image = random_image()
    return send_file(image, mimetype="image/png")


if __name__ == "__main__":
    # define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port
    app.run(host="0.0.0.0", port=os.getenv("PORT"))
