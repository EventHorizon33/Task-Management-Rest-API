from flask import Flask
from routes import tasks_bp

app = Flask(__name__)
app.register_blueprint(tasks_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)



# Flask(__name__): creates the Flask app instance.
# register_blueprint((tasks_bp): plugs all the routes defined in
 # in routes.py Modular structure works because of this.
 # debug=True: auto-restarts the server whenever a change is saved.
 # port=5001: avoida macOS AirPlay conflict on 5000.