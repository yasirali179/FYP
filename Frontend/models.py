from django.db import models

class User(models.Model):
    U_Name = models.CharField(max_length=100);
    U_pswd = models.CharField(max_length=30);
    U_email = models.CharField(max_length=100, default=0);
    def __str__(self):
        return self.U_Name


class Destinations(models.Model):
    Des_Id = models.SlugField(max_length=150, unique=True, default=0);
    Des_Name = models.CharField(max_length=200);
    imgs = models.ManyToManyField('Images', blank=True)
    pic = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    Des_H1 = models.CharField(max_length=2000);
    Des_Description1 = models.CharField(max_length=2000);
    state = models.CharField(max_length=200);
    Area = models.CharField(max_length=200);
    Languages = models.CharField(max_length=200);
    history1 = models.CharField(max_length=200);
    history2 = models.CharField(max_length=200);
    history3 = models.CharField(max_length=200);
    Des_H1 = models.CharField(max_length=200);
    revs = models.ManyToManyField('Review', blank=True)
    display = models.BooleanField(default=False)
    Op_review = models.CharField(max_length=11, default=0);
    Op_rating = models.CharField(max_length=100, default=0);

    def __str__(self):
        return str(self.Des_Id)

class Images(models.Model):
    img_id = models.PositiveIntegerField(default=0);
    img1 = models.FileField(upload_to='Trip/', null=True, verbose_name="")
    img2 = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    img3 = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    img4 = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    img5 = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    img6 = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    img7 = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    img8 = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    img9 = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    img10 = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    def __str__(self):
        return str(self.img_id)

class Required_Gear(models.Model):
    require_id = models.PositiveIntegerField(default=0);
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
        return str(self.require_id)

class Services(models.Model):
    service_id = models.PositiveIntegerField(default=0);
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
        return str(self.service_id)

class Activities(models.Model):
    activity_id = models.PositiveIntegerField(default=0);
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
        return str(self.activity_id)

class Tour_Operator(models.Model):
    Op_Id = models.SlugField(max_length=150, unique=True, default=0);
    pic = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    Operator_Name = models.CharField(max_length=100);
    Op_phone = models.CharField(max_length=11, default=0);
    Op_email = models.CharField(max_length=100, default=0);
    Op_review = models.CharField(max_length=11, default=0);
    Op_rating = models.CharField(max_length=100, default=0);
    def __str__(self):
        return self.Operator_Name

class Review(models.Model):
    Rev_Id = models.SlugField(max_length=150,    unique = True, default = 0);
    reviewFor = models.CharField(max_length=200);
    reviewBy = models.CharField(max_length=100, default="Anonymous");
    created_at = models.DateTimeField(auto_now_add=True);
    rev_good = models.CharField(max_length=5000, default='-');
    rev_bad = models.CharField(max_length=5000, default='-');
    def __str__(self):
        return str(self.reviewFor)

class Trip(models.Model):
    Trip_Id = models.SlugField(max_length=150, unique=True, default=0);
    T_Name = models.CharField(max_length=200);
    imgs = models.ManyToManyField(Images, blank=True)
    pic  = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    Dest = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    reqs = models.ManyToManyField(Required_Gear, blank=True)
    noOfDays = models.PositiveIntegerField(default=0);
    noOfNights = models.PositiveIntegerField(default=0);
    sers = models.ManyToManyField(Services, blank=True)
    acts = models.ManyToManyField(Activities, blank=True)
    event_host = models.ForeignKey(Tour_Operator, on_delete=models. CASCADE, null=True, blank=True)
    revs = models.ManyToManyField(Review, blank=True)
    display = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0);
    startLocation = models.CharField(max_length=200);
    startDate = models.CharField(max_length=200);
    def __str__(self):
        return self.T_Name

class Deal(models.Model):
    deal_Id = models.SlugField(max_length=150, unique=True, default=0);
    deal_Name = models.CharField(max_length=200);
    pic  = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    def __str__(self):
        return str(self.deal_Id)