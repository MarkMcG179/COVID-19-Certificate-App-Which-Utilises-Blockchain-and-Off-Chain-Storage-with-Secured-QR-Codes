from website import create_app
import blockchain

app = create_app()


if __name__ == '__main__':
    blockchain.main()
    app.run(debug=True, use_reloader=False) #'use_reloader' prevents the app from reloading, thus preventing duplication of the blockchain