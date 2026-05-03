from airflow import DAG
from airflow.operators.bash import BashOperator
from datatime import datatime

with DAG(
    dag_id = "test_git_sync_dag",
    start_data=datatime[2025, 5, 2],
    schedule_interval= None,
    catchup = False,
    tags = ["git", "test"],
) as dag:

    start = BashOperator(
        task_id = "start_task",
        bash_command = "echo 'Starting Dag exeuction...'"
    )

    middle = BashOperator(
        task_id = "middle_task",
        bash_command = "echo 'Starting Dag exeuction...'"
    )

    end = BashOperator(
        task_id = "end_task",
        bash_command = "echo 'Starting Dag exeuction...'"
    )

    start >> middle >> end