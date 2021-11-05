# 環境設定

## ライブラリの依存関係をインストール

`pipenv install`

## DB の接続情報を書いた.env ファイルを.env.sample に従って準備

```:.env
DB_USERNAME = <your db username>
DB_PASSWORD = <your db user password>
DB_HOSTIP = <your db host ip addr>
DB_NAME = <your db name>
```

## データベースの初期化

`pipenv run init_db`

# サーバー起動

`pipenv run main`

# API Reference

## Devices (api/devices.py)

### 全デバイスの取得

#### `GET` `api/v1/devices`

Sample Code

---

Shell

```terminal
$ curl http://localhost:3000/api/v1/devices
```

Response

```json
{
  "devices": [
    {
      "id": 1,
      "name": "sample_device",
      "status": 0
    },
    {
      "id": 2,
      "name": "sample_device2",
      "status": 0
    }
  ]
}
```

### 指定した id のデバイスの取得

#### `GET` `api/v1/devices/{id}`

Sample Code

---

Shell

```terminal
$ curl http://localhost:3000/api/v1/devices/1
```

Response

```json
{
  "id": 1,
  "name": "sample_device",
  "status": 0
}
```

### デバイスの追加

#### `POST` `api/v1/devices`

Sample Code

---

Shell

```terminal
$ curl -X POST http://localhost:3000/api/v1/devices -H {"Content-Type": application/json} -d {"name": "sample_device"}
```

Response

```json
{
  "id": 2,
  "name": "sample_device2",
  "status": 0
}
```

### 指定した id のデバイスの status 更新

#### `PUT` `api/v1/devices/{id}`

Sample Code

---

Shell

```terminal
$ curl -X PUT http://localhost:3000/api/v1/devices/1 -H {"Content-Type: application/json"} -d {"status": 1}
```

Response

```json
{
  "id": 1,
  "name": "sample_device",
  "status": 1
}
```

### 指定した id のデバイスの削除

#### `DELETE` `api/v1/devices/{id}`

Sample Code

---

Shell

```terminal
$ curl -X DELETE http://localhost:3000/api/v1/devices/1
```

Response

```json

```

## Users (api/users.py)

### 全ユーザーの取得

#### `GET` `api/v1/users`

Sample Code

---

Shell

```terminal
$ curl http://localhost:3000/api/v1/users
```

Response

```json
{
  "users": [
    {
      "id": 1,
      "name": "root",
      "rfid": null
    },
    {
      "id": 2,
      "name": "user1",
      "rfid": null
    }
  ]
}
```

### 指定した id のユーザーの取得

#### `GET` `api/v1/users/{id}`

Sample Code

---

Shell

```terminal
$ curl http://localhost:3000/api/v1/users/1
```

Response

```json
{
  "id": 1,
  "name": "root",
  "rfid": null
}
```

### ユーザーの追加

#### `POST` `api/v1/users`

Sample Code

---

Shell

```terminal
$ curl -X POST http://localhost:3000/api/v1/users -H {"Content-Type": application/json} -d {"name": "user1"}
```

Response

```json
{
  "id": 2,
  "name": "user1",
  "rfid": null
}
```

### 指定した id のユーザーの rfid 更新

#### `PUT` `api/v1/users/{id}`

Sample Code

---

Shell

```terminal
$ curl -X PUT http://localhost:3000/api/v1/users/1 -H {"Content-Type: application/json"} -d {"rfid": "0x45"}
```

Response

```json
{
  "id": 1,
  "name": "root",
  "rfid": 0x45
}
```

### 指定した id のユーザーの削除

#### `DELETE` `api/v1/users/{id}`

Sample Code

---

Shell

```terminal
$ curl -X DELETE http://localhost:3000/api/v1/users/1
```

Response

```json

```
