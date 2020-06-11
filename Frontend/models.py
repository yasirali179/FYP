import datetime
from babel.dates import format_date, format_datetime, format_time
from django.db import models

class User(models.Model):
    U_PH = models.CharField(max_length=11, default=0);
    U_Name = models.CharField(max_length=100);
    U_pswd = models.CharField(max_length=30);
    U_email = models.CharField(max_length=100, default=0);
    U_City = models.CharField(max_length=50, default=0);
    #C_liked = models.ManyToManyField(Trip, blank=True);
    def __str__(self):
        return self.U_Name

#class UserHistory(models.Model):


class TripReview(models.Model):
    reviewFor = models.CharField(max_length=200);
    reviewBy = models.CharField(max_length=100, default="Anonymous");
    created_at = models.DateTimeField(auto_now_add=True);
    rev_good = models.CharField(max_length=5000, default='-');
    rev_bad = models.CharField(max_length=5000, default='-');
    approved=models.BooleanField(default=False);
    rating=models.PositiveIntegerField(default=0);
    def __str__(self):
        return str(self.reviewFor)
class TourCompanyReview(models.Model):
    reviewFor = models.CharField(max_length=200);
    reviewBy = models.CharField(max_length=100, default="Anonymous");
    created_at = models.DateTimeField(auto_now_add=True);
    rev_good = models.CharField(max_length=5000, default='-');
    rev_bad = models.CharField(max_length=5000, default='-');
    approved=models.BooleanField(default=False);
    rating=models.PositiveIntegerField(default=0);
    def __str__(self):
        return str(self.reviewFor)
class DestincationReview(models.Model):
    reviewFor = models.CharField(max_length=200);
    reviewBy = models.CharField(max_length=100, default="Anonymous");
    created_at = models.DateTimeField(auto_now_add=True);
    rev_good = models.CharField(max_length=5000, default='-');
    rev_bad = models.CharField(max_length=5000, default='-');
    approved=models.BooleanField(default=False);
    rating=models.PositiveIntegerField(default=0);
    def __str__(self):
        return str(self.reviewFor)


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
    display = models.BooleanField(default=False)
    revs = models.ManyToManyField(DestincationReview, blank=True)
    Total_Reviews = models.PositiveIntegerField(default=0);
    Total_Rating = models.PositiveIntegerField(default=0);
    Average_Rating = models.FloatField(default=0)
    Total_Trips = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.Des_Name)

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
    U_pswd = models.CharField(max_length=30);
    Op_email = models.CharField(max_length=100, default=0);
    revs = models.ManyToManyField(TourCompanyReview, blank=True)
    Total_Reviews = models.PositiveIntegerField(default=0);
    Total_Rating = models.PositiveIntegerField(default=0);
    Average_Rating = models.FloatField(default=0)
    Total_Trips=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.Operator_Name


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
    display = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0);
    Discount_Price=models.PositiveIntegerField(default=0);
    startLocation = models.CharField(max_length=200);
    startDate = models.CharField(max_length=200);
    Departure_Date=models.DateField(default=datetime.date.today, blank=True)
    active=models.BooleanField(default=False)
    Item_Is_Discount=models.BooleanField(default=False);
    No_of_Seats=models.PositiveIntegerField(default=50);
    revs = models.ManyToManyField(TripReview, blank=True)
    Total_Reviews=models.PositiveIntegerField(default=0);
    Total_Rating=models.PositiveIntegerField(default=0);
    Average_Rating=models.FloatField(default=0)
    def __str__(self):
        self.startDate=format_date(self.Departure_Date, locale='en')
        return self.T_Name



class TripScrap(models.Model):
    T_Name = models.CharField(max_length=200);
    pic = models.URLField( blank=True, verbose_name="")
    noOfDays = models.PositiveIntegerField(default=0);
    noOfNights = models.PositiveIntegerField(default=0);
    display = models.BooleanField(default=False)
    price = models.CharField(max_length=20);
    startLocation = models.CharField(max_length=200);
    startDate = models.CharField(max_length=200);
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.T_Name

class Deal(models.Model):
    deal_Id = models.SlugField(max_length=150, unique=True, default=0);
    deal_Name = models.CharField(max_length=200);
    pic  = models.FileField(upload_to='Trip/', blank=True, verbose_name="")
    def __str__(self):
        return str(self.deal_Id)

class NewsLetterEmails(models.Model):
    Email=models.CharField(max_length=200);
    def __str__(self):
        return self.Email

class Destination_History(models.Model):
    Destination_Name = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    count=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.Destination_Name.Des_Name

class Trip_History(models.Model):
    Trip_Name= models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, blank=True)
    count=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.Trip_Name.T_Name

class Tour_Operator_History(models.Model):
    Tour_Operator_Name= models.ForeignKey(Tour_Operator, on_delete=models.CASCADE, null=True, blank=True)
    count=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.Tour_Operator_Name.Operator_Name


class newsfeed(models.Model):
    Title= models.CharField(max_length=200, default=0);
    Source= models.CharField(max_length=200, default=0);
    description= models.CharField(max_length=1000, default=0);
    url=models.URLField();
    date= models.CharField(max_length=100, default=0);

    def __str__(self):
        return self.Title

class News_Sraping_Url(models.Model):
    Url_title=models.CharField(max_length=200, default=0);
    url = models.URLField();

    def __str__(self):
        return self.Url_title

class Trips_Sraping_Url(models.Model):
    Url_title = models.CharField(max_length=200, default=0);
    url = models.URLField();

    def __str__(self):
        return self.Url_title

class Trips_Operators_Sraping_Url(models.Model):
    Url_title = models.CharField(max_length=200, default=0);
    url = models.URLField();

    def __str__(self):
        return self.Url_title


class Cart(models.Model):
    Cart_id=models.CharField(max_length=100,default=0);
    Cust = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    items_in_cart=models.ForeignKey(Trip,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=0)
    Total = models.DecimalField(default=0.000, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.Cust.U_Name

class Order(models.Model):
    O_id=models.CharField(max_length=150,default=0)
    Cust = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    items_in_order = models.ForeignKey(Trip,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=0)
    O_Total = models.DecimalField(default=0.000, max_digits=100, decimal_places=2)
    Order_Verified = models.BooleanField(default=False);
    Order_Packed = models.BooleanField(default=False);
    Order_shipped = models.BooleanField(default=False);
    Order_Received = models.BooleanField(default=False);
    Order_Claimed = models.BooleanField(default=False);
    Order_Canceled = models.BooleanField(default=False);
    Finish = models.BooleanField(default=False);
    Comments = models.CharField(max_length=500,default=0)
    def __str__(self):
        return self.O_id