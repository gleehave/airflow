from airflow import DAG
import pendulum
from datetime import datetime, timedelta
from api.video_status import get_playlist_id, get_video_ids, extract_video_data, save_to_json

local_timezone = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    "email_on_failure": False,
    "email_on_retry": False,
    "max_active_runs": 1,
    "dagrun_timeout": timedelta(hours=1),
    "start_date": datetime(2026, 3, 1, tzinfo=local_timezone),   
}

with DAG(
    dag_id="produce_json",
    default_args=default_args,
    description="DAG to produce JSON file with raw data",
    schedule="0 14 * * *",
    catchup=False,
) as dag:

    # Task 정의하기
    # 1. Playlist ID 가져오기
    playlist_id = get_playlist_id()

    # 2. Video ID 가져오기
    video_ids = get_video_ids(playlist_id)

    # 3. Data 추출
    video_data = extract_video_data(video_ids)
    # 4. JSON 저장
    save_to_json(video_data)

    # 작업간 의존성 설계
    playlist_id >> video_ids >> video_data >> save_to_json