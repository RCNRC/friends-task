from django.db import models
from django.contrib.auth.models import User


RELATIONSHIP_REQUEST_INCOME = 1
RELATIONSHIP_ACTIVE = 2
RELATIONSHIP_REQUEST_OUTCOME = 3
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_REQUEST_INCOME, 'income'),
    (RELATIONSHIP_ACTIVE, 'active'),
    (RELATIONSHIP_REQUEST_OUTCOME, 'outcome'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    def __str__(self):
        return self.user.username


class FriendShip(models.Model):
    from_user = models.ForeignKey(
        UserProfile,
        related_name='relations',
        on_delete=models.CASCADE,
    )
    to_user = models.ForeignKey(
        UserProfile,
        related_name='from_users',
        on_delete=models.CASCADE,
    )
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

    class Meta:
        unique_together = ('from_user', 'to_user')
