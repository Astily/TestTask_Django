from django.test import TestCase, Client
from django.urls import reverse

from .forms import CustomUserChangeForm, CustomUserForm
from .models import CustomUser, LogStore


class YourTestClass(TestCase):
    def setUp(self):

        CustomUser.objects.create_user(username='test_user', first_name='Sam', last_name='Smith', emailPublic='asd@sdf.ye', email='test@test.com',
                                  birth='1993-09-02', phone="0921234567", password='1111', is_active=True, is_staff=True)

    def test_count_user(self):
        num = CustomUser.objects.count()
        self.assertEquals(num, 1)

    def test_html_status_anonymus(self):
        c = Client()
        st = c.get(reverse('edit')).status_code
        self.assertEquals(st, 302)

    def test_html_status_autorized(self):
        login = self.client.post('/edit/', {'username': 'test_user', 'password': '1111'})
        st = self.client.get(reverse('profile', args=[1])).status_code
        self.assertEquals(st, 200)

    def test_logStore(self):
        num = LogStore.objects.count()
        c = self.client.get(reverse('profile', args=[1]))
        num2 = LogStore.objects.count()
        self.assertEqual(num + 1, num2)

    def test_edit_page(self):
        data = {'first_name': 'Tom', 'last_name': 'Wild', 'birth': '1990-01-10', 'biography': 'Bla-Bla-Bla',
                'emailPublic': 'aa@bb.cc', 'phone': '+380971212343'}
        c = self.client.get(reverse('edit'))
        self.assertEquals(c.status_code, 302)

        login = self.client.post(reverse('login'), {'username': 'test_user', 'password': '1111'})
        c = self.client.get(reverse('edit'))
        self.assertEquals(c.status_code, 200)

        c = self.client.post(reverse('edit'), data)
        self.assertEquals(c.status_code, 302)

        form = CustomUserForm(data=data)
        self.assertTrue(form.is_valid())


        user = CustomUser.objects.get(pk=1)
        self.assertEquals(user.first_name, data['first_name'])
        self.assertEquals(user.biography, data['biography'])


