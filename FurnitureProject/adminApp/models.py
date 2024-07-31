from django.db import models

# Create your models here.
class AdminModel (models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

 

class HsliderModel (models.Model):
    hsliderimg = models.ImageField(upload_to="static/images/")

class HvideoModel (models.Model):
    hvideo1 = models.FileField(upload_to="static/images/")
    hvideo2 = models.FileField(upload_to="static/images/")

class HtopicModel (models.Model):
    htopicimg = models.ImageField(upload_to="static/images/")
    htopicimgt = models.TextField(max_length = 100)

class HsvideoModel (models.Model):
    hsvideo = models.FileField(upload_to="static/images/")

class Hgc1Model (models.Model):
    hgc1img = models.ImageField(upload_to="static/images/")

class Hgc2Model (models.Model):
    hgc2img = models.ImageField(upload_to="static/images/")

class Hgc3Model (models.Model):
    hgc3img = models.ImageField(upload_to="static/images/")

class Hgc4Model (models.Model):
    hgc4img = models.ImageField(upload_to="static/images/")

class CfeedbackModel(models.Model):
    fimg = models.ImageField(upload_to="static/images/") 
    cpimg = models.ImageField(upload_to="static/images/") 
    cname = models.CharField(max_length = 200) 
    cfeedback = models.CharField(max_length = 200) 




# Living -----------------------------------------------
    
class LsliderModel (models.Model):
    lsliderimg = models.ImageField(upload_to="static/images/")

class LvideoModel (models.Model):
    lvideo1 = models.FileField(upload_to="static/images/")
    lvideo2 = models.FileField(upload_to="static/images/")

class LtopicModel (models.Model):
    ltopicimg = models.ImageField(upload_to="static/images/")
    ltopicimgt = models.TextField(max_length = 100)

class LsvideoModel (models.Model):
    lsvideo = models.FileField(upload_to="static/images/")

class Lgc1Model (models.Model):
    lgc1img = models.ImageField(upload_to="static/images/")

class Lgc2Model (models.Model):
    lgc2img = models.ImageField(upload_to="static/images/")

class Lgc3Model (models.Model):
    lgc3img = models.ImageField(upload_to="static/images/")

class Lgc4Model (models.Model):
    lgc4img = models.ImageField(upload_to="static/images/")




# KITCHEN --------------------------------------------------------
    
class KsliderModel (models.Model):
    ksliderimg = models.ImageField(upload_to="static/images/")

class KvideoModel (models.Model):
    kvideo1 = models.FileField(upload_to="static/images/")
    kvideo2 = models.FileField(upload_to="static/images/")

class KtopicModel (models.Model):
    ktopicimg = models.ImageField(upload_to="static/images/")
    ktopicimgt = models.TextField(max_length = 100)

class KsvideoModel (models.Model):
    ksvideo = models.FileField(upload_to="static/images/")

class Kgc1Model (models.Model):
    kgc1img = models.ImageField(upload_to="static/images/")

class Kgc2Model (models.Model):
    kgc2img = models.ImageField(upload_to="static/images/")

class Kgc3Model (models.Model):
    kgc3img = models.ImageField(upload_to="static/images/")

class Kgc4Model (models.Model):
    kgc4img = models.ImageField(upload_to="static/images/")





# Bedroom -----------------------------------------------------
    
class BsliderModel (models.Model):
    bsliderimg = models.ImageField(upload_to="static/images/")

class BvideoModel (models.Model):
    bvideo1 = models.FileField(upload_to="static/images/")
    bvideo2 = models.FileField(upload_to="static/images/")

class BtopicModel (models.Model):
    btopicimg = models.ImageField(upload_to="static/images/")
    btopicimgt = models.TextField(max_length = 100)

class BsvideoModel (models.Model):
    bsvideo = models.FileField(upload_to="static/images/")

class Bgc1Model (models.Model):
    bgc1img = models.ImageField(upload_to="static/images/")

class Bgc2Model (models.Model):
    bgc2img = models.ImageField(upload_to="static/images/")

class Bgc3Model (models.Model):
    bgc3img = models.ImageField(upload_to="static/images/")

class Bgc4Model (models.Model):
    bgc4img = models.ImageField(upload_to="static/images/")




# Outdoor ---------------------------------------------------------------

class OsliderModel (models.Model):
    osliderimg = models.ImageField(upload_to="static/images/")

class OvideoModel (models.Model):
    ovideo1 = models.FileField(upload_to="static/images/")
    ovideo2 = models.FileField(upload_to="static/images/")

class OtopicModel (models.Model):
    otopicimg = models.ImageField(upload_to="static/images/")
    otopicimgt = models.TextField(max_length = 100)

class OsvideoModel (models.Model):
    osvideo = models.FileField(upload_to="static/images/")

class Ogc1Model (models.Model):
    ogc1img = models.ImageField(upload_to="static/images/")

class Ogc2Model (models.Model):
    ogc2img = models.ImageField(upload_to="static/images/")

class Ogc3Model (models.Model):
    ogc3img = models.ImageField(upload_to="static/images/")

class Ogc4Model (models.Model):
    ogc4img = models.ImageField(upload_to="static/images/")




# Cafe -------------------------------------------------------

class CsliderModel (models.Model):
    csliderimg = models.ImageField(upload_to="static/images/")

class CvideoModel (models.Model):
    cvideo1 = models.FileField(upload_to="static/images/")
    cvideo2 = models.FileField(upload_to="static/images/")

class CtopicModel (models.Model):
    ctopicimg = models.ImageField(upload_to="static/images/")
    ctopicimgt = models.TextField(max_length = 100)

class CsvideoModel (models.Model):
    csvideo = models.FileField(upload_to="static/images/")

class Cgc1Model (models.Model):
    cgc1img = models.ImageField(upload_to="static/images/")

class Cgc2Model (models.Model):
    cgc2img = models.ImageField(upload_to="static/images/")

class Cgc3Model (models.Model):
    cgc3img = models.ImageField(upload_to="static/images/")

class Cgc4Model (models.Model):
    cgc4img = models.ImageField(upload_to="static/images/")




# Office --------------------------------------------------------

class OfsliderModel (models.Model):
    ofsliderimg = models.ImageField(upload_to="static/images/")

class OfvideoModel (models.Model):
    ofvideo1 = models.FileField(upload_to="static/images/")
    ofvideo2 = models.FileField(upload_to="static/images/")

class OftopicModel (models.Model):
    oftopicimg = models.ImageField(upload_to="static/images/")
    oftopicimgt = models.TextField(max_length = 100)

class OfsvideoModel (models.Model):
    ofsvideo = models.FileField(upload_to="static/images/")

class Ofgc1Model (models.Model):
    ofgc1img = models.ImageField(upload_to="static/images/")

class Ofgc2Model (models.Model):
    ofgc2img = models.ImageField(upload_to="static/images/")

class Ofgc3Model (models.Model):
    ofgc3img = models.ImageField(upload_to="static/images/")

class Ofgc4Model (models.Model):
    ofgc4img = models.ImageField(upload_to="static/images/")



# Others ---------------------------------------------------------

class OttopicModel (models.Model):
    ottopicimg = models.ImageField(upload_to="static/images/")
    ottopicimgt = models.TextField(max_length = 100)

class OtsvideoModel (models.Model):
    otsvideo = models.FileField(upload_to="static/images/")

class Otgc1Model (models.Model):
    otgc1img = models.ImageField(upload_to="static/images/")

class Otgc2Model (models.Model):
    otgc2img = models.ImageField(upload_to="static/images/")

class Otgc3Model (models.Model):
    otgc3img = models.ImageField(upload_to="static/images/")

class Otgc4Model (models.Model):
    otgc4img = models.ImageField(upload_to="static/images/")   




#About --------------------------------------------------------------------------

class AboutModel (models.Model):
    abtitle = models.CharField(max_length = 100) 
    abdis = models.TextField()

class MemberModel (models.Model):
    tmphoto = models.ImageField(upload_to="static/images" )
    tmname = models.CharField(max_length = 100)
    tmposition = models.CharField(max_length =100 )
    tmabout = models.CharField(max_length = 200)
    tmphone = models.CharField(max_length = 15)


#Blog ------------------------------------------------------------------------------

class BlogModel (models.Model):
    bimage = models.ImageField(upload_to="static/images/")
    btitle = models.CharField(max_length = 100)
    bdate = models.CharField(max_length = 12)
    bdis = models.TextField()
    blog_by = models.CharField(max_length = 50)



#Contact us -----------------------------------------------------------------------

class ContactModel (models.Model):
    address = models.CharField(max_length =200)
    phoneno = models.CharField(max_length = 15)
    email = models.EmailField()