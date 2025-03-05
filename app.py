from flask import *
import os



app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
app.run(debug=True)