# Airflow
#### Docker Image Reference
- https://hub.docker.com/r/apache/airflow

#### Airflow Component
<img width="1021" height="619" alt="스크린샷 2026-02-28 오후 12 14 36" src="https://github.com/user-attachments/assets/88e411ff-5e52-45cf-ab47-61d1ba483507" />

##### Scheduler
- 어떤 작업(Task)을, 언제 실행할지 결정
- Scheduler 내부에 실행(Executor)가 포함되어있음.
    - Sequential Executor : 단일 작업 순차 실행
    - Local Executor : 하나의 머신에서 여러 작업 병렬 실행
    - Celery Exectuor
    - Kubernetes Executor

##### Airflow Web Server
- DAG를 모니터링하고, 실행할 수 있게 제공하는 UI
- `localhost:8080`으로 접근 가능

##### DAG (Directed Acyclic Graph)
- Drected : Airflow 작업은 순서가 정해져있음
- Acyclic : 순환이 없음. 즉, 하나의 작업이 자기 자신에 의존할 수 없음
- Graph   : 작업끼리의 의존 관계를 표현

##### Metadata Database
- DAG 정의
- 코드
- 스케줄러의 메타데이터
- 로그
- 변수
- 커넥션 정보
- 설정 정보

#### 그 외 상황에 따라 사용하는 요소
##### Airflow Trigger
- 비동기(Deferrable) 오퍼레이터를 지원한다.
- 예를 들어, S3 버킷에 특정 파일이 업로드될 때까지 대기하는 Sensor가 있다면 	Trigger는 해당 S3 버킷을 모니터링 하고, 파일이 감지되면 Trigger가 스케줄러에 신호를 보내 후속 작업을 재개

##### Message Broker
- 스케줄러가 보낸 메시지를 워커에게 전달
    - Exectutor가 Message Broker에 접근해서 Worker에게 전달


## Airflow - DB 설정
```
postgres=# \du

postgres=# CREATE DATABASE airflow_db;
CREATE USER airflow_user WITH PASSWORD 'airflow_pass';
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;
CREATE DATABASE
CREATE ROLE
```

## Airflow - Webserver 작동
<img width="1671" height="434" alt="스크린샷 2026-03-01 오후 1 43 01" src="https://github.com/user-attachments/assets/7b98f80b-c487-4faa-861a-c6d1347c6abd" />

<img width="1674" height="334" alt="스크린샷 2026-03-01 오후 1 43 47" src="https://github.com/user-attachments/assets/b978126c-77fb-45c3-9ae7-473787ae6be7" />

<img width="1669" height="317" alt="스크린샷 2026-03-01 오후 1 50 31" src="https://github.com/user-attachments/assets/49d60e64-b52d-4cc7-ab53-21cf8d96928c" />

