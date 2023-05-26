# Finanstats

## Database
### Spin it up
To start the DB, make sure that Docker is installed and run `docker-compose up -d`
### Update to latest migration version
Make sure that all dependencies are installed with `pip install -r requirements.txt` <br/>
Then run `alembic upgrade head`
