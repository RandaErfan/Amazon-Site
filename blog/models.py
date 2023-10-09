from django.db import models
from django.urls import reverse

# Create your models here.

    #
    #current_price_tracker = FieldTracker(fields=['current_price'])
    #
    #def save(self, *args, **kwargs):
      #create
       # if self.pk is None: 
        #    print('if self.pk is None : INSERT')
        #else:
          #  print('if self.pk is NOT None : UPDATE')
          #  old_record=self.current_price_tracker.changed()
           # if(old_record.get('current_price') !=self.current_price):
            #    record = StockUpdates(stock_id=1,old_price=old_record.get('current_price'), 
             #                     new_price=self.current_price)
              #  record.save()
               # signals.stock_changed_signal.send(sender=self ,code=self.code,name=self.name,image=self.image,
                #	                              created_at=self.created_at,updated_at=self.updated_at,
                #                                 old_price=old_record.get('current_price'),new_value=self.current_price)
    
       # super().save(*args, **kwargs)   

