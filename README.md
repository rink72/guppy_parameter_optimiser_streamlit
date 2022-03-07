# guppy_parameter_optimiser_streamlit
Streamlit webapp for Guppy Parameter Optimiser data

## Application configuration
The application requires a postGres database to store data. This can be configured by creating `secrets.local.toml` in the `.streamlit` folder. An example configuration for this file is below.

```toml
[pg_credentials]
host = "host.address.com"
database = "databasename"
user = "databaseuser"
password = "databasepassword"
```

## Initialising database
To create the required tables and initialise some seed data you can run:

```bash
python src/initialise-database.py
```

Required environment variables:

- `GUPPY_CONFIG_PATH` - The path to the configuration file. Usually `secrets.local.toml` in the `.streamlit` folder

This will create the required tables if missing and add some initial seed data. If the tables and data are already present, they will not be modified.

## Running application
To start the application locally

```bash
streamlit run src/app.py
```

## Importing data

If there is new data to be imported from CSV, this can be done by running:

```bash
python src/import-csv-data.py
```

Required environment variables:

- `GUPPPY_CSV_PATH` - The path to the CSV file to import
- `GUPPY_CONFIG_PATH` - The path to the configuration file. Usually `secrets.local.toml` in the `.streamlit` folder

