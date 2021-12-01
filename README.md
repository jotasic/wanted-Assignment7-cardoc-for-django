# Assignment7-TW

원티드x위코드 백엔드 프리온보딩 과제7
- 과제 출제 기업 정보
  - 기업명 : 카닥

> 이 과제를 nestjs를 이용해서도 구현하였습니다. 우측 링크를 참고해주세요 [github주소](https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment7-TW-NESTJS)

## Member
| 이름  | github                                   |
|-------|-----------------------------------------|
|김태우 |[jotasic](https://github.com/jotasic)     | 

## 프로젝트 후기
- https://velog.io/@burnkim61/프리온보딩-과제-7

## 과제 내용
<details>
<summary><b>과제내용 자세히 보기</b></summary>
<div markdown="1">

### **[필수 포함 사항]**
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - **서버 구조 및 디자인 패턴에 대한 개략적인 설명**
    - 완료된 시스템이 배포된 서버의 주소
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
  
### 1. 배경 및 공통 요구사항

<aside>
😁 **카닥에서 실제로 사용하는 프레임워크를 토대로 타이어 API를 설계 및 구현합니다.**

</aside>

- 데이터베이스 환경은 별도로 제공하지 않습니다.
 **RDB중 원하는 방식을 선택**하면 되며, sqlite3 같은 별도의 설치없이 이용 가능한 in-memory DB도 좋으며, 가능하다면 Docker로 준비하셔도 됩니다.
- 단, 결과 제출 시 README.md 파일에 실행 방법을 완벽히 서술하여 DB를 포함하여 전체적인 서버를 구동하는데 문제없도록 해야합니다.
- 데이터베이스 관련처리는 raw query가 아닌 **ORM을 이용하여 구현**합니다.
- Response Codes API를 성공적으로 호출할 경우 200번 코드를 반환하고, 그 외의 경우에는 아래의 코드로 반환합니다.

| Response Code  | Description                     |
|-------|------------------------------------------|
|200 OK	|성공
|400 Bad Request	|Parameter가 잘못된 (범위, 값 등)|
|401 Unauthorized	|인증을 위한 Header가 잘못됨|
|500 Internal Server Error	|기타 서버 에러|

---

### 2. 사용자 생성 API

🎁 **요구사항**

- ID/Password로 사용자를 생성하는 API.
- 인증 토큰을 발급하고 이후의 API는 인증된 사용자만 호출할 수 있다.

```jsx
/* Request Body 예제 */

 { "id": "candycandy", "password": "ASdfdsf3232@" }
```

---

### 3. 사용자가 소유한 타이어 정보를 저장하는 API

🎁 **요구사항**

- 자동차 차종 ID(trimID)를 이용하여 사용자가 소유한 자동차 정보를 저장한다.
- 한 번에 최대 5명까지의 사용자에 대한 요청을 받을 수 있도록 해야한다. 즉 사용자 정보와 trimId 5쌍을 요청데이터로 하여금 API를 호출할 수 있다는 의미이다.

```jsx
/* Request Body 예제 */
[
  {
    "id": "candycandy",
    "trimId": 5000
  },
  {
    "id": "mylovewolkswagen",
    "trimId": 9000
  },
  {
    "id": "bmwwow",
    "trimId": 11000
  },
  {
    "id": "dreamcar",
    "trimId": 15000
  }
]
```

🔍 **상세구현 가이드**

- 자동차 정보 조회 API의 사용은 아래와 같이 5000, 9000부분에 trimId를 넘겨서 조회할 수 있다.
 **자동차 정보 조회 API 사용 예제**
  
📄 [https://dev.mycar.cardoc.co.kr/v1/trim/5000](https://dev.mycar.cardoc.co.kr/v1/trim/5000)
  
📄 [https://dev.mycar.cardoc.co.kr/v1/trim/9000](https://dev.mycar.cardoc.co.kr/v1/trim/9000)

📄 [https://dev.mycar.cardoc.co.kr/v1/trim/11000](https://dev.mycar.cardoc.co.kr/v1/trim/11000)

📄 [https://dev.mycar.cardoc.co.kr/v1/trim/15000](https://dev.mycar.cardoc.co.kr/v1/trim/15000)
  
  
- 조회된 정보에서 타이어 정보는 spec → driving → frontTire/rearTire 에서 찾을 수 있다.
- 타이어 정보는 205/75R18의 포맷이 정상이다. 205는 타이어 폭을 의미하고 75R은 편평비, 그리고 마지막 18은 휠사이즈로써 {폭}/{편평비}R{18}과 같은 구조이다.
 위와 같은 형식의 데이터일 경우만 DB에 항목별로 나누어 서로다른 Column에 저장하도록 한다.

  
### 4. 사용자가 소유한 타이어 정보 조회 API

🎁 **요구사항**

- 사용자 ID를 통해서 2번 API에서 저장한 타이어 정보를 조회할 수 있어야 한다.

</div>
</details>

## 사용 기술 및 tools
> - Back-End :  <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/PostgreSQL 14.0-0064a5?style=for-the-badge&logo=PostgreSQL&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC :  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>&nbsp;

## 모델링
![image](https://user-images.githubusercontent.com/8219812/142984423-91c4b109-4ab8-4d4e-b6dd-7ee54bbdae10.png)

## API
- [Postman Doc](https://documenter.getpostman.com/view/16042359/UVJYJyot)


## 서버구조 및 아키텍쳐

![image](https://user-images.githubusercontent.com/8219812/143032089-92176d71-6887-4e3e-83c2-19a664835a3e.png)

- 배포 환경 기준이며, 3개의 docker 컨테이너를 구동할 수 있게, `docker-compose` file를 작성하였습니다.

### Django 내부
![image](https://user-images.githubusercontent.com/8219812/143771232-1f666a84-57cd-4fc0-b7c9-5620beefed66.png)


## 구현 기능

### 사용자 생성 API
- `id`와 `password`를 입력받아서 유효성 체크 후, 회원가입을 합니다.
- 회원가입이 성공하면, AccessToken과 RefreshToken을 반환합니다.
-  Django Model의 pk의 기본 값은 id 입니다. 요구한 사항의 맞추기 위해서 pk 기본 값을 id에서 pk_id 로 변경하였습니다.
-  Token발급은 [simple_jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)를 사용하였습니다. 따라서 로그인과 토큰 갱신 부분은 따로 구현하지 않고 제공해주는 View를 연결하였습니다.

### 사용자가 소유한 타이어 정보를 저장하는 API
- 과제 구현 요구 사항을 보았을 때, Token만 있다면 다른 user의 타이어 정보도 저장 할 수 있다고 판단하였습니다.
- 받은 정보를 검사해서 user `id`가 유효한지 검사하고, `trimId`도 유효한지 외부 API 호출을 통해서 검사하였습니다. 응답이 400, 500 일 경우 해당 `trimId`는 잘못되었다고 판단하였습니다.
- 요구사항에는 5개까지 요청을 받을 수 있다고 하여, 여러번의 `Database Create`를 해야되고, 중간에 잘못된 user `id`나 `trimId`가 올 시, `Rollback`를 해야되지 때문에, Transaction 처리를 하였습니다.
- 타이어 정보는 `trimId`의 대한 자동차 정보를 API를 통해서 받으면, [python-benedict](https://pypi.org/project/python-benedict/)를 이용해서 전/후 타이어의 값을 접근하였습니다.
- 그 후, 포멧이 맞으면, 각 수치 값을 가져오는 작업은 [parse](https://pypi.org/project/parse/)를 사용하였습니다.
- 가공한 데이터를 기반으로 기존에 동일한 정보가 `trie table`에 있으면 가져올 수 있게 `get_or_create()`를 사용하였습니다.
- 마지막으로 `users`와 `tires`중간 테이블인 `user_tires table`에도 `get_or_create()`를 사용하여 데이터의 중복을 피하였습니다.

### 사용자가 소유한 타이어 정보 조회 API
- Token만 있다면 다른 user의 타이어 정보도 조회 할 수 있습니다.
- 존재하지 않는 user가 입력 시, 요구사항에 맞게 400을 반환하도록 하였습니다.


### python-benedict
- python-benedict의 장점은 계층 구조로 된 딕셔너리를 접근할 때, 코드를 간결하게 작성할 수 있습니다.
  ```python
  # 일반적인 접근 방식 (에러처리를 고려하지 않은 코드)
  data['spec']['driving']['frontTire']['value']
  
  # python-benedict를 사용한 접근 방식
  trim_info = benedict(data)
  trim_info.get_str('spec.driving.frontTire.value', '')
  ```
- 또한 계층 구조의 딕셔너리도 만들 수 있어서 test code mock data를 만들때, 유용하게 사용하였습니다.
  ```python
    mock_body = benedict()
    mock_body['spec.driving.frontTire.value'] = '225/60R16'
    print(mock_body.dict())
    # resuelt {'spec': {'driving' : {'frontTire' : {'value' : '225/60R16'}}}}
  ```

## 배포정보
|구분   |  정보          |비고|
|-------|----------------|----|
|배포플랫폼 | AWS EC2    |    |
|API 주소 |http://18.188.189.173:8061/          |    |


## API TEST 방법

<details>
  <summary><b>API TEST 방법 자세히 보기</b></summary>
<div markdown="1">

1. 우측 링크를 클릭해서 Postman으로 들어갑니다. [링크](https://www.postman.com/wecode-21-1st-kaka0/workspace/assignment7-cardoc/collection/16042359-a366ebbd-8548-41b4-9793-986bd6d81a8a?ctx=documentation)

2. Postman 우측 상단에  ENVIRONMENT 설정 버튼를 클릭해서(눈 모양) `DJANGP_SERVER_URL` 설정이 올바른지 확인합니다. (http://18.188.189.173:8061) 올바르지 않으면 수정합니다.

![image](https://user-images.githubusercontent.com/8219812/143769923-b47703d6-94f9-4c2c-a57c-c8007f16404b.png)

3. 제공한 회원가입 API를 이용해서 `Cardoc-Django`탭에 있는 회원가입을 진행합니다. 회원가입이 성공하면 Access, Refresh Token을 반환합니다.

![image](https://user-images.githubusercontent.com/8219812/143769970-6c51e15b-8f61-44d0-ad6b-93898f03fee5.png)

4. Access 토큰을 이미지를 참고해서 입력하고, 저장합니다.

![image](https://user-images.githubusercontent.com/8219812/143770006-25500af2-aac7-46ee-853b-7f8717077601.png)
  
5. 이제 Access Token이 설정되었기 때문에, 다른 API를 호출할 수 있습니다.

6 만약 Send 버튼이 비활성화 이시면 fork를 이용해서 해당 postman project를 복사해서 시도하길 바랍니다.
  
  ![image](https://user-images.githubusercontent.com/8219812/143040169-cb3bbba5-7583-4937-b5b6-35489bcd5c7d.png)
  
</div>
</details>

## 설치 및 실행 방법
<details>
 <summary><b>설치 및 실행 방법 자세히 보기</b></summary>
<div markdown="1">
  
###  Local 개발 및 테스트용

1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment7-TW
    cd Assignment7-TW
    ```

2. docker-compose 명령어를 이용해서 서버와 db를 실행시킨다.
    ```bash
    docker-compose -f ./docker-compose-dev-local.yml up
    docker-compose -f ./docker-compose-dev-local.yml up -d //백그라운드 실행
    ```

###  배포용 
1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
  ```bash
  git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment7-TW
  cd Assignment7-TW
  ```

2. 환경설정 파일을 만든다.

  .dockerenv.deploy.backend
  
    ```bash
      DJANGO_SECRET_KEY='django시크릿키'
      SQL_DATABASE_NAME=database이름
      SQL_PASSWORD=database비밀번호
    ```
  
  .dockerenv.deploy.db
  
    ```bash
      POSTGRES_DB=database이름
      POSTGRES_PASSWORD=database비밀번호
    ```
 
3. docker-compose 명령어를 이용해서 서버와 db를 실행시킨다.
  
  ```bash
  docker-compose -f ./docker-compose-deploy.yml up --build -d
  ```
  
</div>
</details>

## 폴더 구조
```bash
📦 Assignment7
 ┣ 📂 cardoc
 ┃ ┣ 📂 settings
 ┃ ┃ ┣ 📜 base.py
 ┃ ┃ ┣ 📜 deploy.py
 ┃ ┃ ┗ 📜 dev_local.py
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 asgi.py
 ┃ ┣ 📜 urls.py
 ┃ ┗ 📜 wsgi.py
 ┣ 📂 cars
 ┃ ┣ 📂 migrations
 ┃ ┃ ┣ 📜 0001_initial.py
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 apps.py
 ┃ ┣ 📜 models.py
 ┃ ┣ 📜 serializers.py
 ┃ ┣ 📜 tests.py
 ┃ ┗ 📜 views.py
 ┣ 📂 commands
 ┃ ┣ 📂 management
 ┃ ┃ ┣ 📂 commands
 ┃ ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┃ ┗ 📜 wait_for_db_connected.py
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┗ 📜 __init__.py
 ┣ 📂 config
 ┃ ┗ 📂 nginx
 ┃ ┃ ┗ 📜 nginx.conf
 ┣ 📂 static
 ┣ 📂 users
 ┃ ┣ 📂 migrations
 ┃ ┃ ┣ 📜 0001_initial.py
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 admin.py
 ┃ ┣ 📜 apps.py
 ┃ ┣ 📜 managers.py
 ┃ ┣ 📜 models.py
 ┃ ┣ 📜 serializers.py
 ┃ ┣ 📜 tests.py
 ┃ ┣ 📜 urls.py
 ┃ ┗ 📜 views.py
 ┣ 📜 .gitignore
 ┣ 📜 Dockerfile-deploy
 ┣ 📜 Dockerfile-dev-local
 ┣ 📜 README.md
 ┣ 📜 docker-compose-deploy.yml
 ┣ 📜 docker-compose-dev-local.yml
 ┣ 📜 graph.png
 ┣ 📜 manage.py
 ┣ 📜 pull_request_template.md
 ┗ 📜 requirements.txt
```

# Reference
- 이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 에서 출제한 과제를 기반으로 만들었습니다.
- 본 과제는 저작권의 보호를 받으며, 문제에 대한 정보를 배포하는 등의 행위를 금지 합니다.
