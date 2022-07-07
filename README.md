# CANedge 데이터 분석 및 시각화

CSS-Electronics사의 파이썬 API 를 활용해 CANedge 데이터 전처리
이후 InfluxDB 와 Grafana 를 통한 데이터 시각화

## 개발환경

---

<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Pythont&logoColor=white"/>

[Generic badge](https://img.shields.io/badge/version-3.8.10-green.svg)
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=Docker&logoColor=white"/>
[Generic badge](https://img.shields.io/badge/version-20.10.17-green.svg)

<img src="https://img.shields.io/badge/InfluxDB-22ADF6?style=flat&logo=InfluxDB&logoColor=white"/>
<img src="https://img.shields.io/badge/Grafana-F46800?style=flat&logo=Grafana&logoColor=white"/>

Python 3.8.10  
Docker 20.10.17  
influxdb  
grafana

![Generic badge](https://img.shields.io/badge/version-3.8.10-green.svg)

## 사용법

### 0 : 오른쪽 초록색 버튼을 누른뒤 project를 zip 으로 다운받은뒤 압축해제

---

### 1 : inputs.py 수정

---

```
# specify your InfluxDB details
influx_bucket = "influx_bucket_name"
token = "influx_token"
influx_url = "influx_endpoint"
org_id = "influx_org_id"
```

사용자에 InfluxDB 를 참고하여 수정한다

### 2 : virtual environment 설치와 requirements.txt 에있는 파이썬 라이브러리 설치

---

##### Windows

```
python -m venv env & env\Scripts\activate & pip install -r requirements.txt

```

##### Linux

```
python3 -m venv env && source env/bin/activate && pip install -r requirements.txt

```

python3 이 안된다면 python 으로 바꿔서 해볼것
설치후 env 파일이 생긴것을 확인할수 있음 env 파일이있으면 삭제후 재설치

### 3 : env 모드로 진입

---

##### Windows

```
env\Scripts\activate

```

##### Linux

```
source env/bin/activate

```

### 4 : main 파일을 실행:

---

```
python3 main.py

```

성공시 아래의 문구가 여러번 출력되며 influx db에 데이터가 쌓임

```
Signal: response (mean: 4.0 | records: 63 | resampling: 1S)
- SUCCESS: 63 records of 2C4E8905 written to InfluxDB
```

### 5 : Grafana 설정:

---

Configuration/Plugins 에서 TrackMap 인스톨
Dashboards/Browse 에서 Import 버튼클릭 이후 dashboard-templates 폴더안의 dashboard-template-sample-data.json 을 업로드한다

이후 시간대와 속성값을 잘 선택하여 데이터가 표기되는지 확인한다

<!-- ## 실행방법

---

```
/home/test/api-examples/ canedge-influxdb-writer-master

안의 inputs.py 의 DBC 와 MF4 파일을 원하는대로 수정한뒤

linux 는 source env/bin/activate 로
 virtual environment 에 진입한뒤
 python3 main.py 로 데이터 전송


``` -->

## 참고

https://github.com/CSS-Electronics/api-examples  
https://github.com/CSS-Electronics/canedge-influxdb-writer
