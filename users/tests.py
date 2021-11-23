import json

from benedict                        import benedict
from unittest.mock                   import patch
from django.conf                     import settings
from django.contrib.auth             import get_user_model
from rest_framework                  import status
from rest_framework.test             import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from cars.models import Tire
from .models     import UserTire


class usersTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            id       = 'taewookim',
            password = '12345678',
        )
        
    def tearDown(self):
        get_user_model().objects.all().delete()

    def test_registration_success(self):
        data = {
            "id"       : "cardoc",
            "password" : "12345678",
        }

        response = self.client.post('/users', data=json.dumps(data), content_type='application/json')
        data     = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', data)
        self.assertIn('refresh', data)

    def test_registration_failed_duto_duplicated_id(self):
        data = {
            "id"       : "taewookim",
            "password" : "12345678",
        }

        response = self.client.post('/users', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TokenTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            id       = 'taewookim',
            password = '12345678',
        )
        
    def tearDown(self):
        get_user_model().objects.all().delete()
    
    def test_get_tocken_success(self):
        data = {
            "id"       : "taewookim",
            "password" : "12345678"
        }

        response = self.client.post('/users/token', data=json.dumps(data), content_type='application/json')
        data     = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', data)
        self.assertIn('refresh', data)

    def test_refresh_token_success(self):
        token    = RefreshToken.for_user(self.user)
        refresh  = {'refresh' : str(token)}

        response = self.client.post('/users/token/refresh', data=refresh)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh_token_failed(self):
        token    = RefreshToken.for_user(self.user)
        refresh  = {'refresh' : str(token)[:-1]}

        response = self.client.post('/users/token/refresh', data=refresh)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_tocken_failed_duto_invalid_password(self):
        data = {
            "id"       : "taewookim",
            "password" : "1234567"
        }

        response = self.client.post('/users/token', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
class UserTireRegistrationTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            id  = 'taewookim',
            password = '12345678',
        )
    
    def tearDown(self):
        UserTire.objects.all().delete()
        Tire.objects.all().delete()
        get_user_model().objects.all().delete()
    
    @patch('users.views.requests')
    def test_register_tire_success(self, mocked_requests):
        class MockRequestResponse:
            def __init__(self, json_body, status_code):
                self.json_body   = json_body
                self.status_code = status_code
            
            def json(self):
                return self.json_body

        mock_body = benedict()
        mock_body['spec.driving.frontTire.value'] = '225/60R16'
        mock_body['spec.driving.rearTire.value']  = 'P195/60 R15'
        mocked_requests.get.side_effect = [MockRequestResponse(mock_body.dict(), 200)]

        data = [
            {'id': 'taewookim', 'trimId': 1000}
        ]

        self.client.force_authenticate(self.user)
        response = self.client.post('/users/register-tires', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Tire.objects.filter(width=225, aspect_ratio=60, wheel_size=16).exists())
        self.assertTrue(Tire.objects.filter(width=195, aspect_ratio=60, wheel_size=15).exists())

    @patch('users.views.requests')
    def test_register_tire_transaction_rollback(self, mocked_requests):
        class MockRequestResponse:
            def __init__(self, json_body, status_code):
                self.json_body   = json_body
                self.status_code = status_code
            
            def json(self):
                return self.json_body

        mock_body = benedict()
        mock_body['spec.driving.frontTire.value'] = '225/60R16'
        mock_body['spec.driving.rearTire.value']  = '195/60R15'
        mocked_requests.get.side_effect = [MockRequestResponse(mock_body.dict(), 200)]

        data = [
            {'id': 'taewookim', 'trimId': 1000},
            {'id': 'no_user', 'trimId': 1000}
        ]

        self.client.force_authenticate(self.user)
        response = self.client.post('/users/register-tires', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Tire.objects.all().count(), 0)
        self.assertEqual(UserTire.objects.all().count(), 0)

    @patch('users.views.requests')
    def test_register_duplicated_tire(self, mocked_requests):
        class MockRequestResponse:
            def __init__(self, json_body, status_code):
                self.json_body   = json_body
                self.status_code = status_code
            
            def json(self):
                return self.json_body

        mock_body = benedict()
        mock_body['spec.driving.frontTire.value'] = '225/60R16'
        mock_body['spec.driving.rearTire.value']  = '195/60R15'
        mocked_requests.get.side_effect = [MockRequestResponse(mock_body.dict(), 200), MockRequestResponse(mock_body.dict(), 200)]

        data = [
            {'id': 'taewookim', 'trimId': 1000},
            {'id': 'taewookim', 'trimId': 1000},
        ]

        self.client.force_authenticate(self.user)
        response = self.client.post('/users/register-tires', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tire.objects.filter(usertire__user=self.user).count(), 2)
        self.assertEqual(UserTire.objects.filter(user=self.user).count(), 2)

    def test_register_tire_faild_duto_no_key(self):
        data = [
            {'trimId': 1000}
        ]

        self.client.force_authenticate(self.user)
        response = self.client.post('/users/register-tires', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_tire_faild_duto_dose_not_exsist_id(self):
        data = [
            {'id': 'no_user', 'trimId': 1000}
        ]

        self.client.force_authenticate(self.user)
        response = self.client.post('/users/register-tires', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_tire_faild_duto_emtpy_body(self):
        data = []

        self.client.force_authenticate(self.user)
        response = self.client.post('/users/register-tires', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_tire_faild_duto_exceeded_body_registration_count_at_one_time(self,):
        data = [ {'id': 'taewookim', 'trimId': 1000} 
                for i in range(settings.MAX_REGISTRATION_TIRE_COUNT+1)]

        self.client.force_authenticate(self.user)
        response = self.client.post('/users/register-tires', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_tire_faild_duto_no_auth(self):
        data = [
            {'id': 'taewookim', 'trimId': 1000}
        ]

        response = self.client.post('/users/register-tires', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserTireListTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            id       = 'taewookim',
            password = '12345678',
        )
        self.tire1 = Tire.objects.create(
            width        = 255,
            aspect_ratio = 60,
            wheel_size   = 16
        )
        self.tire2 = Tire.objects.create(
            width        = 195,
            aspect_ratio = 60,
            wheel_size   = 15
        )

        UserTire.objects.create(user=self.user, tire=self.tire1)
        UserTire.objects.create(user=self.user, tire=self.tire2)

    def test_lookup_user_tires_success(self):
        expected_data = [
            {
                'width'      : 255,
                'aspectRatio': 60,
                'wheelSize'  : 16
            },
            {
                'width'      : 195,
                'aspectRatio': 60,
                'wheelSize'  : 15
            }
        ]

        self.client.force_authenticate(self.user)
        response = self.client.get(f'/users/{self.user.id}/tires')
        self.assertEqual(response.status_code, status.HTTP_200_OK)   
        self.assertEqual(response.json(), expected_data)

    def test_lookup_user_tires_failed_duto_not_exsist_id(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(f'/users/no_user/tires')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_lookup_user_tires_failed_duto_no_auth(self):
        response = self.client.get(f'/users/{self.user.id}/tires')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)