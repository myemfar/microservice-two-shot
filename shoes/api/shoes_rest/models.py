from django.db import models

# Create your models here.
class Shoe(models.Model):
    manufacturer = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture_url = models.URLField()
    bin = models.ForeignKey(
        "BinVO", related_name="shoes", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class BinVO(models.Model):
    closet_name = models.CharField(max_length=200)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()
    import_href = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.closet_name
