from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable
from Save_Db_Function.Get_Sorting import save_sorts_summary

with DAG("Getsort_summary_Data", start_date=datetime(2023, 11, 30),
schedule_interval='@daily', max_active_runs=1, catchup=False) as dag:

    Tstc_script_A = PythonOperator(
        task_id="Get_Api_Data",
        python_callable=save_sorts_summary
    )