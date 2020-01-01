from django.db import models

class User(models.Model):
    U_Name = models.CharField(max_length=100);
    U_pswd = models.CharField(max_length=30);
    U_email = models.CharField(max_length=100, default=0);
    def __str__(self):
        return self.U_Name

class Images(models.Model):
    imagesOf = models.CharField(max_length=200);
    img1 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    img2 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    img3 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    img4 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    img5 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    img6 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    img7 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    img8 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    img9 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    img10 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    def __str__(self):
        return self.imagesOf

class Required_Gear(models.Model):
    gearFor = models.CharField(max_length=200);
    req1 = models.CharField(max_length=200, default='-');
    req2 = models.CharField(max_length=200, default='-');
    req3 = models.CharField(max_length=200, default='-');
    req4 = models.CharField(max_length=200, default='-');
    req5 = models.CharField(max_length=200, default='-');
    req6 = models.CharField(max_length=200, default='-');
    req7 = models.CharField(max_length=200, default='-');
    req8 = models.CharField(max_length=200, default='-');
    req9 = models.CharField(max_length=200, default='-');
    req10 = models.CharField(max_length=200, default='-');
    def __str__(self):
        return self.gearFor

class Services(models.Model):
    servicesFor = models.CharField(max_length=200);
    ser1 = models.CharField(max_length=200, default='-');
    ser2 = models.CharField(max_length=200, default='-');
    ser3 = models.CharField(max_length=200, default='-');
    ser4 = models.CharField(max_length=200, default='-');
    ser5 = models.CharField(max_length=200, default='-');
    ser6 = models.CharField(max_length=200, default='-');
    ser7 = models.CharField(max_length=200, default='-');
    ser8 = models.CharField(max_length=200, default='-');
    ser9 = models.CharField(max_length=200, default='-');
    ser10 = models.CharField(max_length=200, default='-');
    def __str__(self):
        return self.servicesFor

class Activities(models.Model):
    activitiesFor = models.CharField(max_length=200);
    act1 = models.CharField(max_length=200, default='-');
    act2 = models.CharField(max_length=200, default='-');
    act3 = models.CharField(max_length=200, default='-');
    act4 = models.CharField(max_length=200, default='-');
    act5 = models.CharField(max_length=200, default='-');
    act6 = models.CharField(max_length=200, default='-');
    act7 = models.CharField(max_length=200, default='-');
    act8 = models.CharField(max_length=200, default='-');
    act9 = models.CharField(max_length=200, default='-');
    act10 = models.CharField(max_length=200, default='-');
    def __str__(self):
        return self.activitiesFor

class Tour_Operator(models.Model):
    Op_Id = models.SlugField(max_length=150, unique=True, default=0);
    Op_Name = models.CharField(max_length=100);
    Op_phone = models.CharField(max_length=11, default=0);
    Op_email = models.CharField(max_length=100, default=0);
    def __str__(self):
        return self.Op_Name

class Review(models.Model):
    Rev_Id = models.SlugField(max_length=150, unique=True, default=0);
    reviewFor = models.CharField(max_length=200);
    reviewBy = models.CharField(max_length=100, default="Anonymous");
   # addedOn = models.DateField.auto_now();
    rev_good = models.CharField(max_length=5000, default='-');
    rev_bad = models.CharField(max_length=5000, default='-');
    def __str__(self):
        return self.reviewFor

class Trip(models.Model):
    Trip_Id = models.SlugField(max_length=150, unique=True, default=0);
    T_Name = models.CharField(max_length=200);
    imgs = models.ManyToManyField(Images, blank=True)
    Des = models.CharField(max_length=5000, default='-');
    reqs = models.ManyToManyField(Required_Gear, blank=True)
    noOfDays = models.PositiveIntegerField(default=0);
    noOfNights = models.PositiveIntegerField(default=0);
    sers = models.ManyToManyField(Services, blank=True)
    acts = models.ManyToManyField(Activities, blank=True)
    event_host = models.ForeignKey(Tour_Operator, on_delete=models. CASCADE, null=True, blank=True)
    revs = models.ManyToManyField(Review, blank=True)
    def __str__(self):
        return self.T_Name