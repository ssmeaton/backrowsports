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
    # Function to create static tables
    def create_table(query, table_class='static-table table-striped'):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes=table_class, index=False)

    # Queries for team overview tables
    team_queries = {
        'avg_metres_srp': 'SELECT team, avg_metres FROM SRP24_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_metres_prem': 'SELECT team, avg_metres FROM PREM24_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_metres_urc': 'SELECT team, avg_metres FROM URC24_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_metres_t14': 'SELECT team, avg_metres FROM T1424_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
    }
    team_tables = {name: create_table(query) for name, query in team_queries.items()}

    # Queries for player overview tables
    player_queries = {
        'top_tries_srp': 'SELECT name, total_tries FROM SRP24_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_tries_prem': 'SELECT name, total_tries FROM PREM24_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_tries_urc': 'SELECT name, total_tries FROM URC24_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_tries_t14': 'SELECT name, total_tries FROM T1424_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
    }
    player_tables = {name: create_table(query) for name, query in player_queries.items()}

    # Combine all tables into a single dictionary to pass to the template
    all_tables = {**team_tables, **player_tables}

    return render_template('home.html', **all_tables)

@app.route('/SRP24_teamoverview')
def srp24_teamoverview():
    df = pd.read_sql_query('SELECT * FROM SRP24_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM SRP24_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM SRP24_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM SRP24_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM SRP24_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM SRP24_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM SRP24_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('SRP24_TeamSeasonOverview.html', **tables)

@app.route('/SRP24_playeroverview')
def srp24_playeroverview():
    df = pd.read_sql_query('SELECT * FROM SRP24_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM SRP24_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM SRP24_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM SRP24_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM SRP24_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM SRP24_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM SRP24_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('SRP24_PlayerSeasonOverview.html', **tables)


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

@app.route('/SRP22_teamoverview')
def srp22_teamoverview():
    df = pd.read_sql_query('SELECT * FROM SRP22_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM SRP22_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM SRP22_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM SRP22_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM SRP22_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM SRP22_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM SRP22_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('SRP22_TeamSeasonOverview.html', **tables)

@app.route('/SRP22_playeroverview')
def srp22_playeroverview():
    df = pd.read_sql_query('SELECT * FROM SRP22_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM SRP22_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM SRP22_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM SRP22_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM SRP22_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM SRP22_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM SRP22_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('SRP22_PlayerSeasonOverview.html', **tables)



@app.route('/PREM24_teamoverview')
def prem24_teamoverview():
    df = pd.read_sql_query('SELECT * FROM PREM24_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM PREM24_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM PREM24_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM PREM24_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM PREM24_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM PREM24_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM PREM24_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('PREM24_TeamSeasonOverview.html', **tables)

@app.route('/PREM24_playeroverview')
def prem24_playeroverview():
    df = pd.read_sql_query('SELECT * FROM PREM24_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM PREM24_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM PREM24_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM PREM24_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM PREM24_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM PREM24_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM PREM24_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('PREM24_PlayerSeasonOverview.html', **tables)

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

@app.route('/PREM22_teamoverview')
def prem22_teamoverview():
    df = pd.read_sql_query('SELECT * FROM PREM22_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM PREM22_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM PREM22_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM PREM22_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM PREM22_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM PREM22_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM PREM22_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('PREM22_TeamSeasonOverview.html', **tables)

@app.route('/PREM22_playeroverview')
def prem22_playeroverview():
    df = pd.read_sql_query('SELECT * FROM PREM22_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM PREM22_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM PREM22_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM PREM22_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM PREM22_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM PREM22_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM PREM22_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('PREM22_PlayerSeasonOverview.html', **tables)




@app.route('/URC24_teamoverview')
def urc24_teamoverview():
    df = pd.read_sql_query('SELECT * FROM URC24_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM URC24_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM URC24_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM URC24_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM URC24_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM URC24_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM URC24_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('URC24_TeamSeasonOverview.html', **tables)

@app.route('/URC24_playeroverview')
def urc24_playeroverview():
    df = pd.read_sql_query('SELECT * FROM URC24_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM URC24_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM URC24_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM URC24_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM URC24_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM URC24_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM URC24_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('URC24_PlayerSeasonOverview.html', **tables)

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

@app.route('/URC22_teamoverview')
def urc22_teamoverview():
    df = pd.read_sql_query('SELECT * FROM URC22_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM URC22_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM URC22_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM URC22_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM URC22_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM URC22_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM URC22_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('URC22_TeamSeasonOverview.html', **tables)

@app.route('/URC22_playeroverview')
def urc22_playeroverview():
    df = pd.read_sql_query('SELECT * FROM URC22_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM URC22_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM URC22_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM URC22_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM URC22_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM URC22_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM URC22_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('URC22_PlayerSeasonOverview.html', **tables)

@app.route('/T1424_teamoverview')
def t1424_teamoverview():
    df = pd.read_sql_query('SELECT * FROM T1424_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM T1424_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM T1424_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM T1424_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM T1424_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM T1424_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM T1424_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('T1424_TeamSeasonOverview.html', **tables)

@app.route('/T1424_playeroverview')
def t1424_playeroverview():
    df = pd.read_sql_query('SELECT * FROM T1424_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM T1424_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM T1424_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM T1424_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM T1424_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM T1424_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM T1424_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('T1424_PlayerSeasonOverview.html', **tables)

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

@app.route('/T1422_teamoverview')
def t1422_teamoverview():
    df = pd.read_sql_query('SELECT * FROM T1422_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM T1422_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM T1422_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM T1422_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM T1422_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM T1422_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM T1422_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('T1422_TeamSeasonOverview.html', **tables)

@app.route('/T1422_playeroverview')
def t1422_playeroverview():
    df = pd.read_sql_query('SELECT * FROM T1422_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM T1422_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM T1422_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM T1422_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM T1422_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM T1422_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM T1422_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('T1422_PlayerSeasonOverview.html', **tables)

@app.route('/RWC23_teamoverview')
def rwc23_teamoverview():
    df = pd.read_sql_query('SELECT * FROM RWC23_TeamSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        df = df.round(2)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'avg_cb': 'SELECT team, avg_cb FROM RWC23_TeamSeasonOverview ORDER BY avg_cb DESC LIMIT 5',
        'avg_db': 'SELECT team, avg_db FROM RWC23_TeamSeasonOverview ORDER BY avg_db DESC LIMIT 5',
        'avg_runs': 'SELECT team, avg_runs FROM RWC23_TeamSeasonOverview ORDER BY avg_runs DESC LIMIT 5',
        'avg_metres': 'SELECT team, avg_metres FROM RWC23_TeamSeasonOverview ORDER BY avg_metres DESC LIMIT 5',
        'avg_offl': 'SELECT team, avg_offl FROM RWC23_TeamSeasonOverview ORDER BY avg_offl DESC LIMIT 5',
        'avg_tkl': 'SELECT team, avg_tkl FROM RWC23_TeamSeasonOverview ORDER BY avg_tkl DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('RWC23_TeamSeasonOverview.html', **tables)

@app.route('/RWC23_playeroverview')
def rwc23_playeroverview():
    df = pd.read_sql_query('SELECT * FROM RWC23_PlayerSeasonOverview', con=db.engine)
    df = df.round(2)
    table = df.to_html(classes='table table-striped', index=False)

    # Function to create static tables
    def create_table(query):
        df = pd.read_sql_query(query, con=db.engine)
        return df.to_html(classes='static-table table-striped', index=False)

    # Generate static tables
    queries = {
        'top_tries': 'SELECT name, total_tries FROM RWC23_PlayerSeasonOverview ORDER BY total_tries DESC LIMIT 5',
        'top_defenders_beaten': 'SELECT name, total_db FROM RWC23_PlayerSeasonOverview ORDER BY total_db DESC LIMIT 5',
        'top_clean_breaks': 'SELECT name, total_cb FROM RWC23_PlayerSeasonOverview ORDER BY total_cb DESC LIMIT 5',
        'top_tackles': 'SELECT name, total_tkl FROM RWC23_PlayerSeasonOverview ORDER BY total_tkl DESC LIMIT 5',
        'top_runs': 'SELECT name, total_runs FROM RWC23_PlayerSeasonOverview ORDER BY total_runs DESC LIMIT 5',
        'top_metres': 'SELECT name, total_metres FROM RWC23_PlayerSeasonOverview ORDER BY total_metres DESC LIMIT 5',
    }
    tables = {name: create_table(query) for name, query in queries.items()}

    # Add the main dynamic table to the tables dictionary
    tables['table'] = table

    return render_template('RWC23_PlayerSeasonOverview.html', **tables)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
