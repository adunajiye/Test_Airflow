from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable
from Save_Db_Function.Get_Trade import save_trade

with DAG("Trade_Data", start_date=datetime(2023, 11, 30),
schedule_interval='@daily', max_active_runs=1, catchup=False) as dag:

    Tstc_script_A = PythonOperator(
        task_id="Get_Api_Data",
        python_callable=save_trade
    )