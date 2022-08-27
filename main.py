
from Website import create_app

global app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)