from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from shop.abstract import BaseModel, ActiveModel, OrderModel

UserModel = get_user_model()