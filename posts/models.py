from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    # 이필드를 통해 업로드되면 post 미디어 루트를 기준으로해서, 폴더를한번더 감쌀 수가 있다
    # 이미지가 통으로 저장되는게 아니라 경로가 들어간다!
    created_at = models.DateTimeField()
    # 새로운필드를 정의할때, 등호왼쪽에오는것의 이름
    # 실제적용되는 필드의 타입에따라서 바뀌어서 들어가는 경로가 있을 수 있다.

    
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
        return f'{self.body}'