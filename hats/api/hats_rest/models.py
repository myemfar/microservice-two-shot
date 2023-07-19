from django.db import models
# from django.urls import reverse


class LocationVO(models.Model):
    closet_name = models.CharField(max_length=100)
    import_href = models.CharField(max_length=200, unique=True)


class Hat(models.Model):
    fabric = models.CharField(max_length=100)
    style_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture = models.URLField(null=True)
    location = models.ForeignKey(
        LocationVO,
        related_name="hats",
        on_delete=models.PROTECT,
    )

    # def get_api_url(self):
    #     return reverse("api_bin", kwargs={"pk": self.pk})

    # def __str__(self):
    #     return f"{self.closet_name} - {self.bin_number}/{self.bin_size}"
