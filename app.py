from app import app

if __name__ == '__main__':
    port = int(4000)
    app.run(debug=False, port=port, host='0.0.0.0')
