from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL')

# This checks if the DATABASE_URL starts with "postgres://" and replaces it with "postgresql://"
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

if DATABASE_URL:  # We are running on Heroku or another production environment
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
else:  # We are running locally
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kooringal25@localhost:5432/rugbydb'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/SRP23_teamoverview')
def srp23_teamoverview():
    df = pd.read_sql_query('SELECT * FROM SRP23_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM SRP23_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM SRP23_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM SRP23_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM SRP23_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM SRP23_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM SRP23_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('SRP23_TeamSeasonOverview.html', **tables)


@app.route('/SRP23_playeroverview')
def srp23_playeroverview():
    df = pd.read_sql_query('SELECT * FROM SRP23_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM SRP23_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM SRP23_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM SRP23_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM SRP23_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM SRP23_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM SRP23_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('SRP23_PlayerSeasonOverview.html', **tables)



@app.route('/PREM23_teamoverview')
def prem23_teamoverview():
    df = pd.read_sql_query('SELECT * FROM PREM23_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM PREM23_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM PREM23_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM PREM23_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM PREM23_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM PREM23_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM PREM23_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('PREM23_TeamSeasonOverview.html', **tables)

@app.route('/PREM23_playeroverview')
def prem23_playeroverview():
    df = pd.read_sql_query('SELECT * FROM PREM23_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM PREM23_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM PREM23_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM PREM23_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM PREM23_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM PREM23_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM PREM23_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('PREM23_PlayerSeasonOverview.html', **tables)



@app.route('/URC23_teamoverview')
def urc23_teamoverview():
    df = pd.read_sql_query('SELECT * FROM URC23_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM URC23_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM URC23_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM URC23_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM URC23_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM URC23_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM URC23_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('URC23_TeamSeasonOverview.html', **tables)

@app.route('/URC23_playeroverview')
def urc23_playeroverview():
    df = pd.read_sql_query('SELECT * FROM URC23_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM URC23_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM URC23_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM URC23_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM URC23_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM URC23_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM URC23_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('URC23_PlayerSeasonOverview.html', **tables)



@app.route('/T1423_teamoverview')
def t1423_teamoverview():
    df = pd.read_sql_query('SELECT * FROM T1423_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM T1423_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM T1423_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM T1423_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM T1423_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM T1423_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM T1423_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('T1423_TeamSeasonOverview.html', **tables)

@app.route('/T1423_playeroverview')
def t1423_playeroverview():
    df = pd.read_sql_query('SELECT * FROM T1423_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM T1423_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM T1423_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM T1423_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM T1423_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM T1423_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM T1423_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('T1423_PlayerSeasonOverview.html', **tables)



if __name__ == '__main__':
    app.run(debug=True)

