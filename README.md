# CANedge 데이터 분석 및 시각화

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Pythont&logoColor=white" alt="Badge">
<img src="https://img.shields.io/badge/version-3.8.10-green.svg">
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=Docker&logoColor=white" alt="Badge"/>
<img src="https://img.shields.io/badge/version-20.10.17-green.svg">
<img src="https://img.shields.io/badge/InfluxDB-22ADF6?style=flat&logo=InfluxDB&logoColor=white"/>
<img src="https://img.shields.io/badge/Grafana-F46800?style=flat&logo=Grafana&logoColor=white"/>
</p>

CSS-Electronics사의 파이썬 API 를 활용해 CANedge 데이터 전처리
이후 InfluxDB 와 Grafana 를 통한 데이터 시각화

.MF4 파일과 .dbc파일 을 통해 데이터를 추출합니다

이후 데이터를 influxDB에 업로드하고 grafana 를 통해 시각화합니다

<br>

<br>

## 파일 미리보기

- LOG/: raw 데이터를 담고있습니다(.MF4)
- dbc_files/: DBC 파일을 담고있습니다.
- dashboard-templates : grafana 에 import 될 flex 쿼리문을 담고있습니다
- main.py : exec) 모드에서 실행시 influxdb에 데이터를 가공추출하여 업로드 합니다
- utils.py: 다른 스크립트에서 사용하는 클래스와 함수가 들어있습니다
- inputs.py: 사용자의 influx db 의 세부사항이 있습니다

## 초기설정

https://github.com/ksqrt/How-to-install-and-link-Grafana-and-influxdb

https://canlogger.csselectronics.com/canedge-getting-started/log-file-tools/browser-dashboard/influxdb-writer/initial-setup/

위 두 링크를 참고하여 influxDB와 grafana setup을 마칩니다.

<br>

## 사용방법

<br>

### 1 : inputs.py 수정

---

inputs.py 파일을 개인에 맞게 수정합니다
<br>

```
# specify your InfluxDB details
influx_bucket = "influx_bucket_name"
token = "influx_token"
influx_url = "influx_endpoint"
org_id = "influx_org_id"
```

사용자에 InfluxDB 를 참고하여 수정합니다  
<br>

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

python3 이 안된다면 python 으로 다시해봅니다.  
설치후 env 파일이 생긴것을 확인 할수있습니다  
이미 env 파일이 있으면 삭제후 명령어로 재설치 합니다

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

성공시 아래의 문구가 여러번 출력되며 influx db에 데이터가 쌓입니다.

```
Signal: response (mean: 4.0 | records: 63 | resampling: 1S)
- SUCCESS: 63 records of 2C4E8905 written to InfluxDB
```

### 5 : Grafana 설정:

---

Dashboards/Browse 에서 Import 버튼클릭 이후 dashboard-templates 폴더안의 dashboard-template-sample-data.json 을 업로드합니다

이후 시간대와 속성값을 잘 선택하여 데이터가 표기되는지 확인해봅니다.
Grafana 의 기본시간대 때문에 NO DATA 가 뜰수도있으니 시간대변경을 하며 잘 확인해봅니다.

### 6 : 결과물 확인
---
![https://lh6.googleusercontent.com/2cGFz5ZpP57_mrg9rbuBg7KW6rfrnFdRUsPrTN8PxXZbux-_ramJVPRNjqvg-4PXheyxrN5_FrOSCcrr9bXI=w1920-h942-rw
](https://lh6.googleusercontent.com/2cGFz5ZpP57_mrg9rbuBg7KW6rfrnFdRUsPrTN8PxXZbux-_ramJVPRNjqvg-4PXheyxrN5_FrOSCcrr9bXI=w1920-h942-rw)


## 참고

https://canlogger.csselectronics.com/canedge-getting-started/log-file-tools/browser-dashboard/influxdb-writer/initial-setup/

https://github.com/CSS-Electronics/api-examples  
https://github.com/CSS-Electronics/canedge-influxdb-writer
