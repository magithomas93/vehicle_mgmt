from django.db import models


class Customer(models.Model):
    cust_name=models.CharField(max_length=120,unique=True)
    address=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone_no=models.PositiveIntegerField()
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.cust_name
class Device(models.Model):
    devicename=models.CharField(max_length=120,unique=True)
    imei=models.CharField(max_length=15)
    primarysim=models.IntegerField()
    secondarysim=models.IntegerField()
    options = (
        ("bios", "bios"),
        ("uefi", "uefi"),
        ("ssd", "ssd")
    )
    status = models.CharField(max_length=120, choices=options, default="bios")

    def __str__(self):
        return self.dev_name
class DeviceManagement(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    device=models.ForeignKey(Device,on_delete=models.CASCADE)