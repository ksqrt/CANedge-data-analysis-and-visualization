# -----------------------------------------------
# specify your InfluxDB details
# # 1. local
# influx_bucket = "test1"
# token = "MuC6p8UweFKfqnpQ-k_bqgKzU7AclX7VFt-rnGlkIHnrIM6mdXto23MBr4cOPR7h77RqqhMIi7Bc2MmD9DNAhA=="
# influx_url = "http://localhost:8086/"
# org_id = "829013afce059956"

# 2. docker
influx_bucket = "test"
token = "F2i3a8rNog_lcRgHeU-5w4MKQX7xhsQHpYx_BobGinOTpeqKBNyybNgjS0C7Ws9L4_TRrZGpJB5uFBMk5Sg4Ag=="
influx_url = "http://localhost:8086"
org_id = "fffecc1fa476a203"

# -----------------------------------------------
# specify devices to process from local disk via ["folder/device_id"] or S3 via ["bucket/device_id"]
devices = ["ksqrt/958D2219"]
# -----------------------------------------------
# specify DBC paths and a list of signals to process ([]: include all signals)
dbc_paths = ["dbc_files/CSS-Electronics-OBD2-v1.4.dbc"]
signals = []

# specify resampling frequency ("": no resampling)
res = "1S"

# -----------------------------------------------
# specify whether to load data from S3 (and add server details if relevant)
s3 = True
key = "AKIAXZF5HFDB4WYRTBTM"
secret = "PrbooX8qzZ2YtnrEAYJ9WsYLoSTbXwRAfmu26yu4"
endpoint = "http://s3.ap-northeast-2.amazonaws.com"
# e.g. http://s3.us-east-1.amazonaws.com or http://192.168.0.1:9000
# cert = "path/to/cert.crt"  # if MinIO + TLS, add path to cert and update utils.py/setup_fs to verify

# -----------------------------------------------
# if dynamic = True, data is loaded dynamically based on most recent data in InfluxDB - else default_start is used
dynamic = True
default_start = "2022-01-01 00:00:00"
# offsets data to start at 'today - days_offset'. Set to None to use original timestamps
days_offset = None

# if you're using data encryption, you can add the password below
pw = {"default": "password"}

# if you need to process multi-frame data, set tp_type to "uds", "j1939" or "nmea"
tp_type = ""
