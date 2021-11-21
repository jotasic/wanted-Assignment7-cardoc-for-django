# Assignment7-TW

원티드x위코드 백엔드 프리온보딩 과제7
- 과제 출제 기업 정보
  - 기업명 : xx

## Member
| 이름  | github                                   |
|-------|------------------------------------------|
|김태우 |[jotasic](https://github.com/jotasic)     | 

## 과제 내용
<details>
<summary>과제내용 보기</summary>
<div markdown="1">

### **[필수 포함 사항]**
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - **서버 구조 및 디자인 패턴에 대한 개략적인 설명**
    - 완료된 시스템이 배포된 서버의 주소
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

</div>
</details>

## 사용 기술 및 tools
> - Back-End :  <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/PostgreSQL 14.0-0064a5?style=for-the-badge&logo=PostgreSQL&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC :  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>&nbsp;

## 모델링


## API
- [Postman Doc]()

## 구현 기능


## 배포정보
|구분   |  정보          |비고|
|-------|----------------|----|
|배포플랫폼 | AWS EC2    |    |
|API 주소 |http://18.188.189.173:8061/          |    |


## API TEST 방법
1. 우측 링크를 클릭해서 Postman으로 들어갑니다. [링크]()


## 설치 및 실행 방법
<details>
<summary>설치 및 실행 방법 자세히 보기</summary>
<div markdown="1">
  
###  Local 개발 및 테스트용

1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment7-TW
    cd Assignment7-TW
    ```

2. 가상 환경을 만들고 프로젝트에 사용한 python package를 받는다.
    ```bash
    conda create --name Assignment7-TW python=3.8
    conda actvate Assignment7-TW
    pip install -r requirements.txt
    ```

3. db를 table 구조를 최신 model에 맞게 설정한다.
    ```bash
    python manage.py migrate
    ```

4. 서버를 실행한다.
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

###  배포용 
1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
  ```bash
  git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment7-TW
  cd Assignment7-TW
  ```
2. docker를 실행해서 서버를 구동한다.
  ```bash
  docker-compose -f ./docker-compose-deploy.yml up --build -d
  ```
</div>
</details>

## 폴더 구조
```bash

```


## TIL정리 (Blog)


# Reference
- 이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 xx에서 출제한 과제를 기반으로 만들었습니다.
- 본 과제는 저작권의 보호를 받으며, 문제에 대한 정보를 배포하는 등의 행위를 금지 합니다.
