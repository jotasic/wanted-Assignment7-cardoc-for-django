from django.contrib.auth             import get_user_model
from rest_framework                  import status
from rest_framework.test             import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class usersTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            user_id  = 'taewookim',
            password = '12345678',
        )

    def test_registration_success(self):
        data = {
            "user_id" : "cardoc",
            "password" : "12345678",
        }
        response = self.client.post('/users', data=data)
        data     = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', data)
        self.assertIn('refresh', data)

    def test_registration_failed_duto_duplicated_user_id(self):
        data = {
            "user_id" : "taewookim",
            "password" : "12345678",
        }
        response = self.client.post('/users', data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TokenTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            user_id  = 'taewookim',
            password = '12345678',
        )
    
    def test_get_tocken_success(self):
        data = {
            "user_id"  : "taewookim",
            "password" : "12345678"
        }
        response = self.client.post('/users/token', data=data)
        data     = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', data)
        self.assertIn('refresh', data)

    def test_get_tocken_failed_duto_invalid_password(self):
        data = {
            "user_id"  : "taewookim",
            "password" : "1234567"
        }
        response = self.client.post('/users/token', data=data)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

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