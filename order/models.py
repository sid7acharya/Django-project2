from django.db import models
from user.models import User,UserAddress
from book.models import Book,BookOption
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=100)
    PENDING="P"
    COMPLETED="C"
    
    STATUS_CHOICES= ((PENDING,_("pending")), (COMPLETED,_("completed")))
    
    buyer=models.ForeignKey(User,verbose_name=("Book Buyer"), on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default=PENDING)
    shipping_address=models.ForeignKey(UserAddress,related_name="shipping_orders",on_delete=models.SET_NULL,blank=True,null=True,)
    billing_address=models.ForeignKey(UserAddress,related_name="billing_orders",on_delete=models.SET_NULL,blank=True,null=True)
    
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.buyer.username
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)  # Assuming item is a Book
    quantity = models.IntegerField()
    order_option = models.ForeignKey(BookOption, on_delete=models.CASCADE)
         
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    order_option=models.ForeignKey(BookOption, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.buyer.get_full_name()
        
    @cached_property
    def cost(self):
            """
                Total cost of the ordered item
        """
            return round(self.quantity * self.item.price, 2) 
        
        
class Rent(models.Model):
    PENDING="P"
    COMPLETED="C"
    CANCELLED="X"
    
    STATUS_CHOICES=(
        (PENDING,_("Pending")),
        (COMPLETED,_("Completed")),
        (CANCELLED,_("Cancelled")),
    )

    renter = models.ForeignKey(User,verbose_name=("User"),on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    rent_date = models.DateField(_("Rent Date"), auto_now_add=True)
    return_date = models.DateField(_("Return Date"))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)

    class Meta:
        verbose_name = _("Rent")
        verbose_name_plural = _("Rents")

    def __str__(self):
        return f"{self.renter.username} - {self.book.title}"
    

class Buy(models.Model):
    book = models.ForeignKey(Book,verbose_name=("Book"),on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.book.name} - Buy: {self.price}"
    


    