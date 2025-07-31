from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_image = models.CharField(max_length=2048, blank=True, null=True)
    google_uid = models.CharField(max_length=255, unique=True)
    trial_credits = models.IntegerField(default=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'users'
        managed = False


class PhotoUpload(models.Model):
    upload_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    image_url = models.TextField()
    uploaded_at = models.DateTimeField()

    class Meta:
        db_table = 'photouploads'
        managed = False


class TestResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    upload = models.ForeignKey(PhotoUpload, on_delete=models.CASCADE, db_column='upload_id')
    disease_name = models.CharField(max_length=255)
    confidence = models.FloatField()
    tested_at = models.DateTimeField()

    class Meta:
        db_table = 'testresults'
        managed = False


class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        db_table = 'subscriptions'
        managed = False


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    transaction_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10)
    payment_status = models.CharField(max_length=10)
    paid_at = models.DateTimeField()

    class Meta:
        db_table = 'payments'
        managed = False